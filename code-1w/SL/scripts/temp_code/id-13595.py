def analyze_balance(data):
    # Irrelevant pre-processing: normalize unused features
    normalized_peaks = [x / max(data) for x in data if x > 0]
    decay_weights = [0.9 ** i for i in range(len(data))]
    weighted_sum = sum(d * w for d, w in zip(data, decay_weights))

    # Key computation path
    positive_count = len([x for x in data if x > 10])
    negative_count = len([x for x in data if x < -5])
    balance_ratio = positive_count / (negative_count + 1)

    # Distractor: complex but unused conditional logic
    adjustment_factor = 0
    if balance_ratio > 2:
        adjustment_factor = 1.5
    elif balance_ratio < 0.5:
        adjustment_factor = -1.2
    else:
        for i in range(3):
            adjustment_factor += 0.1 * i  # Minor increment, ultimately irrelevant

    # Actual answer-determining logic
    trend_momentum = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    stability_score = len(data) - abs(positive_count - negative_count)
    equilibrium_score = stability_score + trend_momentum

    # Dead code branch: never executed due to fixed condition
    if False:
        equilibrium_score *= 0.5
        equilibrium_score += 100

    return equilibrium_score

# Main execution
raw_metrics = [12, -8, 15, -3, 20, 0, -6, 11, -10, 18]
filter_threshold = 5
processed_metrics = [x for x in raw_metrics if abs(x) >= filter_threshold]
equilibrium_score = analyze_balance(processed_metrics)
print(f'Result: {equilibrium_score}')