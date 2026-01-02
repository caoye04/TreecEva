def analyze_trends(data, baseline):
    trend_scores = []
    adjustments = []
    cumulative_shift = 0

    for i, value in enumerate(data):
        deviation = value - baseline
        if deviation > 5:
            trend_scores.append(3)
        elif deviation > 2:
            trend_scores.append(2)
        elif deviation < -2:
            trend_scores.append(-1 * abs(deviation))
        else:
            trend_scores.append(0)
        
        shift = abs(deviation) * 0.1
        cumulative_shift += shift
        adjustments.append(shift)

    normalized_trend = sum(trend_scores) / len(trend_scores) if trend_scores else 0
    return normalized_trend, cumulative_shift, adjustments


def evaluate_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    stability = 100 - variance
    return stability


def process_performance(metrics, thresholds):
    primary_metric = metrics['throughput']
    secondary_metric = metrics['latency']
    error_rate = metrics['error_rate']

    # Simulated string-based status processing (uses string method)
    status_str = "_high_latency" if secondary_metric > thresholds['latency'] else "_optimal"
    status_tag = f"status{status_str}".upper().replace('_', '')
    tag_value = len(status_tag) if 'HIGH' in status_tag else len(status_tag) // 2

    # Irrelevant transformation on labels (distractor)
    labels = ['sys', 'net', 'io', 'cpu']
    labeled_metrics = {lbl.upper(): val for lbl, val in zip(labels, [10, 20, 30, 40])}
    entropy_offset = 0
    for k, v in labeled_metrics.items():
        if 'Y' in k:
            entropy_offset += v * 0.01

    # Core logic begins
    throughput_score = primary_metric * 0.8
    latency_penalty = 0
    if secondary_metric > thresholds['latency']:
        latency_penalty = (secondary_metric - thresholds['latency']) * 1.5

    error_correction = max(0, 10 - error_rate * 2)

    # Use of enumerate in filtering (relevant)
    filtered_metrics = []
    for idx, m in enumerate([throughput_score, error_correction]):
        if idx == 0 or m > 5:
            filtered_metrics.append(m)

    base_score = sum(filtered_metrics) - latency_penalty + tag_value

    # Additional irrelevant computation (dead path)
    hypothetical_bonus = 0
    scenarios = ['peak', 'normal', 'failover']
    for s in scenarios:
        if 'z' in s:  # never true
            hypothetical_bonus += 10

    final_score = base_score + entropy_offset
    return int(final_score)

# Main execution
sensor_data = [102, 98, 110, 105, 95]
metrics = {
    'throughput': 95.0,
    'latency': 45.0,
    'error_rate': 3.0
}
thresholds = {
    'latency': 40.0
}

# Irrelevant preprocessing (distractor)
data_pairs = list(zip(sensor_data, [x+1 for x in sensor_data]))
duplicate_check = set(tuple(sorted(pair)) for pair in data_pairs)

# Real execution path
trend_analysis, total_drift, _ = analyze_trends(sensor_data, baseline=100)
stability = evaluate_stability([88, 92, 85, 90])
final_score = process_performance(metrics, thresholds)
print(f"Result: {final_score}")