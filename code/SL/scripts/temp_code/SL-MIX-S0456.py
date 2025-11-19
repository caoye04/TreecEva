from collections import defaultdict
from itertools import permutations
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        wrapper.execution_time = end - start
        return result
    return wrapper

class ResourceContext:
    def __enter__(self):
        self.resource_data = defaultdict(int)
        return self.resource_data
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

@timing_decorator
def compute_similarity(tokens1, tokens2):
    # Compute similarity as number of common permutations of length 2
    perms1 = set(permutations(tokens1, 2))
    perms2 = set(permutations(tokens2, 2))
    return len(perms1.intersection(perms2))

documents = [
    "machine learning algorithms",
    "deep learning neural networks",
    "reinforcement learning agents"
]

tokenized_docs = [doc.split() for doc in documents]

aggregate_score = 0

with ResourceContext() as resources:
    for i in range(len(tokenized_docs)):
        for j in range(i+1, len(tokenized_docs)):
            score = compute_similarity(tokenized_docs[i], tokenized_docs[j])
            aggregate_score += score * (i+j)
            resources[f'doc_pair_{i}_{j}'] = score

# Apply correction factor based on decorator timing
if hasattr(compute_similarity, 'execution_time'):
    aggregate_score = int(aggregate_score / (compute_similarity.execution_time * 1000 + 1))

print(f"Result: {aggregate_score}")