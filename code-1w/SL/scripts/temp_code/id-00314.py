def evaluate_performance(data, limits):
    # Irrelevant transformation: unused in final logic
    temp_normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]

    # Distractor variables and computations
    outlier_count = 0
    adjusted_values = []
    for val in data:
        if val > 2 * sum(data) // len(data):
            outlier_count += 1
        adjusted_values.append(val + 5 if val < 0 else val)

    # Unused helper function simulating dead code path
    def calculate_variance(seq):
        mean = sum(seq) / len(seq)
        return sum((x - mean) ** 2 for x in seq) / len(seq)

    # Real logic begins: filter critical metrics above threshold using set operations
    critical_metrics = {i for i, x in enumerate(data) if x > limits.get('critical', 80)}
    warning_metrics = {i for i, x in enumerate(data) if limits.get('warning', 60) < x <= limits.get('critical', 80)}

    # Conditional expression determining weight contribution
    base_score = 100 if len(critical_metrics) == 0 else 60

    # Linear search through indices to adjust score based on proximity clustering
    penalty = 0
    consecutive_warnings = 0
    indices = sorted(list(warning_metrics | critical_metrics))
    for i in range(1, len(indices)):
        if indices[i] - indices[i-1] == 1:
            consecutive_warnings += 1

    # Another irrelevant computation (dead logic)
    average_gap = sum(indices[i] - indices[i-1] for i in range(1, len(indices))) // len(indices) if indices else 0

    # Actual scoring logic with conditional expressions
    if consecutive_warnings >= 3:
        penalty += 15
    elif len(critical_metrics) >= 2:
        penalty += 10
    else:
        penalty += len([x for x in data if x < limits.get('baseline', 30)]) * 2

    # Final score computed here — this is the key execution point
    final_score = base_score - penalty

    # Irrelevant dictionary aggregation (distractor)
    summary = {
        'total': len(data),
        'critical': len(critical_metrics),
        'warnings': len(warning_metrics),
        'score_snapshot': final_score,
        'outliers': outlier_count
    }

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data and thresholds
    metric_data = [78, 85, 87, 45, 90, 92, 50, 88]
    thresholds = {
        'baseline': 30,
        'warning': 60,
        'critical': 85
    }

    # Trigger the key statement
    final_score = evaluate_performance(metric_data, thresholds)
    
    # Print result as required
    print(f"Result: {final_score}")