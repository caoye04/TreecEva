def calculate_final_score(results, multiplier):
    base_scores = [res['score'] for res in results]
    penalties = {entry['name']: entry['faults'] * 2 for entry in results}
    adjusted = [base_scores[i] - penalties[results[i]['name']] for i in range(len(results))]
    total = sum(adjusted) * multiplier
    return int(total)

# Irrelevant auxiliary data (minimal distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
temp_log = [1, 1, 1]  # Unused tracking

# Core input data
results = [
    {'name': 'Alice', 'score': 85, 'faults': 3},
    {'name': 'Bob',   'score': 90, 'faults': 1},
    {'name': 'Carol', 'score': 78, 'faults': 4}
]
bonus_multiplier = 1.1

final_score = calculate_final_score(results, bonus_multiplier)
print(f"Target result: {final_score}")