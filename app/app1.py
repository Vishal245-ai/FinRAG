import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from main import ask_question
from evaluation.numeric_faithfulness import numeric_faithfulness
from evaluation.numeric_accuracy import numeric_accuracy
from evaluation.numeric_utils import extract_numbers
from evaluation.retrieval_metrics import recall_at_k_semantic
from sentence_transformers import SentenceTransformer

@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

embedder = load_embedder()

st.set_page_config (page_title = "FinRAG", layout = "wide")

st.title(" FinRAG - Financial Document QA")

question = st.text_input ("Ask a financial question:")

if st.button("Analyze"):
    with st.spinner ("Analyzing financial documents..."):
        answer, sources = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Evaluation Metrics")

        try:
            faithfulness_score = numeric_faithfulness(answer, sources)

            col1, col2, col3 = st.columns(3)

            col1.metric("Numeric Faithfulness", f"{faithfulness_score:.2f}")

            # Numeric Accuracy
            answer_numbers = extract_numbers(answer)
            with col2:
                if answer_numbers:
                    context_numbers = []
                    for c in sources:
                        context_numbers.extend(extract_numbers(c))

                    if context_numbers:
                        accuracy_score = numeric_accuracy(
                            predicted=answer_numbers[0],
                            ground_truth=context_numbers[0]
                        )
                        st.metric("Numeric Accuracy", f"{accuracy_score:.2f}")
                    else:
                        st.metric("Numeric Accuracy", "N/A")
                else:
                    st.metric("Numeric Accuracy", "N/A")

            # 🔹 Semantic Recall@K
            question_embedding = embedder.encode(question)
            chunk_embeddings = embedder.encode(sources)

            retrieval_score = recall_at_k_semantic(
                chunk_embeddings=chunk_embeddings,
                question_embedding=question_embedding
            )

            col3.metric("Retrieval Recall@K (Semantic)", f"{retrieval_score:.2f}")

            if faithfulness_score < 1.0:
                st.warning("⚠️ Numeric values may not be fully supported by the retrieved documents.")

        except Exception as e:
            st.error("Evaluation failed.")
            st.code(str(e))

        st.subheader(" Retrieved Context")

        for i, s in enumerate(sources):
            with st.expander(f"Chunk {i + 1}"):
                st.write(s)