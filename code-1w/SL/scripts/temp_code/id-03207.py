def evaluate_performance(days_present, scores):
    average_score = sum(scores) // len(scores)  # integer division
    min_threshold = 75
    required_days = 20
    
    # Compute performance bonus using set operations
    perfect_scores = {100}
    high_performers = {s for s in scores if s >= 90}
    bonus = 5 if high_performers & perfect_scores else 0
    
    base_attendance_bonus = 10 if days_present >= required_days else 0
    
    # Final score calculation
    raw_score = average_score + bonus + base_attendance_bonus
    adjustment = -5 if days_present < required_days else 0
    final_score = raw_score + adjustment
    
    return final_score

# Simulate student data
attendance = 22
exam_results = [88, 92, 90, 100, 85]

final_score = evaluate_performance(attendance, exam_results)
print(f"Result: {final_score}")