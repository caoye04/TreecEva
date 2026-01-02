def compute_final_score(students):
    filtered_students = [s for s in students if s['grade'] >= 70]
    bonus = 5
    extra_credit_recipients = 0
    total_score = 0
    
    for idx, student in enumerate(filtered_students):
        base_score = student['grade']
        attendance_factor = 1.1 if student['attendance'] > 90 else 1.0
        adjusted_score = base_score * attendance_factor
        
        if idx % 2 == 0:
            adjusted_score += bonus
            extra_credit_recipients += 1
        
        total_score += adjusted_score
    
    scale_factor = 1.05
    total_score *= scale_factor
    
    # Irrelevant utility variable (distractor)
    avg_attendance = sum(s['attendance'] for s in students) / len(students)
    
    return int(total_score)

# Dataset
students = [
    {'name': 'Alice', 'grade': 85, 'attendance': 95},
    {'name': 'Bob', 'grade': 60, 'attendance': 85},
    {'name': 'Charlie', 'grade': 72, 'attendance': 92},
    {'name': 'Diana', 'grade': 78, 'attendance': 88},
    {'name': 'Eve', 'grade': 67, 'attendance': 94}
]

total_score = compute_final_score(students)
print(f"Result: {total_score}")