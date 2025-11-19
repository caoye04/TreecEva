from itertools import permutations
from functools import reduce

def calculate_marker_combination_score(marker_combo):
    if len(marker_combo) < 2:
        return 0
    # Calculate score using XOR of ASCII values
    score = 0
    for i in range(len(marker_combo)-1):
        score ^= ord(marker_combo[i]) ^ ord(marker_combo[i+1])
    return score

def is_valid_marker_path(path):
    # Path is valid if no two adjacent markers are the same letter (case-insensitive)
    for i in range(len(path)-1):
        if path[i].lower() == path[i+1].lower():
            return False
    return True

def explore_genetic_marker_paths(available_markers, current_path=[], depth=0):
    global cumulative_marker_score
    
    # Early return condition
    if depth > 3:
        return
    
    # If we have a valid path of at least 2 markers, add its score
    if len(current_path) >= 2 and is_valid_marker_path(current_path):
        cumulative_marker_score += calculate_marker_combination_score(current_path)
    
    # Recursive exploration with backtracking
    for marker in available_markers:
        # Skip if adding this marker would make path invalid
        if current_path and marker.lower() == current_path[-1].lower():
            continue
            
        current_path.append(marker)
        explore_genetic_marker_paths(available_markers, current_path, depth + 1)
        current_path.pop()  # Backtrack

def get_all_valid_permutation_scores(markers):
    scores = []
    for r in range(2, min(4, len(markers)+1)):  # Limit permutation length
        for perm in permutations(markers, r):
            if is_valid_marker_path(list(perm)):
                scores.append(calculate_marker_combination_score(list(perm)))
    return scores

# Initialize tracking variable
cumulative_marker_score = 0

# Available genetic markers for analysis
marker_panel = ['A', 'T', 'G', 'C', 'X']

# Method 1: Recursive exploration with backtracking
explore_genetic_marker_paths(marker_panel)

# Method 2: Direct permutation calculation
permutation_scores = get_all_valid_permutation_scores(marker_panel)
combined_scores = list(map(lambda x: x * 2, permutation_scores))  # Double each score
filtered_scores = list(filter(lambda x: x > 10, combined_scores))  # Keep scores > 10
reduced_score = reduce(lambda acc, val: acc + val, filtered_scores, 0) if filtered_scores else 0

cumulative_marker_score += reduced_score

print(f"Result: {cumulative_marker_score}")