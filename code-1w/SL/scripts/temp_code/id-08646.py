from collections import defaultdict, Counter

# Simulated sensor data stream with noise and redundant readings
timestamped_readings = [
    (1001, [0.8, 1.2, 3.1, 2.9, 5.0]),
    (1002, [0.7, 1.3, 3.2, 3.0, 4.8]),
    (1003, [0.6, 1.1, 3.0, 2.8, 5.1]),
    (1004, [2.5, 1.0, 2.9, 2.7, 5.2]),  # spike in first sensor
    (1005, [0.9, 1.4, 3.3, 3.1, 4.7])
]

# Irrelevant baseline calibration map (distractor)
calibration_map = {
    'sensor_a': lambda x: x * 1.02,
    'sensor_b': lambda x: x * 0.99,
    'sensor_c': lambda x: x * 1.01,
    'sensor_d': lambda x: x * 1.03,
    'sensor_e': lambda x: x * 0.98
}

# Preprocess: extract only valid windows (ignore entries where any sensor > 4.0)
valid_windows = []
anomaly_log = []
spike_count = 0

for ts, readings in timestamped_readings:
    if any(r > 4.0 for r in readings):
        anomaly_log.append((ts, readings))
        spike_count += 1
        continue  # skip anomalous readings
    valid_windows.append(readings)

# Dead code path: predictive modeling stub (never used)
def predict_next_state(data_window):
    """Predict next state (unused function - red herring)"""
    return [sum(d)/len(d) + 0.1 for d in zip(*data_window)]

# Distractor: historical trend analysis (computed but not used)
historical_averages = defaultdict(list)
for window in valid_windows:
    for i, val in enumerate(window):
        historical_averages[f'sensor_{i}'].append(val)

overall_trends = {}
for sensor, vals in historical_averages.items():
    overall_trends[sensor] = sum(vals) / len(vals)

# Real computation begins: compute rolling consistency score
consistency_scores = []
for window in valid_windows:
    diffs = [abs(window[i] - window[i+1]) for i in range(len(window)-1)]
    consistency_scores.append(1 / (1 + sum(diffs)))  # higher = more stable

# Compute entropy-based irregularity index (partially relevant)
from math import log

def compute_entropy(values):
    counter = Counter(values)
    total = len(values)
    return -sum((count/total) * log(count/total) for count in counter.values())

entropy_values = [compute_entropy([round(x, 1) for x in w]) for w in valid_windows]

# Aggregate health score: weighted combination of consistency and entropy
aggregate_health_score = 0
for i, (c, e) in enumerate(zip(consistency_scores, entropy_values)):
    weight = 0.7 if i % 2 == 0 else 0.3
    aggregate_health_score += weight * c * 100 + (1 - weight) * e * 50

# Anomaly factor based on spike history (only one spike detected)
anomaly_factor = max(spike_count, 1) * len(anomaly_log) or 1

# Key statement: final diagnostic calculation
final_diagnostic = aggregate_health_score // anomaly_factor

# Irrelevant post-processing: generate report codes (dead logic)
report_codes = []
for ts, _ in anomaly_log:
    code = f"ERR-{ts % 100}-{spike_count ^ 2}"
    report_codes.append(code)

# Another decoy: simulate fallback thresholding
if final_diagnostic < 50:
    fallback_buffer = [c for c in consistency_scores if c > 0.5]
    if fallback_buffer:
        final_diagnostic = (final_diagnostic + sum(fallback_buffer)) / 2

# Output the target result
print(f"Result: {final_diagnostic}")