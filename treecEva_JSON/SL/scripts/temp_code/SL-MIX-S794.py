from itertools import combinations
from collections import defaultdict

genetic_markers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
marker_indices = {marker: idx+1 for idx, marker in enumerate(genetic_markers)}

# Generate all 3-marker combinations
all_combinations = list(combinations(genetic_markers, 3))

# Apply filters
valid_combinations = []
for combo in all_combinations:
    # Filter 1: Cannot contain both A and B
    if 'A' in combo and 'B' in combo:
        continue
    
    # Filter 2: Lexicographical product must not exceed 100
    product = 1
    for marker in combo:
        product *= marker_indices[marker]
    
    if product <= 100:
        valid_combinations.append(combo)

# Score each valid combination by summing ASCII values
combination_scores = {}
for combo in valid_combinations:
    score = sum(ord(marker) for marker in combo)
    combination_scores[combo] = score

# Find the highest scoring combination
if combination_scores:
    max_score = max(combination_scores.values())
else:
    max_score = 0

print(f"Result: {max_score}")