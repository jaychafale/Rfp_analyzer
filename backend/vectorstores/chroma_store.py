#import chromadb
#from chromadb.utils import embedding_functions

class ChromaVectorStore:
    def __init__(self, collection_name="rfp_collection"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_embeddings(self, embeddings, texts):
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=[str(i) for i in range(len(texts))]
        )

    def search(self, query_embedding, top_k=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results['documents'][0]
