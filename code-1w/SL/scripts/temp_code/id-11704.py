def analyze_component(metrics, weights):
    weighted_sum = 0
    normalization_factor = sum(weights.values())
    temp_debug_value = 0
    
    for key, value in metrics.items():
        if key in weights:
            contribution = value * weights[key]
            weighted_sum += contribution
            temp_debug_value += contribution ** 0.5  # Irrelevant to final result
    
    return weighted_sum / normalization_factor if normalization_factor else 0


def validate_stability(readings):
    variance = 0
    mean = sum(readings) / len(readings)
    for r in readings:
        variance += (r - mean) ** 2
    variance /= len(readings)
    return variance < 50

# Simulated benchmark data from system diagnostics
diagnostic_log = {
    'cpu_load': [0.78, 0.82, 0.75, 0.91],
    'memory_usage': [0.64, 0.71, 0.68, 0.73],
    'disk_latency': [12, 15, 11, 14]
}

metric_weights = {
    'throughput': 0.4,
    'latency': 0.35,
    'consistency': 0.25
}

system_metrics = {
    'throughput': 89.4,
    'latency': 42.6,
    'consistency': 76.3
}

stability_readings = [88, 91, 85, 89, 90, 87]

# Auxiliary tracking variables (some unused)
counter_tracker = {i: 0 for i in range(5)}
debug_snapshot = []
aggregate_baseline = 0

for i in range(3):
    aggregate_baseline += system_metrics['throughput'] * 0.1
    debug_snapshot.append(f'Stage {i} baseline: {aggregate_baseline}')

# Misleading intermediate calculation
temp_result = 0
for val in diagnostic_log['disk_latency']:
    temp_result += val ** 2
adjustment_factor = temp_result / 100  # Not used in final computation

# Core performance score calculation
efficiency_score = analyze_component(system_metrics, metric_weights)

# Secondary validation check (result used conditionally)
is_stable = validate_stability(stability_readings)

bonus_award = 0
if is_stable:
    bonus_award = 10
    extra_validation = efficiency_score * 0.1  # Distractor

penalty = 0
if efficiency_score < 70:
    penalty = 5

# Final integration step
final_score = efficiency_score + bonus_award - penalty

# Red herring: unrelated data grouping
grouped_data = {}
for i, val in enumerate(stability_readings):
    group_key = f'group_{val // 10}'
    if group_key not in grouped_data:
        grouped_data[group_key] = []
    grouped_data[group_key].append(val)

# Output target result
Result: {final_score}