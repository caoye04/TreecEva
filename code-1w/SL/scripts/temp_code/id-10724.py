def analyze_performance(raw_data, thresholds):
    processed = []
    temp_debug_log = []
    cumulative_shift = 0

    for idx, (value, threshold) in enumerate(zip(raw_data, thresholds)):
        if value < 0:
            adjusted = abs(value) * 1.5
        else:
            adjusted = value + 0.1 * idx

        exceeded = adjusted > threshold
        safety_margin = (adjusted - threshold) if exceeded else (threshold - adjusted)

        temp_debug_log.append(f"Step {idx}: margin={safety_margin:.2f}")

        if exceeded and safety_margin > 5:
            processed.append(adjusted * 0.9)
        elif not exceeded:
            processed.append(adjusted * 1.1)
        else:
            processed.append(adjusted)

        cumulative_shift += len([x for x in str(int(adjusted)) if int(x) % 2 == 0])

    normalized_metrics = []
    base_reference = sum(processed) / len(processed) if processed else 1

    for i, val in enumerate(processed):
        norm = (val / base_reference) * 100
        noise_offset = (i % 3) * 0.05
        normalized_metrics.append(round(norm + noise_offset, 3))

    outlier_count = sum(1 for x in normalized_metrics if x > 120)
    correction_factor = 0.95 if outlier_count > 2 else 1.0

    for j in range(len(normalized_metrics)):
        normalized_metrics[j] *= correction_factor

    final_score = max(normalized_metrics)
    
    # Irrelevant tracking
    debug_stats = {
        'total_steps': len(temp_debug_log),
        'even_digit_shift': cumulative_shift,
        'outliers': outlier_count
    }
    
    # Dead computation branch
    if len(raw_data) > 100:
        fallback = sum(debug_stats.values())
        final_score = fallback  # Never reached

    print(f"Result: {final_score}")

# Inputs
raw_input = [23, -15, 44, 67, 31, 50, 29]
threshold_settings = [25, 20, 40, 60, 35, 55, 30]

analyze_performance(raw_input, threshold_settings)