def analyze_trend(data, threshold=0.5):
    trend_scores = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        score = 1 if diff > threshold else (-1 if diff < -threshold else 0)
        trend_scores.append(score)
    
    # Distractor: unused smoothing logic
    smoothed = [sum(trend_scores[max(0, i-2):i+1]) / (i+1) for i in range(len(trend_scores))]
    total_volatility = sum(abs(d - sum(trend_scores)/len(trend_scores)) for d in trend_scores)
    
    return sum(trend_scores)


def calculate_stability_index(seq):
    if len(seq) < 2:
        return 0
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 3)


def evaluate_performance(metrics, weights):
    weighted_sum = 0
    temp_adjustment = 0
    
    # Real computation path
    for k, v in metrics.items():
        if k in weights:
            if k == 'consistency':
                temp_adjustment = v * 0.1
            weighted_sum += v * weights[k]
    
    # Semi-relevant transformation
    adjusted_metrics = {k: v + temp_adjustment for k, v in metrics.items()}
    
    # Secondary calculation with slicing distraction
    history_window = list(adjusted_metrics.values())[1:4]
    bonus = 0
    if len(history_window) >= 3 and history_window[0] < history_window[-1]:
        bonus = 5
    
    # Final computation
    final = int(weighted_sum + bonus)
    
    # Dead code - irrelevant structure
    summary_report = {
        'raw': metrics,
        'adjustments': temp_adjustment,
        'window': history_window
    }
    
    return final

# Main execution
raw_data = [0.8, 0.85, 0.92, 0.88, 0.91, 0.93]
metrics = {
    'trend': analyze_trend(raw_data),
    'consistency': calculate_stability_index(raw_data),
    'efficiency': 8,
    'latency': 12
}

weights = {
    'trend': 3,
    'consistency': 2,
    'efficiency': 4
}

# Key statement
final_score = evaluate_performance(metrics, weights)

# Irrelevant post-processing
normalized = [x / sum(metrics.values()) for x in metrics.values()]
decay_factor = 0.95 ** len(normalized)

print(f"Result: {final_score}")