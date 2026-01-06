import os
import pdfplumber

DATA_DIR = "data/docs"
CHUNK_SIZE = 400
CHUNK_OVERLAP = 50


def load_pdfs():
    documents = []

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(DATA_DIR, filename)
            text = ""

            try:
                with pdfplumber.open(path) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
            except Exception:
                continue

            if text.strip():
                documents.append({
                    "source": filename,
                    "text": text
                })

    return documents


def chunk_text(text):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + CHUNK_SIZE
        chunks.append(" ".join(words[start:end]))
        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def get_chunks():
    all_chunks = []
    documents = load_pdfs()

    for doc in documents:
        for i, chunk in enumerate(chunk_text(doc["text"])):
            all_chunks.append({
                "source": doc["source"],
                "chunk_id": i,
                "text": chunk
            })

    return all_chunks
