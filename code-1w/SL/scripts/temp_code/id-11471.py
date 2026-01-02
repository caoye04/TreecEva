def analyze_data_stream(data_points):
    # Irrelevant statistical counters (distractors)
    total_samples = len(data_points)
    outlier_count = 0
    cumulative_noise = 0.0
    adjusted_values = []

    # Process each data point with filtering logic
    for val in data_points:
        if val < -50 or val > 50:
            outlier_count += 1
            continue
        if val % 7 == 0:
            cumulative_noise += abs(val) * 0.1
        adjusted_values.append(val + (1 if val > 0 else -1))

    # Secondary transformation: smooth the adjusted values
    smoothed = []
    for i in range(len(adjusted_values)):
        window = adjusted_values[max(0, i-1):min(i+2, len(adjusted_values))]
        smoothed.append(sum(window) / len(window))

    # Compute key metrics (some are distractions)
    raw_sum = sum(smoothed)
    peak_magnitude = max(abs(min(smoothed)), abs(max(smoothed)))
    stability_factor = len([x for x in smoothed if -10 <= x <= 10])
    fluctuation_index = sum(abs(smoothed[i] - smoothed[i-1]) for i in range(1, len(smoothed)))

    # Core logic: performance metric depends only on raw_sum and stability_factor
    # All other variables above are semi-relevant or irrelevant
    return raw_sum, stability_factor, fluctuation_index, cumulative_noise


def calculate_performance_metric(input_sequence):
    base_value, relevance_score, _, _ = analyze_data_stream(input_sequence)
    
    # Conditional expression determining scaling factor
    scaling = 1.5 if relevance_score > 20 else (0.8 if relevance_score > 10 else 0.3)
    
    # Additional distraction: unused derived metrics
    normalized_base = base_value / (abs(base_value) + 1e-5)
    entropy_proxy = -sum((x/100)*((x/100)+1e-5) for x in input_sequence[:10])
    
    # Final score calculation - only base_value and scaling matter
    final_score = base_value * scaling
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Simulated sensor readings (deterministic input)
data_stream = [i * 3 - 15 for i in range(30)]
final_score = calculate_performance_metric(data_stream)