def analyze_performance(metrics, thresholds):
    alert_flags = []
    stability_index = 0
    temp_adjustment = 0

    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        if metric > threshold * 1.1:
            alert_flags.append((i, 'HIGH'))
            temp_adjustment += 0.5
        elif metric < threshold * 0.9:
            alert_flags.append((i, 'LOW'))
            temp_adjustment -= 0.3
        else:
            alert_flags.append((i, 'NORMAL'))

        stability_index ^= int(metric) & 7  # bitwise tracking of lower bits

    # Irrelevant aggregation (distractor)
    avg_flag_length = sum(len(flag[1]) for flag in alert_flags) / len(alert_flags) if alert_flags else 0

    return stability_index, temp_adjustment, avg_flag_length


def compute_final_score(data_points, config):
    base_weights = [0.8, 1.2, 0.9, 1.1]
    adjusted_values = []

    for val in data_points:
        adjusted_val = val
        if val < config['min_bound']:
            adjusted_val = config['min_bound']
        elif val > config['max_bound']:
            adjusted_val = config['max_bound']
        adjusted_values.append(adjusted_val)

    # Dummy normalization (not used later)
    normalized = [round((v - min(adjusted_values)) / (max(adjusted_values) - min(adjusted_values) + 1e-8), 4)
                 for v in adjusted_values]

    weighted_sum = sum(v * w for v, w in zip(adjusted_values, base_weights[:len(adjusted_values)]))

    # Secondary logic with conditional expression
    penalty = 10 if weighted_sum > 150 else (5 if weighted_sum > 100 else 0)

    # Call helper with distractor return values
    stability, drift, _ = analyze_performance(adjusted_values, [70, 85, 60, 90])

    # Complex but relevant final computation
    final_score = (weighted_sum - penalty)
    final_score += (stability * 2)
    final_score -= int(drift)

    # Dead code path (misleading)
    if False:
        backup_correction = sum(normalized) * 100
        final_score = max(final_score, backup_correction)

    return int(final_score)

# Input data
metrics_data = [72, 88, 55, 95]
config_params = {
    'min_bound': 60,
    'max_bound': 90
}

# Execute
final_score = compute_final_score(metrics_data, config_params)
print(f"Result: {final_score}")