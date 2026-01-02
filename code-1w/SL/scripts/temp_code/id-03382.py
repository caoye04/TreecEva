from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            count += 1
    return count

def compute_final_score(data):
    total = sum(data)
    adjustment = len([x for x in data if x > 5])
    bonus = 0
    if any(x % 7 == 0 for x in data):
        bonus = 10
    return total + adjustment + bonus

def validate_sequence(seq):
    chars = set('ACGT')
    return all(c in chars for c in seq)

dna_sequence = 'AGCTAGGATACGT'

# Irrelevant processing: analyzing nucleotide but not used in final result
nucleotide_count = analyze_pattern(dna_sequence)

# Misleading data transformation
transformed_values = [ord(c) - 65 for c in dna_sequence]
filtered_vals = [v for v in transformed_values if v < 15]

# Core data for computation
raw_input = [3, 7, 9, 2, 8, 14, 5]

# Distractor: complex combination generation with no impact
useless_pairs = list(combinations(raw_input, 2))
sum_of_pairs = sum(a * b for a, b in useless_pairs)  # Dead-end computation

# Semi-relevant filtering
processed_data = [x for x in raw_input if x % 2 != 0]

# Another distraction: sorting and reversing with no use
sorted_reversed = sorted(processed_data, reverse=True)
max_val = max(sorted_reversed) if sorted_reversed else 0

# Key computational step
final_score = compute_final_score(processed_data)

# Print required output
print(f"Result: {final_score}")