import ollama


def read_txt_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        return file.read()

def read_json_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        return file.read()


chat = ollama.chat(model="deepseek-r1:8b",
                   messages=[{"role": "user",
                              "content": "请基于以下信息回答用户问题，如果信息中没有找到，就回答不知道。"
                                         + "已知信息： " + read_txt_file("../AI-info/knowledge.txt")
                                         + "用户问题：灵动科技是一家什么公司"}])
print(chat)
print(chat['message']['content'])