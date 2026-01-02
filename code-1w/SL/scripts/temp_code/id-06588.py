def calculate_final_score(data, importance):
    # Preprocess rankings with normalization (mean subtraction)
    mean_val = sum(data) / len(data)
    normalized = [x - mean_val for x in data]

    # Apply weight transformation using lambda for dynamic scaling
    scaler = lambda x, w: x * (w ** 0.5)
    scaled_values = [scaler(norm, importance[i]) for i, norm in enumerate(normalized)]

    # Secondary irrelevant transformation (distractor)
    squared_chain = [(val ** 2) + 1 for val in scaled_values]
    filtered_chain = [v for v in squared_chain if v > 1]  # Always true, so no filtering

    # Simulate ranking displacement (unused in final logic)
    displacement = 0
    for i in range(len(scaled_values)):
        if i % 2 == 0:
            displacement += scaled_values[i] * 0.1

    # Core calculation: weighted rank score with rounding to nearest integer
    raw_sum = sum(scaled_values)
    adjustment = len(data) // 2
    final_score = int(round(raw_sum + adjustment))

    # Irrelevant debug print simulation (dead code)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {displacement}, {filtered_chain}')

    return final_score

# Main execution context
rank_data = [85, 90, 78, 92, 88]
weights = [1.2, 1.5, 0.8, 2.0, 1.4]

# Initialize auxiliary tracking variables (distractors)
total_entries = len(rank_data)
duplicate_check = set(rank_data)
sorted_ranks = sorted(rank_data, reverse=True)
mid_value = sorted_ranks[total_entries // 2]  # Not used later

# Key statement
final_score = calculate_final_score(rank_data, weights)

print(f'Result: {final_score}')