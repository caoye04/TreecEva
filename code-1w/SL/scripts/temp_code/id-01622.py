def calculate_final_score(data):
    base_score = data['exam'] * 0.6
    bonus = 5 if data['attendance'] > 90 else 0
    project_factor = 1.1 if data['project_grade'] in ['A', 'B'] else 0.9
    adjusted_score = (base_score + data['project']) * project_factor
    return int(adjusted_score + bonus)

student_data = {
    'exam': 85,
    'project': 40,
    'attendance': 92,
    'project_grade': 'B',
    'enrollment_year': 2021
}

# Irrelevant utility function (minor distraction)
def format_name(first, last):
    return f"{last}, {first}"

final_score = calculate_final_score(student_data)
print(f"Result: {final_score}")