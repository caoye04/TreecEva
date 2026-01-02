from collections import defaultdict
from itertools import combinations

# Simulate a competitive coding event with ranking adjustments
def calculate_adjusted_rank(base_rank, penalty_factor):
    if base_rank <= 0:
        return 1
    adjustment = (base_rank * 0.95) + penalty_factor
    return int(adjustment) if adjustment > 1 else 1

# Misleading helper: not actually used in final computation
def compute_theoretical_max(n):
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += i ^ j  # XOR sum for all pairs
    return total

# Main processing function
def process_results(ranks, coeffs):
    temp_store = defaultdict(float)
    cumulative = 0
    
    # Real logic begins
    for idx, rank in enumerate(ranks):
        if idx % 2 == 0:
            adjusted = calculate_adjusted_rank(rank, 0.8)
        else:
            adjusted = calculate_adjusted_rank(rank, 1.2)
        
        # Apply weight and track
        weighted_val = adjusted * coeffs[idx]
        temp_store[f'entry_{idx}'] = weighted_val
        cumulative += weighted_val
    
    # Distractor block: computes something irrelevant
    unused_pairs = []
    for pair in combinations(temp_store.keys(), 2):
        key1, key2 = pair
        diff = temp_store[key1] - temp_store[key2]
        if abs(diff) > 5:
            unused_pairs.append(pair)
    
    # Actual final transformation
    scale_factor = len(ranks) / 8
    inflated = cumulative * scale_factor
    penalty = sum(1 for x in ranks if x > 5) * 0.5
    final = inflated - penalty
    
    # Dead code: never accessed
    debug_info = {"size": len(unused_pairs), "scale": scale_factor}
    
    return int(final)

# Input data
initial_ranks = [3, 7, 2, 9, 4, 6]
weight_vector = [1.1, 0.9, 1.3, 0.8, 1.0, 1.2]

# Irrelevant precomputation (distractor)
theoretical_limit = compute_theoretical_max(len(initial_ranks))

# Key statement
final_score = process_results(initial_ranks, weight_vector)

# Output result as required
print(f"Target result: {final_score}")