from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 78, 'temp': 42, 'uptime': 1500},
    {'node': 'B', 'load': 65, 'temp': 38, 'uptime': 1800},
    {'node': 'C', 'load': 90, 'temp': 45, 'uptime': 1200},
    {'node': 'A', 'load': 82, 'temp': 43, 'uptime': 1550},
    {'node': 'B', 'load': 70, 'temp': 39, 'uptime': 1850},
    {'node': 'D', 'load': 55, 'temp': 35, 'uptime': 2000}
]

# Irrelevant statistical tracking (distractor)
stats_tracker = defaultdict(lambda: {'count': 0, 'total_temp': 0})
for entry in telemetry_stream:
    node = entry['node']
    stats_tracker[node]['count'] += 1
    stats_tracker[node]['total_temp'] += entry['temp']

avg_temps = {k: v['total_temp'] / v['count'] for k, v in stats_tracker.items()}

# Efficiency mapping with arbitrary heuristics (some relevant, some not)
efficiency_map = {}
for entry in telemetry_stream:
    load = entry['load']
    # Complex but partially irrelevant formula
    efficiency = (100 - load) * (1 + math.sin(math.radians(entry['temp'])))
    efficiency_map[entry['node']] = efficiency

# Dead code path - never used (red herring)
def deprecated_scaling(node):
    base = 1.0
    if node == 'A':
        base *= 0.95
    elif node == 'B':
        base *= 0.97
    return base * 100

# Misleading intermediate calculation (unused)
temp_bias_correction = sum([math.log(40 + e['temp']) for e in telemetry_stream]) / len(telemetry_stream)

# Core reliability model (relevant)
reliability_scores = {}
for entry in telemetry_stream:
    score = (entry['uptime'] / 100) * (1 - entry['load'] / 150)
    if entry['node'] not in reliability_scores or score > reliability_scores[entry['node']]:
        reliability_scores[entry['node']] = score

# Simulated efficiency logs over time (relevant)
efficiency_logs = [
    [0.85, 0.87, 0.84],
    [0.90, 0.88, 0.89],
    [0.82, 0.83, 0.80],
    [0.91, 0.92, 0.90]
]

# Weighting mechanism using collections.Counter (relevant)
node_frequency = Counter([e['node'] for e in telemetry_stream])

# Composite weight calculation with distractors
raw_weights = {}
decoy_offset = 0.1 * len(stats_tracker)  # Unused distraction
for node, count in node_frequency.items():
    raw_weights[node] = count * reliability_scores.get(node, 0.1)

total_weight = sum(raw_weights.values())
reliability_weights = {k: v / total_weight for k, v in raw_weights.items()}

# Fake normalization chain (irrelevant)
fake_normalized = {}
for k, v in efficiency_map.items():
    fake_normalized[k] = v / (v + 0.5) if v > 0 else 0.1

# Real aggregation function with nested logic
def calculate_aggregate(weights, logs):
    flat_logs = [item for sublist in logs for item in sublist]
    log_average = sum(flat_logs) / len(flat_logs)
    
    # Secondary adjustment based on weight distribution entropy (partially relevant)
    entropy = 0
    for w in weights.values():
        if w > 0:
            entropy -= w * math.log(w)
    
    # Tertiary boost from longest uptime (distractor: uses min instead of max by mistake)
    fake_uptime_boost = min([e['uptime'] for e in telemetry_stream]) / 10000
    
    # Actual key computation
    base_performance = log_average * 100
    stability_factor = entropy * 15
    
    # Final score formula (only this line matters)
    final_component = base_performance + stability_factor
    
    # Dead assignment (misleading)
    final_component *= (1 + fake_uptime_boost)  
    
    return int(round(final_component))

# Trigger execution
current_node = 'A'
baseline_shift = 0
for i, log in enumerate(efficiency_logs):
    if i % 2 == 0:
        baseline_shift += sum(log) / len(log)

# Critical statement
final_score = calculate_aggregate(reliability_weights, efficiency_logs)

# Output result
print(f"Result: {final_score}")