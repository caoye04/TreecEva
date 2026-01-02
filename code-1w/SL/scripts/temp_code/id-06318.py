from itertools import compress, cycle

def analyze_performance(metrics):
    # Irrelevant transformation: normalize metrics (not used in final logic)
    normalized = [m / max(metrics) for m in metrics]
    threshold = sum(normalized) / len(normalized)
    high_performers = list(compress(range(len(metrics)), (m > threshold for m in normalized)))
    return high_performers

def calculate_final_score(ranks, weights):
    # Core logic: weighted rank aggregation with tie-breaking via index position
    weighted_sum = 0
    adjustment_factor = 0
    
    # Real computation begins
    sorted_indices = sorted(range(len(ranks)), key=lambda i: ranks[i])
    rank_order = [0] * len(ranks)
    for pos, idx in enumerate(sorted_indices):
        rank_order[idx] = pos + 1
    
    # Apply weights with cyclic padding if needed
    weight_cycle = cycle(weights)
    applied_weights = [next(weight_cycle) for _ in range(len(ranks))]
    
    # Accumulate weighted score
    for i in range(len(ranks)):
        weighted_sum += rank_order[i] * applied_weights[i]
    
    # Misleading adjustment: computes deviation but doesn't apply it
    temp_deviation = sum(abs(rank_order[j] - applied_weights[j]) for j in range(len(ranks)))
    dummy_correction = temp_deviation * 0.1  # Computed but unused
    
    # Final adjustment based on parity of total rank positions
    total_rank_value = sum(rank_order)
    if total_rank_value % 2 == 0:
        adjustment_factor = 5
    else:
        adjustment_factor = -3
    
    result = weighted_sum + adjustment_factor
    
    # Dead code branch: never executed due to prior logic
    if False and len(ranks) > 100:
        fallback = sum(rank_order) // len(ranks)
        result = fallback

    return int(result)

# Main execution block
if __name__ == '__main__':
    # Input data
    performance_metrics = [88, 92, 76, 94, 85]
    rank_data = [3, 1, 4, 1, 5]  # Duplicate values to test sorting stability implications
    bonus_weights = [2, 3, 1]

    # Distractor call: analysis not used later
    top_achievers = analyze_performance(performance_metrics)
    
    # Auxiliary calculation: looks important but irrelevant
    avg_rank = sum(rank_data) / len(rank_data)
    rank_variance = sum((r - avg_rank) ** 2 for r in rank_data) / len(rank_data)
    pseudo_z_scores = [(r - avg_rank) / (rank_variance ** 0.5) for r in rank_data]

    # Key computation
    final_score = calculate_final_score(rank_data, bonus_weights)
    
    # Output result as required
    print(f"Result: {final_score}")