from collections import defaultdict, Counter
import math

# Simulated system telemetry data (irrelevant to final result)
telemetry_log = [
    'ERR: timeout', 'OK: sensor_7', 'WARN: fluctuation',
    'OK: sensor_3', 'ERR: timeout', 'OK: sensor_7'
]

telemetry_counts = Counter(telemetry_log)
dropped_packets = sum(v for k, v in telemetry_counts.items() if 'ERR' in k)

# Irrelevant network buffer simulation
buffer_states = [128, 256, 512, 1024]
current_buffer = buffer_states[2] // 4  # Distractor

# Core algorithm inputs
baseline = {'latency': 45, 'throughput': 200, 'error_rate': 0.02}
metrics = {
    'latency': 36,
    'throughput': 240,
    'error_rate': 0.015,
    'retries': 3,
    'jitter': 4.2
}

# Decoy function - looks important but unused
def calculate_health_index(data):
    score = 0
    for val in data.values():
        if isinstance(val, (int, float)):
            score += math.sqrt(abs(val)) * 0.1
    return round(score, 2)

# Unused recursive helper (red herring)
def binary_weight(depth, max_depth=5):
    if depth >= max_depth:
        return 1
    return 2 * binary_weight(depth + 1, max_depth)

# Misleading intermediate transformation
temp_normalized = {}
for key in baseline.keys():
    if key == 'latency':
        temp_normalized[key] = metrics[key] < baseline[key]
    elif key == 'throughput':
        temp_normalized[key] = metrics[key] > baseline[key]
    else:
        temp_normalized[key] = abs(metrics[key] - baseline[key]) < baseline[key] * 0.1

# Distractor: complex string analysis on irrelevant tags
tags = "perf, latency_opt, v2.1, experimental"
tag_list = tags.split(', ')
version_flag = any('v2' in t for t in tag_list)

flagged_components = []
for item in tag_list:
    if 'experimental' in item or 'beta' in item:
        flagged_components.append(item)

# Real logic begins here — subtle and buried among noise
def assess_metric_change(current, target, invert=False):
    ratio = current / target
    if invert:  # latency and error_rate are inverted metrics
        return max(0, (1 - (ratio - 1)) * 100)
    else:
        return (ratio - 1) * 100

# Secondary distractor: unused data structure manipulation
history = [(38, 210), (42, 195), (37, 230)]
history_avg_latency = sum(x[0] for x in history) / len(history)
history_trend = 'improving' if history[-1][0] < history[0][0] else 'worsening'

# Real evaluation logic buried deep
weighted_adjustment = defaultdict(float)

# Only these three keys matter; others ignored
for param in ['latency', 'throughput', 'error_rate']:
    raw_change = assess_metric_change(
        metrics[param], 
        baseline[param], 
        invert=(param in ['latency', 'error_rate'])
    )
    if param == 'throughput':
        weight = 0.4
    elif param == 'latency':
        weight = 0.35
    else:  # error_rate
        weight = 0.25
    weighted_adjustment[param] = raw_change * weight

# Hidden correction factor based on string length (non-obvious link)
correction_code = "Q4X9"  # Version marker
version_bonus = len(correction_code) if version_flag else 0  # Always 0 — red herring

# Actual integration step
base_performance_score = 100
aggregate_delta = sum(weighted_adjustment.values())

# Final computation — only this matters
final_score = base_performance_score + aggregate_delta

# Print required output
print(f"Result: {final_score}")