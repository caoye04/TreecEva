from collections import defaultdict

# Simulate student test scores across multiple subjects
student_scores = [
    ('Alice', 'Math', 85),
    ('Bob', 'Math', 78),
    ('Alice', 'Science', 90),
    ('Charlie', 'Math', 88),
    ('Bob', 'Science', 82),
    ('Alice', 'Math', 95)
]

# Aggregate scores by subject using defaultdict
subject_scores = defaultdict(list)
for name, subject, score in student_scores:
    subject_scores[subject].append(score)

# Extract Math scores and filter those above 80
math_scores = subject_scores['Math']
filtered_scores = [score for score in math_scores if score > 80]

# Compute final result
result = sum(filtered_scores)
print(f"Result: {result}")