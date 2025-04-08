from utils.llm import call_gemini

def analyze_eligibility(chunk_text: str, company_data: str) -> dict:
    prompt = f"""
You are an expert in government RFP eligibility review. Based on the RFP section and company data below, determine if the company is eligible.

Company Profile:
{company_data}

RFP Section:
{chunk_text}

Respond in JSON:
{{
  "eligibility_criteria": [...],
  "missing_requirements": [...],
  "verdict": "Eligible" or "Ineligible",
  "summary": "..."
}}
"""
    return call_gemini(prompt)
