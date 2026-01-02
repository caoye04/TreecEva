def evaluate_performance(metrics, weights):
    # Initialize variables
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = {}
    
    # Irrelevant data transformation (distractor)
    for k, v in metrics.items():
        if isinstance(v, float):
            temp_result[k + '_norm'] = round(v * 0.95, 3)

    # Core logic begins
    for key in ['accuracy', 'latency', 'throughput', 'reliability']:
        if key in metrics and key in weights:
            contribution = metrics[key] * weights[key]
            base_score += contribution
            
            # Bonus logic based on thresholds
            if metrics[key] > 85 and key in ['accuracy', 'throughput']:
                bonus_tracker.append(contribution * 0.1)
            elif metrics[key] < 60 and key == 'latency':
                penalty_adjustment -= 5
    
    # Secondary processing with tuple unpacking
    extra_bonuses = (10, 5, 2)
    for bonus in extra_bonuses:
        if bonus > 7:
            penalty_adjustment += bonus // 2  # Only affects adjustment

    # Destructuring assignment (irrelevant to final score)
    x, y, z = extra_bonuses
    y = z * 2  # Dead computation

    # Final aggregation
    final_score = base_score + sum(bonus_tracker) + penalty_adjustment
    
    # Misleading print (not part of result)
    debug_info = {"temp": temp_result, "tracker": bonus_tracker}
    
    return int(final_score)

# Main execution
metrics = {
    'accuracy': 92,
    'latency': 45,
    'throughput': 88,
    'reliability': 76,
    'scalability': 67  # Not used in core calculation
}

weights = {
    'accuracy': 0.4,
    'latency': 0.2,
    'throughput': 0.3,
    'reliability': 0.1
}

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")