from collections import defaultdict
import math

documents = [
    "machine learning algorithms optimize performance",
    "deep learning neural networks process data",
    "reinforcement learning agents explore environments",
    "supervised learning models classify inputs"
]

term_freq = defaultdict(int)
doc_freq = defaultdict(int)
total_docs = len(documents)

for doc in documents:
    tokens = doc.lower().split()
    unique_terms = set(tokens)
    for term in unique_terms:
        doc_freq[term] += 1
    for token in tokens:
        term_freq[token] += 1

idf_scores = {}
for term in doc_freq:
    idf_scores[term] = math.log(total_docs / doc_freq[term])

query = "learning algorithms neural networks"
query_tokens = query.lower().split()

score_accumulator = 0
processed_terms = set()

for term in query_tokens:
    if term in term_freq and term not in processed_terms:
        tf = term_freq[term]
        idf = idf_scores.get(term, 0)
        score_accumulator += (tf * idf) % 7
        processed_terms.add(term)

# Execution point Y
final_score = int(score_accumulator * 10) % 13
print(f"Result: {final_score}")