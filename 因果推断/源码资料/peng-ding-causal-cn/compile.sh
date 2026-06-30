#!/bin/bash
set -e

FILE="Causalinference-cn"

echo "=== 第一次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 编译参考文献 ==="
bibtex ${FILE}.aux

echo "=== 第二次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第三次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 编译完成 ==="
ls -la ${FILE}.pdf
