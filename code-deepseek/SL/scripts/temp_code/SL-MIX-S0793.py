from collections import Counter

student_responses = ['A', 'B', 'C', 'A', 'B', 'A', 'D', 'C', 'A', 'B']
response_counts = Counter(student_responses)
score_weights = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
weighted_scores = {}

for answer, count in response_counts.items():
    weighted_scores[answer] = count * score_weights[answer]

final_score = sum(weighted_scores.values())
print(f"Result: {final_score}")