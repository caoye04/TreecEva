from itertools import permutations
from collections import Counter
from dataclasses import dataclass

genomic_sequences = ['atgc', 'tgcA', 'GCAT', 'catg']
base_weights = {'A': 2, 'T': 3, 'G': 5, 'C': 7}

# Define a decorator for logging function calls
def log_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_calls
def compute_weighted_score(freq_dict):
    score = 0
    for base, count in freq_dict.items():
        if base in base_weights:
            score += count * base_weights[base]
    return score

# Process sequences
processed_sequences = []
for seq in genomic_sequences:
    # Convert to uppercase
    upper_seq = seq.upper()
    # Replace 'A' with 'X' temporarily for pattern analysis
    modified_seq = upper_seq.replace('A', 'X')
    processed_sequences.append(modified_seq)

# Count all characters in processed sequences
all_chars = ''.join(processed_sequences)
frequency_count = Counter(all_chars)

# Apply combinatorics to generate possible base arrangements
bases = list('XTGC')
perm_count = len(list(permutations(bases, 2)))

# Calculate final score using lambda closure
adjustment_factor = perm_count
scoring_func = lambda freq: compute_weighted_score(freq) * adjustment_factor
final_score = scoring_func(frequency_count)

print(f'Result: {final_score}')