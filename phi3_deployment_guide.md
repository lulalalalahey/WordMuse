# Phi-3-mini 本地部署指南

## 概述
Phi-3-mini是微软开发的轻量级大语言模型，拥有3.8B参数，适合在本地环境部署使用。本指南将介绍如何使用Ollama工具在Windows系统上本地部署Phi-3-mini模型。

## 前提条件
- Windows 10/11 操作系统
- 至少8GB RAM（推荐16GB）
- 稳定的网络连接（用于下载模型）

## 步骤1：安装Ollama
Ollama是一个用于在本地运行大语言模型的命令行工具，支持Windows、macOS和Linux。

1. 访问Ollama官方网站：https://ollama.com/
2. 点击"Download for Windows"按钮下载安装程序
3. 运行下载的安装程序，按照提示完成安装

## 步骤2：验证Ollama安装
1. 打开命令提示符（CMD）或PowerShell
2. 输入以下命令验证安装是否成功：
   ```
   ollama --version
   ```
3. 如果安装成功，将显示Ollama的版本信息

## 步骤3：下载并运行Phi-3-mini模型
1. 在命令提示符中输入以下命令：
   ```
   ollama run phi3
   ```
2. Ollama将自动下载Phi-3-mini模型（约2GB）
3. 下载完成后，模型将自动启动，您可以开始与模型对话

## 步骤4：创建简单的Web界面（可选）
如果您想通过Web界面与模型交互，可以使用以下方法：

### 使用Open WebUI
1. 确保您已安装Docker
2. 运行以下命令：
   ```
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
   ```
3. 打开浏览器，访问http://localhost:3000
4. 在Web界面中选择Phi-3-mini模型进行对话

## 步骤5：通过Python代码与模型交互（可选）
您可以使用Python代码与本地部署的Phi-3-mini模型交互。以下是一个简单的示例：

```python
import requests

def query_phi3(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()['response']
    else:
        return f"Error: {response.status_code}"

# 使用示例
result = query_phi3("请介绍一下你自己")
print(result)
```

## 常见问题解决
1. **下载速度慢**：可以尝试使用国内镜像源或更换网络环境
2. **内存不足**：关闭其他占用内存的应用程序，或考虑升级硬件
3. **模型启动失败**：确保您的系统满足最低要求，并重试命令

## 进阶配置
- 模型参数调整：可以通过Ollama的配置文件调整模型的温度、最大 tokens 等参数
- 自定义模型：您可以基于Phi-3-mini创建自己的微调模型

希望本指南对您有所帮助！如有任何问题，请参考Ollama和Phi-3-mini的官方文档。