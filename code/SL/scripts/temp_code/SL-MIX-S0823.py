student_scores = {'alice': 85, 'bob': 92, 'charlie': 78, 'diana': 96, 'eve': 88}

# Find student with highest score
highest_score = -1
highest_student = ''
for student, score in student_scores.items():
    if score > highest_score:
        highest_score = score
        highest_student = student

# Calculate class average (distractor operation)
average_score = sum(student_scores.values()) / len(student_scores)

# Get final score
final_score = student_scores[highest_student]
print(f"Result: {final_score}")