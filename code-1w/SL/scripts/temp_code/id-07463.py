from itertools import combinations
from functools import reduce

# Simulate candidate evaluation scores across multiple criteria
def normalize_scores(scores):
    total = sum(scores)
    return [s / total for s in scores] if total else [0] * len(scores)

def generate_pairs(elements):
    # Irrelevant helper: generates all pairs (not used in final logic)
    return list(combinations(elements, 2))

def apply_weighting(values, weights):
    return [v * w for v, w in zip(values, weights)]

def calculate_rank_penalty(position):
    # Higher penalty for lower ranks
    return position ** 2

def calculate_final_score(ranks, importance_weights):
    # Normalize the rank values
    normalized_ranks = normalize_scores(ranks)
    
    # Apply domain-specific weighting
    weighted_norm = apply_weighting(normalized_ranks, importance_weights)
    
    # Calculate base score as product of non-zero components
    base_score = reduce(lambda x, y: x * y if y != 0 else x, weighted_norm, 1)
    
    # Add adjustment based on worst rank (minimizing highest index)
    max_rank = max(ranks)
    adjustment = -calculate_rank_penalty(max_rank)
    
    # Dummy logic to increase cognitive load
    temp_shift = sum([i * 0.1 for i in range(len(ranks))])  # Unused distraction
    offset = len([x for x in ranks if x > 2])  # Semi-relevant but not used directly
    
    # Final aggregation
    raw_final = base_score * 100 + adjustment
    
    # Clamp to reasonable range
    final_score = max(raw_final, -100000)
    
    # Dead code branch (never executed)
    if False:
        fallback = sum(weighted_norm) * 50
        final_score = fallback
        
    return int(final_score)

# Input data
rankings = [3, 1, 4, 2]
weights = [0.5, 0.8, 0.7, 0.9]

# Generate unused combinatorial pairs (distractor)
potential_pairs = generate_pairs(rankings)

# Normalize rankings (used)
norm_ranks = normalize_scores(rankings)

# Weighted normalization (used later)
weighted_ranks = apply_weighting(norm_ranks, weights)

# Compute final score using main function
def compute_aggregate():
    # Intermediate transformation
    scaled = [r * 10 for r in norm_ranks]
    # Another distraction variable
    entropy = -sum(p * __import__('math').log(p) for p in norm_ranks if p > 0)
    return calculate_final_score(rankings, weights)

final_score = compute_aggregate()

# Output result
print(f"Result: {final_score}")