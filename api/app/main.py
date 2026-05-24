from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from typing import List
from .schemas import DocType, UploadResponse

load_dotenv('../../notebooks/.env')  

from .rag import RAGStore
from .schemas import (
    UploadResponse, AskRequest, AskResponse,
    ComplianceRequest, ComplianceVerdict
)

app = FastAPI(title="Vacation Policy RAG Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

store = RAGStore()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/docs/list")
def list_docs():
    return {"docs": store.list_docs()}

@app.post("/docs/upload", response_model=UploadResponse)
async def upload_doc(
    file: UploadFile = File(...),
    doc_type: DocType = Form(..., description=""),
):
    try:
        content = await file.read()
        new_id, chunks = store.upsert_document(
            doc_type=doc_type,
            filename=file.filename or "file",
            content=content,
            doc_id=doc_id
        )
        return UploadResponse(doc_id=new_id, doc_type=doc_type, chunks_indexed=chunks)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/docs/upload/batch")
async def upload_batch(
    files: List[UploadFile] = File(...),
    doc_type: DocType = Form(...),
):
    results = []
    for f in files:
        content = await f.read()
        doc_id, chunks = store.upsert_document(
            doc_type=doc_type,
            filename=f.filename or "file",
            content=content,
        )
        results.append({
            "doc_id": doc_id,
            "filename": f.filename,
            "chunks_indexed": chunks,
        })
    return {"uploaded": results}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        answer, citations = store.ask(req.question, doc_ids=req.doc_ids)
        used = req.doc_ids or [d["doc_id"] for d in store.list_docs()]
        return AskResponse(answer=answer, used_doc_ids=used, citations=citations)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/compliance/check", response_model=ComplianceVerdict)
def compliance_check(req: ComplianceRequest):
    try:
        return store.check_compliance(doc_ids=req.doc_ids, focus=req.focus)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))