import chromadb

client = chromadb.PersistentClient(path="./my_chroma_db")
coll = client.get_collection("my_knowledge_base")

# 查看文档总数
print("文档数量：", coll.count())

# 读取全部数据
res = coll.get(
    limit=100,
    include=["documents", "metadatas", "embeddings"]
)

coll.delete()
print("\n====全部数据====")
for idx, doc in enumerate(res["documents"]):
    print(f"\nid: {res['ids'][idx]}")
    print(f"meta: {res['metadatas'][idx]}")
    print(f"文本内容：{doc}")


coll.add(documents=["红烧肉是一道经典的中国传统菜肴，口感肥而不腻。"], ids=["doc4"])
print("\n====全部数据====")
for idx, doc in enumerate(res["documents"]):
    print(f"\nid: {res['ids'][idx]}")
    print(f"meta: {res['metadatas'][idx]}")
    print(f"文本内容：{doc}")

