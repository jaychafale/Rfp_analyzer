import re
from typing import List

def chunk_pdf_text(text: str, max_chunk_length: int = 800) -> List[str]:
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Split on paragraph boundaries
    paragraphs = re.split(r"(?<=[.?!])\s+(?=[A-Z])", text)

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk_length:
            current_chunk += " " + para
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
