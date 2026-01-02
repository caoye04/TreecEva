student_grades = [85, 90, 78, 92, 88, 76, 95, 89]

# Calculate average grade
average_grade = sum(student_grades) / len(student_grades)

# Identify grades above average
high_performers = {grade for grade in student_grades if grade > average_grade}

# Define passing threshold
passing_threshold = 80

# Filter scores that are both high-performing and above passing threshold
filtered_scores = high_performers & {score for score in student_grades if score >= passing_threshold}

# Compute final score as the maximum of filtered scores
final_score = max(filtered_scores)

print(f"Result: {final_score}")