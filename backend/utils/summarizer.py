from utils.llm import call_gemini

SUMMARY_TEMPLATE = """
You are an expert RFP analyst. Summarize the following outputs across multiple document sections into a clear, professional summary of the {agent_type} findings.

Respond in plain English.

--- Begin Outputs ---
{outputs}
--- End Outputs ---
"""

def summarize_agent_outputs(agent_outputs: list[dict], agent_type: str) -> str:
    outputs_text = "\n\n".join([str(o) for o in agent_outputs if o])
    prompt = SUMMARY_TEMPLATE.format(agent_type=agent_type, outputs=outputs_text)
    response = call_gemini(prompt)
    return response.get("summary", response) if isinstance(response, dict) else response
