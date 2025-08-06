import requests
import json

def query_phi3(prompt, model="phi3", stream=False):
    """
    向本地部署的Phi-3-mini模型发送查询
    
    参数:
    prompt (str): 输入的提示文本
    model (str): 模型名称，默认为"phi3"
    stream (bool): 是否流式返回结果
    
    返回:
    str: 模型的响应结果
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}"
    except requests.exceptions.ConnectionError:
        return "连接失败，请确保Ollama服务正在运行并且Phi-3-mini模型已成功部署"
    except requests.exceptions.Timeout:
        return "请求超时，请检查网络连接或模型响应时间"
    except Exception as e:
        return f"发生错误: {str(e)}"

def interactive_chat():
    """启动交互式聊天会话"""
    print("欢迎使用Phi-3-mini本地模型聊天工具！")
    print("输入'退出'或'exit'结束会话")
    print("\n")
    
    while True:
        user_input = input("你: ")
        if user_input.lower() in ['退出', 'exit']:
            print("再见！")
            break
        
        print("思考中...")
        response = query_phi3(user_input)
        print(f"Phi-3-mini: {response}")
        print("\n")

if __name__ == "__main__":
    interactive_chat()