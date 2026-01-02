def analyze_system_load(loads):
    threshold = 75
    high_loads = list(filter(lambda x: x > threshold, loads))
    return len(high_loads) * 1.5


def calculate_efficiency(ratios):
    adjusted = [r * 0.8 + 10 for r in ratios if r < 50]
    return sum(adjusted) if adjusted else 0

# Simulated telemetry data from distributed nodes
node_metrics = {
    'cpu': [65, 80, 70, 90, 45],
    'memory': [70, 85, 60, 95, 40],
    'disk_io': [50, 60, 55, 70, 50],
    'network': [80, 75, 85, 90, 70]
}

weights = {
    'cpu': 0.3,
    'memory': 0.25,
    'disk_io': 0.15,
    'network': 0.3
}

# Auxiliary computations (some irrelevant)
baseline_shift = sum(node_metrics['cpu']) / len(node_metrics['cpu']) * 0.05
offset_correction = baseline_shift * 0.1  # Unused distraction

# Derived metrics with mixed relevance
high_cpu_events = analyze_system_load(node_metrics['cpu'])
memory_efficiency = calculate_efficiency(node_metrics['memory'])

# Secondary processing chain
aggregated = {}
for k, v in node_metrics.items():
    avg = sum(v) / len(v)
    peak_ratio = max(v) / 100.0
    score_component = avg * 0.6 + peak_ratio * 20
    aggregated[k] = round(score_component, 2)

# Irrelevant transformation (dead path)
if offset_correction > 1:
    transformed = {key: val * 1.1 for key, val in aggregated.items()}
else:
    dummy_flag = True  # Misleading control flow

# Core evaluation logic
metrics = []
for key in ['cpu', 'memory', 'disk_io', 'network']:
    base_val = aggregated[key]
    if key == 'cpu':
        base_val += high_cpu_events * 0.1
    elif key == 'memory':
        base_val += memory_efficiency * 0.01
    metrics.append(base_val)

# Final weighted scoring with lambda-based combination
evaluate_performance = lambda m, w: sum(m[i] * list(w.values())[i] for i in range(len(m)))

final_score = evaluate_performance(metrics, weights)

# Extraneous post-calculation
buffer_zone = final_score * 0.02  # Distractor variable
sanity_check = final_score > 50 and high_cpu_events > 3  # Red herring boolean

Result: {final_score}