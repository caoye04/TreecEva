def analyze_metrics(raw_values, threshold=5.0):
    # Irrelevant tracking variables
    total_iterations = 0
    debug_log = []

    filtered_data = [x for x in raw_values if x > threshold]
    normalized = list(map(lambda x: round(x / sum(filtered_data) * 100, 3), filtered_data))

    # Distractor: complex-looking but unused computation
    outlier_count = 0
    for i, val in enumerate(normalized):
        if val > 50:
            outlier_count += 1
        total_iterations += 1  # Logged but not used

    stats = {
        'mean': sum(normalized) / len(normalized),
        'peak': max(normalized),
        'size': len(normalized)
    }

    return stats, normalized


def calculate_efficiency(data_chunk):
    base_score = 0
    adjustment_factor = 0.85

    for idx, (i, val) in enumerate(zip(range(len(data_chunk)), data_chunk)):
        if i % 2 == 0:
            base_score += val * adjustment_factor
        else:
            base_score -= val * 0.1

    # Secondary logic path that looks important but doesn't alter core result
    temp_result = [x for x in data_chunk if x > 10]
    if len(temp_result) > 2:
        base_score += len(temp_result)

    return round(base_score, 4)

# Main execution block
sensor_readings = [12.5, 3.2, 8.7, 15.6, 4.1, 9.3, 11.0, 6.8]
sensor_stats, processed_data = analyze_metrics(sensor_readings, threshold=4.0)

# Key statement
efficiency_score = calculate_efficiency(processed_data)

# Debugging red herring (not affecting result)
consistency_check = all(x < 30 for x in processed_data)
diagnostic_flag = False if consistency_check else True

# Print final target result
print(f"Result: {efficiency_score}")