import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule  # 导入Rule组件代替Divider

console = Console()

def build_prompt(word):
    """
    构建提示词模板
    参数:
    word (str): 用户输入的英文单词
    返回:
    str: 构建好的提示词
    """
    prompt = f"""
    我正在学习英语单词，请你帮我深入讲解这个单词，特别是GRE考试中可能出现的含义：

    【单词】：{word}

    请按如下格式返回内容（尽量丰富）：

    1. 【中文意思】：
       - 简洁准确的翻译
       - GRE考试中可能出现的特殊/不常用含义
    2. 【英文释义】：Provide a clear English definition of this word, focusing on its academic/formal usage. Do not include any Chinese translations in this section.
    3. 【词根词缀】：分析词根、前缀或后缀，帮助我理解它的构造。
    4. 【趣味记忆法】：
       - 可以用谐音联想来记忆这个词吗？如果可以，请提供谐音记忆法。
       - 编一个小故事帮助我记住它。
       - 有这个词的词源历史吗？简要讲讲。
    5. 【例句】：至少提供 2~3 个英文例句，并附上中文翻译，优先选择学术/正式语境下的例句。
    """
    return prompt.strip()


def query_model(prompt, model="qwen3:4b", stream=False):
    """
    向本地部署的LLM模型发送查询
    参数:
    prompt (str): 输入的提示文本
    model (str): 模型名称，默认为"qwen3:4b"
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
        response = requests.post(url, json=payload, timeout=60)
        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}"
    except requests.exceptions.ConnectionError:
        return "连接失败，请确保Ollama服务正在运行并且模型已成功部署"
    except requests.exceptions.Timeout:
        return "请求超时，请检查网络连接或模型响应时间"
    except Exception as e:
        return f"发生错误: {str(e)}"


def display_result(word, result):
    """
    美观地显示查询结果
    参数:
    word (str): 查询的单词
    result (str): 模型返回的结果
    """
    console.clear()
    # 标题面板
    title_text = Text(f"📚 英语单词趣味记忆查询器 📚", style="bold magenta")
    word_text = Text(f"查询单词: {word}", style="bold cyan")
    console.print(Panel(title_text, border_style="magenta"))
    console.print(word_text)
    console.print(Rule(style="blue"))

    # 显示结果
    try:
        # 尝试按格式解析结果
        sections = result.split("\n\n")
        for section in sections:
            if section.strip():
                # 为不同部分添加颜色
                if "【中文意思】" in section:
                    console.print(Panel(section, border_style="green", expand=False))
                elif "【英文释义】" in section:
                    console.print(Panel(section, border_style="blue", expand=False))
                elif "【词根词缀】" in section:
                    console.print(Panel(section, border_style="yellow", expand=False))
                elif "【趣味记忆法】" in section:
                    console.print(Panel(section, border_style="orange", expand=False))
                elif "【例句】" in section:
                    console.print(Panel(section, border_style="purple", expand=False))
                else:
                    console.print(section)
    except:
        # 如果解析失败，直接显示结果
        console.print(Panel(result, border_style="red", expand=False))

    console.print(Rule(style="blue"))
    console.print(Text("输入新单词继续查询，或输入'exit'退出", style="italic green"))


def main():
    """
    主函数，运行英语单词趣味记忆查询器
    """
    console.clear()
    title_text = Text("🎉 欢迎使用英语单词趣味记忆查询器 🎉", style="bold magenta")
    instruction_text = Text("输入英文单词查询详细解释，输入'exit'退出程序", style="italic blue")
    console.print(Panel(title_text, border_style="magenta"))
    console.print(instruction_text)
    console.print(Rule(style="blue"))

    while True:
        user_input = input("请输入英文单词: ")
        if user_input.lower() == 'exit':
            console.print(Text("感谢使用，再见！", style="bold green"))
            break

        if not user_input.strip():
            console.print(Text("请输入有效的英文单词！", style="bold red"))
            continue

        # 构建提示词并查询模型
        prompt = build_prompt(user_input)
        console.print(Text("正在查询，请稍候...", style="italic yellow"))
        result = query_model(prompt)
        
        # 显示结果
        display_result(user_input, result)

if __name__ == "__main__":
    main()