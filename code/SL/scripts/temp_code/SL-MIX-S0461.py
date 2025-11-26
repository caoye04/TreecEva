def calculate_performance(metrics):
    # Calculate weighted performance score
    weights = [0.3, 0.4, 0.3]
    weighted_sum = sum(metric * weight for metric, weight in zip(metrics, weights))
    
    # Apply bonus for high performers (distractor - doesn't affect final result)
    base_multiplier = 1.2 if max(metrics) > 85 else 1.0
    
    # Calculate adjusted scores with scaling
    scaling_factor = 1.5
    adjusted_scores = []
    for i, metric in enumerate(metrics):
        scaled_value = metric * scaling_factor
        adjusted_value = scaled_value if i % 2 == 0 else metric + 10
        adjusted_scores.append(adjusted_value)
    
    # Intermediate calculation that's not used (distractor)
    temp_calculation = sum(adjusted_scores[:2]) * base_multiplier
    
    # Final result selection
    final_score = adjusted_scores[-1]
    
    print(f"Result: {final_score}")
    return final_score

# Test data
performance_metrics = [72, 88, 65, 91, 78]
result = calculate_performance(performance_metrics)