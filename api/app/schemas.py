from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class DocType(str, Enum):
    policy = "policy"
    contract = "contract"
    other = "other"

class UploadResponse(BaseModel):
    doc_id: str
    doc_type: DocType
    chunks_indexed: int

class AskRequest(BaseModel):
    question: str = Field(
        example="Summarize the uploaded HR policy"
    )
    doc_ids: Optional[List[str]] = Field(
        default=None,
        description="If not provided, the search will run across all uploaded documents."
    )

class AskResponse(BaseModel):
    answer: str
    used_doc_ids: List[str]
    citations: List[str] = Field(default_factory=list)

class ComplianceRequest(BaseModel):
    doc_ids: Optional[List[str]] = None
    focus: str = Field(
        default="vacation policy",
        example="minimum vacation duration",
        description=(
            "Compliance focus area, for example: "
            "'minimum vacation duration', "
            "'carry-over policy', "
            "'payment terms', etc."
        ),
    )

class ComplianceVerdict(BaseModel):
    compliant: bool = Field(description="Whether the documents comply with the policy")
    summary: str = Field(description="Short compliance summary in 1-3 sentences")
    violations: List[str] = Field(default_factory=list, description="List of detected violations or inconsistencies")
    evidence: List[str] = Field(default_factory=list, description="Relevant quotations or excerpts from documents and policies")
    recommendations: List[str] = Field(default_factory=list, description="Recommended corrections or clarifications")
