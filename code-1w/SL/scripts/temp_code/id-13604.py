from collections import defaultdict, Counter
import itertools

# Simulate system performance metrics over time
metrics = {
    'latency_ms': [120, 85, 95, 130, 110, 90],
    'throughput_ips': [480, 520, 490, 510, 505, 495],
    'error_rate': [0.002, 0.001, 0.003, 0.0015, 0.0008, 0.0022]
}

# Weight configuration for scoring (higher weight = more important)
weights = {'latency_ms': 0.4, 'throughput_ips': 0.5, 'error_rate': 0.6}

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 0)
thresholds['latency_ms'] = 100
thresholds['throughput_ips'] = 500
thresholds['error_rate'] = 0.002

# Historical trend analysis (partially used, partially irrelevant)
trend_slopes = {}
for key in metrics:
    diffs = [metrics[key][i+1] - metrics[key][i] for i in range(len(metrics[key])-1)]
    trend_slopes[key] = sum(diffs) / len(diffs)

# Misleading normalization function (never called)
def normalize_values(data):
    result = {}
    for k, v in data.items():
        min_val, max_val = min(v), max(v)
        result[k] = [(x - min_val) / (max_val - min_val) for x in v]
    return result

# Decoy statistical function using itertools (dead code path)
def compute_rolling_stats(values, window=3):
    rolling_means = []
    for i in range(len(values) - window + 1):
        window_slice = values[i:i+window]
        rolling_means.append(sum(window_slice)/len(window_slice))
    return list(itertools.accumulate(rolling_means))

# Unused anomaly detection logic (red herring)
anomalies = defaultdict(list)
for metric_name, readings in metrics.items():
    avg = sum(readings) / len(readings)
    std_dev = (sum((x - avg)**2 for x in readings) / len(readings)) ** 0.5
    for idx, val in enumerate(readings):
        if abs(val - avg) > 1.8 * std_dev:
            anomalies[metric_name].append(idx)

# Auxiliary transformation (only one part is actually used later)
transformed = {}
for k, v in metrics.items():
    if k == 'latency_ms':
        transformed[k] = [1000/x for x in v]  # Convert to latency score (inverse)
    elif k == 'throughput_ips':
        transformed[k] = [x/10 for x in v]     # Scale down
    else:
        transformed[k] = [1 - x for x in v]   # Invert error rate

# Complex multi-step evaluation logic
base_scores = {}
for key in metrics:
    raw_avg = sum(metrics[key]) / len(metrics[key])
    if key == 'latency_ms':
        base_scores[key] = 100 * (1 - min(raw_avg / 200, 1))
    elif key == 'throughput_ips':
        base_scores[key] = 100 * min(raw_avg / 600, 1)
    else:
        base_scores[key] = 100 * (1 - min(raw_avg / 0.01, 1))

# Secondary adjustment based on trend (actual usage begins here)
improvement_bonus = 0
if trend_slopes['latency_ms'] < 0 and trend_slopes['throughput_ips'] > 0:
    improvement_bonus = 5
elif trend_slopes['error_rate'] < 0:
    improvement_bonus = 2

# Conditional scaling factor
scaling_factor = 1.0
if base_scores['latency_ms'] > 90 and base_scores['throughput_ips'] > 85:
    scaling_factor = 1.1

# Actual core computation path (key reasoning chain)
weighted_parts = {}
for key in weights:
    weighted_parts[key] = base_scores[key] * (1 - weights[key])

composite_score = sum(weighted_parts.values())
scaled_composite = composite_score * scaling_factor
bonus_applied = scaled_composite + improvement_bonus

# Final nonlinear transformation (critical point)
final_score = int(bonus_applied + (bonus_applied * 0.05 * (1 if anomalies['latency_ms'] else 0)))

# Extraneous visualization prep (distractor block)
plot_data = []
for t in itertools.product([0,1], repeat=3):
    plot_data.append(t)

data_summary = Counter(plot_data)

# Output the target result
print(f"Result: {final_score}")