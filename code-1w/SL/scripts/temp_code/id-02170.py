def calculate_efficiency(metrics, logs):
    base_value = sum([x * 0.85 for x in metrics if x > 10])
    adjustment_factor = 1.0
    
    # Irrelevant tracking variables (distractors)
    peak_usage = max(metrics) if metrics else 0
    avg_latency = sum(logs) / len(logs) if logs else 0.0
    temp_buffer = [i ** 0.5 for i in range(1, 6)]  # Unused computation
    
    # Conditional logic with red herring branch
    if len(metrics) > 5:
        adjustment_factor *= 0.95
    elif len(metrics) == 3:
        adjustment_factor *= 1.05  # Not triggered
    
    # Real adjustment based on log length
    if len(logs) % 2 == 0:
        adjustment_factor *= 1.1
    
    # Secondary derived values (some irrelevant)
    outlier_count = len([x for x in metrics if x < 5])
    scaling_shift = outlier_count * 0.05  # Minor impact
    
    # Final efficiency formula
    raw_efficiency = base_value * adjustment_factor
    efficiency_score = int(raw_efficiency + scaling_shift)
    
    # Dead code path (never executed under this input)
    if False:
        efficiency_score -= 10
    
    final_adjustment = efficiency_score
    return final_adjustment

# Input data
workload_metrics = [12, 15, 8, 20, 45, 30]
overhead_trace = [110, 205, 180, 220, 190]

# Execute
result = calculate_efficiency(workload_metrics, overhead_trace)
efficiency_score = result

# Output target variable
print(f"Target result: {efficiency_score}")