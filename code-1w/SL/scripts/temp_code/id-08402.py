def calculate_final_score(students):
    total_score = 0
    scores = [s['grade'] for s in students if s['active']]
    for i, score in enumerate(scores):
        if i % 2 == 0:
            total_score += score * 1.5
        else:
            total_score += score
    return int(total_score)

students = [
    {'name': 'Alice', 'grade': 80, 'active': True},
    {'name': 'Bob', 'grade': 90, 'active': False},
    {'name': 'Charlie', 'grade': 70, 'active': True},
    {'name': 'Diana', 'grade': 85, 'active': True},
    {'name': 'Eve', 'grade': 95, 'active': True}
]

# Irrelevant helper (minimal distraction)
def get_names(students_list):
    return [s['name'] for s in students_list]

names = get_names(students)

# Key computation
final_result = calculate_final_score(students)
total_score = final_result
print(f"Result: {total_score}")