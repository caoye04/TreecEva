def analyze_trends(raw_values):
    normalized = [x / max(raw_values) for x in raw_values]
    trends = []
    for i in range(1, len(normalized)):
        if normalized[i] > normalized[i-1]:
            trends.append(1)
        elif normalized[i] < normalized[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends


def filter_outliers(data, factor=1.5):
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]


def compute_weights(n):
    weights = [1 / (i+1) for i in range(n)]
    total = sum(weights)
    return [w / total for w in weights]


def evaluate_performance(metrics, config):
    # Irrelevant pre-processing
    temp_result = [m * 2 for m in metrics]
    temp_result = [t for t in temp_result if t > 0]
    
    # Real logic starts: apply decay and thresholding
    decayed = [metrics[i] * (0.9 ** i) for i in range(len(metrics))]
    
    # Misleading dictionary usage
    stats = {
        'count': len(decayed),
        'peak': max(decayed),
        'base_avg': sum(decayed) / len(decayed),
        'noise_floor': 0.05
    }
    
    adjusted = []
    for d in decayed:
        if d > config['threshold'] * stats['peak']:
            adjusted.append(d * config['bonus_multiplier'])
        else:
            adjusted.append(d * config['penalty_factor'])
    
    # Another distraction: sorting that isn't used
    dummy_sorted = sorted(adjusted, reverse=True)
    dummy_sum = sum(dummy_sorted[:3])  # unused
    
    # Weighted scoring using computed weights
    weights = compute_weights(len(adjusted))
    final_score = sum(adjusted[i] * weights[i] for i in range(len(adjusted)))
    
    # Red herring computation
    secondary_metric = sum(1 for a in adjusted if a > 1.0)
    scaling_factor = 1.0 + (secondary_metric * 0.01)
    
    # Final score unaffected by scaling_factor due to problem design
    return int(final_score * 100) / 100.0  # round to 2 decimal places

# Main execution
raw_input = [120, 135, 130, 142, 148, 138, 155, 162, 158, 170]

cleaned_data = filter_outliers(raw_input, factor=2.0)
trend_pattern = analyze_trends(cleaned_data)

metric_data = [abs(v) + 0.1 for v in cleaned_data]

# Unused transformation
transformed = [round((x - min(metric_data)) / (max(metric_data) - min(metric_data)), 3) for x in metric_data]

thresholds = {
    'threshold': 0.65,
    'bonus_multiplier': 1.4,
    'penalty_factor': 0.7
}

# Key statement
final_score = evaluate_performance(metric_data, thresholds)

print(f"Result: {final_score}")