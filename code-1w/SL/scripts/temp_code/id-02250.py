import itertools

# Simulated system performance metrics from distributed components
task_throughput = [120, 150, 130, 160, 145]
error_rates = [0.01, 0.008, 0.012, 0.005, 0.009]
response_times = [230, 190, 210, 180, 205]
resource_utilization = [78, 85, 80, 88, 82]

# Irrelevant auxiliary data (distractor)
heartbeat_signals = [[1, 0, 1], [0, 1, 1], [1, 1, 0], [0, 0, 1], [1, 1, 1]]
dummy_checksums = list(map(lambda x: (x * 3 + 7) % 101, resource_utilization))

# Weight configurations for evaluation (some are decoys)
weights = {
    'throughput': 0.3,
    'errors': -0.4,
    'latency': -0.2,
    'usage': 0.1,
    'fake_metric_a': 0.05,
    'fake_metric_b': -0.03
}

# Misleading transformation (dead path)
def apply_noise(data, factor=0.05):
    import random
    return [x + random.uniform(-factor, factor) * x for x in data]

# Unused normalization function (distractor)
def normalize_minmax(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Core evaluation logic
metrics = {
    'throughput': sum(task_throughput) / len(task_throughput),
    'errors': sum(error_rates) / len(error_rates),
    'latency': sum(response_times) / len(response_times),
    'usage': sum(resource_utilization) / len(resource_utilization)
}

# Complex derived adjustment using itertools and slicing
adjustment_window = list(itertools.accumulate(
    [abs(response_times[i] - response_times[i-1]) for i in range(1, len(response_times))]
))

if len(adjustment_window) > 3:
    recent_fluctuations = adjustment_window[-3:]
    fluctuation_penalty = sum(recent_fluctuations) / 3
else:
    fluctuation_penalty = 0

# Additional red herring: simulated timestamp drift correction (unused)
timestamp_drift = [i * 0.02 for i in range(len(task_throughput))]
corrected_time = [rt - dt for rt, dt in zip(response_times, timestamp_drift)]

# Real adjustment based on fluctuation penalty
metrics['latency'] += fluctuation_penalty

# Decoy scoring with fake metrics (never used)
fake_scores = {
    'fake_metric_a': (metrics['throughput'] * weights['fake_metric_a']) ** 0.5,
    'fake_metric_b': metrics['usage'] * abs(weights['fake_metric_b'])
}

# Actual performance evaluation function
def evaluate_performance(met, w):
    score = 0.0
    # Key calculation with correct weight application
    score += met['throughput'] * w['throughput']
    score += met['errors'] * w['errors']
    score += met['latency'] * w['latency']
    score += met['usage'] * w['usage']
    
    # Spurious nested condition (misleading)
    if met['usage'] > 80:
        temp_boost = 5.0
        if met['errors'] < 0.01:
            temp_boost *= 1.2
            # Dead code branch
            for _ in range(2):
                temp_boost = (temp_boost ** 0.5) * 0.9
        score += temp_boost  # This looks important but is actually minor
    
    return round(score, 6)

# Final computation
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")