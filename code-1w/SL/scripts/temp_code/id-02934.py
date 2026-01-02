def evaluate_performance(metrics, base):
    adjustment_factor = 0.85
    weighted_sum = sum([m * (i + 1) for i, m in enumerate(metrics)])
    base_adjusted = base * adjustment_factor
    
    # Irrelevant intermediate calculation (distractor)
    temp_scores = [x ** 0.5 for x in metrics if x > 5]
    avg_temp = sum(temp_scores) / len(temp_scores) if temp_scores else 0
    
    # Semi-relevant transformation
    transformed = list(map(lambda x: x * base_adjusted / 100, metrics))
    
    # Red herring: unused complex expression
    outlier_check = any([abs(x - base) > 2 * base for x in metrics])
    normalization_shift = 10 if outlier_check else 5
    
    # Core logic hidden among distractions
    raw_score = sum(transformed) / len(transformed) if transformed else 0
    penalty = 0
    for val in metrics:
        if val < base * 0.5:
            penalty += 1.5
    
    # Actual final computation
    final_score = raw_score - penalty + normalization_shift
    return final_score

# Simulated sensor-derived metric data (avoiding 'sensor' theme directly)
metric_data = [8, 12, 5, 15, 3, 9]
baseline = 7

# Unused auxiliary variables (distractors)
data_copy = metric_data[:]
sorted_data = sorted(metric_data, reverse=True)
duplicate_count = len(metric_data) - len(set(metric_data))

# Key execution point
final_score = evaluate_performance(metric_data, baseline)

# Print result
print(f"Target result: {final_score}")