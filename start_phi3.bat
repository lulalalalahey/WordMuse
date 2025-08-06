@echo off

:: 启动Ollama服务
echo 正在启动Ollama服务...
start "Ollama Service" cmd /k "ollama serve"

:: 等待服务启动
echo 等待Ollama服务启动...
timeout /t 5 /nobreak >nul

:: 运行Phi-3-mini模型
echo 正在启动Phi-3-mini模型...
start "Phi-3-mini Chat" cmd /k "ollama run phi3"

:: 提示用户
 echo Phi-3-mini模型已启动，您可以在新打开的命令窗口中与模型交互。
 echo 如果需要使用Python客户端，请运行: python phi3_client.py
 pause
 exit