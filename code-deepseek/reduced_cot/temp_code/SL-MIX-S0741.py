def calculate_performance_score(metrics):
    # Filter relevant metrics using lambda
    relevant_metrics = list(filter(lambda x: x > 50, metrics))
    
    # Calculate base score (distraction - not used in final)
    temp_score = sum(relevant_metrics) // len(relevant_metrics) if relevant_metrics else 0
    
    # Process with set operations
    unique_metrics = set(relevant_metrics)
    processed_set = {x * 2 for x in unique_metrics if x < 80}
    
    # Calculate bonus (distraction - not actually used)
    bonus_calc = len(processed_set) * 5
    
    # Main scoring logic
    score_dict = {}
    for metric in relevant_metrics:
        if metric > 60:
            score_dict[metric] = metric * 1.5
        else:
            score_dict[metric] = metric * 0.8
    
    # Final calculation
    final_score = sum(score_dict.values()) // len(score_dict) if score_dict else 0
    
    # Additional unused computation
    unused_total = sum(processed_set) + bonus_calc
    
    return final_score

# Test data
performance_data = [45, 65, 72, 88, 52, 91, 63, 77]
final_score = calculate_performance_score(performance_data)
print(f"Target result: {final_score}")