from collections import defaultdict

# Simulate student quiz results with multiple attempts
attempts = [
    ('alice', 'quiz1', 8), ('bob', 'quiz1', 7), ('alice', 'quiz1', 9),
    ('carol', 'quiz2', 10), ('bob', 'quiz2', 6), ('alice', 'quiz2', 8),
    ('carol', 'quiz1', 9), ('bob', 'quiz1', 8)
]

# Aggregate scores per student per quiz
quiz_scores = defaultdict(list)
for student, quiz, score in attempts:
    quiz_scores[(student, quiz)].append(score)

# Compute highest score for each student-quiz pair
max_scores = {}
for (student, quiz), scores in quiz_scores.items():
    max_scores[(student, quiz)] = max(scores)

# Calculate total best score per student
student_total = defaultdict(int)
for (student, _), score in max_scores.items():
    student_total[student] += score

# Apply bonus logic for early perfect score
perfect_bonus_applied = False
base_total = 0
for student, total in sorted(student_total.items()):
    base_total += total
    if not perfect_bonus_applied and total >= 10:
        base_total += 5
        break  # Stop after first high-performing student gets bonus

# Irrelevant string processing (minor distraction)
tags = ['std', 'qz', 'sc']
label = ''.join([tag[0] for tag in tags]).upper()  # SC: no effect on result

total_score = base_total
print(f"Result: {total_score}")