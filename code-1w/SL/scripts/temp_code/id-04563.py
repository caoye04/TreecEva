from collections import defaultdict

# Simulate student quiz results with multiple attempts
student_attempts = [
    ('alice', 'quiz1', 85),
    ('bob', 'quiz1', 78),
    ('alice', 'quiz1', 92),  # improved score
    ('carol', 'quiz1', 90),
    ('bob', 'quiz1', 81),   # improved score
    ('alice', 'quiz2', 76),
    ('bob', 'quiz2', 88),
    ('carol', 'quiz2', 85),
    ('carol', 'quiz2', 87),  # retake
]

# Aggregate best scores per student per quiz
best_scores = defaultdict(lambda: defaultdict(int))

for student, quiz, score in student_attempts:
    if score > best_scores[student][quiz]:
        best_scores[student][quiz] = score

# Calculate average best score per student
student_avg = {}
for student in best_scores:
    scores = list(best_scores[student].values())
    student_avg[student] = sum(scores) / len(scores)

# Apply performance adjustment based on consistency (min 3 attempts)
total_attempts = defaultdict(int)
for student, _, _ in student_attempts:
    total_attempts[student] += 1

consistency_bonus = {s: 5 if total_attempts[s] >= 3 else 0 for s in student_avg}

# Compute final score as adjusted average
adjusted_averages = {
    s: student_avg[s] + consistency_bonus[s] for s in student_avg
}

# Secondary calculation: class average (distractor)
class_average = sum(adjusted_averages.values()) / len(adjusted_averages)
overall_median = 82.5  # assumed from prior data

# Main result computation
final_score = int(sum(adjusted_averages.values()))  # total of adjusted averages

# Print result
print(f"Result: {final_score}")