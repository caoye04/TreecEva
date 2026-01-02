def calculate_final_score(students, thresholds):
    scores = []
    for student, data in students.items():
        attendance_ratio = data['attendance'] / 30
        participation_factor = 1.2 if data['participation'] > thresholds['high_participation'] else 0.8
        base_score = data['exam'] * 0.7 + data['project'] * 0.3
        adjusted_score = base_score * participation_factor
        if attendance_ratio < thresholds['min_attendance']:
            adjusted_score *= 0.5
        scores.append(adjusted_score)
    
    # Irrelevant distraction: unused variable
    max_possible = max(scores) if scores else 0
    
    average = sum(scores) / len(scores) if scores else 0
    bonus = (lambda x: x * 0.1 if x > 80 else 0)(average)
    return round(average + bonus, 2)

# Main data
students = {
    'Alice': {'exam': 88, 'project': 92, 'attendance': 27, 'participation': 18},
    'Bob': {'exam': 76, 'project': 80, 'attendance': 24, 'participation': 12},
    'Charlie': {'exam': 94, 'project': 85, 'attendance': 30, 'participation': 20}
}

thresholds = {
    'high_participation': 15,
    'min_attendance': 0.8
}

# Calculation
final_score = calculate_final_score(students, thresholds)
print(f"Result: {final_score}")