def calculate_final_score(ranks, coeffs):
    # Simulate a weighted ranking system with red herrings
    temp_results = []
    offset = len(ranks) * 2
    scaling_factor = 0.5
    
    # Real computation: weighted sum using enumerate and zip
    weighted_sum = 0
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        adjustment = 1 if i % 2 == 0 else -1
        temp_value = rank * weight * scaling_factor + adjustment
        temp_results.append(temp_value)

    # Distractor: unused sorting and dead path
    sorted_temp = sorted(temp_results, reverse=True)
    if len(sorted_temp) > 10:
        fallback = sum(sorted_temp[:5])
    else:
        fallback = 0  # Dead code

    # Actual logic: use only even-indexed contributions
    contribution = sum(val for idx, val in enumerate(temp_results) if idx % 2 == 0)

    # More distraction: irrelevant combinatorics
    pair_count = 0
    for i in range(len(ranks)):
        for j in range(i + 1, len(ranks)):
            if ranks[i] < ranks[j]:
                pair_count += 1  # Unused metric

    # Final score depends on contribution and fixed offset
    final_result = int(contribution + offset)
    return final_result

# Input data
ranking_positions = [10, 8, 12, 5, 7]
importance_weights = [3, 4, 2, 5, 3]

# Irrelevant pre-computations
avg_rank = sum(ranking_positions) / len(ranking_positions)
deviations = [abs(x - avg_rank) for x in ranking_positions]
total_dev = sum(deviations)

# Key execution point
final_score = calculate_final_score(ranking_positions, importance_weights)
print(f"Result: {final_score}")