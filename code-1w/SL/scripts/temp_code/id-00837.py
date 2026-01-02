def calculate_final_score(ranks, coeffs):
    # Simulate a ranking system with weighted aggregation
    normalized = [r / sum(ranks) for r in ranks]
    weighted_vals = [n * c for n, c in zip(normalized, coeffs)]
    
    # Distractor: irrelevant transformation on same data
    squared_ranks = [r ** 2 for r in ranks]
    avg_square = sum(squared_ranks) / len(squared_ranks)
    temp_offset = avg_square * 0.1  # Not used in final logic

    # More distractions: sorting but not using result directly
    sorted_pairs = sorted(enumerate(weighted_vals), key=lambda x: x[1], reverse=True)
    top_indices = [i for i, _ in sorted_pairs[:3]]

    # Actual computation path
    raw_sum = sum(weighted_vals)
    penalty = 0
    for i, w in enumerate(coeffs):
        if i % 2 == 1:
            penalty += 0.5 * normalized[i]

    adjustment = len([x for x in ranks if x > 1]) * 0.01  # Minor correction factor
    intermediate_result = raw_sum - penalty + adjustment

    # Final scaling based on control flow
    if intermediate_result > 0.5:
        final_value = intermediate_result * 1.2
    else:
        final_value = intermediate_result * 0.8

    return final_value

# Main execution
rankings = [5, 8, 3, 9, 2]
weights = [0.4, 0.3, 0.5, 0.2, 0.6]

# Irrelevant preprocessing
zipped_data = list(zip(rankings, weights))
duplicate_check = set(r // 2 for r in rankings)
shadow_copy = rankings.copy()
shadow_copy.append(100)  # Dead-end mutation

# Key computation
final_score = calculate_final_score(rankings, weights)

# Output result
print(f"Result: {final_score}")