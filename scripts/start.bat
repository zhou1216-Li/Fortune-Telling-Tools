@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%" >nul

echo ==========================================
echo   启动 Flask Web 应用
echo ==========================================
echo.

echo 正在检查依赖...
python -c "import flask" 2>nul
if errorlevel 1 (
    echo.
    echo [错误] Flask 未安装！
    echo.
    echo 请先运行 scripts\install.bat 安装依赖，或执行以下命令：
    echo   pip install -r requirements.txt
    echo.
    call :restore_and_exit 1
)

python -c "import requests" 2>nul
if errorlevel 1 (
    echo.
    echo [错误] requests 未安装！
    echo.
    echo 请先运行 scripts\install.bat 安装依赖，或执行以下命令：
    echo   pip install -r requirements.txt
    echo.
    call :restore_and_exit 1
)

echo [成功] 依赖检查通过
echo.
echo 正在启动应用...
echo.

python run.py

call :restore_and_exit %ERRORLEVEL%
exit /b 0

:restore_and_exit
set "EXIT_CODE=%~1"
popd >nul
endlocal & (
    if "%EXIT_CODE%"=="0" (
        pause
        exit /b 0
    ) else (
        pause
        exit /b %EXIT_CODE%
    )
)

