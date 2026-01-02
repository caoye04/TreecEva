from collections import defaultdict, Counter
import math

# Simulate system performance metrics over time
timestamps = [100, 101, 102, 103, 104, 105]
raw_data = [
    {'cpu': 85, 'mem': 70, 'latency': 45, 'req_per_sec': 98},
    {'cpu': 90, 'mem': 75, 'latency': 50, 'req_per_sec': 95},
    {'cpu': 92, 'mem': 78, 'latency': 55, 'req_per_sec': 90},
    {'cpu': 87, 'mem': 72, 'latency': 52, 'req_per_sec': 93},
    {'cpu': 83, 'mem': 68, 'latency': 48, 'req_per_sec': 97},
    {'cpu': 80, 'mem': 65, 'latency': 44, 'req_per_sec': 99}
]

# Irrelevant preprocessing: analyze timestamp gaps (unused later)
time_gaps = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
median_gap = sorted(time_gaps)[len(time_gaps)//2]

decoy_counter = Counter()
for entry in raw_data:
    bucket = 'high' if entry['cpu'] > 85 else 'normal'
    decoy_counter[bucket] += 1

# Distractor function: looks useful but unused
def calculate_anomaly_score(data_list):
    anomalies = 0
    for d in data_list:
        if d['latency'] > 50 and d['req_per_sec'] < 92:
            anomalies += 1
    return anomalies * 10

# Another red herring: complex transformation with no impact
temp_aggregation = defaultdict(float)
for t, d in zip(timestamps, raw_data):
    temp_aggregation[t] = sum(d.values()) / len(d)

snapshot_weights = {t: 0.1 + (t - 100) * 0.01 for t in timestamps}
weighted_sum = sum(temp_aggregation[t] * snapshot_weights[t] for t in timestamps)

# Real computation begins here
baseline_metrics = {
    'cpu': 80,
    'mem': 70,
    'latency': 50,
    'req_per_sec': 95
}

weights = {
    'cpu': 0.3,
    'mem': 0.2,
    'latency': 0.4,
    'req_per_sec': 0.1
}

# Simulated calibration offset (distractor, not used in final calc)
calibration_factor = math.log(1 + weighted_sum / 100)

# Actual signal processing: deviation from baseline
metrics = []
for entry in raw_data:
    deviation_score = 0
    for key in baseline_metrics:
        actual = entry[key]
        expected = baseline_metrics[key]
        # Higher latency or lower req_per_sec is bad; others are high-is-bad
        if key == 'latency':
            dev = max(0, actual - expected)
        elif key == 'req_per_sec':
            dev = max(0, expected - actual)
        else:
            dev = max(0, actual - expected)
        deviation_score += dev
    
    # Normalize and invert: lower deviation = higher health
    health = 100 - (deviation_score * 2)
    metrics.append(max(health, 20))  # floor at 20

# Another distraction: frequency analysis of health bands
health_counter = Counter()
for m in metrics:
    band = (m // 10) * 10
    health_counter[band] += 1

# Weighted average using weights (core logic)
weighted_metrics = []
debug_info = []
for i, m in enumerate(metrics):
    time_weight = 0.8 + (i * 0.05)  # increasing recency bias
    adjusted = m * time_weight
    weighted_metrics.append(adjusted)
    debug_info.append(f'Sample {i}: {adjusted:.2f}')

# Dead code path: never executed
dummy_route_taken = False
if sum(m) < 0:  # Impossible condition
    backup_weights = [0.1] * len(metrics)
    final_value = sum(m * w for m, w in zip(metrics, backup_weights))
    dummy_route_taken = True
else:
    pass  # Placeholder

# Core evaluation function
def evaluate_performance(performance_list, importance_weights):
    total_weight = sum(importance_weights.values())
    normalized_weights = {k: v / total_weight for k, v in importance_weights.items()}
    
    # Map list to weight using index alignment (not keys)
    composite = 0
    for idx, score in enumerate(performance_list):
        # Use cyclic weight assignment based on index
        weight_keys = list(normalized_weights.keys())
        effective_weight = normalized_weights[weight_keys[idx % len(weight_keys)]]
        composite += score * effective_weight * 1.1  # boost factor
    
    # Apply ceiling cap
    return min(composite, 500)

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Additional noise: post-processing that doesn't affect result
audit_log = defaultdict(list)
for i, val in enumerate(weighted_metrics):
    audit_log['values'].append(val)
audit_log['processed'] = True

# Final output
print(f"Result: {final_score}")