# Student score tracking system

# Initialize dictionaries with student data
student_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan']
test_scores = [92, 78, 85, 90, 88]

# Create a dictionary to track attendance
attendance_log = {}
for idx, name in enumerate(student_names):
    attendance_log[name] = idx + 3  # Days present this week

# Create a dictionary with student scores
student_scores = {}
for name, score in zip(student_names, test_scores):
    # Store only scores above 75
    if score > 75:
        student_scores[name] = score

# Calculate statistics
max_score = max(test_scores)
min_score = min(test_scores)

# Calculate the average score of students in the student_scores dictionary
avg_score = sum(student_scores.values()) / len(student_scores)

# Calculate participation bonus based on attendance
bonus_points = sum(attendance_log.values()) / len(attendance_log)

print(f"Result: {avg_score}")