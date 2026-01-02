def calculate_final_score(students, passing_threshold):
    scores = [student['grade'] for student in students]
    passed_count = sum(1 for s in scores if s >= passing_threshold)
    weighted_passed = passed_count * 1.5
    
    # Irrelevant distraction: unused variable
    average_grade = sum(scores) / len(scores) if scores else 0
    
    grade_distribution = {grade: scores.count(grade) for grade in set(scores)}
    bonus = len([g for g in scores if g == 100]) * 2
    
    final_score = weighted_passed + bonus
    return final_score

# Main data
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 90},
    {'name': 'Charlie', 'grade': 78},
    {'name': 'Diana', 'grade': 100},
    {'name': 'Eve', 'grade': 95},
    {'name': 'Frank', 'grade': 100}
]
passing_threshold = 80

result = calculate_final_score(students, passing_threshold)
print(f"Result: {result}")