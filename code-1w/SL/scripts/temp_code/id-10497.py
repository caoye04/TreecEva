import math

# Irrelevant helper function (dead code path)
def unused_network_util(data):
    return sum([x * 0.1 for x in data if x > 5])

# Misleading intermediate calculation with decoy result
temp_offset = 42
legacy_threshold = temp_offset * 2  # Distractor: looks important but unused

# Simulated system metrics with mixed data types and red herrings
metrics = {
    'latency': [120, 110, 115, 130],
    'throughput': [850, 870, 860, 880],
    'errors': [3, 1, 2, 0],
    'jitter': [5, 7, 6, 8],
    'redundant_flag': True,
    'placeholder': None
}

# Benchmark baseline data – some values are misleadingly close to answer
benchmark_data = {
    'base_latency': 100,
    'base_throughput': 800,
    'tolerance_window': 10,
    'decay_factor': 0.95,
    'noise_floor': [0.5, 0.3, 0.7]  # Unused in final logic
}

# Complex preprocessing with list comprehension and filtering
filtered_latency = [x for x in metrics['latency'] if x < 125]
adjusted_throughput = list(map(lambda x: x - benchmark_data['base_throughput'], metrics['throughput']))

# Irrelevant set operations as distraction
unique_error_states = set(metrics['errors'])
state_transitions = {0, 1, 2, 3} - unique_error_states  # Dead computation

# Hidden core logic embedded within multiple layers
scaling_factor = len(filtered_latency) / math.sqrt(len(adjusted_throughput))

# Decoy calculation using similar variables (misleads via proximity)
decoy_score = sum(metrics['jitter']) * benchmark_data['tolerance_window']  # Looks plausible

# Core performance evaluation with nested logic and conditional adjustments
def evaluate_performance(met, bench):
    base = bench['base_throughput'] / bench['base_latency']
    latency_ratio = sum([x / bench['base_latency'] for x in met['latency']]) / len(met['latency'])
    
    # Conditional weight adjustment based on error trend (real logic path)
    error_trend = all(e <= 1 for e in met['errors'][:-1])  # Only first three matter
    weight = 1.2 if error_trend else 0.8
    
    # Real throughput boost from consistency
    consistent = all(abs(adjusted_throughput[i] - adjusted_throughput[i+1]) < 20 
                   for i in range(len(adjusted_throughput)-1))
    boost = 1.15 if consistent else 1.0
    
    # Main formula hidden among distractions
    raw_score = base * latency_ratio * weight * boost
    
    # Final nonlinear transformation (key step)
    final_norm = math.log(raw_score * scaling_factor + 1)
    
    # This line is critical: modifies score based on legacy threshold (unused var mentioned earlier)
    # But actually uses different logic
    penalty = 0.9 if legacy_threshold > 80 else 1.0  # Uses distractor var but condition always true
    
    return int(final_norm * 100 * penalty)  # Deterministic integer output

# Trigger execution
temp_offset = None  # Overwrites earlier value to confuse tracing
final_score = evaluate_performance(metrics, benchmark_data)
print(f"Result: {final_score}")