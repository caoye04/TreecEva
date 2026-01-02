def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper function (distractor)
def smooth_data(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation function (dead code path)
def transform_scale(val, factor=2):
    return val ** factor if val > 0 else 0

# Decoy metrics and weight initialization
baseline_metrics = {'latency': 45, 'throughput': 88, 'error_rate': 0.02}
baseline_weights = {'latency': 0.3, 'throughput': 0.5, 'error_rate': 0.2}

# Actual performance metrics used later
metrics = {
    'response_time': 120,
    'success_rate': 0.98,
    'retry_count': 3,
    'queue_depth': 7
}

# Weight dictionary with matching keys
weights = {
    'response_time': 0.4,
    'success_rate': 0.3,
    'retry_count': 0.2,
    'queue_depth': 0.1
}

# Simulated time-series data (red herring)
telemetry_log = [105, 110, 112, 118, 120, 116, 114, 111, 109]
peaks_detected = analyze_pattern(telemetry_log)

# Misleading intermediate calculation
adjusted_latency = baseline_metrics['latency'] * 1.2
normalized_error = round(baseline_metrics['error_rate'] * 100, 2)

# Lambda-based normalization function (used in final calculation)
normalize = lambda x, scale: 100 - (x / scale) if x > 0 else 100

# Dictionary of normalization scales
scales = {
    'response_time': 200,
    'retry_count': 10,
    'queue_depth': 20
}

# Initialize score components
raw_scores = {}
for key in ['response_time', 'retry_count', 'queue_depth']:
    raw_scores[key] = normalize(metrics[key], scales[key])

# Explicit success rate conversion (simple linear mapping)
raw_scores['success_rate'] = metrics['success_rate'] * 100

# Composite scoring with weighted sum
weighted_sum = 0.0
for metric_name in weights.keys():
    if metric_name == 'success_rate':
        contribution = raw_scores[metric_name] * weights[metric_name]
    elif metric_name == 'response_time':
        # Special handling: capped at 90 for fairness
        base_score = raw_scores[metric_name]
        adjusted_score = min(base_score, 90)
        contribution = adjusted_score * weights[metric_name]
    else:
        contribution = raw_scores[metric_name] * weights[metric_name]
    weighted_sum += contribution

# Final non-linear adjustment based on retry-to-success ratio
ratio_penalty = (metrics['retry_count'] / metrics['success_rate']) * 0.5
final_score = int(weighted_sum - ratio_penalty)

# Output result as required
print(f"Target result: {final_score}")