#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"

echo "=========================================="
echo "  启动 Flask Web 应用"
echo "=========================================="
echo

echo "正在检查依赖..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo
    echo "[错误] Flask 未安装！"
    echo
    echo "请先运行 scripts/install.sh 安装依赖，或执行以下命令："
    echo "  pip3 install -r requirements.txt"
    echo
    exit 1
fi

if ! python3 -c "import requests" 2>/dev/null; then
    echo
    echo "[错误] requests 未安装！"
    echo
    echo "请先运行 scripts/install.sh 安装依赖，或执行以下命令："
    echo "  pip3 install -r requirements.txt"
    echo
    exit 1
fi

echo "[成功] 依赖检查通过"
echo
echo "正在启动应用..."
echo

python3 run.py

