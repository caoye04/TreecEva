def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function analyzing efficiency (dead code path)."""
    count = 0
    for val in data:
        if val > threshold * max(data):
            count += 1
    return count

# Unused data structures as distractors
temp_readings = [0.4, 0.6, 0.8, 0.9, 0.3]
pressure_levels = {"p1": 0.2, "p2": 0.5, "p3": 0.7}
status_flags = {1: 'active', 2: 'standby', 3: 'idle'}

# Relevant input data for evaluation
metrics = {
    'accuracy': 0.92,
    'latency': 0.15,
    'throughput': 850,
    'energy': 45.3,
    'consistency': 0.88
}

weights = {
    'accuracy': 0.3,
    'latency': 0.1,
    'throughput': 0.25,
    'energy': 0.15,
    'consistency': 0.2
}

# Misleading intermediate calculations
baseline_score = sum([metrics[k] * 0.2 for k in metrics])  # Equal-weight red herring
adjusted_latency = (1 - metrics['latency']) * 100  # Distraction transformation

# Complex normalization using lambda and dictionary operations
normalize = lambda x, low, high: (x - low) / (high - low) if high != low else 0

# Simulated reference bounds (some irrelevant)
ref_bounds = {
    'accuracy': (0.6, 1.0),
    'latency': (0.05, 0.3),
    'throughput': (500, 1000),
    'energy': (20, 60),
    'consistency': (0.7, 1.0)
}

# Distractor: unused normalized values
norm_metrics = {
    key: normalize(metrics[key], ref_bounds[key][0], ref_bounds[key][1]) 
    for key in metrics
}

# Fake aggregation with set operations (irrelevant)
metric_keys = set(metrics.keys())
weight_keys = set(weights.keys())
symmetric_diff = metric_keys.symmetric_difference(weight_keys)  # Always empty, but looks important

# Core logic hidden among distractions
scaling_factor = 1000 // 10  # Integer division red herring: evaluates to 100

# Real computation buried in complexity
def compute_weighted_sum(data_dict, weight_dict):
    total = 0.0
    for key in data_dict:
        if key in weight_dict:
            # Apply non-linear penalty for latency
            value = data_dict[key]
            if key == 'latency':
                value = 1 - value  # invert since lower is better
            total += value * weight_dict[key]
    return total * scaling_factor  # Scale up result

# Secondary distraction: recursive fake analysis
def predict_trend(values, depth=3):
    if depth <= 0 or len(values) == 0:
        return 0
    mid = len(values) // 2
    return values[mid] + predict_trend(values[:mid], depth-1)

# Another decoy function using bit operations (unused)
def encode_metric(value):
    raw = int(value * 100)
    return (raw << 2) ^ 0xAA  # Bit manipulation distraction

# Main evaluation logic disguised as one among many
intermediate_result = compute_weighted_sum(metrics, weights)

# Final adjustment using rounding and comparison logic
if intermediate_result > 85:
    adjustment = round(intermediate_result * 0.05)
else:
    adjustment = 0

final_score = int(intermediate_result - adjustment)

# Print required output
print(f"Result: {final_score}")