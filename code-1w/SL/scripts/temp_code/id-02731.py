def calculate_performance_rating(hours_worked, tasks_completed, error_count):
    base_score = tasks_completed * 10 - error_count * 5
    efficiency_ratio = tasks_completed / hours_worked if hours_worked > 0 else 0
    
    # Determine if performance milestone was achieved
    achieved_milestone = efficiency_ratio >= 2.0 and tasks_completed >= 8
    
    # Adjust base score for overtime
    adjusted_base = base_score - 10 if hours_worked > 12 else base_score + 5
    
    # Bonus logic based on conditional expression
    bonus = 25 if achieved_milestone else 10
    
    # Critical assignment with conditional expression
    final_score = adjusted_base + (bonus if achieved_milestone else 0)
    
    # Irrelevant tracking variable (minor distraction)
    status_label = "High Performer" if final_score >= 90 else "Standard"
    
    return final_score

result = calculate_performance_rating(11, 9, 3)
print(f"Result: {result}")