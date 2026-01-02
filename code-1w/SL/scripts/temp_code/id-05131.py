def calculate_final_score():
    # Student's raw test scores
    raw_scores = [85, 90, 78, 92]
    
    # Normalize scores using modulo 100 (in case any score exceeds)
    normalized = [score % 100 for score in raw_scores]
    
    # Calculate average
    avg_score = sum(normalized) / len(normalized)
    
    # Bonus logic based on performance consistency
    score_range = max(normalized) - min(normalized)
    if score_range <= 15:
        bonus = 7.5
    else:
        bonus = 3.0
    
    # Apply bonus and round to 1 decimal place
    final_score = round(avg_score + bonus, 1)
    
    # Irrelevant distraction: string processing of subject names
    subjects = "Math,Physics,Chemistry,Biology"
    subject_set = set(subjects.split(','))
    elective_count = len(subject_set & {"Art", "Music", "Physical Education"})  # Always 0
    
    # Another distraction: unused arithmetic
    adjustment_factor = (len(subject_set) * 2) % 7
    
    return final_score

result = calculate_final_score()
print(f"Result: {result}")