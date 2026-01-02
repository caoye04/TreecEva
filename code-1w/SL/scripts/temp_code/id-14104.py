from itertools import combinations

def analyze_trends(data, window_size=3):
    trends = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / window_size
        if avg > 50:
            trends.append(1)
        else:
            trends.append(0)
    return trends

def filter_outliers(values, factor=1.5):
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals) // 4]
    q3 = sorted_vals[3 * len(sorted_vals) // 4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]

def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    temp_results = {k: v ** 0.5 for k, v in metrics.items() if v > 0}
    
    # Real computation starts
    base_score = 0
    penalty = 0
    
    # Simulate multi-step reasoning with conditionals and accumulations
    for key, value in metrics.items():
        threshold = thresholds.get(key, 50)
        if value >= threshold:
            base_score += 10
        else:
            penalty += 5
    
    # Secondary logic path - only applies under certain conditions (not triggered)
    if len(metrics) > 10:
        adjustment = sum(v // 10 for v in metrics.values())
    else:
        adjustment = 0  # Dead code path (misleading)

    # Use of set operations (required)
    metric_names = set(metrics.keys())
    required_fields = {'accuracy', 'latency', 'throughput'}
    missing = required_fields - metric_names
    if missing:
        penalty += len(missing) * 3

    # Use of dictionary aggregation
    summary_stats = {
        'total_contrib': base_score,
        'total_penalty': penalty,
        'net': base_score - penalty
    }
    
    # Final score computed here (key point)
    final_score = summary_stats['net'] + 15
    
    # Red herring: unused variable involving itertools
    combo_check = list(combinations(required_fields, 2))
    dummy_sum = sum(len(str(x)) for x in combo_check)  # Distractor
    
    return final_score

# Main execution
raw_data = [45, 60, 70, 30, 80, 65, 20, 90]
trend_analysis = analyze_trends(raw_data)
cleaned_data = filter_outliers(raw_data)

# Build metrics (real input)
metrics = {
    'accuracy': 88,
    'latency': 45,
    'throughput': 52,
    'reliability': 67,
    'scalability': 58
}
thresholds = {
    'accuracy': 80,
    'latency': 50,
    'throughput': 50,
    'reliability': 60
}

# Key execution point
final_score = evaluate_performance(metrics, thresholds)

print(f"Result: {final_score}")