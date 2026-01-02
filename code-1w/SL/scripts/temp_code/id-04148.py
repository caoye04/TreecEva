def analyze_feedback(ratings, thresholds):
    feedback_map = {}
    temp_aggregates = []

    for i, rating in enumerate(ratings):
        category = 'low' if rating < thresholds[0] else 'high'
        if rating >= thresholds[1]:
            category = 'exceptional'
        elif rating >= thresholds[0]:
            category = 'medium'

        feedback_map[i] = category

        squared_dev = (rating - sum(ratings) / len(ratings)) ** 2
        temp_aggregates.append(squared_dev)

    # Irrelevant smoothing operation (dead-end computation)
    smoothed = list(map(lambda x: x * 0.95, temp_aggregates))

    return feedback_map


ratings_data = [85, 92, 78, 96, 88]
threshold_levels = [80, 90]

# Misleading intermediate processing
offsets = [r - 80 for r in ratings_data]
deviations = [abs(o - 5) for o in offsets]
useless_pairs = list(zip(offsets, deviations))

feedback_result = analyze_feedback(ratings_data, threshold_levels)

# Weight assignment with red herring
weights = {"low": 1, "medium": 2, "high": 3, "exceptional": 5}
weight_sum = sum(weights.values())  # Unused value (distraction)

scaling_factor = 1.0
if len(feedback_result) > 4:
    scaling_factor *= 1.1

# Another irrelevant transformation
mapped_codes = [ord(k[0]) for k in feedback_result.values()]
checksum = sum(mapped_codes) % 100  # Distractor metric

# Core logic hidden among noise
aggregate_performance = lambda fb_map, w_map: sum(w_map[v] for v in fb_map.values())
final_score = aggregate_performance(feedback_result, weights)

# Extra dead code branch
if checksum < 0:
    final_score -= 10

# Print result as required
print(f"Result: {final_score}")