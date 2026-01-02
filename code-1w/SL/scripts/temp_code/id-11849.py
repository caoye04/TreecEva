from collections import defaultdict

# Simulate student quiz scores with attempts
student_attempts = [
    {'name': 'Alice', 'scores': [8, 9, 7]},
    {'name': 'Bob', 'scores': [6, 7]},
    {'name': 'Charlie', 'scores': [10, 9, 10, 8]}
]

# Irrelevant distractor: unused variable
max_possible_score = 10

# Compute average improvement per student
improvements = []
for attempt in student_attempts:
    scores = attempt['scores']
    if len(scores) > 1:
        improvement = scores[-1] - scores[0]
        improvements.append(improvement)

# Weighting mechanism: last score has double weight
weighted_values = []
for attempt in student_attempts:
    scores = attempt['scores']
    weighted = scores[-1] * 2 - scores[0]
    weighted_values.append(weighted)

# Aggregate final score
bonus = 3  # Minor adjustment
base_total = sum(improvements)
total_score = sum(weighted_values)
total_score += bonus

print(f"Result: {total_score}")