def generate_prompt_for_agent(agent: str, rfp_chunk: str, company_profile: str):
    base = {
        "compliance": f"""You are a legal expert checking for proposal compliance.

Given the RFP section below and company profile, identify any compliance issues or mismatches.

RFP Section:
{rfp_chunk}

Company Profile:
{company_profile}

Respond in JSON with:
{{"compliance_issues": [...], "verdict": "...", "summary": "..."}}""",

        "eligibility": f"""You are an eligibility assessor for government contracts.

Compare the RFP section against the company profile to extract and verify eligibility criteria.

RFP Section:
{rfp_chunk}

Company Profile:
{company_profile}

Respond in JSON with:
{{"eligibility_criteria": [...], "missing_requirements": [...], "verdict": "...", "summary": "..."}}""",

        "risk": f"""You're an AI risk advisor.

Identify potential risks from this RFP section that might impact the bidding company based on their profile.

RFP Section:
{rfp_chunk}

Company Profile:
{company_profile}

Respond in JSON with:
{{"risks_identified": [...], "penalties_or_traps": [...], "severity": "...", "recommendation": "..."}}""",

        "checklist": f"""You're an AI assistant helping build a submission checklist.

Extract all mandatory deliverables, formats, deadlines from this RFP section.

RFP Section:
{rfp_chunk}

Respond in JSON with:
{{"required_documents": [...], "formatting_requirements": [...], "deadlines": [...], "summary": "..."}}"""
    }

    return base[agent]
