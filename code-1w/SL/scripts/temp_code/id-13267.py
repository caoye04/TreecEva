from itertools import combinations

# Simulate ranking-based scoring with noise filtering and weighted bonuses
def preprocess_ranks(raw_ranks):
    filtered = [x for x in raw_ranks if x > 0]
    sorted_ranks = sorted(filtered, reverse=True)
    # Generate all 2-combinations but only use length (distractor)
    combo_count = len(list(combinations(sorted_ranks, 2)))
    normalized = [1 / (rank + 1) for rank in sorted_ranks]
    return normalized

# Misleading helper: computes variance but not used in final score
def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Auxiliary check: counts jumps in sequence, semi-relevant distraction
def count_rank_jumps(ranks):
    jumps = 0
    for i in range(1, len(ranks)):
        if abs(ranks[i] - ranks[i-1]) > 1:
            jumps += 1
    return jumps

# Core logic: applies weights and aggregates
def apply_weighted_bonus(scores, weights):
    weighted_sum = 0.0
    for i, score in enumerate(scores):
        if i < len(weights):
            weighted_sum += score * weights[i]
        else:
            weighted_sum += score * 1.0  # default weight
    return weighted_sum

# Final aggregation function
def calculate_final_score(rank_data, bonus_weights):
    processed = preprocess_ranks(rank_data)
    
    # Irrelevant computation: analyze jumps but don't use result
    _ = count_rank_jumps(rank_data)
    
    # Real computation
    base_score = sum(processed)
    bonus_score = apply_weighted_bonus(processed, bonus_weights)
    
    # Dead code path (never reached due to prior filtering)
    if any(x < 0 for x in rank_data):
        base_score *= 0.9
    
    final_score = int(base_score + bonus_score)
    return final_score

# Input data
rank_data = [4, 2, 0, 6, 3, -1, 5]
bonus_weights = [2, 1, 2, 1]

# Execution flow
variance_noise = compute_variance([1, 2, 3, 4, 5])  # Unused value
intermediate_result = preprocess_ranks(rank_data)
count_jumps = count_rank_jumps(rank_data)  # Computed but irrelevant

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")