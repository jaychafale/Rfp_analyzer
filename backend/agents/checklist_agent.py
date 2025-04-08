from utils.llm import call_gemini

def generate_checklist(chunk_text: str, company_data: str) -> dict:
    prompt = f"""
You are a proposal checklist expert. Analyze the following RFP section and company data to extract all required documents and submission instructions.

Company Profile:
{company_data}

RFP Section:
{chunk_text}

Respond in JSON:
{{
  "required_documents": [...],
  "formatting_requirements": [...],
  "deadlines": [...],
  "summary": "..."
}}
"""
    return call_gemini(prompt)
