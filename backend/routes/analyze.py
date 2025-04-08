from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from utils.pdf_parser import extract_text_from_pdf
from pipeline_dynamic_prompt import run_dynamic_pipeline

router = APIRouter()

@router.post("/analyze/")
async def analyze_rfp(
    rfp_file: UploadFile = File(...),
    company_file: UploadFile = File(...)
):
    try:
        # ✅ Read files correctly
        rfp_content = await rfp_file.read()
        company_content = await company_file.read()

        # ✅ Extract text properly from file-like objects
        rfp_text = extract_text_from_pdf(rfp_content)
        company_text = extract_text_from_pdf(company_content)

        result = run_dynamic_pipeline(rfp_text, company_text)
        return {"analysis": result}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
