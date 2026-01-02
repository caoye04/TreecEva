def calculate_performance_metric():
    # System performance metrics
    cpu_load = [0.65, 0.82, 0.71, 0.93, 0.67]
    memory_usage = [0.58, 0.76, 0.64, 0.88, 0.73]
    
    # Historical baselines
    baseline_metrics = {
        'avg_cpu': sum(cpu_load) / len(cpu_load),
        'avg_memory': sum(memory_usage) / len(memory_usage)
    }
    
    # Efficiency factors
    efficiency_factor = 1.0
    if baseline_metrics['avg_cpu'] > 0.75:
        efficiency_factor *= 0.9
    if baseline_metrics['avg_memory'] > 0.70:
        efficiency_factor *= 0.95
    
    # Compute composite score
    raw_score = (baseline_metrics['avg_cpu'] + baseline_metrics['avg_memory']) * 50
    adjusted_score = raw_score * efficiency_factor
    
    # Apply stability bonus
    stability_bonus = 0
    for i in range(1, len(cpu_load)):
        if abs(cpu_load[i] - cpu_load[i-1]) < 0.15:
            stability_bonus += 2
    
    final_score = adjusted_score + stability_bonus
    return final_score

result = calculate_performance_metric()
print(f"Result: {result}")