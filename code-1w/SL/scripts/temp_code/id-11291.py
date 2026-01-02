def analyze_sentiment(intensity_list):
    sentiment_scores = {}
    for i, intensity in enumerate(intensity_list):
        if intensity > 0.5:
            sentiment_scores[i] = intensity * 1.5
        else:
            sentiment_scores[i] = intensity * 0.8
    return sentiment_scores

intensity_values = [0.3, 0.7, 0.6, 0.2, 0.9]
scores = analyze_sentiment(intensity_values)

feedback_map = {k: v * 2 for k, v in scores.items()}

user_weights = [1, 3, 2, 1, 4]
temp_offset = 0
for idx, (key, val) in enumerate(zip(feedback_map.keys(), feedback_map.values())):
    temp_offset += (idx + 1) * val

baseline = sum(user_weights) / len(user_weights)
adjusted_feedback = set()
for key, value in feedback_map.items():
    if value >= 0.8:
        adjusted_feedback.add(key)

# Misleading computation with dead-end logic
shadow_score = 0
for k in feedback_map:
    if k % 2 == 0:
        shadow_score += feedback_map[k] * 0.1  # Not used later

irrelevant_tracker = []
for w in user_weights:
    irrelevant_tracker.append(w ** 0.5)  # Dead code path

# Core aggregation logic
rolling_sum = 0
weight_sum = 0
for idx, weight in enumerate(user_weights):
    if idx in adjusted_feedback:
        rolling_sum += feedback_map[idx] * weight
        weight_sum += weight

final_score = rolling_sum / weight_sum if weight_sum != 0 else 0

# Print final result as required
print(f"Result: {final_score}")