# agents/prompt_engineer.py

def generate_prompt(category: str, chunk: str, company_data: str) -> str:
    if category == "compliance":
        return f"""
You are a compliance expert.

Given the following RFP section and company background, identify any compliance issues.

RFP Section:
{chunk}

Company Data:
{company_data}

Respond in JSON with keys:
- compliance_issues
- verdict
- summary
"""
    elif category == "eligibility":
        return f"""
You are an eligibility analyst for government contracts.

Given the RFP chunk and the company's data, extract required eligibility criteria and determine if the company qualifies.

RFP:
{chunk}

Company:
{company_data}

Respond in JSON:
- eligibility_criteria
- missing_requirements
- verdict
- summary
"""
    elif category == "risk":
        return f"""
You are a legal risk analyst.

Analyze this RFP chunk in the context of the company profile and identify legal or operational risks.

RFP:
{chunk}

Company:
{company_data}

Return JSON with:
- risks_identified
- penalties_or_traps
- severity
- recommendation
"""
    elif category == "checklist":
        return f"""
You are a contracts assistant.

Extract submission checklist items based on this RFP section. Include formatting, deadlines, documents, and key steps.

RFP Section:
{chunk}

Respond in JSON:
- required_documents
- formatting_requirements
- deadlines
- summary
"""
    else:
        return f"Invalid category: {category}"


# 🔁 Add this helper function
def generate_prompts_for_chunk(chunk: str, company_data: str) -> dict:
    return {
        "compliance": generate_prompt("compliance", chunk, company_data),
        "eligibility": generate_prompt("eligibility", chunk, company_data),
        "risk": generate_prompt("risk", chunk, company_data),
        "checklist": generate_prompt("checklist", chunk, company_data),
    }
