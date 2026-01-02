from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic scoring
def analyze_readings(readings):
    stats = defaultdict(int)
    anomalies = []
    temporal_flags = [False] * len(readings)

    # Irrelevant frequency counter (distractor)
    freq_count = Counter()
    for val in readings:
        freq_count[val] += 1

    cumulative = 0
    threshold = sum(readings) / len(readings) * 1.3

    for i, val in enumerate(readings):
        if val > threshold and val % 2 == 1:
            anomalies.append(i)
            temporal_flags[i] = True

        if i > 0 and readings[i] < readings[i-1]:
            stats['drops'] += 1

        cumulative += abs(val)

    stats['total_anomalies'] = len(anomalies)
    stats['cumulative_magnitude'] = cumulative

    # Dead code path - never accessed under current logic (red herring)
    debug_snapshot = None
    if len(anomalies) > 100:
        debug_snapshot = [readings[i] for i in anomalies]

    return stats, anomalies, temporal_flags

# System calibration constants (some irrelevant)
calibration_map = {
    'gain': 1.07,
    'offset': -0.33,
    'decay': 0.86,
    'dummy_key': 999  # Unused parameter
}

# Primary dataset
sensor_log = [
    12, 15, 14, 18, 21, 19, 25, 22, 30, 28,
    11, 16, 13, 20, 17, 24, 26, 31, 23, 29
]

# Secondary derived values (some used, some not)
smoothed_values = [round(x * calibration_map['gain'] + calibration_map['offset']) for x in sensor_log]
parity_check = sum(1 for x in smoothed_values if x % 2 == 0)
even_ratio = parity_check / len(smoothed_values)

# Execute main analysis
diagnostics, detected_anomalies, flags = analyze_readings(smoothed_values)

# Intermediate computations with mixed relevance
base_score = diagnostics['cumulative_magnitude'] // (diagnostics['total_anomalies'] or 1)
anomaly_cluster_score = 0
if detected_anomalies:
    gaps = [detected_anomalies[i+1] - detected_anomalies[i] for i in range(len(detected_anomalies)-1)]
    if gaps:
        anomaly_cluster_score = len([g for g in gaps if g <= 3])

# Distractor: unused transformation chain
temp_array = [x ** 0.5 for x in sensor_log if x > 15]
aggregated_temp = sum(temp_array) / len(temp_array) if temp_array else 0
snapshot_reference = {i: v for i, v in enumerate(sensor_log) if v > 25}

# Conditional correction factor based on pattern density
correction_factor = 1
if diagnostics['drops'] > 8:
    correction_factor = 2
elif diagnostics['drops'] > 5:
    correction_factor = 1.5
else:
    correction_factor = 0.8

# Anomaly offset derived from cluster score and drop patterns
anomaly_offset = 0
if anomaly_cluster_score > 0:
    anomaly_offset = diagnostics['total_anomalies'] * 3 + anomaly_cluster_score * 5
else:
    anomaly_offset = diagnostics['total_anomalies'] * 2

# Critical assignment point — target of evaluation
final_diagnostic = base_score + anomaly_offset * correction_factor

# Irrelevant final aggregation (misleading)
consistency_metric = 0
for k, v in diagnostics.items():
    if v > 0:
        consistency_metric += math.log(v + 1)

# Print required result
print(f"Result: {final_diagnostic}")