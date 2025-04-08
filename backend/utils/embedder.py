from utils.llm import call_gemini_embedding

def embed_text(text: str) -> list[float]:
    return call_gemini_embedding(text)
