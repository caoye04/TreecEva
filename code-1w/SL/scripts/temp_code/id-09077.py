def main():
    # Simulate sensor data processing with performance metrics
    raw_readings = [18, 23, 14, 35, 22]
    calibration_offset = 3
    processed_values = [x + calibration_offset for x in raw_readings]

    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(processed_values)):
        if i == 0:
            smoothed.append(processed_values[i])
        else:
            smoothed.append((processed_values[i] + processed_values[i-1]) / 2)

    # Key metrics computation
    base_accuracy = sum(processed_values) / len(processed_values)
    fluctuation_index = max(processed_values) - min(processed_values)

    # Latency simulation (partially relevant)
    response_times_ms = [45, 67, 51, 89, 42]
    avg_latency = sum(response_times_ms) / len(response_times_ms)
    latency_penalty = 0.1 * avg_latency

    # Weight adjustment using conditional expression
    dynamic_weight = 1.2 if avg_latency < 60 else 0.8

    # Build accuracy vector with noise injection (some distraction)
    noise_factor = 0.05
    accuracy = [val * (1 + noise_factor) for val in processed_values]
    accuracy = sum(accuracy) / len(accuracy)  # scalar final accuracy

    # Construct latency weights (only one element used later)
    latency_weights = {
        'base': avg_latency,
        'penalty': latency_penalty,
        'threshold_met': avg_latency < 70,
        'bonus': 10 if latency_penalty < 8 else 5
    }

    # Dead code path - never executed (dead code distractor)
    debug_mode = False
    if debug_mode:
        print("Debug: All systems nominal")
        for v in raw_readings:
            assert v > 0, "Invalid reading"

    # Conditional expression used in aggregation logic
    def aggregate_performance(acc, lat_weights):
        base_component = acc * 0.7
        penalty_adjusted = lat_weights['penalty'] * 0.3
        bonus_applied = lat_weights['bonus'] if lat_weights['threshold_met'] else 0
        return base_component - penalty_adjusted + bonus_applied \
            if acc > 20 else base_component + bonus_applied

    final_score = aggregate_performance(accuracy, latency_weights)

    # Spurious secondary calculation (misleading)
    normalized_score = (final_score - min(processed_values)) / (max(processed_values) - min(processed_values))
    ceiling_bounded = int(min(normalized_score, 95))

    # Output target result
    print(f"Target result: {final_score}")

if __name__ == '__main__':
    main()