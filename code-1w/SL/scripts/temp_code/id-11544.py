def evaluate_performance(rankings, threshold):
    adjusted_ranks = []
    temp_offset = 0
    for i, rank in enumerate(rankings):
        if rank < threshold:
            adjusted_ranks.append(rank + i)
        else:
            adjusted_ranks.append(rank * 2)
    
    # Irrelevant tracking variables (distractors)
    max_seen = max(adjusted_ranks)
    total_skipped = 0
    cumulative_shift = 0
    for j in range(len(adjusted_ranks)):
        if adjusted_ranks[j] > 20:
            total_skipped += 1
        cumulative_shift += j * 0.5

    # Set operation to check coverage (semi-relevant but not critical)
    unique_adjusted = set(adjusted_ranks)
    expected_set = set(range(1, len(adjusted_ranks) + 1))
    missing_elements = expected_set - unique_adjusted

    # Secondary processing with zip (core concept)
    shift_compensation = [x - i for i, x in enumerate(adjusted_ranks)]
    paired_data = list(zip(adjusted_ranks, shift_compensation))

    final_value = 0
    for val, comp in paired_data:
        if val > comp:
            final_value += val // 2
        else:
            final_value += comp

    # Key red herring: complex-looking but unused calculation
    phantom_score = sum([i**2 for i in range(len(paired_data)) if i % 2 == 0])
    debug_snapshot = {"size": len(paired_data), "sum": sum(adjusted_ranks)}

    final_score = final_value - len(missing_elements)
    return final_score

# Input data
rankings = [3, 7, 2, 8, 1]
base_threshold = 5
auxiliary_weights = [0.1, 0.3, 0.5]  # Unused distractor

# Execution point of interest
final_score = evaluate_performance(rankings, base_threshold)
print(f"Result: {final_score}")