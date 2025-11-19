from functools import reduce
from itertools import combinations
import math

def tokenize_and_weight(text_block):
    tokens = text_block.lower().replace(',', '').split()
    freq_map = {}
    for token in tokens:
        freq_map[token] = freq_map.get(token, 0) + 1
    return freq_map

def compute_entropy(freq_dict):
    total = sum(freq_dict.values())
    probs = [count / total for count in freq_dict.values()]
    return -sum(p * math.log(p) for p in probs if p > 0)

corpus_snippet = "The quick brown fox jumps over the lazy dog, and the dog barks back at the fox"
token_frequencies = tokenize_and_weight(corpus_snippet)

# Apply transformation weights using dictionary comprehension
weights = {word: len(word) for word in token_frequencies}
weighted_freq = {w: f * weights[w] for w, f in token_frequencies.items()}

# Merge with positional bonus (dynamic programming approach)
positional_bonus = {word: idx for idx, word in enumerate(sorted(weighted_freq.keys()), 1)}
final_scores = {w: weighted_freq[w] + positional_bonus[w] for w in weighted_freq}

# Compute combinatorial diversity measure
unique_words = list(final_scores.keys())
combos = list(combinations(unique_words, 2))
diversity_impact = sum(abs(final_scores[a] - final_scores[b]) for a, b in combos)

# Statistical normalization
values = list(final_scores.values())
mean_val = sum(values) / len(values)
sq_diffs = [(x - mean_val) ** 2 for x in values]
variance = sum(sq_diffs) / len(values)

# Lexical richness computation
lexical_richness_score = int(round((diversity_impact / len(combos)) * math.sqrt(variance)))
print(f"Result: {lexical_richness_score}")