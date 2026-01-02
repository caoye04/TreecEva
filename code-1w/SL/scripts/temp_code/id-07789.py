def evaluate_performance(weights, data):
    # Preprocess: normalize data using modular arithmetic
    normalized = [(x % 97) / 97.0 for x in data]

    # Irrelevant transformation: frequency analysis (distractor)
    freq_map = {}
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
    avg_freq = sum(freq_map.values()) / len(freq_map) if freq_map else 0

    # Secondary distractor: simulate decay over time (not used in final logic)
    time_decay = lambda t: 0.95 ** t
    decay_correction = [time_decay(i) for i in range(len(normalized))]

    # Core logic begins: apply weighted transform with non-linear activation
    activated = []
    for i, val in enumerate(normalized):
        if val > 0.5:
            activated.append(val ** 0.5 * 1.2)
        elif val < 0.2:
            activated.append(val * 0.8)
        else:
            activated.append(val)

    # Weighted aggregation
    weighted_sum = 0.0
    total_weight = 0.0
    for i, w in enumerate(weights):
        weight_contribution = abs(w) + 0.1  # Ensure positive contribution
        weighted_sum += activated[i % len(activated)] * weight_contribution
        total_weight += weight_contribution

    # Apply threshold filter: ignore low performers
    if weighted_sum / total_weight < 0.3:
        return 0

    # Final score computation
    stability_factor = 1.0
    for j in range(1, len(data)):
        diff = abs(data[j] - data[j-1])
        if diff > 50:
            stability_factor *= 0.9

    # Distractor: unused complexity
    outlier_count = sum(1 for d in data if d < 10 or d > 90)
    adjustment_proxy = outlier_count * 0.01  # Computed but not used

    final_score = int((weighted_sum / total_weight) * 100 * stability_factor)

    return final_score

# Input data
metric_weights = [2.1, -1.3, 3.4, 0.8, 1.9]
raw_data = [85, 12, 67, 91, 44, 23, 77]

# Execute main logic
temp_result = evaluate_performance(metric_weights, raw_data)
final_score = evaluate_performance(metric_weights, raw_data)
print(f"Result: {final_score}")