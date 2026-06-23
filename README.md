# Simple RAG Application with LangChain

This repository contains a basic implementation of **Retrieval-Augmented Generation (RAG)** using the **LangChain** framework. This application allows you to load your own documents and ask an AI questions based specifically on that data.

## 💡 The Concept
This project demonstrates how to move beyond generic AI responses. By using RAG, the application follows a three-step process:
1. **Ingest:** Load a text or PDF file.
2. **Retrieve:** Find the parts of the file most relevant to your question.
3. **Augment:** Provide that context to the AI so it answers based on your data rather than its general training.

## 🛠️ Technology Stack
- **Language:** Python
- **Orchestration:** LangChain
- **Vector Storage:** ChromaDB (to store and search your text)
- **Model:** OpenAI GPT (accessible via API)

## 🚀 Getting Started in GitHub Codespaces
1. **Open in Codespaces:** Click the 'Code' button and select 'Create codespace on main'.
2. **Install Dependencies:**
   Run this in the terminal:
   ```bash
   pip install langchain langchain-openai chromadb
Configure Your API Key:
Prepare Your Data: Place any .txt file you want the AI to read into the project folder.
Run the App:
📂 Project Structure
main.py: The core logic for loading data and starting the chat.
requirements.txt: List of necessary Python libraries.
data/: Folder where you store the documents the AI should "read."

---

### How this relates to your Sources
While RAG and LangChain are separate concepts, you could eventually use the **Transport Layer** documentation in your sources [1, 3] as the "data" for your RAG application. This would allow you to build an AI that can answer specific technical questions about **TCP sequence numbers** [4] or **UDP's connectionless nature** [5] based directly on your provided text.
