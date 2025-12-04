student_scores = [85, 92, 78, 96, 88]
student_levels = ('beginner', 'intermediate', 'advanced', 'intermediate', 'beginner')

# Calculate bonus points based on levels
bonus_map = {'beginner': 5, 'intermediate': 3, 'advanced': 1}
bonus_calculations = [score + bonus_map[level] for score, level in zip(student_scores, student_levels)]

# Intermediate calculations (some are distractions)
score_sum = sum(student_scores)
average_score = score_sum / len(student_scores)
max_bonus = max(bonus_map.values())

# Apply bonus and adjust for grade boundaries
adjusted_scores = {}
for level in set(student_levels):
    level_scores = [score for score, lvl in zip(bonus_calculations, student_levels) if lvl == level]
    adjusted_scores[level] = sum(level_scores) // len(level_scores) if level_scores else 0

# Additional distractor calculations
preliminary_total = sum(adjusted_scores.values())
scale_factor = 1.05
scaled_total = preliminary_total * scale_factor

# Final target calculation
final_score = adjusted_scores[student_levels[2]]
print(f"Target result: {final_score}")