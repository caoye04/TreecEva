def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 1) / (10 - 1)
        else:
            normalized[k] = 0
    
    # Distractor: Compute average metric (not used)
    avg_metric = sum(metrics.values()) / len(metrics)
    
    # Weighted aggregation with conditional boosts
    base_score = 0
    bonus_count = 0
    
    # Use enumerate to track index and apply positional logic
    for i, (key, value) in enumerate(metrics.items()):
        weight = weights.get(key, 0.1)
        contribution = value * weight
        base_score += contribution
        
        # Apply bonus if metric exceeds threshold and index condition
        if value >= 8 and i % 2 == 0:
            bonus_count += 1
    
    # Distractor: string-based status check (dead code path)
    status_flags = ['low', 'medium', 'high']
    performance_str = 'performance: good' if base_score > 5 else 'performance: fair'
    flag_check = 'high' in status_flags
    
    # Use zip to pair metrics with weights for secondary analysis (unused)
    pairs = list(zip(metrics.keys(), weights.values()))
    total_pairs = len(pairs)
    
    # Final score computation: only bonus_count and base_score matter
    final_bonus = bonus_count * 2.5
    final_score = base_score + final_bonus
    
    # Irrelevant formatting operation
    summary = f'Score: {final_score:.1f}'
    
    return final_score

# Main execution
metrics = {'accuracy': 9, 'latency': 6, 'throughput': 8, 'reliability': 7}
weights = {'accuracy': 0.4, 'latency': 0.2, 'throughput': 0.3, 'reliability': 0.1}

# Trigger the key statement
temp_var = [x.upper() for x in ['a', 'b'] if 'a' in x]  # dead list comp
interim_result = sum([len(temp_var)])  # irrelevant

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")