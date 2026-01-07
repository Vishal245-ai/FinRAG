FinRAG – Financial Document Question Answering System

FinRAG is an end-to-end Retrieval-Augmented Generation (RAG) system designed for question answering over financial documents (e.g., SEC 10-K filings).
It combines FAISS vector search, local LLMs via Ollama, and custom evaluation metrics to ensure accurate, faithful, and explainable answers.

# Key Features

- Semantic retrieval using FAISS vector search
- Local LLM inference with Ollama (no external APIs)
- Designed for financial documents (10-K, reports, PDFs)

# Evaluation metrics shown in Streamlit UI
Numeric Faithfulness
Numeric Accuracy (continuous 0–1)
Semantic Recall@K

# Guardrails
Blocks investment advice
Rejects vague / short queries

# Interactive Streamlit application

# Project Architecture
FinRAG/
│
├── app/
│   └── app1.py                 # Streamlit UI
│
├── data/
│   ├── chunks.json             # Text chunks
│   ├── faiss.index             # FAISS vector index
│   └── metadata.json           # Chunk metadata
│
├── evaluation/
│   ├── benchmark.py
│   ├── numeric_accuracy.py     # Continuous numeric accuracy (0–1)
│   ├── numeric_faithfulness.py # Hallucination check for numbers
│   ├── numeric_utils.py        # Number extraction utilities
│   └── retrieval_metrics.py    # Semantic Recall@K
│
├── generation/
│   ├── llm.py                  # Ollama LLM interface
│   └── prompt.py               # Prompt construction
│
├── ingestion/
│   ├── pdf_parser.py           # PDF text extraction
│   └── chunker.py              # Document chunking
│
├── retrieval/
│   ├── embeddings.py           # Embedding model
│   └── vector_store.py         # FAISS wrapper
│
├── main.py                     # Core RAG pipeline
├── .env                        # Environment variables
├── .gitignore
└── README.md

#️ Tech Stack

Python 3.10+
FAISS – vector similarity search
Sentence Transformers – embeddings
Ollama – local LLM inference
Streamlit – UI
PyPDF – PDF parsing

# RAG Pipeline Overview

Ingestion
PDFs parsed and chunked
Embedding
Chunks embedded using sentence-transformers
Vector Search
FAISS retrieves top-K relevant chunks
Prompt Construction
Context + question → structured prompt
Answer Generation
Ollama LLM generates answer
Evaluation
Faithfulness, accuracy, and retrieval quality measured

# Evaluation Metrics (Displayed in UI)
1️⃣ Numeric Faithfulness (0–1)

Checks whether numbers in the answer appear in retrieved context
→ Detects numeric hallucinations

2️⃣ Numeric Accuracy (0–1)

Measures how close predicted numbers are to document numbers
→ Continuous score (not binary)

3️⃣ Semantic Recall@K (0–1)

Measures whether retrieved chunks semantically cover the question

# Running the App
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start Ollama
ollama serve
ollama pull mistral   # or llama3

3️⃣ Launch Streamlit
streamlit run app/app1.py

# Example Questions

What reporting requirements are described under Section 13(a) in the 10-K?
What internal controls are disclosed for financial reporting?
What was the total debt at year end?

# Safety & Guardrails

❌ Investment advice blocked
❌ Vague questions rejected
❌ Hallucinated numbers flagged
✅ Context-only answering enforced

# Why FAISS Instead of Chroma / LangChain?
FAISS → faster, production-grade vector search
Custom RAG logic → full control & transparency
No LangChain/LangGraph → reduced abstraction, easier debugging
Designed for ML/Data Science portfolios, not black-box pipelines

# Resume-Ready Project Description (ATS-Optimized)

FinRAG – Financial Document QA System
Built an end-to-end Retrieval-Augmented Generation (RAG) system using FAISS, Ollama LLMs, and Streamlit to answer complex financial queries from SEC 10-K filings with evaluation metrics for faithfulness, numeric accuracy, and retrieval quality.

# Use Cases

Financial document analysis
Compliance & audit support
Earnings report summarization
Internal knowledge assistants
Research & due-diligence tools

# Future Enhancements
Multi-document comparison
Table extraction
Hybrid BM25 + vector search
LangGraph-based agent routing
Fine-grained citation highlighting
