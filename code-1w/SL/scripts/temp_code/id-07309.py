def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for performance analysis (dead code path)."""
    return sum(1 for x in data if x > threshold) / len(data)

# Distractor: Unused but plausible-looking data structures
decoy_weights = [0.1, 0.2, 0.3, 0.4]
duplicate_metrics = {'latency': 0.92, 'throughput': 180, 'error_rate': 0.006, 'jitter': 0.03}

# Core problem setup: System health evaluation with weighted scoring
metrics = {
    'cpu_load': 0.68,
    'memory_usage': 0.81,
    'disk_io': 124,
    'network_latency': 45,
    'packet_loss': 0.004
}

weights = {
    'cpu_load': 0.25,
    'memory_usage': 0.25,
    'disk_io': 0.2,
    'network_latency': 0.15,
    'packet_loss': 0.15
}

# Irrelevant transformation chain (distractor)
processed = list(map(lambda x: x * 1.05, [metrics['cpu_load'], metrics['memory_usage']]))
adjusted = [min(x, 1.0) for x in processed]

# Fake normalization function that's never called
def normalize(val, min_val=0, max_val=1):
    return (val - min_val) / (max_val - min_val) if max_val != min_val else 0

# Real logic begins: Disk I/O needs scaling to match 0-1 range
scaled_disk_io = min(metrics['disk_io'] / 200, 1.0)

# Multiple conditional adjustments (some irrelevant)
temp_adjustments = []
for k, v in metrics.items():
    if k == 'cpu_load' and v < 0.7:
        temp_adjustments.append(0.05)
    elif k == 'memory_usage' and v > 0.8:
        temp_adjustments.append(-0.07)
    elif k == 'network_latency' and v < 50:
        temp_adjustments.append(0.03)

bias_correction = sum(temp_adjustments)  # Only this matters

# Decoy list comprehension with zip and enumerate (partial distractor)
sample_data = [3, 7, 2, 8]
indices_and_values = [(i, val) for i, val in enumerate(sample_data)]
paired = list(zip(indices_and_values, reversed(sample_data)))

# Set operations used idiomatically but mostly irrelevant
valid_keys = set(metrics.keys())
desired_keys = {'cpu_load', 'memory_usage', 'disk_io', 'network_latency', 'packet_loss'}
missing = desired_keys - valid_keys
extra = valid_keys - desired_keys

# Critical computation hidden among distractions
def evaluate_performance(met, wts):
    # Apply corrections only to relevant metrics
    base_scores = {
        'cpu_load': 1 - met['cpu_load'],
        'memory_usage': 1 - met['memory_usage'],
        'disk_io': 1 - scaled_disk_io,
        'network_latency': (100 - met['network_latency']) / 100,
        'packet_loss': 1 - met['packet_loss']
    }
    
    # Weighted sum with bias correction
    weighted_sum = 0.0
    for key in wts:
        if key in base_scores:
            weighted_sum += base_scores[key] * wts[key]
    
    # Apply accumulated bias correction
    result = weighted_sum + bias_correction
    
    # Final clamp to valid range
    return max(0.0, min(result, 1.0))

# Secondary distraction: Unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

sequence = [fibonacci(i) for i in range(5)]  # [0, 1, 1, 2, 3]

# Another red herring: Complex dictionary transformation
summary_stats = {
    f"stat_{i}": {"value": v, "flagged": v > 0.8} 
    for i, v in enumerate([metrics['cpu_load'], metrics['memory_usage'], scaled_disk_io])
}

# Actual answer computation buried in logic
final_score = evaluate_performance(metrics, weights)

# Output required format
print(f"Target result: {final_score}")