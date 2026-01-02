def evaluate_performance(metrics, base):
    # Initialize relevant and irrelevant variables
    final_score = 0
    temp_buffer = []
    outlier_count = 0
    adjustment_factor = 1.0

    # Simulated metric weights (some are distractions)
    weights = {'latency': 0.3, 'throughput': 0.5, 'jitter': 0.1, 'redundancy': 0.05}
    scaling_factor = len(metrics) * 0.9  # semi-relevant but not directly used

    # Track active metrics using set operations
    expected_metrics = {'latency', 'throughput', 'jitter', 'packet_loss'}
    metric_set = set(metrics.keys())
    missing = expected_metrics - metric_set
    extra = metric_set - expected_metrics

    # Irrelevant statistical tracking
    total_variance = 0.0
    for key in metrics:
        deviation = abs(metrics[key] - base.get(key, 0))
        total_variance += deviation * 0.1  # dead-end computation

    # Core logic: score based on key metrics
    if 'throughput' in metrics:
        throughput_score = metrics['throughput'] * weights['throughput']
        if throughput_score > 40:
            bonus = 10 if 'latency' in metrics and metrics['latency'] < 50 else 5
            final_score += bonus

    if 'latency' in metrics:
        latency_penalty = 0
        if metrics['latency'] > 100:
            latency_penalty = 15
        elif metrics['latency'] > 75:
            latency_penalty = 8
        final_score -= latency_penalty

    # Use of set intersection to determine feature completeness
    completeness = len(expected_metrics.intersection(metric_set))
    if completeness == 4:
        final_score += 25
    elif completeness >= 3:
        final_score += 12
    else:
        final_score += 3

    # Distractor: complex but unused calculation with bitwise ops
    debug_flag = 0xABC ^ 0xDEF
    mask = (debug_flag & 0xFF) >> 4
    masked_value = mask | 0x10

    # Final adjustment based on jitter and packet loss presence
    if 'jitter' in metrics and 'packet_loss' in metrics:
        stability_bonus = (metrics['jitter'] < 5) * (metrics['packet_loss'] < 2) * 18
        final_score += stability_bonus

    return int(final_score)

# Baseline reference data
baseline_data = {
    'latency': 60,
    'throughput': 80,
    'jitter': 3,
    'packet_loss': 1.5
}

# Input metric dictionary with all required fields plus one extra (to trigger 'extra')
input_metrics = {
    'latency': 70,
    'throughput': 95,
    'jitter': 2,
    'packet_loss': 0.8,
    'redundancy': 0.9  # irrelevant metric
}

# Execution point of interest
final_score = evaluate_performance(input_metrics, baseline_data)
print(f"Result: {final_score}")