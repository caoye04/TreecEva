from collections import defaultdict

def calculate_final_score(class_list):
    scores = defaultdict(int)
    for student in class_list:
        name = student['name']
        grades = student['grades']
        average = sum(grades) / len(grades)
        if average >= 90:
            scores[name] = 100
        elif average >= 80:
            scores[name] = 90
        else:
            scores[name] = 80
    return sum(scores.values())

students = [
    {'name': 'Alice', 'grades': [85, 92, 78]},
    {'name': 'Bob', 'grades': [95, 90, 88]},
    {'name': 'Charlie', 'grades': [70, 75, 80]}
]

# Irrelevant tracking variable (minimal distraction)
total_entries = len(students)

final_score = calculate_final_score(students)
print(f"Result: {final_score}")