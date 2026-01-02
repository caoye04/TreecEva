from collections import defaultdict

# Simulate a simple vector space model for document ranking
def compute_similarity(query, doc):
    return sum(q * d for q, d in zip(query, doc))

query_vector = [0.8, 1.2, 0.5]
document_vectors = [
    [0.9, 1.0, 0.4],
    [0.2, 0.3, 0.8],
    [1.0, 0.9, 0.6]
]

# Irrelevant baseline scores (distractor)
baseline_scores = [0.5, 0.7, 0.6]

# Ranking documents using similarity score
ranked_docs = []
scores = defaultdict(float)

for i, doc in enumerate(document_vectors):
    score = compute_similarity(query_vector, doc)
    scores[i] = round(score, 4)
    ranked_docs.append((i, score))

# Sort by score descending
ranked_docs.sort(key=lambda x: x[1], reverse=True)

top_doc_index = ranked_docs[0][0]

# Conditional expression to adjust score if top document has high coherence
adjustment = 0.1 if scores[top_doc_index] > 1.8 else 0.0
final_score = scores[top_doc_index] + adjustment

result = final_score

print(f"Result: {result}")