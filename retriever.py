import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed_texts(texts):
    return model.encode(texts, normalize_embeddings=True)


def build_faiss_index(embeddings):
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    return index


def semantic_search(query, index, chunks, top_k=3):
    query_embedding = model.encode([query], normalize_embeddings=True)
    scores, indices = index.search(query_embedding, top_k)

    return [
        {
            "score": float(score),
            "source": chunks[idx]["source"],
            "text": chunks[idx]["text"]
        }
        for idx, score in zip(indices[0], scores[0])
    ]
