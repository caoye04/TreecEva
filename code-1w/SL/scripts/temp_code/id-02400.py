def calculate_final_score(students):
    scores = [s['grade'] for s in students if s['active']]
    averages = [max(65, min(95, sum(scores) / len(scores)))]
    curve = 1.05 if len(scores) > 3 else 1.0
    adjusted = [round(score * curve, 2) for score in averages]
    return int(sum(adjusted))

students = [
    {'name': 'Alice', 'grade': 88, 'active': True},
    {'name': 'Bob', 'grade': 94, 'active': True},
    {'name': 'Charlie', 'grade': 76, 'active': False},
    {'name': 'Diana', 'grade': 90, 'active': True},
    {'name': 'Eve', 'grade': 85, 'active': True},
    {'name': 'Frank', 'grade': 79, 'active': True}
]

# Extraneous but harmless variable
irrelevant_counter = 0

final_score = calculate_final_score(students)
print(f"Result: {final_score}")