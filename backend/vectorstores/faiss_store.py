from utils.embedder import embed_text
import faiss
import numpy as np

def store_and_search_chunks(chunks: list[str], top_k=10) -> list[str]:
    embeddings = [embed_text(c) for c in chunks]

    # Filter out invalid embeddings
    valid_pairs = [(chunk, emb) for chunk, emb in zip(chunks, embeddings) if emb and len(emb) == 768]
    if not valid_pairs:
        raise ValueError("No valid embeddings generated for any chunks.")

    valid_chunks, valid_embeddings = zip(*valid_pairs)

    matrix = np.array(valid_embeddings).astype("float32")
    dim = matrix.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(matrix)

    query_vector = matrix[0].reshape(1, -1)
    distances, indices = index.search(query_vector, top_k)

    return [valid_chunks[i] for i in indices[0]]
