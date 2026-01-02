from collections import defaultdict

# Student exam scores and weight configuration
exam_scores = {'midterm': 84, 'final': 92, 'project': 78, 'quiz': 95}
extra_bonuses = [5, 3, 2]

# Weight mapping using defaultdict for missing components
exam_weights = defaultdict(float)
exam_weights.update({'midterm': 0.25, 'final': 0.40, 'project': 0.25})

# Irrelevant variable (minor distraction)
temp_adjustment = sum(extra_bonuses) * 0.1

# Scoring logic with lambda for dynamic adjustment
calculate_final = lambda weights: sum(exam_scores[exam] * weights[exam] for exam in weights)

# Apply calculation
weighted_total = calculate_final(exam_weights)
final_score = round(weighted_total + temp_adjustment, 2)

Result: final_score