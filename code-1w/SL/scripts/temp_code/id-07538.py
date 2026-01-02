def analyze_trends(data, baseline):
    trend_scores = []
    temp_buffer = []
    for val in data:
        deviation = abs(val - baseline)
        if deviation > 10:
            trend_scores.append(3)
        elif deviation > 5:
            trend_scores.append(2)
        elif deviation > 2:
            trend_scores.append(1)
        else:
            trend_scores.append(0)
        temp_buffer.append(deviation * 0.1)  # unused buffer (distractor)

    return trend_scores


def filter_outliers(scores):
    # Semi-relevant: modifies a copy but original list not used later
    filtered = [s for s in scores if s <= 2]
    outlier_count = len(scores) - len(filtered)
    scale_factor = 1.0 + (outlier_count * 0.05)  # computed but not used
    return filtered


def compute_weighted_average(lst, weights=None):
    if not lst:
        return 0
    if weights is None or len(weights) != len(lst):
        weights = [1] * len(lst)
    weighted_sum = sum(a * b for a, b in zip(lst, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight if total_weight else 0


def evaluate_performance(metrics, thresholds):
    adjusted = []
    debug_logs = []  # dead storage (distractor)
    
    for i, (name, value) in enumerate(metrics.items()):
        threshold = thresholds.get(name, 10)
        if value > threshold:
            score = 10
        elif value > threshold * 0.7:
            score = 6
        elif value > threshold * 0.4:
            score = 3
        else:
            score = 0
        adjusted.append(score)
        
        # Distractor computation
        normalized = value / (threshold + 1e-5)
        debug_logs.append(f'{name}: {normalized:.3f}')

    # Unused but plausible analysis
    high_performers = [k for k, v in metrics.items() if v > thresholds.get(k, 10)]
    stability_check = len(high_performers) >= 2

    # Real computation path
    weights = [2, 1, 3, 2, 1]  # aligned with metric order
    avg_score = compute_weighted_average(adjusted, weights)
    bonus = 5 if stability_check and avg_score > 5 else 0
    final_raw = avg_score + bonus
    
    # Final transformation
    return int(round(final_raw))

# Main execution
raw_data = [12, 15, 9, 20, 6]
baseline_ref = 10
scores_raw = analyze_trends(raw_data, baseline_ref)
filtered_scores = filter_outliers(scores_raw)

metrics = {
    'response_time': 8.5,
    'throughput': 11.2,
    'accuracy': 9.1,
    'latency': 4.3,
    'availability': 10.7
}
thresholds = {
    'response_time': 9.0,
    'throughput': 10.5,
    'accuracy': 9.5,
    'latency': 5.0,
    'availability': 10.0
}

intermediate_result = compute_weighted_average(scores_raw)
placeholder_call = filter_outliers([1, 3, 0, 3, 1])  # red herring call

final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")