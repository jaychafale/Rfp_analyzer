import os
from vector_store.faiss_store import FAISSVectorStore

def store_embeddings(vectors, texts, db_name="default"):
    if os.getenv("VECTOR_DB_TYPE") == "faiss":
        faiss_store = FAISSVectorStore()
        faiss_store.store_embeddings(vectors, texts, db_name)
        return faiss_store
    else:
        raise ValueError("ChromaDB not available. Install chromadb and Visual C++ Build Tools.")
