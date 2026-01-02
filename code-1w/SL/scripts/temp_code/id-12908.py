def calculate_final_score(scores, importance_weights):
    normalized = [score / 100 for score in scores]
    weighted = [n * w for n, w in zip(normalized, importance_weights)]
    raw_total = sum(weighted)
    bonus = 5 if raw_total > 0.8 else 0
    return int(raw_total * 100) + bonus

# Irrelevant auxiliary data (minimal distraction)
student_names = ['Alice', 'Bob', 'Charlie']
timestamp = '2023-09-15'

raw_scores = [88, 92, 76, 85]
weights = [0.3, 0.4, 0.2, 0.1]

final_score = calculate_final_score(raw_scores, weights)
print(f'Result: {final_score}')