from collections import defaultdict
from itertools import combinations

# Simulate student test responses and correct answers
correct_answers = ['A', 'B', 'C', 'D', 'A']
student_responses = {
    'Alice': ['A', 'B', 'C', 'D', 'A'],
    'Bob': ['A', 'C', 'C', 'D', 'B'],
    'Charlie': ['A', 'B', 'D', 'D', 'A']
}

# Count correct responses per question
question_scores = defaultdict(int)
for responses in student_responses.values():
    for i, ans in enumerate(responses):
        if ans == correct_answers[i]:
            question_scores[i] += 1

# Calculate total correct counts across all students
total_correct_per_student = []
for name, responses in student_responses.items():
    correct_count = sum(1 for i in range(len(responses)) if responses[i] == correct_answers[i])
    total_correct_per_student.append(correct_count)

# Compute average score per student
average_score = sum(total_correct_per_student) / len(total_correct_per_student)

# Find pairs of students with identical answers on all questions
identical_pairs = 0
for s1, s2 in combinations(student_responses.keys(), 2):
    if student_responses[s1] == student_responses[s2]:
        identical_pairs += 1

# Final score calculation based on weighted metrics
weight_accuracy = 0.7
weight_consistency = 0.3
consistency_bonus = 1 if identical_pairs >= 1 else 0

result = (average_score * weight_accuracy) + (consistency_bonus * weight_consistency)
print(f"Result: {result}")