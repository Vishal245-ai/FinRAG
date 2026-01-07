import faiss
import json

class VectorStore:
    def __init__ (self, index_path, chunks_path):
        self.index = faiss.read_index(str(index_path))
        with open(chunks_path) as f:
            self.chunks = json.load(f)

    def search(self, query_embedding, k = 5):
        _, indices = self.index.search(query_embedding , k)
        return [self.chunks[i] for i in indices[0]]
