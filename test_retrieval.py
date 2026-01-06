from ingest import get_chunks
from retriever import embed_texts, build_faiss_index, semantic_search

chunks = get_chunks()
texts = [c["text"] for c in chunks]

embeddings = embed_texts(texts)
index = build_faiss_index(embeddings)

query = "How are customer payments protected?"
results = semantic_search(query, index, chunks)

for res in results:
    print(res["source"])
    print(res["text"][:300])
    print()
