def process_results(records, threshold):
    filtered = [r for r in records if r['score'] >= threshold]
    bonuses = list(map(lambda x: x['bonus'], filtered))
    total_bonus = sum(bonuses)
    base_scores = {r['id']: r['score'] for r in filtered}
    final_sum = sum(base_scores.values()) + total_bonus
    return final_sum

# Irrelevant auxiliary data (minor distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
temp_log = [100, 200, 300]

# Core data
assessments = [
    {'id': 1, 'score': 75, 'bonus': 5},
    {'id': 2, 'score': 88, 'bonus': 12},
    {'id': 3, 'score': 90, 'bonus': 10},
    {'id': 4, 'score': 60, 'bonus': 8},
    {'id': 5, 'score': 92, 'bonus': 15}
]
passing_threshold = 70

final_score = process_results(assessments, passing_threshold)
print(f"Result: {final_score}")