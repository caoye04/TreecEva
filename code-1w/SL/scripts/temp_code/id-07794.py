import math

# Simulated sensor data processing pipeline
def analyze_sensor_readings(data_points):
    raw_sum = 0
    adjusted_sum = 0
    anomaly_count = 0
    temporal_weights = []

    # Precompute time decay factors (distractor: not all are used)
    for i in range(len(data_points)):
        weight = math.exp(-0.1 * i)
        temporal_weights.append(round(weight, 4))

    baseline_ref = sum(data_points) / len(data_points)
    variance_accum = 0

    # Primary analysis loop with conditional adjustments
    for val in data_points:
        if val < 0.9 * baseline_ref or val > 1.1 * baseline_ref:
            anomaly_count += 1

        adjusted_val = val * (1 + 0.05 * math.sin(val))  # minor correction
        adjusted_sum += adjusted_val

        # Irrelevant intermediate calculation (distractor)
        temp_offset = (adjusted_val ** 0.5) % 1
        raw_sum += val + temp_offset * 0.01

    # Compute statistical metrics
    for val in data_points:
        variance_accum += (val - baseline_ref) ** 2

    if len(data_points) > 1:
        std_deviation = math.sqrt(variance_accum / (len(data_points) - 1))
    else:
        std_deviation = 0

    # Efficiency model using lambda (required feature)
    efficiency_func = lambda x, y: (x / (y + 1e-5)) * 100

    # Key derived metrics
    stability_index = 1 / (std_deviation + 1)
    normalized_signal = adjusted_sum / len(data_points)
    reliability_factor = max(0, 1 - (anomaly_count / len(data_points)))

    # Secondary distractor calculations
    theoretical_max = max(data_points) * len(data_points) * 1.05
    unused_ratio = raw_sum / (theoretical_max + 1e-5)
    phantom_threshold = baseline_ref * 0.75 + std_deviation * 2

    # Core logic: compute final efficiency score
    base_efficiency = efficiency_func(normalized_signal, baseline_ref)
    penalty_modifier = 0.85 if anomaly_count > len(data_points) * 0.1 else 1.0
    
    # Final integration step
    final_efficiency = base_efficiency * penalty_modifier * reliability_factor
    
    # Additional red herring: unused transformation chain
    transformed_vals = [math.log(1 + abs(x), 10) for x in data_points]
    aggregate_transform = sum(transformed_vals) / len(transformed_vals)
    dummy_correction = aggregate_transform * 0.3 if std_deviation > 2 else 0

    # Critical assignment point
    efficiency_score = round(final_efficiency * stability_index, 3)
    
    # Tracking multiple outputs (only one matters)
    final_metrics = []
    final_metrics.append(efficiency_score)
    final_metrics.append(unused_ratio)
    final_metrics.append(dummy_correction)

    return final_metrics[0]

# Input data (fixed seed for determinism)
sensor_data = [12.5, 13.1, 11.8, 14.2, 13.0, 12.7, 15.6, 11.9, 13.3, 12.9]

# Execute and print target result
result = analyze_sensor_readings(sensor_data)
print(f"Target result: {result}")