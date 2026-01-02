def analyze_feedback(ratings):
    baseline = sum(ratings) / len(ratings)
    adjusted = [r * (1.1 if r >= baseline else 0.9) for r in ratings]
    normalized = [(val - min(adjusted)) / (max(adjusted) - min(adjusted)) * 100 for val in adjusted]
    return set([round(x) for x in normalized])

ratings_data = [4.2, 3.8, 4.5, 4.0, 3.7, 4.3, 4.1]
feedback_set = analyze_feedback(ratings_data)

outlier_detection = {x for x in feedback_set if x < 45 or x > 95}
refined_set = feedback_set - outlier_detection

# Irrelevant transformation chain
temp_values = [x ** 0.5 for x in feedback_set if x % 2 == 0]
dummy_aggregate = sum(temp_values) / len(temp_values) if temp_values else 0
shadow_score = dummy_aggregate * 1.7

# Calibration logic with red herring variables
baseline_shift = len(ratings_data) * 0.15
volume_factor = len(feedback_set) + len(outlier_detection)
calibration_factor = (baseline_shift / volume_factor) if volume_factor != 0 else 0

scaling_map = list(map(lambda x: x * (1 + calibration_factor), refined_set))

# Dead code path - never executed but looks relevant
if len(outlier_detection) > 10:
    scaling_map = [x * 0.95 for x in scaling_map]

# Secondary filtering that doesn't affect final result
efficiency_flags = [1 if x > 60 else 0 for x in scaling_map]
activation_count = sum(efficiency_flags)

aggregate_performance = lambda data, factor: round(
    sum(data) / len(data) * (1 + factor) + activation_count * 0.1
)

final_score = aggregate_performance(refined_set, calibration_factor)
print(f"Result: {final_score}")