def calculate_final_score(ranks, coeffs):
    # Simulate weighted ranking aggregation with distractors
    base = 0
    offset = len(ranks) * 0.5
    temp_sum = 0
    intermediate_results = []

    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        adjusted_rank = (rank + 0.1) * weight
        squared_penalty = (rank ** 2) * 0.01  # Irrelevant penalty term
        temp_sum += adjusted_rank - squared_penalty
        intermediate_results.append(adjusted_rank)

    # Distractor: unused normalization path
    if len(intermediate_results) > 10:
        normalized = [x / sum(intermediate_results) for x in intermediate_results]
    else:
        normalized = None  # Dead code branch

    # Real computation continues
    bonus = 0
    for idx in range(len(ranks)):
        if idx % 2 == 0 and ranks[idx] < 5:
            bonus += 0.25

    # Additional distraction: slicing unused portion
    slice_part = intermediate_results[::2]
    dummy_aggregate = sum(slice_part[:3]) if len(slice_part) >= 3 else 0

    # Final score formula
    final = temp_sum + bonus - offset

    # Secondary distractor: redundant tracking
    stats_log = {
        'count': len(ranks),
        'max_intermediate': max(intermediate_results),
        'ignored_metric': dummy_aggregate * 0.1
    }

    return round(final, 4)

# Main execution
if __name__ == '__main__':
    # Input data
    rankings = [3, 1, 4, 1, 5, 9, 2]
    weights = [0.8, 1.2, 0.9, 1.1, 0.7, 0.5, 1.0]

    # Unused variables to increase cognitive load
    backup_weights = [w * 0.95 for w in weights]
    historical_ranks = rankings[::-1]
    outlier_flags = [r > 8 for r in rankings]

    # Key statement
    final_score = calculate_final_score(rankings, weights)
    
    # Print result as required
    print(f"Result: {final_score}")