def calculate_final_score(scores, importance_weights):
    weighted_sum = sum([score * weight for score, weight in zip(scores, importance_weights)])
    max_possible = sum(importance_weights) * 100
    adjustment_factor = 0.95 if weighted_sum > 75 else 1.05
    return (weighted_sum / max_possible) * 100 * adjustment_factor

# Irrelevant auxiliary data (minor distraction)
student_names = ['Alice', 'Bob', 'Charlie']
timestamp = '2023-11-15'

raw_scores = [88, 92, 76, 85]
weights = [0.2, 0.3, 0.15, 0.35]

# Key computation
final_score = calculate_final_score(raw_scores, weights)

print(f"Result: {final_score}")