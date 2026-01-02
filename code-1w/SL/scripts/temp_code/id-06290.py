def analyze_trends(data, threshold=0.5):
    trends = {}
    for i, value in enumerate(data):
        if value > threshold:
            trends[i] = 'positive'
        elif value < -threshold:
            trends[i] = 'negative'
        else:
            trends[i] = 'neutral'
    return trends

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    mag = sum(x ** 2 for x in v) ** 0.5
    return [x / mag for x in v] if mag else v

# Another decoy: complex but unused transformation
def spectral_decomposition(matrix):
    result = []
    for i in range(len(matrix)):
        row_trace = 0
        for j in range(len(matrix[i])):
            if i == j:
                row_trace += matrix[i][j] * 1.5
        result.append(row_trace)
    return result

# Misleading intermediate calculation (not used in final result)
baseline_adjustment = 0
for k in range(8):
    baseline_adjustment += (k * k) % 7
baseline_adjustment = (baseline_adjustment // 3) - 10

# Real data processing starts here
def compute_stability_index(sequence):
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    return round(sum(diffs) / len(diffs), 4) if diffs else 0.0

sensor_readings = [0.1, 0.4, 0.7, 0.9, 0.3, 0.2, 0.8]
stability = compute_stability_index(sensor_readings)

# Simulated system metrics (some fields are red herrings)
metrics = {
    'latency': 120,
    'throughput': 850,
    'error_rate': 0.023,
    'consistency': stability,  # Only this one depends on prior logic
    'redundancy': 4,
    'bandwidth_usage': 78
}

# Weight map: higher weight = more important
weights = {
    'latency': 0.2,
    'throughput': 0.15,
    'error_rate': 0.3,
    'consistency': 0.25,  # Weight applied to stability from earlier
    'uptime': 0.1,  # Unused metric (misdirection)
    'security_level': 0.0  # Zero weight = irrelevant
}

# Fake dependency chain to distract
historical_data = [0.12, 0.15, 0.11, 0.14]
adjusted_history = [x * 1.05 for x in historical_data]
legacy_score = sum(adjusted_history) * 0.9

# Core evaluation logic — only this matters
extra_weights = {'redundancy': 0.05, 'bandwidth_usage': 0.05}
weights.update(extra_weights)

# Evaluate performance using only keys present in both metrics and weights
effective_keys = set(metrics.keys()) & set(weights.keys())
score_components = []
for key in effective_keys:
    weighted_value = metrics[key] * weights[key]
    score_components.append(weighted_value)

total_weight = sum(weights[k] for k in effective_keys)

# Final computation
if total_weight > 0:
    final_score = sum(score_components) / total_weight
else:
    final_score = 0.0

# Print target result
print(f"Target result: {final_score}")