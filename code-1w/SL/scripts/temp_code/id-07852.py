def calculate_performance_rating():
    # Employee performance evaluation based on task completion and quality
    tasks_completed = [2, 5, 3, 8, 1]
    quality_flags = 'HMLHH'
    
    base_points = sum(tasks_completed)
    bonus = 0
    
    # Apply quality multipliers using string indexing
    for i, flag in enumerate(quality_flags):
        if flag == 'H':
            bonus += 2
        elif flag == 'M':
            bonus += 1
    
    # Adjust score with bonus and apply experience multiplier
    exp_factor = 1.5
    adjusted_total = (base_points + bonus) * exp_factor
    
    # Final calibration using slicing to consider only recent tasks
    recent_tasks = tasks_completed[-3:]  # last three tasks
    recent_boost = sum(recent_tasks) // 3  # average contribution
    
    final_score = int(adjusted_total + recent_boost)
    
    # Irrelevant utility: counts vowels in department name (minimal distraction)
    dept_name = "Engineering"
    vowel_count = len([c for c in dept_name.lower() if c in 'aeiou'])
    
    return final_score

result = calculate_performance_rating()
print(f"Target result: {result}")