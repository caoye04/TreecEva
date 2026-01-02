def evaluate_performance(metrics, threshold):
    adjusted_values = [round(x * 1.05) for x in metrics if x > threshold - 10]
    outliers = [x for x in metrics if x < 50 or x > 95]
    penalty = len(outliers) * 2
    
    temp_sum = 0
    for val in adjusted_values:
        if val % 2 == 0:
            temp_sum += val // 3
        else:
            temp_sum += val // 4

    bonus = 0
    if len(adjusted_values) > 4:
        bonus = 10
    
    intermediate_total = sum(adjusted_values)
    scaling_factor = 0.85 if intermediate_total > 200 else 1.0
    
    # Misleading calculation with dead-end variables
    fake_weight = 0.5
    dummy_offset = 17
    phantom_total = intermediate_total * fake_weight + dummy_offset  # Not used later

    raw_score = temp_sum * scaling_factor + bonus - penalty
    final_score = int(raw_score + 0.5)  # Round to nearest integer
    return final_score

# Simulated sensor metric data
metric_data = [88, 72, 91, 45, 83, 77, 96, 68]
base_threshold = 70

# Extraneous pre-processing (some relevant, some not)
filtered_data = [x for x in metric_data if x >= 60]
sorted_data = sorted(filtered_data, reverse=True)
mean_value = sum(filtered_data) / len(filtered_data)

dummy_stats = {}
dummy_stats['max'] = max(metric_data)
dummy_stats['min'] = min(metric_data)
dummy_stats['range'] = dummy_stats['max'] - dummy_stats['min']

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")