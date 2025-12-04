from collections import Counter

# Analyze student exam scores
raw_scores = [85, 92, 78, 85, 96, 78, 88, 92, 85, 91]
score_counter = Counter(raw_scores)

# Calculate base score adjustments
most_common_score = score_counter.most_common(1)[0][0]
score_adjustment = lambda x: x * 0.1 if x > 90 else x * 0.05
adjusted_scores = list(map(score_adjustment, raw_scores))

# Determine final scoring components
base_adjustment = sum(adjusted_scores) // len(adjusted_scores)
bonus_points = len([score for score in raw_scores if score >= 90])

# Final computation
adjusted_score = base_adjustment * 2
final_score = adjusted_score + bonus_points

print(f"Result: {final_score}")