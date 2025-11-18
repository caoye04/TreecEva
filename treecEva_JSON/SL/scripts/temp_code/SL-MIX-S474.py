import itertools

# Genetic marker indices
markers = frozenset([1, 2, 3, 4, 5, 6])

# Function to calculate combination score
score_func = lambda combo: sum(a ^ b for a, b in itertools.combinations(combo, 2)) + sum(combo)

# Generate all 3-marker combinations
combinations = list(itertools.combinations(markers, 3))

# Calculate scores for all combinations
combination_scores = [score_func(combo) for combo in combinations]

# Find the highest score
max_score = max(combination_scores)

print(f"Result: {max_score}")