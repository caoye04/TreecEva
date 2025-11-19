import hashlib

def word_hash(word):
    return int(hashlib.md5(word.encode()).hexdigest(), 16) % 1000

text_pipeline = [
    "neural", "algorithm", "optimization", "heuristic",
    "synthesis", "abstraction", "computation", "inference"
]

# Transform words using lambda and filter based on length
filtered_words = list(filter(lambda w: len(w) > 7, text_pipeline))
transformed_hashes = [word_hash(w.upper()) for w in filtered_words]

# Initialize score
coherence_score = 0

# Logical chain with short-circuit evaluation
for h in transformed_hashes:
    if h > 500 and (h % 7 == 0 or h % 11 == 0):
        coherence_score += h
    elif not (h <= 200 or h >= 800):
        coherence_score -= h // 2

# Final adjustment using logical operations
coherence_score = coherence_score if coherence_score > 0 else (coherence_score & 0xFF)

print(f"Result: {coherence_score}")