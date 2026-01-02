from collections import defaultdict

# Sample student data with test scores
test_results = [
    ('Alice', 'Math', 85),
    ('Bob', 'Math', 90),
    ('Alice', 'Science', 92),
    ('Charlie', 'Math', 78),
    ('Bob', 'Science', 88),
    ('Alice', 'Math', 95)
]

# Irrelevant distraction variable (minimal interference)
unused_buffer = [0] * 5

# Aggregate scores by subject per student
student_scores = defaultdict(lambda: defaultdict(list))
for name, subject, score in test_results:
    student_scores[name][subject].append(score)

# Compute average score per subject, then overall
averages = []
for name, subjects in student_scores.items():
    for subject, scores in subjects.items():
        avg = sum(scores) / len(scores)
        averages.append(avg)

# Calculate final composite score using conditional expression
overall_avg = sum(averages) / len(averages)
max_possible = 100
penalty_factor = 0.1 if len(test_results) > 5 else 0.0

# Key computation step
final_score = overall_avg * (1 - penalty_factor) if overall_avg > 80 else overall_avg

# Output result
print(f"Result: {final_score}")