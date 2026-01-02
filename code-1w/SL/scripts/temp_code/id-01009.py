def evaluate_performance(metrics, config):
    baseline = 100
    adjustment = 0
    penalty = 0

    # Irrelevant metric tracking (distractor)
    historical_peaks = [max(metrics[k]) for k in metrics if k in ['response_time', 'latency']]
    avg_peak = sum(historical_peaks) / len(historical_peaks) if historical_peaks else 0

    # Real logic starts: compute efficiency score
    cpu_loads = metrics['cpu_usage']
    mem_usage = metrics['memory_utilization']
    efficiency = sum([1 for c in cpu_loads if c < 80])

    # Conditional branching with tuple unpacking
    thresholds = config['critical'], config['warning']
    high_threshold, _ = thresholds

    # Set operation to identify anomaly windows
    spike_indices = {i for i, m in enumerate(mem_usage) if m > high_threshold}
    if len(spike_indices) > 5:
        penalty += 15

    # List comprehension with filtering and arithmetic
    clean_cpu = [c for c in cpu_loads if c > 0]
    avg_cpu = sum(clean_cpu) / len(clean_cpu) if clean_cpu else 0

    # Multiple assignments and distractor variables
    temp_factor, debug_flag, buffer_offset = 0.85, True, len(cpu_loads) % 7

    # Core scoring logic
    if avg_cpu < 60:
        adjustment += 20
    elif avg_cpu < 75:
        adjustment += 10
    else:
        adjustment -= 5

    # Distractor: unused complex calculation
    projected_load = sum([clean_cpu[i] * (0.95 ** i) for i in range(len(clean_cpu))])
    forecast_risk = projected_load / (avg_peak + 1) if avg_peak > 0 else 0

    # Final decision using dictionary lookup
    status_map = {0: 'optimal', 10: 'stable', 20: 'efficient'}
    performance_class = status_map.get(adjustment, 'degraded')

    # Actual answer computation
    base_score = 85
    final_score = base_score + adjustment - penalty

    # Red herring: irrelevant state tracking
    log_entry = {
        'timestamp': '2023-11-05',
        'score_snapshot': final_score,
        'anomalies_detected': len(spike_indices),
        'degraded_conditions': debug_flag and penalty > 0
    }

    return final_score

# Input data
metric_data = {
    'cpu_usage': [65, 58, 72, 61, 54, 70, 63, 59],
    'memory_utilization': [82, 88, 76, 91, 83, 87, 90, 85, 81, 89, 84, 92],
    'response_time': [120, 115, 130, 125],
    'latency': [45, 50, 48]
}
thresholds = {'critical': 85, 'warning': 70}

# Execution point
final_score = evaluate_performance(metric_data, thresholds)
print(f"Result: {final_score}")