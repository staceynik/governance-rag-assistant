# Governance RAG Assistant

AI-powered document governance and compliance assistant with semantic retrieval, local LLM support, and structured compliance analysis.

---

# Governance RAG Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![RAG](https://img.shields.io/badge/AI-RAG-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Features

- Upload and index PDF, TXT, and Markdown documents
- Semantic search using FAISS vector storage
- Question answering over uploaded documents
- Compliance analysis with structured verdicts
- Local inference via Ollama
- Optional OpenAI backend support
- Persistent document and vector storage
- Source citations for retrieved context

---

## Architecture

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Semantic Retrieval
    ↓
LLM (Ollama or OpenAI)
    ↓
Answer / Compliance Verdict
```

---

## Tech Stack

- FastAPI
- LangChain
- FAISS
- Ollama
- OpenAI API
- SentenceTransformers
- Pydantic

---

## Supported Backends

### Ollama (Local)

Runs fully local inference using Ollama.

Example `.env` configuration:

```env
LLM_BACKEND=ollama

HF_EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

Recommended lightweight model:

```bash
ollama pull phi3:mini
```

---

### OpenAI

Optional cloud backend using OpenAI APIs.

```env
LLM_BACKEND=openai

OPENAI_API_KEY=your_openai_api_key
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBED_MODEL=text-embedding-3-small
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/staceynik/governance-rag-assistant.git
cd governance-rag-assistant
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r api/requirements.txt
```

---

## Running the Application

Start Ollama:

```bash
ollama serve
```

Run the API server:

```bash
cd api
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Environment Configuration

Create a `.env` file in the project root.

Example:

```env
LLM_BACKEND=ollama

HF_EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

OPENAI_API_KEY=your_openai_api_key
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBED_MODEL=text-embedding-3-small
```

---

## API Endpoints

### Upload Documents

```http
POST /docs/upload
```

### Ask Questions

```http
POST /ask
```

### Compliance Analysis

```http
POST /compliance/check
```

### List Documents

```http
GET /docs/list
```

### Health Check

```http
GET /health
```

---

## Example Workflow

1. Upload a policy document
2. Upload governance-related documents
3. Ask questions about uploaded content
4. Run compliance analysis
5. Retrieve structured compliance verdicts with supporting evidence

---

## Example Use Cases

- HR policy analysis
- Contract compliance verification
- Governance document retrieval
- Internal document Q&A
- Structured compliance reporting

---

## Project Structure

```text
governance-rag-assistant/
│
├── api/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag.py
│   │   └── schemas.py
│   │
│   ├── storage/
│   │   ├── faiss_index/
│   │   └── docs.json
│   │
│   └── requirements.txt
│
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## Future Improvements

- Improved compliance reasoning workflows
- Better citation formatting
- Contract change detection
- Notification draft generation
- Advanced filtering and retrieval strategies

---

## License

MIT License


