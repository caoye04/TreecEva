def analyze_component(reading, threshold=0.7):
    """Irrelevant diagnostic function (dead code path)"""
    return reading > threshold and reading < 0.9

# Irrelevant sensor data simulation
temp_readings = [0.65, 0.72, 0.83, 0.54]
diagnostic_flags = [analyze_component(x) for x in temp_readings]

# Real data: system performance metrics across 4 dimensions
metrics = [0.88, 0.76, 0.91, 0.67]  # accuracy, efficiency, stability, responsiveness

# Distractor: alternate weight sets (only one is used)
weights_v1 = [0.2, 0.3, 0.4, 0.1]  # incorrect schema
weights_v2 = [0.3, 0.2, 0.3, 0.2]  # correct weights
weights_v3 = [0.25, 0.25, 0.25, 0.25] # uniform fallback

# Misleading normalization (unused)
def normalize(lst):
    s = sum(lst)
    return [x/s for x in lst]

unused_normalized_metrics = normalize(metrics)

# Bit manipulation red herring
bitmask = 0b1010
shifted = bitmask << 2
masked_result = shifted & 0b111100

# Decoy transformation chain
transform_chain = lambda x: x ** 2 if x > 0.8 else x + 0.1
transformed = list(map(transform_chain, metrics))

# Irrelevant string processing (simulating config parsing)
config_line = "PERF_WEIGHTS=0.3|0.2|0.3|0.2"
weight_strings = config_line.split('=')[1].split('|')
parsed_weights = [float(w) for w in weight_strings]

# Critical: validate parsed weights match expected schema
def validate_schema(weights):
    return abs(sum(weights) - 1.0) < 1e-6

is_valid = validate_schema(parsed_weights)

# Unused recursive structure (decoy)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

dummy_factorial = factorial(5)

# Real logic begins here: cross-reference with enumeration and zip
aggregation_pairs = []
for i, (metric, weight) in enumerate(zip(metrics, weights_v2)):
    # Apply position-based adjustment using enumerated index
    adjusted_metric = metric * (1 + 0.05 * ((i % 2) - 0.5))
    aggregation_pairs.append((adjusted_metric, weight))

# Set operation to filter high-weight components (irrelevant filtering)
high_weight_indices = {i for i, w in enumerate(weights_v2) if w >= 0.25}
efficiency_critical = {1, 2}
overlap_set = high_weight_indices & efficiency_critical  # {1,2} ∩ {0,2} = {2}

# Actual weighted sum calculation (core logic)
weighted_sum = 0.0
for adj_val, weight in aggregation_pairs:
    weighted_sum += adj_val * weight

# Secondary adjustment based on overlap (distractor with minimal effect)
bias_correction = 0.01 * len(overlap_set)
adjusted_sum = weighted_sum + bias_correction

# Final nonlinear scaling (key step)
scaled_performance = adjusted_sum * (1.0 + 0.1 * (metrics[0] - 0.8))

# Final scoring with clamping
final_score = max(0.0, min(100.0, scaled_performance * 100))

# Output target result
print(f"Target result: {final_score}")