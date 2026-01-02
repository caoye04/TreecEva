from itertools import groupby

def calculate_final_score(students):
    # Filter out inactive students
    active_students = [s for s in students if s['active']]
    
    # Sort by grade to prepare for grouping
    active_students.sort(key=lambda x: x['grade'])
    
    total_score = 0
    for grade, group in groupby(active_students, key=lambda x: x['grade']):
        student_list = list(group)
        count = len(student_list)
        if count >= 2:
            # Bonus for grades with multiple students
            total_score += sum(s['score'] for s in student_list) + 5 * count
        else:
            total_score += student_list[0]['score']
    
    # Irrelevant distraction: unused variable
    max_grade = max(active_students, key=lambda x: x['score'])['grade']
    
    return total_score

# Define student data
students = [
    {'name': 'Alice', 'score': 85, 'grade': 'A', 'active': True},
    {'name': 'Bob', 'score': 90, 'grade': 'A', 'active': True},
    {'name': 'Charlie', 'score': 78, 'grade': 'B', 'active': False},
    {'name': 'Diana', 'score': 92, 'grade': 'B', 'active': True},
    {'name': 'Eve', 'score': 88, 'grade': 'B', 'active': True},
    {'name': 'Frank', 'score': 95, 'grade': 'C', 'active': True}
]

total_score = calculate_final_score(students)
print(f"Result: {total_score}")