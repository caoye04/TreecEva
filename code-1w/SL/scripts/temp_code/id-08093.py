def calculate_final_score(performance, levels):
    base_score = 0
    bonus_multiplier = 1.0
    
    # Map performance categories to points
    score_map = {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
    
    for category, count in performance.items():
        if category in score_map:
            base_score += score_map[category] * count
    
    # Apply difficulty adjustment using conditional expression
    adjustment = 1.2 if 'advanced' in levels else (1.1 if 'intermediate' in levels else 1.0)
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_debug_flag = False
    
    total_score = base_score * adjustment
    return total_score

# Input data
performance_stats = {'excellent': 2, 'good': 1, 'average': 3}
difficulty_levels = ['beginner', 'intermediate']

# Execution point of interest
total_score = calculate_final_score(performance_stats, difficulty_levels)

print(f"Result: {total_score}")