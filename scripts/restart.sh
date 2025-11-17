#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"

echo "正在停止所有 Flask 进程..."
if command -v lsof >/dev/null 2>&1; then
    lsof -ti:5000 | xargs kill -9 2>/dev/null || true
elif command -v fuser >/dev/null 2>&1; then
    fuser -k 5000/tcp || true
fi

sleep 2
echo
echo "启动 Flask 应用..."
python3 run.py

