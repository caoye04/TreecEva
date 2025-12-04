# Student exam score analysis

# Initialize student scores dictionary
student_scores = {}
student_scores['Alice'] = 85
student_scores['Bob'] = 92
student_scores['Charlie'] = 78
student_scores['Diana'] = 95

# Track class statistics
class_size = len(student_scores)
average_expected = 80

# Calculate total score across all students
total_score = sum(student_scores.values())

# Calculate average score
average_score = total_score / class_size

# Determine if class performed above expectations
above_expected = average_score > average_expected

print(f"Result: {total_score}")