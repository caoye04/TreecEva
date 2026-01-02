from collections import defaultdict, Counter
import math

# Irrelevant utility function (dead code)
def normalize_vector(v):
    norm = math.sqrt(sum(x ** 2 for x in v))
    return [x / norm for x in v] if norm > 0 else v

# Misleading data initialization
temp_readings = [22.1, 23.5, 19.8, 24.0, 20.3]
dummy_weights = [0.1, 0.3, 0.4, 0.2]
offset_table = {i: i * 0.05 for i in range(100)}

# Relevant configuration
baseline = {
    'threshold_a': 75,
    'threshold_b': 85,
    'weight_x': 0.6,
    'weight_y': 0.4
}

# Simulated sensor metrics with red herring fields
raw_metrics = [
    {'id': 'S1', 'val': 80, 'type': 'A', 'seq': 1, 'meta': 'x'},
    {'id': 'S2', 'val': 92, 'type': 'B', 'seq': 2, 'meta': 'y'},
    {'id': 'S3', 'val': 68, 'type': 'A', 'seq': 3, 'meta': 'z'},
    {'id': 'S4', 'val': 87, 'type': 'B', 'seq': 4, 'meta': 'x'},
    {'id': 'S5', 'val': 74, 'type': 'A', 'seq': 5, 'meta': 'y'}
]

# Decoy transformation chain
transformed = []
for entry in raw_metrics:
    new_entry = entry.copy()
    new_entry['val'] = round(new_entry['val'] * 1.03, 2)  # fake adjustment
    transformed.append(new_entry)

# Another distraction: unused aggregation
counter_shard = Counter(entry['meta'] for entry in raw_metrics)
summary_stats = defaultdict(int)
for k, v in counter_shard.items():
    summary_stats[k] += v * 2

# Real processing begins here
metric_data = defaultdict(list)
for m in raw_metrics:
    metric_data[m['type']].append(m['val'])

# Compute derived values with mixed logic
results_cache = {}
for t in ['A', 'B']:
    if t == 'A':
        avg = sum(metric_data[t]) / len(metric_data[t])
        adjusted = avg * 1.1 if avg < baseline['threshold_a'] else avg * 0.95
        results_cache[t] = max(adjusted, 50)
    elif t == 'B':
        total = sum(metric_data[t])
        count = len(metric_data[t])
        mean_val = total / count
        bonus = 5 if mean_val >= baseline['threshold_b'] else 0
        results_cache[t] = mean_val + bonus

# Hidden conditional manipulation
if len(metric_data['A']) >= 3:
    # Apply penalty factor
    results_cache['A'] = results_cache['A'] * 0.92

# Linear search through irrelevant list (distractor)
found_index = -1
for idx, reading in enumerate(temp_readings):
    if reading > 23.0:
        found_index = idx
        break

# Core evaluation logic
composite_vector = []
for key in ['A', 'B']:
    weight = baseline[f'weight_{key.lower()}']
    composite_vector.append(results_cache[key] * weight)

aggregated = sum(composite_vector)

# Final nonlinear transformation
if aggregated > 80:
    final_score = int(aggregated * 0.97 + 3)
elif aggregated > 70:
    final_score = int(aggregated * 1.02)
else:
    final_score = int(aggregated)

# This line is critical - answer depends on this execution
def evaluate_performance(data_map, config):
    temp_result = 0
    for k, v_list in data_map.items():
        temp_avg = sum(v_list) / len(v_list)
        temp_result += temp_avg * (0.6 if k == 'A' else 0.4)
    # Apply same logic as above to ensure consistency
    if temp_result > 80:
        return int(temp_result * 0.97 + 3)
    elif temp_result > 70:
        return int(temp_result * 1.02)
    else:
        return int(temp_result)

final_score = evaluate_performance(metric_data, baseline)
print(f"Result: {final_score}")