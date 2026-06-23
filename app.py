from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

loader = TextLoader("data/knowledge_base.txt")
documents = loader.load()

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_db = Chroma.from_documents(
    documents,
    embeddings
)

retriever = vector_db.as_retriever()

llm = ChatOllama(model="llama3.2")

question = "Compare how TCP and UDP handle reliable delivery."

docs = retriever.invoke(question)

context = "\n".join([doc.page_content for doc in docs])

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)

print(response.content)