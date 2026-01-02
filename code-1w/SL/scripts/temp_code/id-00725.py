def calculate_final_score(data):
    base_score = data['exam'] * 0.6
    project_bonus = data['projects'] * 5
    if data['attendance'] >= 90:
        base_score += 10
    elif data['attendance'] >= 75:
        base_score += 5
    
    # Irrelevant metric (minor distraction)
    compliance_rate = data['assignments_submitted'] / data['total_assignments']
    
    final_score = base_score + project_bonus
    
    # Additional unrelated calculation (minimal interference)
    feedback_count = len(data['feedback'])
    
    return final_score

# Student data input
student_data = {
    'exam': 88,
    'projects': 3,
    'attendance': 82,
    'assignments_submitted': 18,
    'total_assignments': 20,
    'feedback': ['good', 'improvement needed', 'excellent']
}

final_score = calculate_final_score(student_data)
print(f"Result: {final_score}")