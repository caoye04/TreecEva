import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Misleading intermediate calculation with decoy logic
temp_offset = sum([i * 0.1 for i in range(10)]) - 4.5  # Evaluates to 0, red herring

# Simulated system metrics from a hypothetical performance monitor
metrics = {
    'latency': 120,      # ms
    'throughput': 850,    # requests/sec
    'error_rate': 0.012,  # fraction
    'memory_usage': 67.3, # percent
    'cpu_burst': 94.1     # percent peak
}

# Weight configuration for scoring (some weights are irrelevant)
weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'error_rate': 0.2,
    'memory_usage': 0.15,
    'disk_io': 0.1       # Irrelevant key (no corresponding metric)
}

# Decoy normalization function that's not used
def normalize_values(vals):
    max_val = max(vals.values())
    return {k: v / max_val for k, v in vals.items()}

# Hidden scaling factor based on conditional logic (critical!)
def get_adaptive_factor(x):
    if x < 100:
        return 1.1
    elif x > 100 and x < 150:
        return 0.95 + (x - 100) * 0.003
    else:
        return 1.1 - (x - 150) * 0.002

# Recursive smoothing function applied to throughput (used indirectly)
def smooth_value(n, depth=3):
    if depth == 0 or n <= 1:
        return n
    return 0.9 * smooth_value(n * 0.95, depth - 1) + 0.1 * n

# Simulated calibration curve for error correction (partially relevant)
calibration_data = [math.sin(i * 0.1) for i in range(10)]
offset_correction = sum(calibration_data) / len(calibration_data)  # ~0.41

# Auxiliary transformation table (distractor)
transform_map = {k: v * 0.01 for k, v in metrics.items()}

# Key function that computes final score
def evaluate_performance(met, wgt):
    base_score = 0.0
    relevance_adjustment = 0.0
    
    # Apply only matching keys between metrics and weights
    for key in wgt:
        if key in met:
            raw_contribution = met[key]
            
            # Special nonlinear adjustment for latency
            if key == 'latency':
                adjusted = 100 - min(raw_contribution, 200)  # inverted score
                adaptive_factor = get_adaptive_factor(raw_contribution)
                base_score += adjusted * wgt[key] * adaptive_factor
            # Throughput gets recursive smoothing
            elif key == 'throughput':
                smoothed = smooth_value(raw_contribution)
                base_score += (smoothed / 10) * wgt[key]  # scaled down
            # Error rate penalization
            elif key == 'error_rate':
                penalty = 50 * raw_contribution
                base_score += (100 - penalty) * wgt[key]
            # Memory usage has soft cap
            elif key == 'memory_usage':
                capped = min(raw_contribution, 80)
                base_score += (80 - capped) * wgt[key]
        else:
            # Dead branch with no effect
            relevance_adjustment += 0.01
    
    # Final nonlinear transformation using offset_correction (minor effect)
    final = base_score * (1 + offset_correction * 0.05)
    
    # Add hidden bonus if all metrics are above threshold (not triggered)
    if all(v > 50 for v in met.values() if isinstance(v, (int, float))):
        final += 10
    
    return round(final, 4)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")