def analyze_trends(values):
    trend_scores = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_scores.append(1.2)
        elif values[i] < values[i-1]:
            trend_scores.append(-0.8)
        else:
            trend_scores.append(0.5)
    return sum(trend_scores) if trend_scores else 0

# Simulate sensor stability index
def calculate_stability(readings):
    variance = sum([(r - sum(readings)/len(readings))**2 for r in readings]) / len(readings)
    stability = 10 / (1 + variance)
    return round(stability, 2)

# Evaluate overall metric performancedef evaluate_performance(metrics):
    base_adjustment = 0.0
    adjustment_tracker = []
    
    # Irrelevant preprocessing: normalize names (distractor)
    normalized_keys = [k.strip('_').lower() for k in metrics.keys()]
    temp_map = {k: v for k, v in zip(normalized_keys, metrics.values())}
    
    # Real logic begins
    volatility_list = [v for k, v in metrics.items() if 'volatility' in k]
    if len(volatility_list) > 0:
        avg_volatility = sum(volatility_list) / len(volatility_list)
        base_adjustment += 15 if avg_volatility < 3.0 else -10
    
    # Secondary condition using dictionary lookup
    critical_thresholds = {'t1': 85, 't2': 90, 't3': 75}
    threshold_met = sum(1 for v in metrics.values() if v > 80)
    base_adjustment += 5 * threshold_met
    
    # Use of set to remove duplicates (semi-relevant)
    unique_metrics = list(set([round(v) for v in metrics.values()]))
    high_performers = [v for v in unique_metrics if v > 70]
    bonus = len(high_performers) * 3
    
    # Misleading complex comprehension (partly unused)
    derived_weights = {f'w{i}': val * 0.7 + base_adjustment for i, val in enumerate(unique_metrics)}
    weight_sum = sum(derived_weights.values())
    
    # Actual score calculation (depends only on base_adjustment and bonus)
    raw_score = sum(metrics.values())
    final_score = raw_score + base_adjustment + bonus
    
    # Dead code path (never executed)
    if False:
        fallback = calculate_stability([1,1,1])
        final_score -= fallback
    
    return int(final_score)

# Input data
data_stream = [88, 2.1, 92, 1.8, 76, 3.5]
metric_data = {
    'throughput': data_stream[0],
    'volatility_q1': data_stream[1],
    'response_t1': data_stream[2],
    'volatility_q2': data_stream[3],
    'efficiency': data_stream[4],
    'volatility_avg': data_stream[5]
}

# Additional distractor variables
temporal_analysis = analyze_trends(data_stream)
stability_index = calculate_stability([2.1, 1.8, 3.5])

# Key execution point
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")