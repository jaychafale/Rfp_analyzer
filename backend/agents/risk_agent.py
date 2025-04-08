from utils.llm import call_gemini

def analyze_risk(chunk_text: str, company_data: str) -> dict:
    prompt = f"""
You are an expert risk analyst reviewing a government RFP response. Identify potential risks based on the provided RFP section and company profile.

Company Profile:
{company_data}

RFP Section:
{chunk_text}

Respond in JSON format:
{{
  "risks_identified": [...],
  "penalties_or_traps": [...],
  "severity": "Low/Medium/High",
  "recommendation": "...",
  "summary": "..."
}}
"""
    return call_gemini(prompt)
