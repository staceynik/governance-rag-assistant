````markdown
# Governance RAG Assistant

AI-powered document governance and compliance assistant with semantic retrieval, local LLM support, and structured compliance analysis.

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

Example:

```env
LLM_BACKEND=ollama

HF_EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

Recommended lightweight model for development:

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
git clone <repo-url>
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

Start Ollama (optional for local inference):

```bash
ollama serve
```

Run the API server:

```bash
cd api
uvicorn app.main:app --reload
```

Swagger UI:

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

Upload and index documents.

---

### Ask Questions

```http
POST /ask
```

Ask questions over uploaded documents using semantic retrieval.

---

### Compliance Analysis

```http
POST /compliance/check
```

Analyze uploaded documents against governance or policy requirements.

---

### List Documents

```http
GET /docs/list
```

Returns indexed documents.

---

### Health Check

```http
GET /health
```

Returns API status and configured backend.

---

## Example Workflow

1. Upload a policy document
2. Upload employee or governance-related documents
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

## Notes

This project is designed as a lightweight, portfolio-oriented AI governance assistant focused on:

- semantic retrieval
- explainable outputs
- local AI inference
- structured compliance analysis

It intentionally avoids unnecessary architectural complexity in favor of a compact and understandable implementation.

## License

MIT License
````
