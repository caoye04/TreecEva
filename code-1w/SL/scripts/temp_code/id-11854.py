from itertools import combinations

def analyze_text_similarity(documents):
    word_sets = [set(doc.lower().split()) for doc in documents]
    
    similarity_scores = []
    for i, j in combinations(range(len(documents)), 2):
        common_words = word_sets[i] & word_sets[j]
        union_words = word_sets[i] | word_sets[j]
        if union_words:
            jaccard_index = len(common_words) / len(union_words)
            similarity_scores.append(jaccard_index)
    
    total_similarity = sum(similarity_scores)
    return total_similarity

# Sample documents
docs = [
    "machine learning models improve with more data",
    "deep learning models require large datasets",
    "more data helps machine learning performance"
]

result = analyze_text_similarity(docs)
total_similarity = result
print(f"Result: {total_similarity}")