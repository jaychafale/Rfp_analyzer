from agents.compliance_agent import analyze_compliance
from agents.eligibility_agent import analyze_eligibility
from agents.risk_agent import analyze_risk
from agents.checklist_agent import generate_checklist

def run_tagged_pipeline(tagged_sections: list):
    results = []

    for section in tagged_sections:
        label = section["label"]
        text = section["text"]
        output = {}

        if label == "Compliance":
            output = analyze_compliance(text)
        elif label == "Eligibility":
            output = analyze_eligibility(text)
        elif label == "Risk":
            output = analyze_risk(text)
        elif label == "Checklist":
            output = generate_checklist(text)
        else:
            output = {"error": f"Unknown label: {label}"}

        results.append({
            "label": label,
            "text": text,
            "analysis": output
        })

    return results
