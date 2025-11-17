#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"

echo "=========================================="
echo "  安装 Python 依赖包"
echo "=========================================="
echo

echo "正在检查 Python 环境..."
if ! command -v python3 >/dev/null 2>&1; then
    echo "错误：未找到 Python，请先安装 Python 3.8 或更高版本"
    exit 1
fi

python3 --version

echo
echo "正在升级 pip..."
python3 -m pip install --upgrade pip

echo
echo "正在安装依赖包..."
python3 -m pip install -r requirements.txt

echo
echo "=========================================="
echo "  安装完成！"
echo "=========================================="
echo
echo "现在可以运行: python3 run.py"
echo

