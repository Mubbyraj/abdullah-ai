from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorIndex:

    def __init__(self, documents):

        self.documents = documents

        print("Loading Abdullah AI embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


        texts = [
            doc["content"]
            for doc in documents
        ]


        embeddings = self.model.encode(
            texts
        )


        self.dimension = embeddings.shape[1]


        self.index = faiss.IndexFlatL2(
            self.dimension
        )


        self.index.add(
            np.array(embeddings)
        )


        print(
            f"Vector index created: {len(documents)} documents"
        )


    def search(self, query, top_k=3):

        query_vector = self.model.encode(
            [query]
        )


        distances, indices = self.index.search(
            np.array(query_vector),
            top_k
        )


        results = []

        for idx in indices[0]:

            results.append(
                self.documents[idx]
            )

        return results



def create_vector_index(documents):

    vector = VectorIndex(documents)

    return vector, vector.model