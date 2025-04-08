from utils.llm import call_gemini
from agents.prompt_engineer import generate_prompts_for_chunk
from agents.compliance_agent import analyze_compliance
from agents.eligibility_agent import analyze_eligibility as check_eligibility
from agents.risk_agent import analyze_risk
from agents.checklist_agent import generate_checklist
from utils.chunking import chunk_pdf_text
from utils.summarizer import summarize_agent_outputs  # ✅ new

def run_dynamic_pipeline(rfp_text: str, company_text: str):
    chunks = chunk_pdf_text(rfp_text)

    all_compliance, all_eligibility, all_risk, all_checklist = [], [], [], []

    for chunk in chunks:
        prompts = generate_prompts_for_chunk(chunk, company_text)

        all_compliance.append(analyze_compliance(prompts["compliance"], company_text))
        all_eligibility.append(check_eligibility(prompts["eligibility"], company_text))
        all_risk.append(analyze_risk(prompts["risk"], company_text))
        all_checklist.append(generate_checklist(prompts["checklist"], company_text))



    return {
        "compliance": summarize_agent_outputs(all_compliance, "compliance"),
        "eligibility": summarize_agent_outputs(all_eligibility, "eligibility"),
        "risk": summarize_agent_outputs(all_risk, "risk"),
        "checklist": summarize_agent_outputs(all_checklist, "checklist")
    }

