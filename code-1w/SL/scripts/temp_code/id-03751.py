from collections import defaultdict, Counter

# Simulated health monitoring system with multiple sensor streams
def analyze_vital_trend(data, baseline):
    trend_score = 0
    deviation_count = 0
    temporal_weights = [0.8, 0.9, 1.0, 1.1, 1.2]

    for i, reading in enumerate(data):
        if i >= len(temporal_weights):
            break
        weighted_deviation = abs(reading - baseline) * temporal_weights[i]
        if weighted_deviation > 15:
            deviation_count += 1
        trend_score += weighted_deviation

    # Irrelevant computation (distractor)
    noise_floor = sum([x ** 0.5 for x in data[:3]])
    normalization_factor = max(noise_floor, 1)
    normalized_score = trend_score / normalization_factor

    return trend_score, deviation_count


def evaluate_organ_risk(vitals, risk_map):
    risk_levels = defaultdict(int)
    total_anomalies = 0

    for organ, readings in vitals.items():
        avg_reading = sum(readings) / len(readings)
        closest_risk = min(risk_map[organ], key=lambda x: abs(x - avg_reading))
        risk_index = risk_map[organ].index(closest_risk)
        risk_levels[organ] = risk_index
        total_anomalies += risk_index

    # Dead code path (distractor)
    if False:
        debug_trace = []
        for k, v in risk_levels.items():
            debug_trace.append(f'{k}:{v}')

    return risk_levels, total_anomalies


def compute_stability_index(logs):
    stability = 100.0
    fluctuation_penalty = 0

    for i in range(1, len(logs)):
        diff = abs(logs[i] - logs[i-1])
        if diff > 5:
            fluctuation_penalty += diff * 0.3

    stability -= fluctuation_penalty
    return round(stability, 4)


def process_metrics(sensor_data, limits):
    # Core relevant logic
    primary_signals = ['heart_rate', 'respiratory_rate', 'spo2']
    aggregated_diagnostics = []

    # Extract and preprocess signals
    extracted = {}
    for idx, (key, values) in enumerate(sensor_data.items()):
        if key in primary_signals:
            extracted[idx] = [v for v in values if isinstance(v, (int, float))]

    # Analyze each primary signal
    anomaly_registry = []
    for sig_id, readings in extracted.items():
        base = limits[primary_signals[sig_id]]
        score, count = analyze_vital_trend(readings, base)
        anomaly_registry.append(count)

    # Compute composite metrics
    total_anomalies = sum(anomaly_registry)
    severity_weight = total_anomalies * 1.75

    # Secondary analysis on auxiliary systems (partially irrelevant)
    aux_systems = {k: v for k, v in sensor_data.items() if k not in primary_signals}
    risk_assessment, _ = evaluate_organ_risk(aux_systems, {
        'liver': [40, 50, 60],
        'kidney': [30, 45, 60, 75],
        'neuro': [70, 80, 90, 100]
    })

    # Stability evaluation (red herring - not used in final result)
    temp_logs = sensor_data['thermal_history']
    stability_metric = compute_stability_index(temp_logs)

    # Distractor variables
    calibration_offset = sum([len(v) for v in sensor_data.values()]) * 0.01
    historical_bias = sum([sum(v) / len(v) for v in sensor_data.values() if v]) / 7

    # Critical calculation chain
    intermediate = (severity_weight + len(anomaly_registry)) * 10
    adjustment = 0
    for i, anom in enumerate(anomaly_registry):
        if anom > 2:
            adjustment += i * 0.5

    raw_diagnostic = int(intermediate - adjustment)

    # Final transformation using slicing and zip (required feature)
    codes = [101, 202, 303, 404, 505]
    offsets = [1, -1, 2, -2, 0]
    paired = list(zip(codes[1:4], offsets[1:4]))  # slicing + zip

    final_shift = 0
    for code, offset in paired:
        if raw_diagnostic % code < 50:
            final_shift += offset

    final_diagnostic = raw_diagnostic + final_shift

    # Misleading print (distractor)
    debug_value = final_diagnostic ^ 255  # bit manipulation red herring

    # CORRECT output
    return final_diagnostic

# Input data setup
thresholds = {
    'heart_rate': 72,
    'respiratory_rate': 16,
    'spo2': 98
}

health_data = {
    'heart_rate': [70, 75, 80, 85, 90, 92],
    'respiratory_rate': [14, 18, 20, 22, 25, 26],
    'spo2': [99, 97, 95, 94, 93, 92],
    'liver': [45, 48],
    'kidney': [50, 55],
    'neuro': [85, 88],
    'thermal_history': [36.5, 36.7, 37.1, 37.3, 36.9, 37.0, 37.2],
    'motion_artifacts': [1, 0, 1, 1, 0, 2]
}

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")