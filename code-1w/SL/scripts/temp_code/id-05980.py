def calculate_final_score(class_data, cutoff):
    scores = [student['grade'] for student in class_data if student['attendance'] >= cutoff]
    if not scores:
        return 0
    avg_score = sum(scores) / len(scores)
    bonus = 5 if len(scores) > 3 else 0
    return avg_score + bonus

students_list = [
    {'name': 'Alice', 'grade': 85, 'attendance': 90},
    {'name': 'Bob', 'grade': 78, 'attendance': 85},
    {'name': 'Charlie', 'grade': 92, 'attendance': 95},
    {'name': 'Diana', 'grade': 88, 'attendance': 88},
    {'name': 'Eve', 'grade': 75, 'attendance': 82}
]

# Irrelevant metadata (distractor at intervention level 5)
course_info = {'subject': 'Mathematics', 'level': 'Advanced', 'room': 'B203'}
extra_stats = {'enrollment': 30, 'pass_rate': 0.88}

threshold = 85
final_score = calculate_final_score(students_list, threshold)

# Additional slicing operation (required feature)
top_performers = students_list[:3]

# Print final result as required
print(f"Result: {final_score}")