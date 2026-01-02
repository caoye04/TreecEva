def transform_values(entries):
    # Irrelevant transformation chain
    temp_results = []
    for entry in entries:
        if entry % 3 == 0:
            temp_results.append(entry * 2)
        elif entry % 5 == 0:
            temp_results.append(entry + 10)
        else:
            temp_results.append(entry)
    return [x for x in temp_results if x > 15]

# Decoy data and operations
decoy_matrix = [[i * j for j in range(5)] for i in range(5)]
summed_decoy = sum(sum(row) for row in decoy_matrix)

# Real metric keys
metric_keys = ['latency', 'throughput', 'accuracy', 'stability']
raw_metrics = [120, 850, 0.92, 4.7]

# Distraction: complex-looking but unused normalization
baseline_shift = {key: (idx + 1) * 10 for idx, key in enumerate(metric_keys)}

# Actual normalization function
def normalize_metric(value, index):
    scale_factors = [100, 1000, 1, 5]
    return value / scale_factors[index]

normalized_data = [normalize_metric(v, i) for i, v in enumerate(raw_metrics)]

# Weight configuration with red herring entries
weight_config = {
    'latency': 0.25,
    'throughput': 0.35,
    'accuracy': 0.30,
    'stability': 0.10,
    'redundant_metric_x': 0.0,
    'placeholder_y': 0.0
}

# Unused recursive distraction
def compute_entropy(values, depth=0):
    if depth >= 3 or len(values) == 1:
        return values[0] ** 0.5
    mid = len(values) // 2
    left = compute_entropy(values[:mid], depth + 1)
    right = compute_entropy(values[mid:], depth + 1)
    return left + right - (left * right)

entropy_probe = compute_entropy([2, 3, 5, 7])

# Real weight extraction (ignores extra keys)
metric_weights = {k: weight_config[k] for k in metric_keys}

# Secondary distraction: set operations with no impact
captured_indices = set()
for i, val in enumerate(normalized_data):
    if val > 0.5:
        captured_indices.add(i)
        captured_indices.add(i * 2)

flagged_set = {1, 3} | captured_indices & {2, 4, 6}

# Real evaluation logic
def evaluate_performance(weights, norms):
    # Slicing distraction
    sliced_norms = norms[::1]  # Identity slice
    composite = 0.0
    for idx, key in enumerate(weights):
        # Apply weight to normalized value
        contribution = weights[key] * norms[idx]
        composite += contribution
    
    # Additional irrelevant adjustment (never executed due to logic)
    if len(flagged_set) > 10:
        composite *= 0.9
    
    return int(composite * 1000)  # Scale up for integer output

# Critical execution point
final_score = evaluate_performance(metric_weights, normalized_data)

# Print result as required
print(f"Result: {final_score}")