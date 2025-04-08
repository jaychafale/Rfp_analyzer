from fastapi import APIRouter
from pydantic import BaseModel
from agents.prompt_engineer import generate_prompts_for_chunk

router = APIRouter()

# Request model — expects one RFP section as input
class PromptGenRequest(BaseModel):
    chunk_text: str

# Response model (optional for type safety)
class PromptGenResponse(BaseModel):
    prompts: dict

@router.post("/", response_model=PromptGenResponse)
def generate_prompts(request: PromptGenRequest):
    prompts = generate_prompts_for_chunk(request.chunk_text)
    return {"prompts": prompts}
