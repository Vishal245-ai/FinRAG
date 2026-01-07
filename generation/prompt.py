'''
def build_prompt(context, question):
    if not context:
        context_text = "No relevant context found in the documents."
    else:
        # Extract text safely (handles dict or string)
        context_text = "\n\n".join(
            c["text"] if isinstance(c, dict) and "text" in c else str(c)
            for c in context
        )

    prompt = f"""
You are a financial analyst assistant.
Answer ONLY using the context below.
Do not speculate or provide investment advice.
If the answer is not found, say: "Not disclosed in documents."

Context:
{context_text}

Question:
{question}

Answer:
"""
    return prompt.strip()
'''
def build_prompt(context, question):
    if not context:
        context_text = "No relevant context found."
    else:
        context_text = "\n\n".join(context)

    return f"""
You are a financial document question-answering system.

STRICT RULES:
- Answer ONLY the exact question asked.
- Use ONLY the provided context.
- DO NOT rephrase the question.
- DO NOT explain your reasoning.
- DO NOT provide background or interpretations.
- If the answer is not explicitly stated, reply exactly:
  "Not disclosed in documents."

Context:
{context_text}

Question:
{question}

Answer:
"""
