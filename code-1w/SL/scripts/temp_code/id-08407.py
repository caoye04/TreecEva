def calculate_final_score(students, threshold):
    filtered_students = [s for s in students if s['grade'] >= threshold]
    grades = [s['grade'] for s in filtered_students]
    attendance_bonus = sum(1 for s in filtered_students if s['attendance'] > 90)
    base_score = sum(grades) // len(grades) if grades else 0
    extra_credit = 5 if any(s['honors'] for s in filtered_students) else 0
    final_score = base_score + attendance_bonus + extra_credit
    return final_score

# Dataset
students_data = [
    {'name': 'Alice', 'grade': 85, 'attendance': 95, 'honors': False},
    {'name': 'Bob', 'grade': 90, 'attendance': 88, 'honors': True},
    {'name': 'Charlie', 'grade': 78, 'attendance': 92, 'honors': False},
    {'name': 'Diana', 'grade': 94, 'attendance': 96, 'honors': True}
]
threshold = 80

# Execution
final_score = calculate_final_score(students_data, threshold)
print(f"Result: {final_score}")