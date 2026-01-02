from itertools import combinations

def analyze_trends(data, threshold):
    trend_lines = set()
    for i in range(2, len(data) + 1):
        for combo in combinations(data, i):
            if sum(combo) / len(combo) > threshold:
                trend_lines.add(tuple(sorted(combo)))
    return trend_lines

def filter_outliers(values, limit=3.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    filtered = [v for v in values if abs(v - mean_val) / std_dev < limit]
    return filtered if len(filtered) > 0 else values

def evaluate_performance(metrics, base):
    base_set = set(base)
    extended_metrics = metrics.copy()
    temp_results = []
    
    # Irrelevant transformation - distractor
    transformed = [x * 1.5 + 2 for x in base if x % 2 == 0]
    dummy_sum = sum(transformed) / len(transformed) if transformed else 0
    
    for val in extended_metrics:
        if val > 50:
            temp_results.append(val * 0.8)
        else:
            temp_results.append(val * 1.1)
    
    # Another semi-relevant but non-critical operation
    sorted_temp = sorted(temp_results, reverse=True)
    trimmed = sorted_temp[1:-1] if len(sorted_temp) > 2 else sorted_temp
    
    adjustment_factor = 0.95
    if len(trimmed) % 2 == 0:
        adjustment_factor += 0.05
    
    # Core logic contribution
    valid_count = len(base_set.intersection(set(extended_metrics)))
    bonus = 10 if valid_count >= 3 else 5
    
    # Dead code path - misleading control flow
    if dummy_sum < 0:
        bonus *= -1
    
    aggregated = sum(trimmed) * adjustment_factor + bonus
    scaling_offset = len([x for x in base if x < 40])  # Minor influence
    final_score = int(aggregated - scaling_offset)
    
    return final_score

# Main execution
baseline_data = [12, 25, 45, 67, 89, 33]
dummy_data = [100, 200, 300]  # Unused list - distraction
extraneous_flag = True

metric_set = [25, 45, 55, 67, 75]
noise_metrics = [99, 88, 77]  # Not used directly
trend_set = analyze_trends(baseline_data, 40)
filtered_base = filter_outliers(baseline_data)

final_score = evaluate_performance(metric_set, baseline_data)
print(f"Result: {final_score}")