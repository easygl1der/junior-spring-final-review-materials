import argparse
import asyncio
from pathlib import Path

import httpx


BASE_URL = "https://mineru.net/api/v1/agent"


async def transcribe(pdf_path: Path, output_path: Path) -> None:
    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=httpx.Timeout(180, connect=30),
    ) as http:
        create = await http.post(
            f"{BASE_URL}/parse/file",
            headers={"Content-Type": "application/json"},
            json={
                "file_name": pdf_path.name,
                "language": "en",
                "enable_table": True,
                "is_ocr": False,
                "enable_formula": True,
            },
            timeout=60,
        )
        create.raise_for_status()
        data = create.json()["data"]
        print(f"MinerU task: {data['task_id']}")

        upload = await http.put(data["file_url"], content=pdf_path.read_bytes(), timeout=180)
        upload.raise_for_status()

        markdown_url = ""
        for _ in range(60):
            status = await http.get(f"{BASE_URL}/parse/{data['task_id']}", timeout=60)
            status.raise_for_status()
            item = status.json().get("data") or {}
            state = item.get("state")
            print(f"MinerU state: {state}")
            if state == "done":
                markdown_url = item.get("markdown_url") or ""
                break
            if state == "failed":
                raise RuntimeError(f"MinerU parse failed: {item}")
            await asyncio.sleep(3)

        if not markdown_url:
            raise TimeoutError("MinerU did not finish before the polling timeout")

        markdown = None
        for attempt in range(1, 6):
            try:
                markdown = await http.get(markdown_url, timeout=180)
                markdown.raise_for_status()
                break
            except httpx.HTTPError as exc:
                if attempt == 5:
                    raise
                print(f"Markdown download failed on attempt {attempt}: {exc!r}")
                await asyncio.sleep(3 * attempt)

        if markdown is None:
            raise RuntimeError("MinerU did not return Markdown")

        output_path.write_text(markdown.text, encoding="utf-8")
        print(f"Wrote {output_path} ({len(markdown.text)} characters)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    asyncio.run(transcribe(args.pdf, args.output))


if __name__ == "__main__":
    main()
