import re
from functools import reduce

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Machine learning models require extensive training",
    "Natural language processing enables human-computer interaction",
    "Deep neural networks consist of multiple layers"
]

def tokenize(sentence):
    return re.findall(r'\b\w+\b', sentence)

def calculate_density(tokens):
    if not tokens:
        return 0
    total_length = reduce(lambda acc, word: acc + len(word), tokens, 0)
    avg_length = total_length / len(tokens)
    return len(tokens) * avg_length

# Process sentences and compute scores
sentence_scores = {i: calculate_density(tokenize(sent)) for i, sent in enumerate(sentences)}

# Find maximum density score
max_density_score = max(sentence_scores.values())

print(f"Result: {max_density_score}")