def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend_sum = 0
    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        trend_sum += 1 if diff > 0 else (-1 if diff < 0 else 0)
    return trend_sum

# Simulate sensor stability index
def calculate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    stability_index = 100 / (1 + variance) if variance != 0 else 100
    return stability_index

# Main evaluation logic
def evaluate_performance(metrics, threshold):
    raw_total = sum(metrics)
    adjustment_factor = 0.85 if raw_total > threshold else 1.15
    
    # Irrelevant intermediate calculation (distractor)
    outlier_count = 0
    for val in metrics:
        if val < 5 or val > 95:
            outlier_count += 1
    # Dead code path - never used (distractor)
    if outlier_count > 10:
        adjustment_factor *= 0.9
    
    trend_metric = analyze_trend(metrics)
    stability_metric = calculate_stability(metrics)
    
    # Conditional expression usage (required feature)
    performance_bonus = 10 if trend_metric > 0 else 5
    
    # Core computation leading to answer
    base_score = raw_total * adjustment_factor
    final_normalized = base_score + performance_bonus + (stability_metric * 0.1)
    
    # Additional irrelevant variable (distractor)
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    deviation_penalty = 0
    for m in metrics:
        if abs(m - avg_metric) > 20:
            deviation_penalty += 0.5
    
    # Final score unaffected by penalty (misleading path)
    final_score = int(final_normalized)  # This is the key result
    
    return final_score

# Input data
metric_data = [85, 76, 88, 92, 79, 81, 87, 90, 84, 83]
base_threshold = 800

# Execute main logic
trend_analysis = analyze_trend(metric_data)
stability_value = calculate_stability(metric_data)
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")