#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"

echo "========================================"
echo "命理预测工具 - 启动脚本"
echo "========================================"
echo ""

if ! command -v python3 >/dev/null 2>&1; then
    echo "[错误] 未检测到 Python3，请先安装 Python 3.7+"
    exit 1
fi

echo "[1/3] 检查依赖包..."
if ! python3 -c "import flask" >/dev/null 2>&1; then
    echo "[提示] 正在安装依赖包..."
    if ! pip3 install -r requirements.txt; then
        echo "[错误] 依赖包安装失败，请检查网络连接"
        exit 1
    fi
fi

echo "[2/3] 检查数据库..."
if [ ! -d "data" ]; then
    echo "[提示] 创建数据目录..."
    mkdir -p data
fi

echo "[3/3] 启动应用..."
echo ""
echo "========================================"
echo "应用正在启动，请稍候..."
echo "访问地址: http://localhost:5000"
echo "按 Ctrl+C 停止应用"
echo "========================================"
echo ""

python3 run.py

