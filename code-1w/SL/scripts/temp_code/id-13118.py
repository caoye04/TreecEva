def calculate_final_score(students):
    filtered_names = [s['name'] for s in students if len(s['name']) > 4 and s['active']]
    scores = [s['score'] for s in students if s['score'] >= 60]
    bonus = len(filtered_names) * 5
    base_total = sum(scores)
    total_score = base_total + bonus
    return total_score

students = [
    {'name': 'Alice', 'score': 85, 'active': True},
    {'name': 'Bob', 'score': 55, 'active': True},
    {'name': 'Charlie', 'score': 70, 'active': False},
    {'name': 'Diana', 'score': 90, 'active': True},
    {'name': 'Eve', 'score': 60, 'active': True}
]

# Additional unrelated but harmless computation
dummy_result = ''.join([name['name'][0] for name in students]).lower()

final_result = calculate_final_score(students)
Result: {final_result}