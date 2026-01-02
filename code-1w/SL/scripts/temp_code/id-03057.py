def analyze_trends(data, threshold=5):
    trend_count = 0
    temp_result = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_count += 1
            temp_result.append(data[i] - data[i-1])
    return temp_result if trend_count > threshold else [0]


def filter_outliers(values):
    mean_val = sum(values) / len(values)
    deviation_scores = [(v - mean_val) ** 2 for v in values]
    variance = sum(deviation_scores) / len(deviation_scores)
    std_dev = variance ** 0.5
    filtered = [v for v in values if abs(v - mean_val) <= 2 * std_dev]
    return filtered


def calculate_final_score(raw_series):
    # Step 1: Slice and preprocess
    subset = raw_series[2:9]
    
    # Irrelevant transformation (distractor)
    inverted = [1/x for x in subset if x != 0]
    avg_inverse = sum(inverted) / len(inverted)

    # Step 2: Analyze upward trends
    trends = analyze_trends(subset)

    # Step 3: Apply outlier filtering
    cleaned = filter_outliers(subset)

    # Step 4: Compute weighted contributions
    weights = [0.5 + i*0.1 for i in range(len(cleaned))]
    weighted_sum = sum(w * v for w, v in zip(weights, cleaned))

    # Step 5: Aggregate trend impact (only positive deltas)
    trend_magnitude = sum(x for x in trends if x > 0)

    # Step 6: Combine into final score
    base_score = sum(cleaned) * 0.8
    adjustment = trend_magnitude * 0.3
    final_score = int(base_score + adjustment - weighted_sum * 0.1)

    # Dead code path (distractor)
    if len(raw_series) > 100:
        fallback = sum(raw_series) // 10
        final_score = max(final_score, fallback)

    return final_score

# Main execution
sensor_readings = [3, 5, 4, 6, 8, 7, 9, 11, 10, 13, 12, 14, 16]
processed_data = sensor_readings[:10]

# Misleading intermediate computations
normalization_factor = sum(processed_data) / len(processed_data)
dummy_pairs = [(a, b) for a in processed_data[:4] for b in processed_data[-3:] if a < b]
expanded_view = processed_data + [normalization_factor] * 2

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")