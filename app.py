import streamlit as st

from ingest import get_chunks
from retriever import embed_texts, build_faiss_index, semantic_search
from generator import generate_answer

st.set_page_config(page_title="Construction AI Assistant", layout="wide")

st.title("🏗️ Construction Marketplace AI Assistant")

st.markdown(
    "This assistant answers questions using internal construction documents only. "
    "Responses are generated strictly from retrieved document content."
)

@st.cache_resource
def setup_rag():
    chunks = get_chunks()
    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)
    index = build_faiss_index(embeddings)
    return chunks, index


chunks, index = setup_rag()

question = st.text_input("Enter your question")

if question:
    retrieved_chunks = semantic_search(question, index, chunks, top_k=3)
    answer = generate_answer(question, retrieved_chunks)

    st.subheader("Retrieved Context")
    for i, chunk in enumerate(retrieved_chunks, 1):
        with st.expander(f"Context {i} ({chunk['source']})"):
            st.write(chunk["text"])

    st.subheader("Final Answer")
    st.success(answer)
