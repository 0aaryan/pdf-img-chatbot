from langchain_community.vectorstores import Qdrant


class QdrantDB:
    def __init__(self,collection_name,docs,embeddings):
        self.collection_name = collection_name
        self.db = Qdrant.from_documents(
            docs,
            embeddings,
            location=":memory:", 
            collection_name="my_documents",
        )

    def query(self,query , k = 5):
        return self.db.similarity_search_with_score(query, k=k)
    
    