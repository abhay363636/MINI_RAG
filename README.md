# 🏗️ Construction Marketplace AI Assistant (Mini RAG)

## Overview
This project implements a **Mini Retrieval-Augmented Generation (RAG) chatbot** for a construction marketplace.
The assistant answers user queries **strictly using internal documents** such as policies, specifications, and FAQs,
rather than relying on general model knowledge.

The system retrieves relevant document sections using semantic search and generates answers **grounded only in the
retrieved content**, ensuring transparency and minimizing hallucinations.

---

## Key Features
- Semantic document retrieval using embeddings and FAISS
- Grounded answer generation using an LLM
- Clear transparency by displaying retrieved document context
- Robust document ingestion with handling of non-standard PDFs
- Deployed interactive chatbot using Streamlit

---

## Architecture & Flow

1. **Document Ingestion**
   - Internal PDF documents are loaded and parsed.
   - Documents are split into meaningful overlapping text chunks.

2. **Embedding & Indexing**
   - Each chunk is converted into a vector embedding.
   - A local FAISS index is built for efficient semantic retrieval.

3. **Retrieval**
   - For a user query, the system retrieves the top-k most relevant chunks based on cosine similarity.

4. **Answer Generation**
   - Retrieved chunks are passed to a Large Language Model.
   - The model is explicitly instructed to answer **only using the retrieved context**.

5. **User Interface**
   - A Streamlit-based chatbot allows users to ask questions and view:
     - Retrieved document context
     - Final generated answer

---

## Technologies Used

### Embedding Model
- **sentence-transformers/all-MiniLM-L6-v2**
- Chosen for its efficiency, strong semantic performance, and suitability for local RAG pipelines.

### Vector Store
- **FAISS (local)**
- Enables fast and accurate semantic similarity search without external services.

### Language Model
- **Mistral (via OpenRouter)**
- Used for answer generation with temperature set to zero to ensure deterministic, grounded responses.

### UI Framework
- **Streamlit**
- Provides a lightweight and effective interface for deploying the chatbot.

---

## Document Chunking Strategy
- Chunk size: ~400 words
- Overlap: ~50 words

This approach preserves contextual continuity while improving retrieval relevance.

---

## Grounding & Hallucination Control
To enforce grounding:
- The LLM prompt explicitly instructs the model to answer **only from retrieved document chunks**.
- If the answer is not present in the retrieved context, the model responds:
  > *“I do not have enough information in the provided documents.”*

This ensures factual consistency and avoids unsupported claims.

---

## Handling Non-Standard PDFs
One internal document contained a non-standard PDF structure that could not be parsed initially.
This document was repaired using OCR to convert it into a searchable, text-based PDF before ingestion.

The ingestion pipeline is designed to:
- Gracefully skip unreadable files
- Log errors without breaking the pipeline

---

## Project Structure

```
MINI_RAG/
│
├── app.py                 Streamlit chatbot UI
├── ingest.py              Document loading and chunking
├── retriever.py           Embeddings and FAISS retrieval
├── generator.py           Grounded LLM answer generation
│
├── tests/
│   ├── test_retrieval.py
│   └── test_generation.py
│
├── data/
│   └── docs/               Internal PDF documents
│
├── requirements.txt      Python dependencies
└── README.md
```

---

## How to Run the Project Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set OpenRouter API key
```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

### 3. Run the chatbot
```bash
streamlit run app.py
```

The application will open in your browser.

---

## Testing
Basic test scripts are included to validate:
- Retrieval relevance (`test_retrieval.py`)
- Grounded answer generation (`test_generation.py`)

These are kept separate from the main application logic.

---

## Limitations
- The system answers only based on the provided internal documents.
- It does not use external knowledge or real-time data.
- Answer quality depends on the coverage and clarity of the source documents.

---

## Conclusion
This project demonstrates a complete, transparent, and robust Mini RAG pipeline with local vector search,
grounded LLM responses, and a deployed chatbot interface. It adheres closely to the assignment requirements
while reflecting real-world engineering considerations.
# MINI_RAG
