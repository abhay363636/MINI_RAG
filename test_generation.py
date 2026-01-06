from ingest import get_chunks
from retriever import embed_texts, build_faiss_index, semantic_search
from generator import generate_answer

chunks = get_chunks()
texts = [c["text"] for c in chunks]

embeddings = embed_texts(texts)
index = build_faiss_index(embeddings)

question = "How are customer payments protected?"
retrieved = semantic_search(question, index, chunks)

answer = generate_answer(question, retrieved)

print(answer)
