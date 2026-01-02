def analyze_system_load(usage_data):
    # Irrelevant transformation: normalize data (not used in final result)
    normalized = [u / max(usage_data) for u in usage_data]
    threshold = 0.75
    high_load_count = sum(1 for x in normalized if x > threshold)
    return high_load_count * 2  # Distractor computation

# Unused function – dead code path
compute_efficiency = lambda ops, time: ops / time if time else 0

# Simulated sensor readings – irrelevant to final answer
sensor_logs = [127, 89, 134, 72, 95, 110]
sensor_avg = sum(sensor_logs) / len(sensor_logs)
sensor_status = 'stable' if sensor_avg > 90 else 'unstable'

# Core data structures
metrics = {
    'latency': 45,      # ms
    'throughput': 88,   # req/s
    'error_rate': 2,    # %
    'memory': 67        # % utilization
}

weights = {
    'latency': 0.3,
    'throughput': 0.4,
    'error_rate': -0.2,  # Penalty weight
    'memory': -0.1
}

# Secondary metric – misleading intermediate score
raw_sum = sum(metrics.values())
adjustment_factor = 0.9 + (raw_sum % 10) * 0.01
adjusted_sum = raw_sum * adjustment_factor

# Complex conditional expression – partially relevant
penalty_trigger = metrics['error_rate'] > 1.5 and metrics['memory'] > 60
bonus_applied = True if metrics['throughput'] > 85 else False

# Bit manipulation red herring
encoded_diagnostic = (metrics['latency'] << 2) ^ 0xAA

# Real evaluation logic buried among distractions
def evaluate_performance(met, wgt):
    base_score = 0
    for key in met:
        if key in wgt:
            base_score += met[key] * wgt[key]
    
    # Apply bonus only if conditions are met (bonus_applied is computed above)
    if bonus_applied:
        base_score += 5
    
    # Hidden correction: error_rate below 2.5 gives additional boost
    if met['error_rate'] < 2.5:
        base_score += 3.7  # Critical but non-obvious adjustment
    
    # Distractor: this looks like a clamp but doesn't affect result due to current values
    final = max(0, min(100, base_score))
    return final

# Additional noise: sorting unrelated list
diagnostic_codes = [302, 107, 405, 203]
diagnostic_codes.sort(reverse=True)

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Another decoy function using lambda
assess_health = lambda x: 'good' if x > 70 else 'fair' if x > 50 else 'poor'
health_label = assess_health(final_score)

# Print required output
print(f"Result: {final_score}")