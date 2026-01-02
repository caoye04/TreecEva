def analyze_performance(grades, attendance):
    total_points = sum(grades)
    average_grade = total_points / len(grades)
    attendance_bonus = 5 if attendance >= 90 else 0
    adjusted_scores = [grade + attendance_bonus for grade in grades]
    normalized_scores = []
    for score in adjusted_scores:
        normalized = (score - average_grade) * 0.8 + average_grade
        normalized_scores.append(round(normalized, 2))
    
    # Irrelevant distraction: unused variable
    peak_attendance = max(attendance, 75)
    
    # Key computation step
    threshold_score = max(normalized_scores)
    
    # Additional but non-interfering logic
    passing_count = sum(1 for s in normalized_scores if s >= 60)
    
    print(f"Result: {threshold_score}")
    return threshold_score

# Execute with sample data
data_grades = [78, 85, 62, 91, 80]
student_attendance = 92
analyze_performance(data_grades, student_attendance)