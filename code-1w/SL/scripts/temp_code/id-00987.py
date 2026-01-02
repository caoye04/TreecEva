import math

# Simulated system health monitoring with complex transformations
def analyze_subsystem_log(data, threshold=0.85):
    anomalies = 0
    total_entries = len(data)
    for entry in data:
        if entry['voltage'] < 3.0 or entry['voltage'] > 5.0:
            anomalies += 1
    return anomalies / total_entries if total_entries else 0

# Irrelevant helper function (decoy)
def legacy_checksum(arr):
    acc = 0
    for x in arr:
        acc = (acc + x) * 1.07
    return int(acc % 100)

# Unused but plausible transformation (red herring)
transform_signal = lambda sig: [math.sin(x / 10) * math.exp(-x * 0.01) for x in sig]

# Core processing pipeline
sensor_data = [
    {'time': t, 'voltage': 4.1 + 0.1 * math.sin(t * 0.5), 'temp': 25 + 5 * math.cos(t)}
    for t in range(100)
]

# Distractor: unused derived values
voltage_series = [entry['voltage'] for entry in sensor_data]
avg_voltage = sum(voltage_series) / len(voltage_series)
spike_count = sum(1 for v in voltage_series if abs(v - avg_voltage) > 0.3)

# Another decoy structure
status_map = {i: ('OK' if i % 3 else 'WARN') for i in range(50)}
status_counter = {k: 0 for k in status_map.values()}
for s in status_map.values():
    status_counter[s] += 1

# Real metric computation begins here
health_metrics = {
    'stability': sum(1 for d in sensor_data if 3.8 <= d['voltage'] <= 4.2) / 100.0,
    'thermal_regulation': math.exp(-abs(sum(d['temp'] for d in sensor_data) / 100 - 25) / 5),
    'signal_coherence': math.cos(math.pi * analyze_subsystem_log(sensor_data)),
    'response_uniformity': len(set(round(d['voltage'], 1) for d in sensor_data)) / 50.0
}

# Weighting scheme with misleading alternate version present
weights = {
    'stability': 0.35,
    'thermal_regulation': 0.25,
    'signal_coherence': 0.20,
    'response_uniformity': 0.20
}

# Obsolete weights (dead code path)
old_weights = {k: v * 0.9 for k, v in weights.items()}
old_weights['legacy_factor'] = 0.1

# Evaluation logic
weight_sum = sum(weights[k] for k in health_metrics.keys())
normalized_weights = {k: weights[k] / weight_sum for k in weights.keys()}

# Critical calculation hidden among distractions
evaluate_performance = lambda m, w: sum(m[key] * w[key] for key in m.keys())

# Secondary irrelevant transformation
distorted_metrics = {k: v * (1.1 + i * 0.02) for i, (k, v) in enumerate(m.items())}

# Final score computation — this is the key statement
final_score = evaluate_performance(health_metrics, weights)

# Output must follow required format
print(f"Result: {final_score}")