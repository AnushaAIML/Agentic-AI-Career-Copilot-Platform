import faiss
import numpy as np

from backend.rag.embedder import embed_texts


class FAISSStore:

    def __init__(self):

        self.index = None
        self.documents = []

    def build(self, docs):

        texts = [
            doc["text"]
            for doc in docs
        ]

        embeddings = embed_texts(texts)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings.astype(
                np.float32
            )
        )

        self.documents = docs

    def search(
        self,
        query,
        k=3
    ):

        query_embedding = embed_texts(
            [query]
        )

        distances, indices = self.index.search(
            query_embedding.astype(
                np.float32
            ),
            k
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.documents[idx]
            )

        return results