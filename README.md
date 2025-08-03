# -RAG-Based-Document-Question-Answering-System-Web-
This project is a lightweight Retrieval-Augmented Generation (RAG) pipeline built with **Python**, **Flask**, **FAISS**, **LLM (OpenAI/Ollama)**, and **Docker**. Upload a PDF and ask questions — the app fetches relevant document chunks and answers using an LLM.
# 🧠 RAG-Based Document Question Answering System

This project is a lightweight Retrieval-Augmented Generation (RAG) pipeline built with **Python**, **Flask**, **FAISS**, **LLM (OpenAI/Ollama)**, and **Docker**. Upload a PDF and ask questions — the app fetches relevant document chunks and answers using an LLM.

---

## 🚀 Features

- 📄 Upload a PDF and process it into chunks
- 🧠 Uses FAISS vector store for fast semantic search
- 🔍 Embeds using OpenAI or local `ollama.embeddings`
- 🤖 Answers questions using a Language Model (LLM)
- 🐳 Easily deployable using Docker

---

## 🧰 Tech Stack

| Layer           | Tool / Library           |
|----------------|--------------------------|
| Frontend       | HTML + JavaScript (Flask template) |
| Backend        | Flask (Python)            |
| Embeddings     | OpenAI / Ollama           |
| Vector Store   | FAISS                     |
| LLM            | OpenAI Chat / LLaMA via Ollama |
| Deployment     | Docker                    |

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/rag_app.git
cd rag_app

#2. Set up Python environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py


🐳 Docker Deployment
1. Build Docker Image

docker build -t rag_app .

2. Run Container

docker run -p 5000:5000 rag_app

📁 Project Structure
csharp
Copy
Edit
rag_app/
├── app.py                # Flask backend
├── templates/
│   └── index.html        # Upload + Chat UI
├── static/
│   └── styles.css        # Optional styles
├── rag_pipeline.py       # Core RAG logic (loading, embedding, retrieval)
├── Dockerfile            # For Docker container
├── requirements.txt      # Python dependencies
└── README.md             # Project overview

✍️ Example Use
Upload a PDF file
Ask: "What is the main topic of the document?"
LLM replies using the most relevant context from the uploaded document

----
📦 Requirements
Python 3.9+
Docker (optional, for containerization)
FAISS
Flask
LangChain
OpenAI / Ollama
---
