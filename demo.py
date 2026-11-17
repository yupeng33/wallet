import ollama

# 1. 向本地运行的 deepseek-r1:8b 模型发送请求
response = ollama.chat(model='deepseek-r1:8b', messages=[
    {'role': 'user', 'content': '帮我创建一个demo1.py，打印hello world'}
])

# 2. 打印模型返回的文本内容
print(response)
print(response['message']['content'])