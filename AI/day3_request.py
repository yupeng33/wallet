import json
from httpx import request

# 1. 配置 API 关键信息
API_KEY = "sk-1ff8e2af15ef4b5cb87eceaeafb52fd0"  # 替换为你在官方平台申请的 API Key
URL = "https://api.deepseek.com/chat/completions"  # 接口地址

# 2. 构造请求头 (Headers)
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# 3. 构造请求体 (Body) - 严格对应官方的 JSON 格式要求
data = {
    "model": "deepseek-chat",  # 指定模型名称
    "messages": [
        {"role": "system", "content": "你是一个严谨的编程导师。"},
        {"role": "user", "content": "请用一句话解释什么是 HTTP API？"},
    ],
    "temperature": 0.7,
    "stream": False,  # 非流式传输，一次性返回
}

try:
    # 4. 发起 POST 请求
    # json.dumps(data) 将 Python 字典序列化为 JSON 字符串
    response = request("post", URL, data=json.dumps(data), headers=headers)

    # 5. 解析响应结果
    if response.status_code == 200:
        # response.json() 会自动把返回的 JSON 字符串转为 Python 字典
        res_json = response.json()

        # 层层解析大模型返回的标准结构
        reply = res_json["choices"][0]["message"]["content"]
        print("🤖 大模型回复：")
        print(reply)

        print("\n📊 消费 Token 统计：")
        print(f"输入 Token: {res_json['usage']['prompt_tokens']}")
        print(f"输出 Token: {res_json['usage']['completion_tokens']}")
    else:
        print(f"❌ 请求失败，状态码: {response.status_code}")
        print(f"错误信息: {response.text}")

except Exception as e:
    print(f"💥 发生异常: {e}")
