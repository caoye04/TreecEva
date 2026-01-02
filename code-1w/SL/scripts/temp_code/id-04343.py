def calculate_final_score(students):
    # Extract scores for students with passing attendance
    passing_students = [s for s in students if s[1] >= 75]
    
    # Calculate average test score for passing students
    total_score = sum(s[0] for s in passing_students)
    count = len(passing_students)
    
    # Compute weighted final score: average contributes 80%, bonus for perfect attendance
    average_score = total_score / count if count > 0 else 0
    perfect_attendance_bonus = 10 if any(s[1] == 100 for s in passing_students) else 0
    
    return int(average_score * 0.8 + perfect_attendance_bonus)

# List of tuples: (test_score, attendance_percentage)
students_data = [(88, 82), (95, 60), (76, 90), (90, 100), (85, 70)]

final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")