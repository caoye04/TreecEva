def calculate_final_score(students):
    total_scores = [s['score'] for s in students if s['active']]
    bonus = len([s for s in students if s['score'] > 85 and s['extra_credits']])
    avg = sum(total_scores) / len(total_scores) if total_scores else 0
    adjustment = 5 if avg > 75 else 0
    return int(avg + bonus * 2 + adjustment)

students_data = [
    {'name': 'Alice', 'score': 88, 'active': True, 'extra_credits': True},
    {'name': 'Bob', 'score': 70, 'active': True, 'extra_credits': False},
    {'name': 'Charlie', 'score': 92, 'active': False, 'extra_credits': True},
    {'name': 'Diana', 'score': 82, 'active': True, 'extra_credits': True},
    {'name': 'Eve', 'score': 76, 'active': True, 'extra_credits': False}
]

# Irrelevant helper (minimal distraction)
def get_names(students):
    return [s['name'].upper() for s in students]

final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")