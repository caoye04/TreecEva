import itertools
import statistics
from functools import reduce

def char_frequency_analyzer(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def calculate_variance_score(freq_dict):
    frequencies = list(freq_dict.values())
    if len(frequencies) < 2:
        return 0
    return statistics.variance(frequencies)

cipher_segment = "ABBCDEEFFGHHIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
frequency_map = char_frequency_analyzer(cipher_segment)
variance_score = calculate_variance_score(frequency_map)

# Generate all possible 3-character permutations from unique characters
unique_chars = list(set(cipher_segment))
permutations = list(itertools.permutations(unique_chars, 3))

# Apply greedy algorithm to select permutations with highest ASCII sum
permutation_scores = [(perm, sum(ord(c) for c in perm)) for perm in permutations]
permutation_scores.sort(key=lambda x: x[1], reverse=True)
top_permutations = permutation_scores[:10]

# Calculate combinatorial weight factor
weight_factor = len(list(itertools.combinations(range(10), 3)))

# Encode top permutations into numeric sequence
encoded_sequence = []
for perm, score in top_permutations:
    encoded_value = reduce(lambda acc, char: acc * 256 + ord(char), perm, 0)
    encoded_sequence.append(encoded_value)

# Final cipher score combines variance, weight factor, and encoded sequence properties
final_cipher_score = int(variance_score * weight_factor + statistics.mean(encoded_sequence) // 1000)

print(f"Result: {final_cipher_score}")