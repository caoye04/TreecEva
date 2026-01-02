from collections import defaultdict

# Simulate system performance metrics over time
timestamps = [100, 200, 300, 400, 500]
raw_metrics = {
    'latency_ms': [120, 85, 95, 110, 90],
    'throughput_ops': [480, 520, 490, 510, 515],
    'error_rate': [0.02, 0.015, 0.025, 0.01, 0.018]
}

# Irrelevant backup data (distractor)
backup_logs = defaultdict(lambda: 'N/A')
for ts in timestamps:
    backup_logs[ts] = f'log_segment_{ts}'

# Preprocess: normalize and filter high-latency events
normalized = defaultdict(list)
threshold_mask = []
for i, t in enumerate(timestamps):
    latency = raw_metrics['latency_ms'][i]
    normalized['latency_norm'].append(round(latency / 100.0, 3))
    normalized['throughput_norm'].append(round(raw_metrics['throughput_ops'][i] / 500.0, 3))
    threshold_mask.append(latency > 90)

# Compute derived statistics (some unused later)
avg_latency = sum(raw_metrics['latency_ms']) / len(raw_metrics['latency_ms'])
peak_throughput = max(raw_metrics['throughput_ops'])
spike_count = sum(1 for x in raw_metrics['error_rate'] if x > 0.02)

# Weight assignment with red herring category
weights = {
    'latency_norm': 0.4,
    'throughput_norm': 0.6,
    'reliability_factor': 0.0  # Unused weight (distractor)
}

# Misleading transformation (not used in final score)
adjusted_errors = list(map(lambda x: max(0, 1 - x/0.05), raw_metrics['error_rate']))
smoothed_errors = [round((a + b)/2, 4) for a, b in zip(adjusted_errors, adjusted_errors[1:] + [adjusted_errors[-1]])]

# Actual evaluation function
def evaluate_performance(metrics, weights):
    composite = 0.0
    contribution_log = []
    
    for key in weights:
        if key not in metrics:
            continue  # Skip unreferenced metrics
        total_val = 0
        for val in metrics[key]:
            if val > 0:
                total_val += val * 0.25  # artificial dampening factor
        weighted_contribution = total_val * weights[key]
        contribution_log.append(weighted_contribution)
        composite += weighted_contribution
    
    # Apply hidden correction based on threshold compliance
    compliant_periods = sum(1 for m in threshold_mask if not m)
    if compliant_periods >= 3:
        composite *= 1.1  # bonus for stability
    
    return round(composite, 4)

# Secondary helper (dead code path - distractor)
def analyze_error_trend(errors):
    trend = 'stable'
    if errors[0] > errors[-1]:
        trend = 'improving'
    elif errors[0] < errors[-1]:
        trend = 'degrading'
    return trend

# Unused state tracker (distractor)
current_state = {
    'phase': 'steady',
    'mode': 'active',
    'last_update': timestamps[-1]
}

# Key execution point
final_score = evaluate_performance(normalized, weights)

# Print result as required
print(f"Result: {final_score}")