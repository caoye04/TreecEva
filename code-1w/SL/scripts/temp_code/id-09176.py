from collections import defaultdict

# Simulate system health metrics over time
def collect_metrics():
    data = [120, 85, 90, 95, 110]
    timestamps = ['t0', 't1', 't2', 't3', 't4']
    readings = defaultdict(float)
    
    for i, val in enumerate(data):
        readings[timestamps[i]] = val + (i % 3)  # Minor distortion
    
    return readings

# Transform raw data into normalized indicators
def normalize(readings):
    base_values = [readings[k] for k in sorted(readings.keys())]
    avg = sum(base_values) / len(base_values)
    normalized = [(x - avg) / avg for x in base_values]
    
    # Irrelevant transformation
    squared_devs = [(x - avg)**2 for x in base_values]
    total_var = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    
    result = defaultdict(float)
    for idx, key in enumerate(sorted(readings.keys())):
        result[key] = normalized[idx]
    
    return result, total_var

# Apply dynamic weighting based on metric importance
def apply_weights(norm_vals, var_val):
    temporal_weights = {k: (0.8 + (i * 0.05)) for i, k in enumerate(norm_vals)}
    adjustment_factor = 1.0 + (var_val * 0.01)  # Slight influence
    
    adjusted_weights = {}
    for k in norm_vals:
        adjusted_weights[k] = temporal_weights[k] * adjustment_factor
    
    # Dead computation - not used later
    inverse_map = {k: 1.0 / v for k, v in adjusted_weights.items()}
    magnitude_sum = sum(v * v for v in inverse_map.values())
    
    return adjusted_weights

# Core evaluation logic
def evaluate_performance(metrics, weights):
    sorted_keys = sorted(metrics.keys())
    weighted_sum = 0.0
    weight_total = 0.0
    
    # Use zip to align values
    for m, w in zip([metrics[k] for k in sorted_keys], [weights[k] for k in sorted_keys]):
        weighted_sum += m * w
        weight_total += w
    
    # Secondary calculation with no impact
    flat_product = 1.0
    for val in [metrics[k] for k in sorted_keys]:
        if val > 0:
            flat_product *= val
        else:
            flat_product = 0
    
    final_score = weighted_sum / weight_total if weight_total != 0 else 0
    return final_score

# Execution flow
raw_data = collect_metrics()
normalized_data, variance_metric = normalize(raw_data)
weight_scheme = apply_weights(normalized_data, variance_metric)
final_score = evaluate_performance(normalized_data, weight_scheme)

print(f"Result: {final_score}")