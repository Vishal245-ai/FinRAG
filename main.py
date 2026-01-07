from pathlib import Path
from prompt_toolkit import prompt
from retrieval.embeddings import EmbeddingModel
from retrieval.vector_store import VectorStore
from generation.prompt import build_prompt
from generation.llm import generate_answer
import streamlit as st

Basedir = Path(__file__).resolve().parent

@st.cache_resource
def load_embedder():
    return EmbeddingModel()

@st.cache_resource
def load_store():
    return VectorStore(
        index_path = Basedir / "data" / "faiss.index",
        chunks_path = Basedir / "data" / "chunks.json" )

embedder = load_embedder()
store = load_store()

def ask_question(question, k=5):
    # Guard: empty question
    if not question or len(question.strip()) < 3:
        return "Please enter a valid question.", []

    # Guard: investment advice
    if "invest" in question.lower():
        return "This system does not provide investment advice.", []

    try:
        q_emb = embedder.encode([question])
        context = store.search(q_emb, k)

        prompt = build_prompt(context, question)
        answer = generate_answer(prompt)

        # Safety: ensure answer is always a string
        if not isinstance(answer, str):
            answer = "⚠️ Answer generation failed."

        return answer, context

    except Exception as e:
        # CRITICAL: always return a tuple
        return f"⚠️ System error: {e}", []

