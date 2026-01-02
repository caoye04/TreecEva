def calculate_final_score(data):
    base_score = data['midterm'] * 0.4 + data['final'] * 0.6
    
    # Bonus logic based on participation and attendance
    bonus = 0
    if data['participation'] > 7:
        bonus += 5
    if data['attendance'] >= 90:
        bonus += 3
    
    # Apply bonus only if no major absences
    if data.get('major_absences', 0) == 0:
        base_score += bonus
    
    return round(base_score, 2)

# Simulated student exam data
temp_buffer = [0] * 10  # Irrelevant pre-allocation (minimal interference)
exam_data = {
    'midterm': 85,
    'final': 92,
    'participation': 8,
    'attendance': 95,
    'major_absences': 0
}

# Extraneous variable
interim_result = exam_data['midterm'] + exam_data['final']

final_score = calculate_final_score(exam_data)
print(f"Result: {final_score}")