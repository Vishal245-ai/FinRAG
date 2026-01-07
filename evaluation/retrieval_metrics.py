import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recall_at_k_semantic(chunk_embeddings, question_embedding):
    """
    Returns the maximum cosine similarity between the question
    embedding and retrieved chunk embeddings.
    
    chunk_embeddings: np.ndarray of shape (k, d)
    question_embedding: np.ndarray of shape (d,) or (1, d)
    """
    if len(chunk_embeddings) == 0:
        return 0.0

    question_embedding = np.atleast_2d(question_embedding)

    similarities = cosine_similarity(chunk_embeddings, question_embedding)
    return float(np.max(similarities))
