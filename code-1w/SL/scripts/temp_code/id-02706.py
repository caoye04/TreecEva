def analyze_system_load(usage_log):
    peak_load = max(usage_log)
    avg_load = sum(usage_log) / len(usage_log)
    normalized = [u / peak_load for u in usage_log]
    variance = sum((x - avg_load) ** 2 for x in usage_log) / len(usage_log)
    return avg_load, variance


def filter_outliers(data, threshold=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered

# Simulated sensor readings over time (irrelevant to final answer but adds distraction)
sensor_readings = [23.1, 24.5, 19.8, 25.6, 22.3, 20.1, 26.7, 24.0, 23.9, 100.5, 25.1, 24.7]
smoothed_data = filter_outliers(sensor_readings)

# System performance metrics (core data)
metrics = {
    'response_time': 145,
    'throughput': 890,
    'error_rate': 0.023,
    'memory_usage': 67.8,
    'cpu_efficiency': 0.88
}

# Weighting schema for evaluation (some weights are unused - distractor)
benchmark_weights = {
    'response_time': 0.3,
    'throughput': 0.25,
    'error_rate': 0.2,
    'memory_usage': 0.15,
    'cpu_efficiency': 0.1,
    'bandwidth': 0.05,  # Unused weight - red herring
    'latency_jitter': 0.05  # Unused weight - red herring
}

# Historical baselines (distractor data)
historical_avg = {
    'response_time': 160,
    'throughput': 850,
    'error_rate': 0.03,
    'memory_usage': 70.0
}

# Normalization function for metrics
def normalize_metric(value, key):
    baselines = {'response_time': 200, 'throughput': 1000, 'error_rate': 0.1, 'memory_usage': 100, 'cpu_efficiency': 1.0}
    return value / baselines.get(key, 1)

# Compute derived statistics (some irrelevant)
drift_analysis = {}
for key in ['response_time', 'throughput', 'error_rate']:
    drift = metrics[key] - historical_avg.get(key, 0)
    drift_analysis[key + '_drift'] = drift

# Core evaluation logic
weighted_sum = 0.0
max_possible = 0.0
for key in benchmark_weights:
    if key in metrics:
        normalized = normalize_metric(metrics[key], key)
        weight = benchmark_weights[key]
        weighted_sum += normalized * weight
        max_possible += weight  # Since normalized ≤ 1

# Secondary adjustment based on quality gates
quality_gate_bonus = 0.0
if metrics['error_rate'] < 0.025 and metrics['response_time'] < 150:
    quality_gate_bonus = 0.05

# Final performance score calculation
final_score = (weighted_sum / max_possible) * 100 + quality_gate_bonus * 100

# Irrelevant aggregation of sensor stats (dead computation path)
total_smoothed = sum(smoothed_data)
avg_smoothed = total_smoothed / len(smoothed_data)
load_profile, load_variance = analyze_system_load([int(x) for x in smoothed_data])

# Output the target result
Result: {final_score}