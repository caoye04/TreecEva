# This program finds the highest score among students
# and calculates the difference from the average

# Student exam scores dictionary
student_scores = {
    "Alice": 87,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 83
}

# Find students with scores above 80
qualified_students = []
for student, score in student_scores.items():
    if score > 80:
        qualified_students.append(student)

# Calculate average score
total_score = 0
for score in student_scores.values():
    total_score += score
average_score = total_score / len(student_scores)

# Find the highest score
highest_score = max(student_scores.values())

# Calculate the difference between highest and average
score_difference = highest_score - average_score

# Display results
print(f"Qualified students: {qualified_students}")
print(f"Average score: {average_score}")
print(f"Highest score: {highest_score}")
print(f"Difference from average: {score_difference}")