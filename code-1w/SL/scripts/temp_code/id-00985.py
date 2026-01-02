def preprocess_metrics(raw):
    processed = {}
    scaling_factor = 1.75
    offset = 0.2
    for key, values in raw.items():
        avg = sum(values) / len(values)
        processed[key] = (avg * scaling_factor) + offset
    return processed

# Irrelevant helper function (dead code path)
def deprecated_normalizer(x):
    return [v / max(x) for v in x]

# Another decoy function with misleading intermediate calculations
def calculate_legacy_score(data):
    base = 0
    for d in data:
        if d > 0.5:
            base += d * 1.3
        else:
            base += d * 0.7
    return base * 0.9  # Never used

# Simulate complex system metrics from different subsystems
raw_system_data = {
    'throughput': [0.45, 0.67, 0.52, 0.71],
    'latency': [0.81, 0.63, 0.77, 0.69],
    'error_rate': [0.12, 0.09, 0.15, 0.11],
    'resource_usage': [0.55, 0.62, 0.58, 0.60]
}

# Normalize using min-max (distraction: unused normalization method)
min_max_normalized = {}
for k, v in raw_system_data.items():
    min_val, max_val = min(v), max(v)
    min_max_normalized[k] = [(x - min_val) / (max_val - min_val) for x in v]

# Primary preprocessing pipeline
primary_normalized = preprocess_metrics(raw_system_data)

# Misleading transformation chain
shadow_transform = {}
for idx, (k, v) in enumerate(primary_normalized.items()):
    shift = idx * 0.05
    shadow_transform[k] = v + shift  # Alters but won't be used

# Weight assignment with red herring weights
decoys = {'w_x': 0.1, 'w_y': 0.05, 'w_z': 0.15}
metric_weights = {'throughput': 0.3, 'latency': 0.25, 'error_rate': 0.35, 'resource_usage': 0.1}

# Secondary irrelevant mapping using zip and enumerate (distractor)
dummy_keys = ['a', 'b', 'c', 'd']
for i, (k, v) in enumerate(zip(dummy_keys, metric_weights.keys())):
    pass  # No-op loop to mislead control flow understanding

# Actual evaluation logic
def evaluate_performance(weights, data):
    total = 0.0
    components = []
    for metric, weight in weights.items():
        value = data[metric]
        contribution = weight * value
        components.append(contribution)
    
    # Complex conditional aggregation
    if len(components) > 3:
        adjusted = 0
        for c in components:
            if c > 0.15:
                adjusted += c * 1.1
            else:
                adjusted += c * 0.9
        total = adjusted
    else:
        total = sum(components)
    
    # Apply bonus only if all metrics exceed threshold (never triggered here)
    if all(v > 0.5 for v in data.values()):
        total += 0.2
    
    return total

# Critical execution point
final_score = evaluate_performance(metric_weights, primary_normalized)

# Additional noise: unused list comprehension with zip
_ = [x + y for x, y in zip(primary_normalized['throughput'], primary_normalized['latency'])]

# Output target result
print(f"Target result: {final_score}")