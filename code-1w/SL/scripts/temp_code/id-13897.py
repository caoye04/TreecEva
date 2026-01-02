from collections import defaultdict

# Simulate student quiz scores across multiple attempts
test_scores = [85, 92, 78, 96, 88]
bonus_points = 5  # Irrelevant distractor: not used in median calculation
subject_bonuses = defaultdict(int)
subject_bonuses['math'] += 3  # Distractor: unused in logic

# Sort scores to find median
test_scores.sort()
sorted_scores = test_scores
median_score = sorted_scores[len(sorted_scores) // 2]

# Additional irrelevant tracking
count_per_grade = defaultdict(int)
for score in sorted_scores:
    count_per_grade[score // 10] += 1

Result: {median_score}