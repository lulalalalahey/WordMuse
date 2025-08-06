# 英语单词趣味记忆查询器

这是一个基于本地LLM（如Qwen3:4b）的英语单词学习工具，可以帮助用户深入理解和记忆英语单词。

## 功能特点
- 通过本地部署的LLM模型查询英语单词的详细解释
- 提供中文意思、英文释义、词根词缀分析
- 包含趣味记忆法（谐音联想、小故事、词源历史）
- 提供多个英文例句及中文翻译
- 使用rich库实现美观的终端界面

## 目录结构
```
├── english_word_quiz.py  # 主程序文件
├── start_word_quiz.bat   # 启动批处理文件
├── upload_to_github.bat  # 上传到GitHub的批处理文件
└── README.md             # 项目说明文件
```

## 前提条件
1. 已安装Python 3.7+并添加到系统PATH
2. 已安装Ollama并部署了Qwen3:4b模型
3. （可选）已安装Git（如果要上传到GitHub）

## 使用方法
### 运行程序
1. 双击`start_word_quiz.bat`文件
2. 在终端中输入英文单词进行查询
3. 输入`exit`退出程序

### 上传到GitHub
1. 双击`upload_to_github.bat`文件
2. 按照提示输入GitHub仓库URL
3. 输入提交信息
4. 程序会自动完成上传过程

## 注意事项
- 确保Ollama服务正在运行并且Qwen3:4b模型已成功部署
- 首次运行`start_word_quiz.bat`会自动安装必要的依赖库
- 如果遇到中文显示问题，请确保终端使用UTF-8编码
- 上传到GitHub前，请确保已配置Git用户信息
  ```
  git config --global user.name "你的用户名"
  git config --global user.email "你的邮箱"
  ```

## 问题反馈
如果在使用过程中遇到问题，请随时提交issue或联系作者。