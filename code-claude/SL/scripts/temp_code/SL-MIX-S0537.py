# Calculate total points from student quiz scores

quiz_scores = {
    'Emma': 85,
    'James': 92,
    'Sophia': 78,
    'Michael': 95,
    'Olivia': 88
}

# Add some bonus points for quick completion
time_bonus = {
    'Emma': 2,
    'James': 0,
    'Sophia': 5,
    'Michael': 1,
    'Olivia': 3
}

# Convert dictionary to list of tuples (name, score)
student_scores = []
for name, score in quiz_scores.items():
    final_score = score + time_bonus.get(name, 0)
    student_scores.append((name, final_score))

# Sort students by their scores in ascending order
sorted_scores = sorted(student_scores, key=lambda item: item[1])

# Calculate the total points earned by all students
total_points = sum(map(lambda x: x[1], sorted_scores))

# Display statistics
lowest_score = sorted_scores[0][1]
highest_score = sorted_scores[-1][1]
average = total_points / len(sorted_scores)

print(f"Result: {total_points}")