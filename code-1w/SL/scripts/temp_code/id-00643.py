from itertools import combinations

def analyze_performance(metrics):
    # Auxiliary function that computes pairwise product sums (not directly used)
    pairs = list(combinations(metrics, 2))
    dummy_sum = sum(a * b for a, b in pairs)
    adjusted = [x * 1.1 for x in metrics]
    return adjusted

def calculate_rank_effect(rankings):
    rank_effect = 0
    for i, rank in enumerate(rankings):
        if rank <= 3:
            rank_effect += (4 - rank) * 2
    return rank_effect

def calculate_weight_bias(weights):
    # Calculates variance-like measure (distractor)
    mean_weight = sum(weights) / len(weights)
    weight_variance = sum((w - mean_weight) ** 2 for w in weights) / len(weights)
    normalized = [w / mean_weight for w in weights]
    return weight_variance  # Unused in final logic

def calculate_final_score(rankings, weights):
    base_score = 0
    # Use enumerate and zip together as required
    for idx, (rank, weight) in enumerate(zip(rankings, weights)):
        contribution = (10 - rank) * weight
        if idx % 2 == 0:
            contribution *= 1.5  # Bonus for even indices
        base_score += contribution
    
    # Apply rank effect from helper
    rank_bonus = calculate_rank_effect(rankings)
    base_score += rank_bonus
    
    # Irrelevant transformation
    temp_results = [base_score * 0.95, base_score * 1.05]
    smoothed = sum(temp_results) / 2
    
    # Final adjustment
    final_score = int(smoothed + 0.5)  # Round to nearest integer
    
    return final_score

# Main execution
if __name__ == "__main__":
    # Input data
    rankings = [1, 4, 2, 5, 3]
    weights = [0.8, 1.2, 1.0, 0.9, 1.1]
    
    # Dead code path - never executed
    if False:
        debug_info = analyze_performance(weights)
    
    # Key computation
    final_score = calculate_final_score(rankings, weights)
    
    # Print result
    print(f"Result: {final_score}")