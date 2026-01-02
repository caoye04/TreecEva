from collections import defaultdict

# Simulate student quiz responses and scoring
correct_answers = ['A', 'C', 'B', 'D', 'A']
student_responses = [
    ['A', 'C', 'B', 'D', 'A'],  # Perfect score
    ['A', 'C', 'D', 'D', 'B'],  # Partial match
    ['A', 'C', 'B', 'D', 'C'],  # Close, last one wrong
]

scores = []
total_score = 0
temporary_buffer = [0] * len(correct_answers)  # Irrelevant preallocation (minor distraction)

for idx, response in enumerate(student_responses):
    score = 0
    for i, (resp, ans) in enumerate(zip(response, correct_answers)):
        if resp == ans:
            score += 1
        else:
            if i > 2:  # Early break condition based on position
                break
    scores.append(score)
    total_score += score

    if idx == 1 and score < 4:
        break  # Key statement: early exit after second student

Result: {total_score}