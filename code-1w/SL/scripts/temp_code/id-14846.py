def calculate_performance(data_map):
    base_factor = 3.5
    adjustment = 0
    volatility_index = 0.0
    total_entries = len(data_map)
    valid_count = 0
    temp_sum = 0

    # Misleading pre-scan: calculates irrelevant volatility (not used in final score)
    for key in data_map:
        if 'metric_' in key:
            val = data_map[key]
            volatility_index += abs(val - base_factor) * 0.1

    # Core logic with dictionary operations and conditional adjustments
    for k, v in data_map.items():
        if isinstance(v, int) and v > 0:
            valid_count += 1
            temp_sum += v ** 0.5  # Square root contribution

        if 'offset_flag' in data_map and data_map['offset_flag']:
            adjustment -= 1.2

    # Simulate complex weighting
    if valid_count > 2:
        adjustment += 2.8

    intermediate_result = temp_sum / (valid_count or 1)

    # Red herring: unused transformation chain
    transformed_values = [v * 1.1 for v in data_map.values() if isinstance(v, (int, float))]
    cumulative_effect = sum(transformed_values) % 7 if transformed_values else 0

    # Final computation using only select components
    performance_base = intermediate_result * base_factor
    penalty_rate = data_map.get('penalty_rate', 0.5)
    final_score = performance_base - (penalty_rate * 4) + adjustment

    return final_score

# Input data with mixed types and distractions
dataset = {
    'metric_a': 9,
    'metric_b': 16,
    'metric_c': 25,
    'offset_flag': True,
    'penalty_rate': 1.0,
    'debug_mode': False,
    'timestamp': 1712345678,
    'aux_data': [1, 2, 3],
    'scale_factor': 2.5
}

result = calculate_performance(dataset)
final_score = result
print(f"Result: {final_score}")