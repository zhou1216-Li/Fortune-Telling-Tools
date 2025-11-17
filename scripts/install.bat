@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%" >nul

echo ==========================================
echo   安装 Python 依赖包
echo ==========================================
echo.

echo 正在检查 Python 环境...
python --version
if errorlevel 1 (
    echo 错误：未找到 Python，请先安装 Python 3.8 或更高版本
    call :restore_and_exit 1
)

echo.
echo 正在升级 pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo 错误：pip 升级失败
    call :restore_and_exit 1
)

echo.
echo 正在安装依赖包...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo 安装失败！请检查错误信息
    call :restore_and_exit 1
)

echo.
echo ==========================================
echo   安装完成！
echo ==========================================
echo.
echo 现在可以运行: python run.py
echo.

call :restore_and_exit 0
exit /b 0

:restore_and_exit
set "EXIT_CODE=%~1"
popd >nul
endlocal & exit /b %EXIT_CODE%

