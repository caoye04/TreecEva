def calculate_final_score(students, bonuses):
    base_scores = {s['name']: s['score'] for s in students}
    adjustments = set(bonuses.keys()) & set(base_scores.keys())
    adjusted = 0
    for name in adjustments:
        if base_scores[name] > 75:
            base_scores[name] += bonuses[name]
            adjusted += 1
    result = sum(base_scores.values()) + adjusted
    return result

students_data = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 60},
    {'name': 'Charlie', 'score': 90},
    {'name': 'Diana', 'score': 70}
]

bonus_map = {
    'Alice': 5,
    'Charlie': 10,
    'Eve': 15
}

irrelevant_counter = 0
for s in students_data:
    if s['score'] < 70:
        irrelevant_counter += 1

final_score = calculate_final_score(students_data, bonus_map)
print(f"Target result: {final_score}")