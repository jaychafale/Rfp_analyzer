from utils.chunking import chunk_pdf_text
from vectorstores.faiss_store import store_and_search_chunks
from agents.compliance_agent import analyze_compliance
from agents.eligibility_agent import analyze_eligibility
from agents.risk_agent import analyze_risk
from agents.checklist_agent import generate_checklist

def run_rag_pipeline(pdf_text: str, company_data_text: str):
    chunks = chunk_pdf_text(pdf_text)
    top_chunks = store_and_search_chunks(chunks, top_k=10)

    results = []

    for chunk in top_chunks:
        result = {
            "chunk": chunk,
            "compliance": analyze_compliance(chunk, company_data_text),
            "eligibility": analyze_eligibility(chunk, company_data_text),
            "risk": analyze_risk(chunk, company_data_text),
            "checklist": generate_checklist(chunk, company_data_text)
        }
        results.append(result)

    return results
