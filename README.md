# LangChain RAG Starter: Transport Layer Explorer

This project is a simple **Retrieval-Augmented Generation (RAG)** application built with **LangChain**. It is designed to answer technical questions about **TCP** and **UDP** protocols.

## How it Works
1. **Source Data:** The AI uses a text file in the `data/` folder containing technical specifications about the **Transport Layer**.
2. **Retrieval:** When you ask a question, the system searches the text for relevant sections (like TCP headers or UDP features).
3. **Generation:** The AI uses that specific context to provide an accurate, grounded answer.

## Setup Instructions
1. Open this repository in **GitHub Codespaces**.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your OpenAI API Key to the `.env` file.
4. Run the app: `python app.py`