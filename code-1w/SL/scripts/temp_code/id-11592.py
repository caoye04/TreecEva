from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
def collect_diagnostics():
    diagnostics = defaultdict(int)
    sensors = ['temp', 'pressure', 'flow', 'vibration']
    readings = [[32, 35, 33], [88, 90, 89], [150, 142, 148], [0.8, 1.1, 0.9]]

    for i, sensor in enumerate(sensors):
        base_val = sum(readings[i]) / len(readings[i])
        diagnostics[sensor] = round(base_val, 2)

    # Irrelevant transformation (distractor)
    temp_offset = [x - 25 for x in readings[0]]
    pressure_zscores = [round((x - 89) / 2, 2) for x in readings[1]]

    return diagnostics

def calculate_baseline(diagnostics):
    # Baseline derived from sensor averages
    baseline = 0
    if diagnostics['temp'] > 30:
        baseline += 10
    if diagnostics['pressure'] < 95:
        baseline += 15
    if diagnostics['flow'] > 140:
        baseline += 5

    # Dead code path (misleading)
    if diagnostics['vibration'] > 2.0:
        baseline -= 20  # Never reached

    return baseline

def adjust_for_anomalies(raw_metrics):
    # Anomaly adjustment using conditional logic and list comprehension
    anomalies = [val for val in raw_metrics.values() if val > 50]
    adjustment = 0
    
    for anomaly in anomalies:
        if anomaly > 100:
            adjustment += 3
        elif anomaly > 75:
            adjustment += 2
        else:
            adjustment += 1

    # Unused computation (interference)
    squared_devs = [(x - 80)**2 for x in raw_metrics.values()]
    avg_sq_dev = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    return adjustment * 2

def evaluate_performance(weights, metrics):
    weighted_sum = 0.0
    total_weight = sum(weights.values())

    for key in weights:
        if key in metrics:
            weighted_sum += weights[key] * metrics[key]
    
    score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Secondary adjustment based on logical conditions
    penalty = 0
    if metrics['temp'] > 34:
        penalty += 5
    if metrics['flow'] < 145 and metrics['pressure'] < 90:
        penalty += 3
    
    # Final non-linear transformation (relevant)
    final_score = int(round(score - penalty + (adjust_for_anomalies(metrics) * 1.5)))
    
    # Red herring variables (no impact)
    debug_trace = {k: f"processed_{i}" for i, k in enumerate(metrics.keys())}
    normalization_factor = max(metrics.values()) / 100.0 if metrics else 1
    
    return final_score

# Main execution flow
diag_data = collect_diagnostics()
raw_metrics = dict(diag_data)
raw_metrics['flow'] = 142  # minor correction
raw_metrics['runtime'] = 120  # irrelevant metric

metric_weights = {
    'temp': 0.2,
    'pressure': 0.3,
    'flow': 0.35,
    'vibration': 0.15
}

baseline_score = calculate_baseline(diag_data)
preliminary_total = baseline_score * 2.5  # unused intermediate

# Key statement
final_score = evaluate_performance(metric_weights, raw_metrics)

print(f"Result: {final_score}")