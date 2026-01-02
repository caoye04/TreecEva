def analyze_workload(loads):
    if not loads:
        return 0
    avg_load = sum(loads) / len(loads)
    peak = max(loads)
    normalized_peak = peak / (avg_load + 1e-9)
    efficiency = (avg_load / (peak + 1e-9)) ** 2
    return efficiency * 100


def compute_health_index(status_vals):
    baseline = 75.0
    adjustment = 0.0
    for val in status_vals:
        if val < 30:
            adjustment -= 5
        elif val > 80:
            adjustment += 3
    return baseline + adjustment

# Irrelevant helper (distractor)
def predict_trend(data):
    if len(data) < 2:
        return 0
    slope = (data[-1] - data[0]) / (len(data) - 1)
    return int(slope * 10) // 2

# Unused function (dead code path)
def deprecated_scale(x):
    return (x ** 0.5) * 1.8 + 10

# Distractor variables
temp_cache = [0] * 50
buffer_overflow_flag = False
redundant_factor = 1.07
offset_correction = 2.3

# Core metric keys
metric_weights = {
    'response_time': 0.35,
    'throughput': 0.25,
    'error_rate': -0.40,
    'latency_jitter': -0.20,
    'cpu_util': 0.15
}

thresholds = {
    'critical': 90,
    'warning': 70,
    'normal': 50
}

# Simulated input metrics
metrics = {
    'response_time': 68,
    'throughput': 82,
    'error_rate': 12,
    'latency_jitter': 45,
    'cpu_util': 77,
    'memory_usage': 61,  # unused in calculation (red herring)
    'disk_iops': 200     # irrelevant field
}

# List comprehension with mixed relevance
weighted_components = [
    metrics[key] * weight 
    for key, weight in metric_weights.items() 
    if key in metrics
]

# Secondary transformation with distraction
efficiency_scores = []
for k, v in metrics.items():
    if k == 'error_rate' or k == 'latency_jitter':
        score = 100 - v
    else:
        score = v
    efficiency_scores.append(score)

# Dummy aggregation (misleading intermediate)
fake_aggregate = sum(efficiency_scores) / len(efficiency_scores) + 5

# Real evaluation logic hidden among noise
def evaluate_performance(met, thres):
    base = 0.0
    penalty = 0.0
    bonus = 0.0

    # Use only specific keys from weights
    for key, weight in metric_weights.items():
        val = met.get(key, 0)
        contribution = val * weight
        base += contribution

        # Bonus/penalty rules
        if val >= thres['critical'] and key in ['throughput', 'response_time']:
            bonus += 8
        if val > thres['warning'] and key == 'cpu_util':
            penalty += 3
        if val < thres['normal'] and 'rate' in key:
            bonus += 5

    # Hidden adjustment via list comprehension side-calculation
    jitter_factor = met['latency_jitter'] // 10
    adjustment_sequence = [base + i * jitter_factor for i in range(3)]
    base = adjustment_sequence[2]  # Only last element matters

    # Final non-linear scaling
    raw_score = base + bonus - penalty
    clamped = max(0, min(100, raw_score))
    return int(clamped * 1.76)  # Final transformation to answer space

# Unused but plausible-looking diagnostic
workload_snapshot = [60, 75, 80, 68, 72]
current_efficiency = analyze_workload(workload_snapshot)
projected_trend = predict_trend(workload_snapshot)

# Health index computed but not used (distractor)
system_health = compute_health_index(list(metrics.values()))

# Key execution point
temp_debug_log = {"stage": "pre_eval", "input": dict(metrics)}
final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")