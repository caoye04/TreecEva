from itertools import combinations

def analyze_trends(values, window_size):
    trend_scores = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        avg = sum(window) / len(window)
        trend_scores.append(avg * 0.75)
    return trend_scores

# Simulate sensor data smoothing and threshold detection
def preprocess_signal(signal_data):
    smoothed = [round((a + b + c) / 3, 2) for a, b, c in zip(signal_data, signal_data[1:], signal_data[2:])]
    normalized = [val * 1.1 for val in smoothed]
    return normalized

def evaluate_performance(metrics, limits):
    base_score = 0
    penalty = 0

    # Real logic begins
    high_impact = [m for m in metrics if m > limits['critical']]
    medium_impact = {i: m for i, m in enumerate(metrics) if limits['warning'] < m <= limits['critical']}

    if len(high_impact) < 3:
        base_score += 40
        temp_offset = sum(high_impact) / (len(high_impact) or 1)
        adjustment = temp_offset * 0.1
        base_score += int(adjustment)
    else:
        penalty += 15

    # Distractor: unused combination analysis
    unused_pairs = list(combinations(metrics, 2))
    pair_averages = [sum(pair)/2 for pair in unused_pairs]
    decay_factor = 0.95 ** len(unused_pairs)  # Not used later

    # More real logic
    active_count = len(medium_impact)
    base_score += active_count * 5

    # Irrelevant state tracking
    status_log = []
    for idx in sorted(medium_impact.keys()):
        status_log.append(f"Event at {idx}")

    final = base_score - penalty

    # This set operation is semi-relevant: filters duplicate-like conditions
    metric_set = set(metrics)
    threshold_set = set([int(limits['warning']), int(limits['critical'])])
    overlaps = metric_set.intersection(threshold_set)
    final += len(overlaps) * 3

    return final

# Main execution
raw_data = [23.1, 45.6, 67.3, 89.0, 12.8, 45.2, 78.1, 90.5, 101.2, 44.8]
processed = preprocess_signal(raw_data)
trends = analyze_trends(raw_data, 3)

config = {
    'critical': 85.0,
    'warning': 40.0
}

# Key statement
final_score = evaluate_performance(processed, config)

print(f"Result: {final_score}")