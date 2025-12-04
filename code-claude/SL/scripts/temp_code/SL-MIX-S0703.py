# Calculate points for student assignments
scores = [85, 92, 78, 90, 88, 76, 94, 82]
bonus_threshold = 85
penalty = 2

# Apply bonus to scores above threshold
adjusted_scores = [score + 5 if score >= bonus_threshold else score for score in scores]

# Filter out scores less than 80 after adjustments
filtered_points = [score - penalty for score in adjusted_scores if score >= 80]

# Calculate total points from filtered scores
filtered_sum = sum(filtered_points)
max_possible = len(filtered_points) * 100

percentage = (filtered_sum / max_possible) * 100

print(f"Result: {filtered_sum}")