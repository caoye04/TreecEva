import math

# System health monitoring simulation with diagnostic computation

def analyze_frequency_profile(signal_peaks):
    if not signal_peaks:
        return 0.0
    weighted_sum = sum(p * (i + 1) for i, p in enumerate(signal_peaks))
    normalization = sum(i + 1 for i in range(len(signal_peaks)))
    return weighted_sum / normalization if normalization else 0.0


def detect_anomalies(readings, sensitivity_level=0.85):
    mean_val = sum(readings) / len(readings) if readings else 0
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings) if readings else 0
    std_dev = math.sqrt(variance)
    threshold = sensitivity_level * std_dev
    anomalies = [r for r in readings if abs(r - mean_val) > threshold]
    # Irrelevant transformation
    shadow_score = sum(math.sin(r) for r in readings) * 0.1
    return len(anomalies), threshold

# Decoy function – never used in final computation
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

# Auxiliary diagnostic tool (partially relevant)
def evaluate_stability_index(temporal_data):
    if len(temporal_data) < 2:
        return 0.0
    diffs = [abs(temporal_data[i] - temporal_data[i+1]) for i in range(len(temporal_data)-1)]
    trend_consistency = sum(1 for d in diffs if d < 0.5)
    return trend_consistency / len(diffs)

# Core processing chain
sensor_inputs = [12.4, 15.1, 13.7, 14.2, 16.3, 9.8, 14.0, 13.9, 15.5]
signal_frequencies = [0.5, 0.8, 1.2, 0.9, 1.4]
baseline_shifts = [0.1, -0.3, 0.2, 0.0, -0.1, 0.4]

# Misleading intermediate diagnostics
initial_diagnostic = sum(math.cos(x) for x in sensor_inputs) * 0.01
offset_correction = max(baseline_shifts) - min(baseline_shifts)
dummy_histogram = [sum(1 for x in sensor_inputs if i <= x < i+1) for i in range(9, 18)]

# Real signal path begins here
filtered_readings = [x for x in sensor_inputs if 10 <= x <= 16]
anomaly_count, dynamic_threshold = detect_anomalies(filtered_readings, sensitivity_level=0.78)
frequency_metric = analyze_frequency_profile(signal_frequencies)
stability_metric = evaluate_stability_index(sensor_inputs)

# Complex data structure with red herring fields
processing_chain = {
    'raw': sensor_inputs,
    'filtered': filtered_readings,
    'metrics': {
        'noise_floor': math.exp(-0.1 * len(sensor_inputs)),
        'peak_focus': max(filtered_readings) / (min(filtered_readings) + 1e-5),
        'anomaly_rate': anomaly_count / len(filtered_readings) if filtered_readings else 0,
        'spectral_trend': frequency_metric,
        'temporal_stability': stability_metric
    },
    'flags': {
        'overload': False,
        'drift_detected': abs(baseline_shifts[-1]) > 0.3,
        'sync_locked': True
    }
}

# Unused but plausible-looking diagnostic path
temp_diagnostic = 0
for i, val in enumerate(processing_chain['raw']):
    if i % 3 == 0:
        temp_diagnostic += math.tanh(val * 0.1)

# Threshold policy matrix (some values are decoys)
thresholds = {
    'critical_load': 15.0,
    'recovery_bound': 12.5,
    'stability_min': 0.6,
    'frequency_scale': 1.0,
    'security_margin': 0.85,  # unused
    'calibration_offset': -0.17  # unused
}

# Final aggregation logic — this is the key statement
# Only some components contribute to final result
primary_contributions = [
    processing_chain['metrics']['peak_focus'] * 0.4,
    processing_chain['metrics']['anomaly_rate'] * (-0.3),
    frequency_metric * 0.2,
    stability_metric * 0.1
]

auxiliary_weight = 0.05
if processing_chain['flags']['sync_locked'] and not processing_chain['flags']['overload']:
    auxiliary_weight += 0.05

aggregate_metrics = lambda chain, th: sum(primary_contributions) + auxiliary_weight * th['recovery_bound']

# This is the critical execution point
final_diagnostic = aggregate_metrics(processing_chain, thresholds)

# Dead code path — looks important but does nothing
if final_diagnostic > 1.0:
    adjustment_cycle = []
    for t in thresholds.keys():
        adjustment_cycle.append(f"Recalibrating {t}")

# Output target result
print(f"Result: {final_diagnostic}")