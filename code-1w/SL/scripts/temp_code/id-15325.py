def calculate_final_score(raw_data, limits):
    # Preprocessing: filter and normalize data
    normalized = [x / max(raw_data) for x in raw_data]
    above_threshold = [val for val in normalized if val > limits['upper']]
    below_floor = [val for val in normalized if val < limits['lower']]

    # Misleading computation: unused transformation
    inverted = [1 - v for v in normalized]  
    temp_sum = sum(inverted) * 0.1  # Distractor: not used later

    # Core logic: scoring based on distribution zones
    low_zone = len([v for v in normalized if v < 0.3])
    mid_zone = len([v for v in normalized if 0.3 <= v <= 0.7])
    high_zone = len([v for v in normalized if v > 0.7])

    # Bonus logic: conditional multiplier
    bonus_factor = 1.5 if high_zone > low_zone else 1.0

    # Secondary distractor: complex but unused set operation
    unique_pairs = {(a, b) for a in raw_data for b in raw_data if a != b}
    pair_count_estimate = len(unique_pairs) // 2 if unique_pairs else 0

    # Primary score calculation
    base_score = (high_zone * 10) + (mid_zone * 5) - (low_zone * 3)
    adjusted_score = base_score * bonus_factor

    # Final adjustment using string-based flag (simulates config parsing)
    mode_flag = 'aggressive'.strip()  
    multiplier = 2 if 'agg' in mode_flag else 1
    
    final_score = adjusted_score * multiplier

    return final_score

# Main execution
raw_input = [12, 45, 67, 23, 89, 34, 56, 78, 91, 10]
threshold_config = {'upper': 0.85, 'lower': 0.15}

intermediate_total = sum(x ** 0.5 for x in raw_input)  # Irrelevant precomputation
placeholder_result = sorted(set(str(x) for x in raw_input))  # Dead code path
concatenated = ''.join(placeholder_result)
dummy_matrix = [[i + j for j in range(3)] for i in range(3)]  # Unused structure

final_score = calculate_final_score(raw_input, threshold_config)
print(f"Result: {final_score}")