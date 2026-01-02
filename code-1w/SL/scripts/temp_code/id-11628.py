def analyze_component_health(reading, threshold_map, history):
    if not history:
        return 0
    recent_avg = sum(history[-3:]) / len(history[-3:])
    deviation = abs(reading - recent_avg)
    criticality = 0
    
    # Irrelevant temperature scaling (distractor)
    temp_scale = 1.0
    if reading > threshold_map['overload']:
        temp_scale = 0.9
    elif reading < threshold_map['idle']:
        temp_scale = 1.1
    scaled_dev = deviation * temp_scale  # unused downstream

    # Actual health logic
    if deviation > threshold_map['fluctuation']:
        criticality += 2
    if reading > threshold_map['warning']:
        criticality += 1
    if reading > threshold_map['overload']:
        criticality += 3
    
    # Dead code path (never taken due to input constraints)
    if reading == -999:
        return -1  # sensor error (unused)

    return criticality


def evaluate_stability_index(metrics, weights):
    index = 0.0
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            index += val * weights[i % len(weights)]
        else:
            index -= val * 0.5
    # Obfuscated rounding
    return int(index * 100 + 0.5) / 100.0

# Misleading auxiliary function (not used in final computation)
def calculate_thermal_load(sensor_data, calibration):
    total = 0
    for x in sensor_data:
        total += x ** 2 + calibration
    return total // len(sensor_data)

# Unused data structure (red herring)
legacy_system_configs = {
    'voltage': [3.3, 3.4, 3.2],
    'tolerance': {'high': 5, 'low': 1},
    'mode': 'legacy'
}

# Main diagnostic variables
log_entries = [
    {'time': 0, 'cpu': 70, 'mem': 45, 'disk': 20},
    {'time': 1, 'cpu': 72, 'mem': 47, 'disk': 21},
    {'time': 2, 'cpu': 75, 'mem': 49, 'disk': 23},
    {'time': 3, 'cpu': 88, 'mem': 55, 'disk': 25},
    {'time': 4, 'cpu': 95, 'mem': 60, 'disk': 28}
]

system_thresholds = {
    'warning': 80,
    'overload': 90,
    'fluctuation': 10,
    'idle': 50
}

# Distractor: irrelevant counters
anomaly_count = 0
staging_flag = False

# Historical readings for fluctuation analysis (relevant)
historical_cpu = [65, 68, 70, 72, 74, 75, 78, 80, 82, 85]

# Simulate component evaluation (key logic)
health_scores = []
for entry in log_entries:
    cpu_val = entry['cpu']
    score = analyze_component_health(cpu_val, system_thresholds, historical_cpu)
    health_scores.append(score)
    if cpu_val > system_thresholds['warning']:
        anomaly_count += 1  # distractor counter

# Weight array for stability index (used)
weights = [0.3, 0.5, 0.2]

# Compute composite metrics (partially relevant)
stability_metrics = []
for idx, entry in enumerate(log_entries):
    combined_load = entry['cpu'] * 0.6 + entry['mem'] * 0.3 + entry['disk'] * 0.1
    stability_metrics.append(combined_load)

# Secondary transformation using enumerate and zip (required Python features)
adjusted_metrics = []
for i, (orig, score) in enumerate(zip(stability_metrics, health_scores)):
    adjustment_factor = 1.0
    if i > 2:
        adjustment_factor = 0.9
    adjusted_metrics.append(score * adjustment_factor + (i % 3))

# Build diagnostic map (dictionary operation - required feature)
diagnostic_map = {}
for i, adj in enumerate(adjusted_metrics):
    diagnostic_map[f'phase_{i}'] = round(adj * 1.1, 2)

# Final aggregation
aggregated_diagnostic = sum(diagnostic_map.values())

# Apply non-linear correction based on stability trend
if len(stability_metrics) > 1:
    trend = stability_metrics[-1] - stability_metrics[0]
    if trend > 15:
        aggregated_diagnostic *= 1.2

# Key assignment statement
final_diagnostic = int(round(aggregated_diagnostic))

# Dead code block (misleading)
if staging_flag:
    final_diagnostic = -1
    for k in legacy_system_configs:
        final_diagnostic -= len(k)

# Print result as required
print(f"Result: {final_diagnostic}")