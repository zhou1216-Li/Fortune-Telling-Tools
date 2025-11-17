@echo off
chcp 65001 >nul
setlocal

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
pushd "%PROJECT_ROOT%" >nul

echo 正在停止所有 Flask 进程...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5000 ^| findstr LISTENING') do (
    echo 终止进程 %%a
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 2 /nobreak >nul
echo.
echo 启动 Flask 应用...
python run.py

set "EXIT_CODE=%ERRORLEVEL%"
popd >nul
endlocal
pause
exit /b %EXIT_CODE%

