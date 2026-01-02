def calculate_performance(metrics):
    total_points = sum(metrics['scores'])
    avg_score = total_points / len(metrics['scores'])
    
    # Determine rank based on ceiling of average
    final_rank = -(-avg_score // 1)  # Ceiling division trick for positive numbers
    
    # Irrelevant metric (distractor)
    max_streak = 0
    current_streak = 0
    for val in metrics['scores']:
        if val > 80:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)
    
    # Penalty based on consistency check using slicing
    recent_performance = metrics['scores'][-3:]
    consistent = all(p >= 70 for p in recent_performance)
    penalty = -5 if not consistent else 0
    
    # Key computation
    adjusted_score = final_rank + penalty
    
    # Print result
    print(f"Result: {adjusted_score}")
    return adjusted_score

# Input data
metrics_data = {
    'scores': [85, 90, 72, 68, 76, 81],
    'user_id': 112358
}

result = calculate_performance(metrics_data)