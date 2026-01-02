def calculate_performance(data):
    # Irrelevant transformation (dead-end computation)
    noise_filter = lambda x: (x ** 2 + 3 * x + 1) % 7
    filtered_noise = [noise_filter(val) for val in range(len(data))]

    # Distractor variables - not used in final result
    temp_offset = sum([i * 0.1 for i in range(len(data))])
    dummy_weight = 0.987

    # Core logic: compute weighted trend with decay factor
    trend_values = []
    decay_factor = 0.85
    for i, point in enumerate(data):
        weight = decay_factor ** (len(data) - i - 1)  # more recent = higher weight
        trend_values.append(point * weight)

    base_trend = sum(trend_values)

    # Secondary adjustment using conditional branching and accumulation
    adjustment = 0.0
    threshold = 85
    for val in data:
        if val > threshold:
            adjustment += (val - threshold) * 0.2
        elif val < threshold - 20:
            adjustment -= (threshold - 20 - val) * 0.1

    # Simulated calibration offset (irrelevant to main logic)
    calibration_log = [abs(noise_filter(i) - dummy_weight) for i in range(3)]
    unused_metric = sum(calibration_log) / len(calibration_log)

    # Final performance score calculation
    raw_score = base_trend + adjustment
    normalized_score = raw_score * (1.0 + 0.05 * (len(data) > 5))  # bonus if sufficient data

    # Key variable assignment
    final_score = int(round(normalized_score))

    return final_score

# Input data sequence
benchmark_data = [78, 82, 88, 91, 94, 96]

# Execute main logic
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")