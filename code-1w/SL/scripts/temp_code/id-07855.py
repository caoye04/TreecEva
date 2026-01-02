from itertools import compress

# Simulate employee performance scores across quarterly reviews
department = ['engineering', 'marketing', 'engineering', 'sales', 'engineering', 'marketing']
performance_scores = [85, 72, 90, 68, 94, 75]
attendance_rate = [0.95, 0.80, 0.98, 0.75, 0.92, 0.83]

# Determine eligibility for bonus: engineering or marketing with attendance >= 0.85
is_eligible = [dept in ['engineering', 'marketing'] and att >= 0.85 for dept, att in zip(department, attendance_rate)]

# Extract relevant performance scores for eligible employees
filtered_performance = list(compress(performance_scores, is_eligible))

# Apply curve adjustment only to non-eligible for internal review (distractor)
curve_adjusted = [score * 1.1 if not eligible else score for score, eligible in zip(performance_scores, is_eligible)]
other_metric = sum(curve_adjusted) / len(curve_adjusted)  # Irrelevant metric

total_score = sum(filtered_performance)