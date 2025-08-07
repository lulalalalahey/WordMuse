@echo off

:: 设置UTF-8编码以正确显示中文
chcp 65001 >nul

:: 检查Python是否安装
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 错误: 未找到Python。请先安装Python并确保已添加到系统PATH。
    pause
    exit /b 1
)

:: 检查Ollama服务是否运行
tasklist | findstr "ollama" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 错误: Ollama服务未运行。请先运行start_phi3.bat启动服务。
    pause
    exit /b 1
)

:: 安装必要的依赖库
echo 正在安装必要的依赖库...
python -m pip install --upgrade pip
python -m pip install requests rich

:: 检查安装是否成功
if %ERRORLEVEL% NEQ 0 (
    echo 错误: 依赖库安装失败。
    pause
    exit /b 1
)

:: 启动英语单词趣味记忆查询器
echo 启动英语单词趣味记忆查询器...
python english_word_quiz.py

pause