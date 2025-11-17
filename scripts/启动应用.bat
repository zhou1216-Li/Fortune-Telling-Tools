@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%" >nul

echo ========================================
echo 命理预测工具 - 启动脚本
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到 Python，请先安装 Python 3.7+
    call :restore_and_exit 1
)

echo [1/3] 检查依赖包...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [提示] 正在安装依赖包...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [错误] 依赖包安装失败，请检查网络连接
        call :restore_and_exit 1
    )
)

echo [2/3] 检查数据库...
if not exist "data" (
    echo [提示] 创建数据目录...
    mkdir data
)

echo [3/3] 启动应用...
echo.
echo ========================================
echo 应用正在启动，请稍候...
echo 访问地址: http://localhost:5000
echo 按 Ctrl+C 停止应用
echo ========================================
echo.

python run.py

call :restore_and_exit %ERRORLEVEL%
exit /b 0

:restore_and_exit
set "EXIT_CODE=%~1"
popd >nul
endlocal & (
    pause
    exit /b %EXIT_CODE%
)

