from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from tagged_pipeline import run_tagged_pipeline

router = APIRouter()

class TaggedSection(BaseModel):
    label: str
    text: str

class TaggedAnalysisRequest(BaseModel):
    sections: List[TaggedSection]

@router.post("/")
def analyze_tagged(request: TaggedAnalysisRequest):
    tagged_sections = [section.dict() for section in request.sections]
    results = run_tagged_pipeline(tagged_sections)
    return {"results": results}
