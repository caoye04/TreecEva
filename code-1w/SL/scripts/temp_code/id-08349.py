def calculate_performance(data):
    total_weight = 0.0
    weighted_sum = 0.0
    max_value = float('-inf')
    min_value = float('inf')
    temp_buffer = []
    scaling_factor = 1.5
    offset_correction = 0.2

    # Track indices and values for analysis
    for idx, (value, weight) in enumerate(zip(data['values'], data['weights'])):
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

        adjusted_value = value * scaling_factor + offset_correction
        weighted_sum += adjusted_value * weight
        total_weight += weight
        temp_buffer.append(adjusted_value)

    # Compute derived metrics (some not used in final score)
    range_value = max_value - min_value
    average_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

    # Secondary loop for validation flags (distraction)
    validation_flags = []
    for i, val in enumerate(data['values']):
        if i % 2 == 0 and val > average_temp:
            validation_flags.append(True)
        else:
            validation_flags.append(False)

    # Simulate confidence adjustment (unused)
    confidence_score = 0.95
    if len(validation_flags) > 5:
        confidence_score *= 0.9

    # Actual performance score calculation
    if total_weight > 0:
        raw_score = weighted_sum / total_weight
    else:
        raw_score = 0.0

    # Apply non-linear boost (relevant)
    boosted_score = raw_score * (1 + 0.1 * (raw_score / 100))

    # Final normalization with constant factor
    final_score = boosted_score * 0.85

    return final_score


def main():
    # Input dataset
    benchmark_data = {
        'values': [88, 92, 76, 94, 85, 90, 83],
        'weights': [0.1, 0.2, 0.15, 0.25, 0.1, 0.1, 0.1]
    }

    # Irrelevant pre-processing (distractor)
    sorted_values = sorted(benchmark_data['values'], reverse=True)
    rank_map = {val: idx for idx, val in enumerate(sorted_values)}
    cumulative_distribution = []
    cumsum = 0
    for w in benchmark_data['weights']:
        cumsum += w
        cumulative_distribution.append(cumsum)

    # Core computation
    final_score = calculate_performance(benchmark_data)

    # Unused diagnostic print (dead code path - distraction)
    # print(f'Diagnostic: range={max(benchmark_data["values"]) - min(benchmark_data["values"])}')

    print(f'Target result: {final_score}')

if __name__ == '__main__':
    main()