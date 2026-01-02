def evaluate_performance(metrics):
    base_score = 75
    total_score = base_score
    adjustments = [-5, 10, 0, 15, -8]
    status_flags = [True, False, True, True, False]
    
    for i, (metric, flag) in enumerate(zip(metrics, status_flags)):
        if metric < 60:
            continue
        adjustment = adjustments[i] if flag else -2
        if metric >= 80 and adjustments[i] > 0:
            adjustment *= 2
        total_score += adjustment
    
    extra_buffer = 0
    for j in range(3):
        extra_buffer += j  # Irrelevant operation, minor distraction
    
    return total_score

metrics_input = [70, 85, 55, 90, 78]
result = evaluate_performance(metrics_input)
print(f"Result: {result}")