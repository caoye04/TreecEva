def evaluate_performance(metrics, weights):
    base_score = 0
    adjustment_factor = 0.0
    penalty = 0
    
    # Irrelevant computation: tracking unused latency stats
    latency_stats = {'max': 98, 'min': 5, 'avg': 42}
    avg_latency = sum(latency_stats.values()) / len(latency_stats)
    if avg_latency > 40:
        penalty += 3  # Distractor: not used in final logic

    # Real metric processing starts
    for key in metrics:
        if key in weights:
            base_score += metrics[key] * weights[key]
    
    # Additional distraction: unused normalization block
    max_possible = sum(abs(w) for w in weights.values()) * 100
    if max_possible > 0:
        normalized = base_score / max_possible
        normalized = round(normalized, 4)
    
    # Conditional adjustment based on tuple unpacking and logical checks
    thresholds = (70, 85, 95)
    t_low, t_mid, t_high = thresholds
    
    if base_score >= t_high:
        adjustment_factor = 1.1
    elif base_score >= t_mid:
        adjustment_factor = 1.05
    elif base_score >= t_low:
        adjustment_factor = 1.02
    else:
        adjustment_factor = 0.95
    
    # Simulate minor correction via dictionary lookup
    corrections = {0.95: -2, 1.02: 1, 1.05: 3, 1.1: 5}
    correction = corrections.get(adjustment_factor, 0)
    
    # Final score calculation — only this matters
    final_score = int(base_score + correction)
    
    # Dead code: irrelevant list transformation
    temp_data = [x for x in range(10) if x % 2 == 0]
    temp_data = [x ** 2 for x in temp_data]
    
    return final_score

# Main execution
metrics = {'accuracy': 92, 'precision': 88, 'recall': 94, 'f1': 90}
weights = {'accuracy': 0.4, 'precision': 0.2, 'recall': 0.2, 'f1': 0.2}

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")