def calculate_performance_metric():
    base_values = [x for x in range(15) if x % 3 == 0]
    adjustments = {i: val * 0.5 for i, val in enumerate(base_values)}
    
    # Irrelevant distraction: unused variable
    temp_buffer = [0] * 5
    
    processed = set()
    for key in adjustments:
        if adjustments[key] > 4:
            processed.add(key)
    
    sum_of_adjusted = sum(adjustments[k] for k in processed)
    count_filter = len([v for v in base_values if v >= 6])
    
    # Main computation
    final_score = sum_of_adjusted + count_filter
    return final_score

result = calculate_performance_metric()
print(f"Result: {result}")