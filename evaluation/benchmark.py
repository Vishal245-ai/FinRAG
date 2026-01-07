from main import ask_question
from sentence_transformers import SentenceTransformer, util
from evaluation.numeric_faithfulness import numeric_faithfulness

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_accuracy (pred, gold):
    e1 = model.encode(pred)
    e2 = model.encode(gold)
    return util.cos_sim (e1,e2).item()

def run_benchmark(dataset):
    scores = []
    for item in dataset:
        answer, _ = ask_question(item['question'])
        score = semantic_accuracy(answer, item["answer"])
        scores.append(score)
    return sum(scores)/ len(scores)