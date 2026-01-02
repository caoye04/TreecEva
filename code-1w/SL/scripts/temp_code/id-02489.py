def process_metrics():
    base_values = [3, 7, 2, 9, 4]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]
    weighted_sum = sum([a * b for a, b in zip(base_values, weights)])
    
    # Apply non-linear correction using lambda
    correction_factor = (lambda x: x ** 0.5 if x > 5 else x / 3)(weighted_sum)
    
    # Secondary metric for minor influence
    count_above_average = len([v for v in base_values if v > sum(base_values) / len(base_values)])
    adjustment = 0.5 if count_above_average >= 3 else 0
    
    threshold_score = correction_factor + adjustment
    
    # Early return based on condition
    if threshold_score < 3.0:
        return 0
    
    final_result = threshold_score * 1.1
    return final_result

# Execute and print result
target_variable = process_metrics()
print(f"Result: {target_variable}")