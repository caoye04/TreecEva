def calculate_final_score(students):
    scores = [s['grade'] for s in students if s['active']]
    adjustments = {i: len(name) - 5 for i, name in enumerate([s['name'] for s in students])}
    base_score = sum(scores) // len(scores) if scores else 0
    bonus = 0
    for idx, student in enumerate(students):
        if student['active'] and student['grade'] > base_score:
            bonus += adjustments.get(idx, 0)
    inactive_count = len([s for s in students if not s['active']])
    penalty = inactive_count * 2
    final_score = base_score + bonus - penalty
    return final_score

students = [
    {'name': 'Alice', 'grade': 85, 'active': True},
    {'name': 'Bob', 'grade': 78, 'active': True},
    {'name': 'Charlie', 'grade': 90, 'active': False},
    {'name': 'Diana', 'grade': 92, 'active': True},
    {'name': 'Eve', 'grade': 80, 'active': True}
]

final_score = calculate_final_score(students)
print(f"Target result: {final_score}")