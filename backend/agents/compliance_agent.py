from utils.llm import call_gemini

def analyze_compliance(chunk_text: str, company_data: str) -> dict:
    prompt = f"""
You are a government RFP compliance auditor. You are assessing whether the company below is compliant with this RFP section.

Company Profile:
{company_data}

RFP Section:
{chunk_text}

Respond in JSON:
{{
  "compliance_issues": [...],
  "verdict": "Compliant" or "Non-compliant",
  "summary": "..."
}}
"""
    return call_gemini(prompt)
