def calculate_performance(participants):
    base_points = 25
    multiplier = 3
    bonus_threshold = 5
    
    performance_data = [('Alice', 7), ('Bob', 4), ('Charlie', 9), ('Diana', 6)]
    
    # Calculate total score from participants meeting threshold
    total_score = 0
    adjustment_value = 0
    
    for index, (name, score) in enumerate(performance_data):
        if score >= bonus_threshold:
            earned_points = base_points + (score - bonus_threshold) * multiplier
            total_score += earned_points
        else:
            penalty_points = (bonus_threshold - score) * 2
            adjustment_value -= penalty_points
    
    # Distractor calculations that don't affect final result
    max_possible_score = len(performance_data) * (base_points + 10)
    average_performance = sum(score for _, score in performance_data) / len(performance_data)
    
    # Final calculation
    final_score = total_score + adjustment_value
    print(f"Result: {final_score}")

calculate_performance([])