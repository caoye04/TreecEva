from itertools import combinations

genetic_markers = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6']
marker_scores = {'A1': 7, 'B2': 3, 'C3': 9, 'D4': 2, 'E5': 8, 'F6': 4}

# Define filtering criteria using lambda functions
valid_marker = lambda m: marker_scores[m] > 3
high_score_marker = lambda m: marker_scores[m] > 6
not_adjacent = lambda m1, m2: abs(ord(m1[0]) - ord(m2[0])) != 1

# Generate all possible 3-marker combinations
all_combinations = list(combinations(genetic_markers, 3))

# Apply filtering logic with multiple conditions
filtered_combinations = [
    combo for combo in all_combinations
    if all(valid_marker(marker) for marker in combo) and
       any(high_score_marker(marker) for marker in combo) and
       not_adjacent(combo[0], combo[1]) and
       not_adjacent(combo[1], combo[2])
]

# Count valid combinations satisfying additional constraint
filtered_combinations_count = len([
    combo for combo in filtered_combinations
    if sum(marker_scores[marker] for marker in combo) % 2 == 1
])

print(f"Result: {filtered_combinations_count}")