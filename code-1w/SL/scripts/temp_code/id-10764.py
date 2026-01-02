def analyze_performance(raw_marks, attendance_rate):
    scaled_marks = [mark * 0.85 for mark in raw_marks]
    attendance_bonus = int(attendance_rate * 10)
    adjusted_marks = [mark + attendance_bonus for mark in scaled_marks]
    
    # Normalize scores to 0-100 range
    min_mark, max_mark = min(adjusted_marks), max(adjusted_marks)
    normalized_scores = [100 * (mark - min_mark) / (max_mark - min_mark) for mark in adjusted_marks]
    
    # Irrelevant tracking variable (minor distraction)
    performance_trend = 'improving' if adjusted_marks[-1] > adjusted_marks[0] else 'declining'
    
    threshold_score = max(normalized_scores)
    return threshold_score

# Main execution
student_marks = [78, 85, 92, 64]
attendance = 0.92
result = analyze_performance(student_marks, attendance)
print(f"Result: {result}")