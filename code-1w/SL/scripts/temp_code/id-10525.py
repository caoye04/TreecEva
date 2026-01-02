import itertools

# System health monitoring simulation with diagnostic overrides
def run_diagnostics(sensor_data, threshold=75):
    normal_range = []
    anomalies = []
    temp_adjustments = []
    system_bias = 0

    for entry in sensor_data:
        raw_value = entry['value']
        calibration_factor = entry.get('calibration', 1.0)
        adjusted = raw_value * calibration_factor

        if adjusted > threshold:
            anomalies.append(adjusted)
            if adjusted > 150:
                system_bias += 3
        else:
            normal_range.append(adjusted)

        # Irrelevant temperature drift compensation (distractor)
        if raw_value % 10 == 0:
            temp_adjustments.append(adjusted * 0.05)

    # Dead code path - never executed due to logic above (red herring)
    if len(temp_adjustments) > 100:
        system_bias -= sum(temp_adjustments)

    # Compute moving average over anomalies only if present
    if anomalies:
        avg_anomaly = sum(anomalies) / len(anomalies)
        peak = max(anomalies)
        weighted_score = avg_anomaly * 0.7 + peak * 0.3
    else:
        weighted_score = 0

    # Simulate historical baseline comparison (unused result)
    historical_baseline = [65, 68, 71, 73, 77]
    convergence_rate = 0
    for i, h in enumerate(historical_baseline):
        convergence_rate += abs(h - normal_range[i % len(normal_range)]) if normal_range else 0

    # Real processing: generate metrics using conditional expressions and accumulation
    base_metrics = [x * 1.1 for x in anomalies if x > 80]
    extended_metrics = [x for x in base_metrics if x < 200]

    # Conditional expression with distractor list
    processed_offset = [x ** 0.5 for x in normal_range][-1] if normal_range else 0

    # Aggregation using itertools.chain (relevant usage)
    all_valid = list(itertools.chain(extended_metrics, [processed_offset]))

    # Accumulation with misleading intermediate
    cumulative_shift = 0
    integral_log = []
    for val in all_valid:
        cumulative_shift += val * 0.2
        integral_log.append(cumulative_shift)  # Unused tracking

    # Final aggregation step
    aggregate_metrics = [sum(base_metrics), len(anomalies), cumulative_shift]

    # Key assignment statement
    final_diagnostic = aggregate_metrics[-1] + system_bias

    # Print required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data (deterministic)
sensor_readings = [
    {'value': 60, 'calibration': 1.1},
    {'value': 85, 'calibration': 1.05},
    {'value': 95, 'calibration': 1.02},
    {'value': 160, 'calibration': 0.95},
    {'value': 70, 'calibration': 1.0},
    {'value': 200, 'calibration': 0.8},
    {'value': 55, 'calibration': 1.2}
]

# Execute
diag_result = run_diagnostics(sensor_readings)