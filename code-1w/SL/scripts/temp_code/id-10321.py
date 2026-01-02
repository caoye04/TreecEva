def calculate_final_score(ranks, coeffs):
    # Normalize ranks using min-max scaling (irrelevant for final logic but looks important)
    normalized = [(r - min(ranks)) / (max(ranks) - min(ranks)) if max(ranks) != min(ranks) else 0 for r in ranks]
    
    # Apply coefficient mapping with lambda (used later)
    weighted_map = list(map(lambda x: x[0] * x[1], zip(ranks, coeffs)))
    
    # Secondary transformation - distraction
    squared_offsets = [abs(r - len(ranks))**2 for r in ranks]
    offset_sum = sum(squared_offsets)

    # Core logic: rank-weighted score with threshold adjustment
    raw_score = sum(weighted_map)
    threshold = len(ranks) * 0.5
    adjustment = 0
    
    # Conditional adjustment based on rank distribution (actually used)
    high_performers = [r for r in ranks if r < threshold]
    if len(high_performers) >= 2:
        adjustment = len(high_performers) * 1.5
    
    # Use of enumerate and zip in filtering logic (semi-relevant)
    filtered_weights = []
    for i, w in enumerate(coeffs):
        if ranks[i] < len(ranks):  # arbitrary filter condition
            filtered_weights.append(w * 0.9)
    
    # Final computation path
    base = raw_score + adjustment
    penalty = 0
    for idx, (r, w) in enumerate(zip(ranks, coeffs)):
        if idx % 2 == 0 and r > 2:
            penalty += w * 0.5
    
    # Key result computation
    return int(base - penalty)

# Input data
rankings = [1, 3, 2, 4]
weights = [10, 8, 12, 5]

# Irrelevant pre-processing (distractor)
data_matrix = [[x, y] for x in rankings for y in weights if x % 2 == 0]
duplicate_check = set(tuple(data_matrix))

# Semi-useful transformation (partial use)
scaled_weights = [w * 1.1 for w in weights]

# Unused helper function (dead code - adds interference)
def validate_inputs(x, y):
    if len(x) != len(y):
        raise ValueError("Mismatched lengths")
    return True

# Actual execution
validation_passed = True  # mock state tracking
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")