from collections import defaultdict, Counter
import math

# Simulated system telemetry data (distraction)
telemetry_logs = [
    {'timestamp': 1001, 'load': 0.45, 'errors': 2},
    {'timestamp': 1002, 'load': 0.67, 'errors': 1},
    {'timestamp': 1003, 'load': 0.33, 'errors': 0}
]

def analyze_telemetry(logs):
    # Irrelevant analysis function (dead code path)
    error_count = sum(entry['errors'] for entry in logs)
    avg_load = sum(entry['load'] for entry in logs) / len(logs)
    return {'average_load': round(avg_load, 2), 'total_errors': error_count}

telemetry_analysis = analyze_telemetry(telemetry_logs)  # Unused result

# Core performance evaluation logic
base_threshold = 75
adjustment_factor = 1.8

metric_data = [
    (88, 'response_time', True),
    (72, 'throughput', False),
    (91, 'availability', True),
    (65, 'scalability', False),
    (79, 'reliability', True)
]

# Misleading intermediate transformation (partial distractor)
legacy_weights = {k: v * 0.95 for v in range(1, len(metric_data)+1)}
weight_map = defaultdict(lambda: 0.5)
for i, (_, name, _) in enumerate(metric_data):
    weight_map[name] = round(1.0 + (i * 0.1), 1)

# Auxiliary function that seems important but isn't used in final calculation
def calculate_legacy_score(data, weights):
    total = 0.0
    for i, (value, _, _) in enumerate(data):
        total += value * weights[i+1]
    return total / len(data)

legacy_score = calculate_legacy_score(metric_data, legacy_weights)  # Red herring

# Real processing begins here — nested logic with conditional expressions
status_flags = [flag for _, _, flag in metric_data]
active_count = sum(1 for flag in status_flags if flag)

# Bit manipulation for mode encoding (irrelevant to final score but looks critical)
current_mode = 0b101
maintenance_flag = current_mode & 0b001
operational_mode = current_mode >> 1  # Equals 2

# Conditional branches with decoy logic
if operational_mode == 2:
    adjustment_factor = adjustment_factor ** 2  # Becomes ~3.24
else:
    adjustment_factor = 1.0

# Simulated historical trends (unused)
historical_trend = [
    76.3, 74.1, 77.8, base_threshold, 75.5
]
drift_rate = sum(historical_trend[i+1] - historical_trend[i] for i in range(len(historical_trend)-1)) / 4

# Main scoring logic buried among distractions
def evaluate_metric(value, name, enabled, threshold, factor):
    if not enabled:
        return 0
    # Only enabled metrics contribute
    base_bonus = 10 if value >= threshold else -5
    precision_component = round(math.log(value) * 0.7, 2)
    return value + base_bonus + precision_component

def evaluate_performance(metrics, thresh):
    scores = []
    for val, nm, en in metrics:
        if en:
            score = evaluate_metric(val, nm, en, thresh, adjustment_factor)
            scores.append(score)
    
    # Aggregation using list comprehension and Counter (real usage)
    normalized = [round(s - min(scores), 1) for s in scores]
    freq = Counter(normalized)
    bonus = sum(k * v for k, v in freq.items() if k > 5.0)  # Extra incentive for high spread
    
    raw_mean = sum(scores) / len(scores)
    return int(raw_mean + bonus)  # Final deterministic integer

# Critical execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Output required format
print(f"Result: {final_score}")