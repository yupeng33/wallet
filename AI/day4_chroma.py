import os

import chromadb

# 1. 初始化客户端（此处使用内存模式，程序结束数据即销毁。若要持久化到磁盘，可使用 PersistentClient）
client = chromadb.PersistentClient(path="./my_chroma_db")
# client = chromadb.Client()

print("当前脚本运行目录：", os.getcwd())
print("数据库绝对路径：", os.path.abspath("./my_chroma_db"))

# 2. 创建一个集合（Collection，相当于关系型数据库的 Table，或 ES 的 Index）
# 这里我们指定了使用 L2（欧氏距离）作为相似度计算方法
collection = client.get_or_create_collection(
    name="my_knowledge_base", metadata={"hnsw:space": "l2"}
)

# 3. 添加文本数据到向量库
# 注意：我们这里只传入了原始文本（documents），Chroma 会在底层自动调用默认模型把它们转成向量并存入！
print("正在将文本转化为向量并写入数据库...")
collection.add(
    documents=[
        "大熊猫是中国特有的珍稀动物，主要食物是竹子。",
        "Python 是一种高级编程语言，广泛应用于人工智能和数据科学。",
        "Java 是一门面向对象的编程语言，常用于企业级后端开发。",
        "红烧肉是一道经典的中国传统菜肴，口感肥而不腻。",
    ],
    ids=["doc1", "doc2", "doc3", "doc5"],  # 必须为每条数据提供唯一的 ID
)
print("写入成功！")

# 4. 进行向量相似度检索（Query）
# 即使我们提问的词跟库里的词不完全一样，它也能靠“语义”识别出来
query_text = "我想吃饭"
print(f"\n🔍 用户提问: '{query_text}'")

results = collection.query(
    query_texts=[query_text],
    n_results=1,  # 指定返回最相似的前 1 条结果
)

# 5. 打印检索结果
print("🤖 向量库检索到的最相关知识：")
for doc, distance, doc_id in zip(
    results["documents"][0], results["distances"][0], results["ids"][0]
):
    print(f"[{doc_id}] 内容: {doc}")
    print(f"📊 语义距离 (Distance): {distance}（距离越小表示越相似）")
