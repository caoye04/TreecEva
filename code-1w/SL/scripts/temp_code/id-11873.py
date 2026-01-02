from itertools import combinations

def analyze_patterns(sequence):
    patterns = []
    for length in range(2, len(sequence) + 1):
        for comb in combinations(sequence, length):
            if sum(comb) % 3 == 0:
                patterns.append(comb)
    return len(patterns)

# Irrelevant function - distractor
def compute_entropy(data):
    from math import log
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Main computation chain
rankings = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Distractor variables
temp_data = ['a', 'b', 'c', 'd']
redundant_calc = sum(x**2 for x in rankings if x > 80)
useless_pairs = list(combinations(temp_data, 2))

# Intermediate weighted mapping
weighted_values = {}
for i, (r, w) in enumerate(zip(rankings, weights)):
    weighted_values[f'item_{i}'] = r * w

# Summation with filtering logic
base_score = sum(weighted_values.values())
bonus = 0.0

# Conditional bonus based on combinatorial pattern count
pattern_count = analyze_patterns(rankings)
if pattern_count > 10:
    bonus = 5.0
elif pattern_count > 5:
    bonus = 2.5
else:
    bonus = 0.0

# Additional irrelevant string manipulation
status_tags = ["high" if r >= 85 else "medium" for r in rankings]
joined_status = "-".join(status_tags)
duplicated_tag = joined_status.split('-')[0] * 2

# Final score calculation - key execution point
final_score = base_score + bonus

print(f"Result: {final_score}")