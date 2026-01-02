def evaluate_performance(data, importance):
    temp_result = 0
    adjustments = [0.1, -0.2, 0.15, -0.05]
    baseline = sum(data) / len(data)
    fluctuation_tracker = []

    for i, (value, weight) in enumerate(zip(data, importance)):
        adjusted_value = value * weight
        if i % 2 == 0:
            adjusted_value += adjustments[i % len(adjustments)]
        else:
            temp_offset = (value ** 0.5) * 0.01  # Minor perturbation
            adjusted_value -= temp_offset
        
        smoothing_factor = 1 + (i * 0.01)
        normalized = adjusted_value / smoothing_factor
        
        # Irrelevant string processing distraction
        status_label = 'pass' if normalized > 0.5 else 'review'
        status_flag = status_label.upper() + '_FLAG'
        fluctuation_tracker.append(normalized)

    trend_correction = 0
    for j in range(1, len(fluctuation_tracker)):
        trend_correction += fluctuation_tracker[j] - fluctuation_tracker[j-1]

    # Dead code path - never used
    outlier_count = 0
    for val in data:
        if val > 0.9:
            outlier_count += 1
    auxiliary_metric = outlier_count * 0.3

    # Actual computation path
    weighted_sum = 0
    for i in range(len(data)):
        weighted_sum += data[i] * importance[i]

    # Final adjustment using side computation
    final_score = int((weighted_sum + trend_correction) * 100)

    # Additional irrelevant operations
    summary_text = "Metrics: " + ", ".join([f"{x:.2f}" for x in data])
    encoded_summary = summary_text.replace(".", "p").encode('utf-8')
    dummy_hash = sum(encoded_summary) % 100

    return final_score

# Input data
metrics = [0.78, 0.82, 0.85, 0.76]
weights = [0.2, 0.3, 0.4, 0.1]

# Execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")