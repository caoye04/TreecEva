import itertools

# Simulated system metrics from a distributed computing environment
task_completion_times = [2.3, 1.8, 3.1, 2.5, 2.9, 3.4, 1.7, 2.2]
node_efficiency = [0.88, 0.91, 0.76, 0.85, 0.92, 0.79, 0.83, 0.90]
data_throughput_mbps = [420, 510, 380, 470, 530, 390, 460, 505]
error_rates = [0.0021, 0.0018, 0.0032, 0.0025, 0.0015, 0.0029, 0.0020, 0.0017]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [True, False, True, True, False, False, True, False]
maintenance_windows = [(1, 4), (2, 6), (0, 3), (5, 7)]
redundant_checksums = [sum(task_completion_times[:i]) * 0.97 for i in range(1, len(task_completion_times))]

# Weighting schema for performance evaluation (key input)
weights = {
    'time_weight': 0.35,
    'efficiency_weight': 0.30,
    'throughput_weight': 0.25,
    'error_weight': 0.10
}

# Derived metrics (some relevant, some not)
normalized_times = [max(task_completion_times) - t for t in task_completion_times]  # inverted time
scaled_throughput = [tp / 1000 for tp in data_throughput_mbps]
inverted_errors = [0.01 - er for er in error_rates if er < 0.003]  # partial filter (misleading)

# Dead code path — never executed (red herring)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val for x in data]

# Unused transformation function (decoy)
transform_fn = lambda x, y: (x ** 0.5) * (y * 0.1) if x > y else (x * y) / 2

# Complex aggregation using itertools (valid usage)
rolling_pairs = list(itertools.pairwise(normalized_times))
avg_pair_delta = sum(abs(p[0] - p[1]) for p in rolling_pairs) / len(rolling_pairs) if rolling_pairs else 0.0

# Simulated historical baselines (irrelevant)
historical_avg_time = 2.7
historical_avg_efficiency = 0.84
projected_growth_rate = 1.023

# Core metric computation
metrics = {
    'avg_normalized_time': sum(normalized_times) / len(normalized_times),
    'mean_efficiency': sum(node_efficiency) / len(node_efficiency),
    'avg_throughput': sum(scaled_throughput) / len(scaled_throughput),
    'mean_inverted_error': sum(inverted_errors) / len(inverted_errors)  # uses filtered subset
}

# Spurious intermediate calculation (distraction)
temp_bias_adjustment = 0
for i, flag in enumerate(legacy_system_flags):
    if flag and node_efficiency[i] > 0.85:
        temp_bias_adjustment += 0.012 * task_completion_times[i]

# Another decoy: complex but unused structure
config_profile = {
    'version': '2.1',
    'active_modules': ['A', 'C', 'D'],
    'thresholds': {
        'latency': 3.0,
        'jitter': 0.4,
        'packet_loss': 0.002
    }
}

# Function to evaluate final performance score
def evaluate_performance(perf_metrics, weight_map):
    # Nested logic with conditional scaling
    time_score = perf_metrics['avg_normalized_time'] * weight_map['time_weight']
    eff_score = perf_metrics['mean_efficiency'] * weight_map['efficiency_weight']
    thr_score = perf_metrics['avg_throughput'] * weight_map['throughput_weight']
    
    # Conditional penalty adjustment (short-circuit logic)
    base_error_score = perf_metrics['mean_inverted_error'] * weight_map['error_weight']
    penalty_factor = 0.8 if avg_pair_delta > 0.4 else 1.0  # uses earlier computed delta
    
    # Red herring: unused branch
    if len(redundant_checksums) % 2 == 0:
        checksum_correction = sum(redundant_checksums) * 0.001
    else:
        checksum_correction = 0
    
    # Final weighted combination
    raw_score = time_score + eff_score + thr_score + base_error_score
    adjusted_score = raw_score * penalty_factor  # apply conditional adjustment
    
    # Additional irrelevant transformation
    for window in maintenance_windows:
        adjusted_score -= 0.001 * (window[1] - window[0])  # negligible effect
    
    return round(adjusted_score, 6)

# Execute main logic
current_system_load = sum(task_completion_times) / len(task_completion_times)
baseline_deviation = abs(current_system_load - historical_avg_time)

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Print result
print(f"Result: {final_score}")