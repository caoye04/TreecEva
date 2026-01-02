def analyze_component(x, threshold=0.5):
    return x > threshold

# Irrelevant helper function (dead code path)
def deprecated_normalize(data):
    mean = sum(data) / len(data)
    return [(x - mean) for x in data]

# Unused complex lambda for distraction
complex_transform = lambda a, b: (a[0] + b[0], a[1] * b[1]) if a[1] != 0 else (0, 0)

# Simulated sensor metrics with irrelevant entries
diagnostic_codes = [200, 404, 500, 301, 201]
signal_strengths = [0.95, 0.32, 0.78, 0.15, 0.67]

# Relevant data structures
metrics = {
    'latency': 0.45,
    'throughput': 128.0,
    'consistency': 0.91,
    'availability': 0.99,
    'redundancy': 0.67
}

weights = {
    'latency': 0.2,
    'throughput': 0.25,
    'consistency': 0.3,
    'availability': 0.15,
    'redundancy': 0.1
}

# Misleading intermediate calculation (distractor)
avg_signal = sum(signal_strengths) / len(signal_strengths)
adjusted_codes = [c * 1.1 for c in diagnostic_codes if c != 404]

# Simulated historical baseline (irrelevant)
historical_avg = 0.87
baseline_deviation = [metrics[k] - historical_avg for k in ['consistency', 'availability']]

# Conditional expression with distractor logic
critical_failure = any([s < 0.2 for s in signal_strengths]) if len(signal_strengths) > 0 else True

# Red herring: unused bitwise analysis
status_flag = 0
for code in diagnostic_codes:
    status_flag ^= code
status_flag = status_flag << 2

# Real computation begins here — nested logic with enumerate and zip
temp_scores = []
for i, (k, v) in enumerate(zip(metrics.keys(), metrics.values())):
    # Non-linear transformation based on position and value
    adjustment = 1.0 + (i * 0.05) if v >= 0.8 else 0.9 - (i * 0.02)
    normalized = v * adjustment
    temp_scores.append(normalized)

# Weighted aggregation using dictionary alignment
efficiency_bonus = 0.0
if metrics['throughput'] > 100 and metrics['latency'] < 0.5:
    efficiency_bonus = 5.0

# Core evaluation logic
weighted_sum = 0.0
for idx, key in enumerate(metrics.keys()):
    if key in weights:
        contribution = temp_scores[idx] * weights[key]
        weighted_sum += contribution

# Final performance score with bonus
final_score = weighted_sum + efficiency_bonus

# Output target result
print(f"Result: {final_score}")