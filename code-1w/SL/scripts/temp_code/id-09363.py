def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]

# Irrelevant constants (distractors)
MAX_CAPACITY = 1000
BASELINE_OFFSET = 42
DEFAULT_TIMEOUT = 300

# Real and fake metrics
metrics = [
    ('accuracy', 0.92),
    ('latency', 0.15),
    ('throughput', 850),
    ('energy', 23.7),
    ('reliability', 0.98)
]

weights = {
    'accuracy': 0.3,
    'latency': 0.1,  # Will be transformed
    'throughput': 0.25,
    'energy': 0.15,
    'reliability': 0.2
}

# Fake metric data to mislead
auxiliary_metrics = [
    ('cache_hits', 1200),
    ('bandwidth', 89.2),
    ('temperature', 67)
]

# Unused transformation (dead code path)
def normalize(value, min_val=0, max_val=1):
    return (value - min_val) / (max_val - min_val)

# Red herring list comprehension with no effect
_ = [pow(x[1] * 2, 0.5) for x in auxiliary_metrics if isinstance(x[1], (int, float))]

# Misleading intermediate calculation
shadow_latency = 1 / metrics[1][1]  # 1/0.15 ≈ 6.666, but not used directly

# Latency needs inverse weighting: lower latency is better
adjusted_metrics = []
for name, value in metrics:
    if name == 'latency':
        value = 1 / value  # Now higher = better
    adjusted_metrics.append((name, value))

# Another irrelevant computation (bit manipulation decoy)
encoded_flags = 0
for i in range(len(auxiliary_metrics)):
    encoded_flags |= (1 << i)

temp_result = encoded_flags ^ 0b11111111  # Distraction

# Use enumerate and zip (required Python features)
enumerated_weights = list(enumerate(weights.items()))

# Mapping names to adjusted values via lambda and zip
metric_dict = dict(zip([m[0] for m in adjusted_metrics], [m[1] for m in adjusted_metrics]))

scaling_factor = 10 if metric_dict['accuracy'] > 0.9 else 5

# Core logic wrapped in a lambda for abstraction
transform = lambda x: x * scaling_factor if isinstance(x, (int, float)) else x

# Apply transformation only to relevant fields
scaled_metrics = {}
for idx, (name, weight) in weights.items():
    raw_value = metric_dict[name]
    scaled_value = transform(raw_value)
    scaled_metrics[name] = scaled_value * weight  # Weighted contribution

# Additional distraction: unused loop over enumerate and zip
aggregated = 0
for i, (aux_name, aux_val) in enumerate(zip(['a','b','c'], [1,2,3])):
    aggregated += i * aux_val

# Actual final score computation
weighted_sum = sum(scaled_metrics.values())
penalty = 0
if metric_dict['energy'] > 20:
    penalty = 15  # Energy inefficiency penalty

final_score = weighted_sum - penalty

# Print result as required
print(f"Result: {final_score}")