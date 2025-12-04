# Student performance tracking system
# Calculate the total points earned by a student across different subjects

student_scores = {
    'math': 85,
    'science': 92,
    'history': 78,
    'english': 88,
    'art': 95
}

# Track some additional information
subjects_count = len(student_scores)
max_score = max(student_scores.values())
min_score = min(student_scores.values())

# Calculate average score before adding bonus points
initial_avg = sum(student_scores.values()) / subjects_count

# Add bonus points for extra credit work
student_scores['science'] += 3
student_scores['history'] += 5

# Calculate the total points earned
total_points = sum(student_scores.values())

# Calculate new average after bonus
final_avg = total_points / subjects_count

print(f"Result: {total_points}")