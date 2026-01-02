def calculate_performance(results):
    base_score = 0
    penalty_offset = 0.0
    bonus_tracker = []
    
    for category, metrics in results.items():
        raw_value = metrics['value']
        weight = metrics['weight']
        
        # Irrelevant tracking of bonus trends (semi-relevant but not used)
        if raw_value > 80:
            bonus_tracker.append(weight * 1.2)
        
        # Core scoring logic
        if raw_value >= 75:
            base_score += raw_value * weight / 100
        else:
            base_score -= 5 * weight / 100
        
        # Misleading penalty calculation (never applied)
        temp_penalty = (100 - raw_value) * 0.01
        penalty_offset += temp_penalty
    
    # Distractor: unused normalization step
    if len(bonus_tracker) > 0:
        average_bonus = sum(bonus_tracker) / len(bonus_tracker)
        adjusted_base = base_score * (1 + average_bonus / 100)
    
    # Final adjustment using only base_score
    final = base_score * 1.1
    return round(final, 4)

# Simulated benchmark data
dataset_metrics = {
    'latency': {'value': 88, 'weight': 30},
    'throughput': {'value': 92, 'weight': 40},
    'accuracy': {'value': 73, 'weight': 20},
    'memory': {'value': 65, 'weight': 10}
}

# Unused auxiliary data (distractor)
system_logs = {
    'cpu_peak': 94.5,
    'io_wait': 12.3,
    'context_switches': 4872,
    'cache_miss_rate': 7.8
}

intermediate_total = 0
for k in dataset_metrics:
    intermediate_total += dataset_metrics[k]['weight']

# Key execution point
final_score = calculate_performance(dataset_metrics)

# Output result
print(f"Target result: {final_score}")