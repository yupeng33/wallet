import os
import shutil

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

OLLAMA_BASE_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"


def run_langchain_demo():
    persist_dir = "./my_chroma_db"
    if os.path.exists(persist_dir):
        shutil.rmtree(persist_dir)

    # ==========================================
    # 步骤 1: 创建测试文档 (模拟原始数据)
    # ==========================================
    test_file = "langchain_test.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(
            "LangChain 是一个用于开发由大语言模型驱动的应用程序的框架。\n"
            "它的核心组件包括：Document 模块、TextSplitter 文本分割器、Embedding 向量化工具和 Retriever 检索器。\n"
            "今天我们在进行 Day 5 的学习，内容是跑通一个最基础的 RAG 检索流水线。"
        )
    print("✨ 测试文本创建成功！")

    # ==========================================
    # 步骤 2: 加载文档 (Document Loader)
    # ==========================================
    loader = TextLoader(test_file, encoding="utf-8")
    documents = loader.load()
    print(f"📄 成功加载文档！文档数量: {len(documents)}")

    # ==========================================
    # 步骤 3: 文本分割 (Text Splitter)
    # ==========================================
    # 使用递归字符分割器，设置块大小为 50 字，重叠 10 字
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=50,
        chunk_overlap=10
    )
    split_docs = text_splitter.split_documents(documents)
    print(f"✂️ 文本分割完成！切分后的片段数量: {len(split_docs)}")
    for i, doc in enumerate(split_docs):
        print(f"   👉 片段 {i + 1}: {doc.page_content.strip()}")

    # ==========================================
    # 步骤 4: 向量化并存入向量数据库 (Embedding & VectorStore)
    # ==========================================
    # 初始化 Embedding 模型（本地 Ollama 推理，无需 API Key / 代理）
    embeddings = OllamaEmbeddings(model=EMBED_MODEL, base_url=OLLAMA_BASE_URL)

    # 将分割后的文档存入内存版的 Chroma 向量数据库
    print("🧠 正在进行文本向量化并存入向量库...")
    vectorstore = Chroma.from_documents(split_docs, embeddings, persist_directory=persist_dir)
    print("💾 向量数据库构建成功！")

    # ==========================================
    # 步骤 5: 构建检索链并测试 (Retriever)
    # ==========================================
    # 将向量库转换为检索器，设置返回最相关的 2 个片段
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # 提出问题进行检索
    query = "Day 5 学习什么内容？"
    print(f"\n🔍 检索问题: '{query}'")

    retrieved_docs = retriever.invoke(query)

    print("🎯 检索到的相关文档片段：")
    for i, doc in enumerate(retrieved_docs):
        print(f"   [{i + 1}] {doc.page_content.strip()}")

    # 清理测试文件
    if os.path.exists(test_file):
        os.remove(test_file)


if __name__ == "__main__":
    run_langchain_demo()
