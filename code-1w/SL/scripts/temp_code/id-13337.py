from collections import defaultdict, Counter
import math

# Simulated sensor data from a distributed monitoring system
timestamped_readings = [
    (1623456780, 'node_A', 0.85), (1623456781, 'node_B', 0.72), (1623456782, 'node_A', 0.91),
    (1623456783, 'node_C', 0.65), (1623456784, 'node_B', 0.78), (1623456785, 'node_A', 0.88),
    (1623456786, 'node_D', 0.54), (1623456787, 'node_C', 0.69), (1623456788, 'node_B', 0.75),
    (1623456789, 'node_A', 0.83), (1623456790, 'node_D', 0.59), (1623456791, 'node_C', 0.70)
]

# Irrelevant auxiliary mapping (distractor)
node_codes = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
code_shift = sum(node_codes.values()) % 10  # Dead computation path

# Extract and aggregate readings by node
raw_aggregates = defaultdict(list)
for timestamp, node, value in timestamped_readings:
    raw_aggregates[node].append(value)

# Compute mean per node (relevant for later steps)
mean_per_node = {node: sum(vals)/len(vals) for node, vals in raw_aggregates.items()}

# Decoy transformation: frequency analysis of values (irrelevant)
frequency_map = Counter([round(v, 1) for v in sum(raw_aggregates.values(), [])])
high_freq_values = [val for val, cnt in frequency_map.items() if cnt > 1]

# Simulate historical baseline (mostly irrelevant except one parameter)
historical_stats = {
    'node_A': {'avg': 0.82, 'std': 0.05, 'peak': 0.95},
    'node_B': {'avg': 0.75, 'std': 0.03, 'peak': 0.80},
    'node_C': {'avg': 0.68, 'std': 0.04, 'peak': 0.72},
    'node_D': {'avg': 0.58, 'std': 0.06, 'peak': 0.65}
}

# Misleading normalization function (unused)
def normalize_score(x, base=0.7):
    return (x - base) / (1.0 - base)

# Auxiliary diagnostic flag (red herring)
anomaly_flag = any(mean_per_node[n] > historical_stats[n]['peak'] for n in mean_per_node)

# Primary processing function with nested logic
def analyze_trend(values, threshold):
    if len(values) < 3:
        return 0.0
    # Trend based on last three readings
    recent = values[-3:]
    increasing = all(recent[i] < recent[i+1] for i in range(len(recent)-1))
    decreasing = all(recent[i] > recent[i+1] for i in range(len(recent)-1))
    if increasing:
        return 0.4
    elif decreasing:
        return -0.4
    else:
        return 0.1

# Another decoy function
def calculate_entropy(vals):
    counts = Counter([math.floor(v * 10) for v in vals])
    total = len(vals)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Build log data structure (key input)
log_data = {}
for node_id, values in raw_aggregates.items():
    current_mean = mean_per_node[node_id]
    trend_score = analyze_trend(values, current_mean)
    stability_index = 1.0 - abs(current_mean - historical_stats[node_id]['avg'])
    # Combine into composite metric
    log_data[node_id] = {
        'metric': current_mean + trend_score * 0.5,
        'stability': stability_index,
        'size_hint': len(values)  # Unused field
    }

# System-wide threshold (critical parameter)
system_threshold = 0.85

# Secondary irrelevant list comprehension
expanded_diagnostics = [
    f"{k}:{v['metric']:.2f}" for k, v in log_data.items() \
    if v['metric'] > system_threshold - 0.1
]

# Core decision logic buried in distraction
def process_metrics(data, threshold):
    scores = []
    for node, metrics in data.items():
        base = metrics['metric']
        adj = base * metrics['stability']
        if adj >= threshold:
            penalty = 0.05 * math.sin(len(metrics['metric'].as_integer_ratio()[0])) if hasattr(metrics['metric'], 'as_integer_ratio') else 0
            scores.append(adj - penalty)
        else:
            bonus = 0.02 * math.cos(list(raw_aggregates[node])[-1] * 10)
            scores.append(adj + bonus)
    # Final aggregation
    raw_final = sum(scores)
    # Apply scaling based on number of high-frequency values (irrelevant but looks important)
    freq_factor = len(high_freq_values) * 0.05 if high_freq_values else 0
    adjusted_final = raw_final - freq_factor
    return round(adjusted_final, 6)

# Execute key statement
final_diagnostic = process_metrics(log_data, system_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")