def analyze_trends(values):
    moving_avg = [sum(values[i:i+3]) / 3 for i in range(len(values) - 2)]
    trend_flags = [1 if moving_avg[i] < moving_avg[i+1] else 0 for i in range(len(moving_avg) - 1)]
    return sum(trend_flags)


def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simplified pseudo-entropy
    return round(entropy, 4)


def preprocess_signal(signal_stream):
    filtered = [x for x in signal_stream if x > 0]
    normalized = [round(x / sum(filtered) * 100, 2) for x in filtered]
    cumulative = [sum(normalized[:i+1]) for i in range(len(normalized))]
    return cumulative


def evaluate_performance(metrics, limit):
    # Core logic for final score
    base_score = 0
    bonus = 0
    penalty = 0

    # Relevant transformation
    transformed = [x * 2 + 1 for x in metrics if x % 2 == 1]

    # Irrelevant intermediate calculation (distractor)
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    temp_shift = [x - avg_metric for x in metrics]
    variance_proxy = sum(x ** 2 for x in temp_shift) / len(metrics) if metrics else 0

    # Another distractor: simulate unused state tracking
    state_log = []
    for val in metrics:
        if val > limit * 1.5:
            state_log.append('HIGH')
        elif val < limit * 0.5:
            state_log.append('LOW')
        else:
            state_log.append('NORMAL')

    # Actual scoring logic
    for val in transformed:
        if val > limit:
            base_score += val // 3
            bonus += (val % 4 == 0)  # extra point if divisible by 4
        else:
            penalty += 1

    # Final score with minor adjustment
    final_score = base_score + bonus - penalty

    # Dead code path (never executed due to logic above)
    if len(metrics) > 100:
        fallback = compute_entropy(metrics)
        final_score = int(fallback * 10)

    return final_score

# Main execution
raw_data = [12, 7, 3, 9, 5, 14, 6, 11]
metric_data = preprocess_signal(raw_data)
threshold = 25
final_score = evaluate_performance(metric_data, threshold)
print(f"Result: {final_score}")