from collections import defaultdict

# Simulate system metrics over time
time_logs = [102, 95, 110, 98, 105]
error_flags = [False, False, True, False, False]
response_times = [0.23, 0.45, 0.67, 0.33, 0.51]
throughput_data = [240, 190, 310, 260, 290]

# Irrelevant baseline for distraction
dummy_baseline = sum([t**2 for t in time_logs if t > 100]) // len(time_logs)

# Weight configuration (some are unused to add distraction)
weights = {
    'latency': 0.35,
    'throughput': 0.45,
    'errors': 0.20,
    'stability': 0.15  # Unused in final calculation
}

# Aggregate metrics with distractors
metrics = defaultdict(float)
metrics['latency'] = sum(response_times) / len(response_times)
metrics['throughput'] = sum(throughput_data) / len(throughput_data)

# Misleading transformation
transformed_errors = [1 if e else 0 for e in error_flags]
error_rate = sum(transformed_errors) / len(transformed_errors)

# Distractor: complex stability score (not used)
stability_score = 0
for i in range(1, len(time_logs)):
    diff = abs(time_logs[i] - time_logs[i-1])
    stability_score += diff * 0.1

# Actual logic uses only error count, not rate
metrics['errors'] = sum(transformed_errors)  # Only count matters

# Helper function with extra parameters for confusion
def adjust_for_bias(value, factor=1.0, mode='linear'):
    if mode == 'quadratic':
        return value * factor ** 2
    return value * factor

# Apply adjustment (only one actually affects result)
adjusted_latency = adjust_for_bias(metrics['latency'], weights['latency'], 'linear')
adjusted_throughput = adjust_for_bias(metrics['throughput'], weights['throughput'], 'quadratic')
adjusted_errors = adjust_for_bias(metrics['errors'], weights['errors'], 'linear')

# Final performance evaluation function
def evaluate_performance(m, w):
    # Some local distractions
    temp_debug = [v for v in m.values() if v > 0.5]
    offset_correction = len(temp_debug) * 0.01
    
    score = 0
    if 'latency' in m:
        score += w['latency'] * (1 / m['latency']) * 100
    if 'throughput' in m:
        score += w['throughput'] * m['throughput']
    if 'errors' in m:
        penalty = m['errors'] * 10
        score -= penalty
    
    # Add irrelevant bonus based on dummy condition (never triggers due to logic)
    if all(t < 100 for t in time_logs):  # This is false
        score += 20
    
    return int(score + offset_correction)

# Execute key statement
temp_cache = {k: v for k, v in metrics.items()}  # Dead code
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")