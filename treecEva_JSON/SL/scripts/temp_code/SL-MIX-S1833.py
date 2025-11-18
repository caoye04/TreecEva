from itertools import combinations

genetic_markers = ['MARKER_A', 'MARKER_B', 'MARKER_C', 'MARKER_D', 'MARKER_E', 'MARKER_F']
score_threshold = 85

# Proprietary scoring function for marker combinations
def calculate_marker_score(marker_set):
    base_score = sum(hash(marker) % 100 for marker in marker_set)
    interaction_bonus = 10 if 'MARKER_A' in marker_set and 'MARKER_D' in marker_set else 0
    return base_score + interaction_bonus

# Generate all possible 3-marker combinations
all_combinations = list(combinations(genetic_markers, 3))

# Calculate scores for each combination
combination_scores = [calculate_marker_score(combo) for combo in all_combinations]

# Count combinations exceeding threshold
significant_combinations_count = sum(1 for score in combination_scores if score > score_threshold)

# Apply ternary operator for final adjustment
significant_combinations_count = significant_combinations_count + 5 if significant_combinations_count > 10 else significant_combinations_count * 2

print(f"Result: {significant_combinations_count}")