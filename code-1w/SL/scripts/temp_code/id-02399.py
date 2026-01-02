def calculate_final_score(results):
    base_score = results['midterm'] * 0.4 + results['final'] * 0.6
    
    # Apply bonus if attendance is perfect
    if results['attendance'] == 100:
        base_score += 5
    
    # Apply penalty for late submissions
    if results['late_submissions'] > 2:
        base_score -= 3
    
    return base_score

# Student performance data
test_student = {
    'midterm': 85,
    'final': 90,
    'attendance': 100,
    'late_submissions': 1,
    'extra_credit': 7
}

# Irrelevant calculation (mild distraction)
total_activities = test_student['midterm'] // 10 + test_student['late_submissions']

final_score = calculate_final_score(test_student)
print(f"Result: {final_score}")