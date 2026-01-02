def calculate_final_score(entries, importance_weights):
    total = 0
    adjustment_factor = 0.85
    temp_buffer = []
    cumulative_shift = 0

    for i, (val, weight) in enumerate(zip(entries, importance_weights)):
        if i % 2 == 0:
            adjusted_val = val * weight * adjustment_factor
        else:
            shifted = val + (i // 3)
            adjusted_val = shifted * weight

        temp_buffer.append(adjusted_val)

        # Irrelevant accumulation (distractor)
        cumulative_shift += val % 7

    # Secondary processing with linear search pattern
    max_index = -1
    max_value = float('-inf')
    for idx, item in enumerate(temp_buffer):
        if item > max_value:
            max_value = item
            max_index = idx

    # Apply bonus only if max occurs at even index (semi-relevant)
    bonus = 10 if max_index % 2 == 0 else 0

    # Actual summation used in result
    raw_sum = sum(temp_buffer)

    # Red herring: unused normalization
    normalized = [x / (raw_sum + 1e-9) for x in temp_buffer]

    # Final computation chain
    base_score = raw_sum * 1.1
    penalty = len([x for x in entries if x < 0]) * 2.5
    final_score = base_score - penalty + bonus

    return final_score

# Main data
readings = [12, -5, 8, 14, 3, -1, 9]
coefficients = [0.5, 0.7, 0.6, 0.8, 0.4, 0.9, 0.3]

# Misleading pre-processing (dead code path)
dummy_state = [x ** 2 for x in readings if x > 6]
aggregate_noise = sum(dummy_state) // 3 if dummy_state else 0

result_flag = False
if aggregate_noise > 10:
    result_flag = True

# Key execution point
target_result = calculate_final_score(readings, coefficients)
print(f"Result: {target_result}")