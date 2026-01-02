import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_stream(raw_samples):
    normalized = [x * 0.01 for x in raw_samples if x > -50]
    inverted = [abs(n) for n in normalized][::-1]
    return [n for n in inverted if n < 1.0]

# Irrelevant transformation chain (dead path)
def legacy_filter(sequence):
    temp = [s ** 2 for s in sequence if s > 0.5]
    return [t - 0.1 for t in temp if t > 0.3]

# Core pattern analyzer (actually used)
def analyze_pattern(seq, config):
    base_score = 0
    for i, val in enumerate(seq):
        if i % 3 == 0 and val > config['alpha']:
            base_score += val * 2
        elif i % 3 == 1 and config['beta'] < val < config['gamma']:
            base_score += val * 1.5
    return int(base_score * 100)

# Unused diagnostic function (decoy)
def compute_robustness_index(data):
    if not data:
        return -1
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance * 1000

# Data transformation pipeline
raw_input = list(range(85, 135)) + [45, 30, 70, 120]
filtered_data = preprocess_sensor_stream(raw_input)

# Transform via cycling pattern (using itertools)
expanded = list(itertools.chain.from_iterable(
    itertools.repeat(x, 2) for x in filtered_data[::3]
))

# Multiple irrelevant variables (distractors)
scaling_factor = 1.07
temporal_weights = [0.1 * j for j in range(1, len(expanded) + 1)]
weighted_sum = sum(a * b for a, b in zip(expanded, temporal_weights))
shadow_copy = expanded.copy()
shadow_copy.append(0.99)

# Key transformation: non-trivial mapping
transformed_data = []
for idx, item in enumerate(expanded):
    if idx % 2 == 0:
        transformed_data.append(item + 0.05)
    else:
        transformed_data.append(item - 0.03)

# Threshold configuration (mixed usage)
threshold_map = {
    'alpha': 0.45,
    'beta': 0.33,
    'gamma': 0.88,
    'delta': 0.12  # unused field
}

# Unused conditional branch (misleading control flow)
if len(transformed_data) > 100:
    final_diagnostic = -999
elif any(d > 0.9 for d in transformed_data):
    final_diagnostic = 0
else:
    # This is the actual execution path
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")