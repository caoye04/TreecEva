def calculate_final_score(students):
    scores = [s['grade'] for s in students if s['active']]
    adjustments = [round(s * 0.1) for s in scores]
    weighted = [a * 1.5 for a in adjustments]
    total_score = sum(weighted)
    return total_score

students = [
    {'name': 'Alice', 'grade': 85, 'active': True},
    {'name': 'Bob', 'grade': 90, 'active': False},
    {'name': 'Charlie', 'grade': 78, 'active': True},
    {'name': 'Diana', 'grade': 92, 'active': True}
]

# Irrelevant auxiliary variable (low interference)
student_count = len(students)

result = calculate_final_score(students)
print(f"Result: {result}")