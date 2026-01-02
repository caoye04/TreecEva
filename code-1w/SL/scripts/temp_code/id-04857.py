from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 85, 92, 64, 73, 88, 95, 54, 79, 82]
    metrics = defaultdict(int)
    
    for val in raw_data:
        if val >= 90:
            metrics['excellent'] += 1
        elif val >= 80:
            metrics['good'] += 1
        elif val >= 70:
            metrics['average'] += 1
        else:
            metrics['poor'] += 1
    
    # Irrelevant transformation (distractor)
    temp_vals = [x ** 0.5 for x in raw_data]
    avg_temp = sum(temp_vals) / len(temp_vals)
    
    metrics['raw_count'] = len(raw_data)
    metrics['sum'] = sum(raw_data)
    return metrics

# Analyze trend direction (not used in final result)
def compute_trend(data_dict):
    trend_score = 0
    sequence = [data_dict[k] for k in ['poor', 'average', 'good', 'excellent']]
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_score += 1
    return trend_score

# Main processing function
def process_performance(metrics, threshold):
    base = 0
    multiplier = 1
    
    if metrics['excellent'] > threshold:
        base += 20
        multiplier *= 1.5
    else:
        base += 10
        multiplier *= 0.8
    
    if metrics['poor'] == 0:
        base += 15
    
    # Distractor: unused conditional with side computation
    if metrics['average'] >= 3:
        temp_adjust = (metrics['sum'] // metrics['raw_count']) % 7
        _ = temp_adjust * 2  # dead operation

    # Key logic step
    intermediate = base * multiplier
    
    # Additional distractor variables
    outlier_check = any(v < 60 for v in [78, 85, 92, 64, 73])
    normalization_factor = 1.0 if outlier_check else 0.9
    
    # Final score calculation
    final_score = int(intermediate + metrics['good'] * 2)
    
    # Red herring: unrelated string transformation
    status_msg = "System OK" if final_score > 40 else "Review Needed"
    status_code = len(status_msg.replace(" ", ""))
    
    return final_score

# Execution flow
metrics = collect_metrics()
trend_analysis = compute_trend(metrics)  # computed but not used
threshold = 2
final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")