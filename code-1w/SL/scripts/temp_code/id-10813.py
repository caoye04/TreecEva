from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor fusion system for autonomous drone navigation
def analyze_sensor_variance(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return variance

# Irrelevant signal processing function (decoy)
def apply_fourier_smoothing(signal, passes=3):
    for _ in range(passes):
        smoothed = []
        for i in range(len(signal)):
            neighbors = signal[max(0, i-1):min(len(signal), i+2)]
            smoothed.append(sum(neighbors) / len(neighbors))
        signal = smoothed
    return signal

# Unused fault detection logic (dead path)
def identify_anomalies(logs, threshold=0.85):
    anomaly_flags = []
    for log in logs:
        score = sum(1 for c in log if c.isupper()) / len(log) if log else 0
        anomaly_flags.append(score > threshold)
    return anomaly_flags

# Core evaluation logic with distractors
metric_weights = {
    'latency': 0.4,
    'jitter': 0.15,
    'throughput': 0.3,
    'alignment': 0.1,
    'redundancy': 0.05  # Unused in final calculation (red herring)
}

raw_outcomes = [
    [120, 0.05, 850, 0.92],      # latency (ms), jitter (%), throughput (Mbps), alignment (score)
    [110, 0.07, 900, 0.88],
    [130, 0.04, 830, 0.94],
    [115, 0.06, 870, 0.90]
]

# Phantom normalization (unused)
def normalize_metrics(data):
    normalized = []
    for row in data:
        norm_row = [(val - min(row)) / (max(row) - min(row)) if max(row) != min(row) else 0 for val in row]
        normalized.append(norm_row)
    return normalized

# Hidden transformation chain
baseline_ref = [100, 0.03, 1000, 0.85]
temp_adjustments = defaultdict(float)

for i, metrics in enumerate(raw_outcomes):
    for j, (m, base) in enumerate(zip(metrics, baseline_ref)):
        temp_adjustments[f'delta_{j}'] += abs(m - base)

# Distractor: unused aggregation
summary_stats = Counter()
for outcome in raw_outcomes:
    category = 'high_perf' if outcome[2] > 850 else 'standard'
    summary_stats[category] += 1

# Real processing begins here — buried among noise
transformed_scores = []
for entry in raw_outcomes:
    # Only these four are actually used
    latency, jitter, throughput, alignment = entry
    
    # Performance scoring with non-linear penalties
    latency_penalty = max(0, (latency - 100) * 0.5)
    jitter_penalty = max(0, (jitter - 0.05) * 100)
    throughput_bonus = max(0, (throughput - 800) * 0.05)
    alignment_bonus = alignment * 10
    
    raw_score = 100 - latency_penalty - jitter_penalty + throughput_bonus + alignment_bonus
    transformed_scores.append(raw_score)

# Weighted evaluation (only weights actually used here)
effective_weights = {k: v for k, v in metric_weights.items() if k != 'redundancy'}
weight_sum = sum(effective_weights.values())
scaled_weights = {k: v / weight_sum for k, v in effective_weights.items()}

# Final computation buried in abstraction
aggregated = 0
for idx, score in enumerate(transformed_scores):
    # Circular weighting based on position (distraction)
    cycle_factor = (idx % 3) / 10
    adjusted = score * (1 + cycle_factor)
    aggregated += adjusted

# Actual final score computation
final_score = aggregated / len(transformed_scores)

# Irrelevant slicing operation (distractor)
windows = [transformed_scores[i:i+2] for i in range(0, len(transformed_scores), 2)]
overlaps = list(zip_longest(transformed_scores, transformed_scores[1:], fillvalue=0))

# Print required output
Result: {final_score}