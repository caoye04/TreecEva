def analyze_system_load(loads, threshold=75):
    high_load_periods = [i for i, load in enumerate(loads) if load > threshold]
    return len(high_load_periods), sum(loads) / len(loads)

# Simulated telemetry data (irrelevant but plausible)
telemetry_logs = [
    {'timestamp': 1000, 'cpu': 68, 'mem': 45},
    {'timestamp': 1001, 'cpu': 72, 'mem': 50},
    {'timestamp': 1002, 'cpu': 81, 'mem': 61},
    {'timestamp': 1003, 'cpu': 55, 'mem': 40}
]

# Extract CPU loads for analysis
cpu_loads = [entry['cpu'] for entry in telemetry_logs]

# Analyze system load (distractor computation)
high_count, avg_load = analyze_system_load(cpu_loads)

# Benchmark metrics from multiple subsystems (relevant data)
metrics = {
    'latency': 42,      # ms
    'throughput': 85,   # ops/sec
    'consistency': 78,  # score
    'scalability': 91   # score
}

# Legacy performance counters (red herring)
legacy_metrics = {
    'bandwidth': 120,
    'jitter': 8,
    'reliability': 95
}

# Weight distribution for current evaluation framework (relevant)
benchmark_weights = {
    'latency': 0.2,
    'throughput': 0.3,
    'consistency': 0.25,
    'scalability': 0.25
}

# Historical baselines (unused, misleading)
historical_avg = {
    'latency': 51,
    'throughput': 73,
    'consistency': 70,
    'scalability': 82
}

# Auxiliary function to compute normalized delta (not used directly)
def calculate_improvement(current, baseline):
    improvements = {}
    for key in current:
        if key in baseline:
            improvements[key] = (current[key] - baseline[key]) / baseline[key] * 100
    return improvements

# Complex preprocessing with slicing and filtering (partial distractor)
ordered_keys = sorted(metrics.keys())
sliced_subset = ordered_keys[1:3]  # throughputs and consistency only

# Set operations to identify overlap (plausible but irrelevant)
required_fields = {'latency', 'throughput', 'consistency', 'scalability'}
available_fields = set(metrics.keys())
missing_fields = required_fields - available_fields

# Core evaluation logic (critical path)
def evaluate_performance(met, weights):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Apply weights using sorted keys to ensure deterministic order
    for key in sorted(met.keys()):
        if key in weights:
            weighted_sum += met[key] * weights[key]
            total_weight += weights[key]
    
    # Normalize by total weight (in case of incomplete weights)
    if total_weight > 0:
        performance_index = weighted_sum / total_weight
    else:
        performance_index = 0
    
    # Secondary adjustment based on system stability (fake dependency)
    stability_factor = 1.0
    if 'latency' in met and met['latency'] < 50:
        stability_factor = 1.05  # slight boost for low latency
    
    adjusted_score = performance_index * stability_factor
    
    # Tertiary transformation via bit manipulation (obscure but harmless)
    raw_bits = int(adjusted_score * 100)
    scrambled = (raw_bits ^ 0xFF) & 0xFFFF  # invert lower byte
    descrambled = (scrambled ^ 0xFF) & 0xFFFF
    final_float = descrambled / 100.0
    
    return final_float

# Unused recursive helper (dead code path)
def recursive_aggregate(data, index=0):
    if index >= len(data):
        return 0
    return data[index] + 0.9 * recursive_aggregate(data, index + 1)

# Compute final score (target execution point)
final_score = evaluate_performance(metrics, benchmark_weights)

# Print result as required
print(f"Result: {final_score}")