from sentence_transformers import SentenceTransformer

model = None

def get_model():
    global model

    if model is None:
        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return model

def embed_texts(texts):
    return get_model().encode(
        texts,
        convert_to_numpy=True
    )

def embed_texts(texts):

    return model.encode(
        texts,
        convert_to_numpy=True
    )