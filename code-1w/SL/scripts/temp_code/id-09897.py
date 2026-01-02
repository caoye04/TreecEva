def analyze_component(x, threshold=5.0):
    if x < threshold:
        return x * 1.8 + 2.3
    else:
        return x * 0.9 - 1.1

# Simulate system benchmark results with noise filtering
test_data = [4.2, 6.7, 3.1, 8.9, 5.0, 7.4]
filtered_data = [x for x in test_data if x >= 4.0]  # Ignore low-level noise

scaling_factor = 1.5
adjusted_values = []
for val in filtered_data:
    temp_adjusted = val * scaling_factor
    if temp_adjusted > 10.0:
        temp_adjusted = 10.0  # Cap at maximum sensitivity
    adjusted_values.append(temp_adjusted)

# Secondary validation pass
calibration_offset = 0.7
validated_scores = []
for v in adjusted_values:
    raw_score = analyze_component(v)
    validated_scores.append(raw_score + calibration_offset)

# Compute composite metrics (distractor computations below)
total_interactions = len(validated_scores)
avg_interaction_level = sum(validated_scores) / total_interactions
peak_response = max(validated_scores)
response_variance = sum((x - avg_interaction_level) ** 2 for x in validated_scores) / total_interactions

# Red herring: unused diagnostic trace
trace_log = []
for i, score in enumerate(validated_scores):
    trace_log.append(f"Step {i}: {score:.3f}")

# Weighted integration using decay factors (actual relevant logic)
decay_weights = [0.9**i for i in range(len(validated_scores))]
weighted_sum = sum(score * w for score, w in zip(validated_scores, decay_weights))
normalization_factor = sum(decay_weights)

# Final performance calculation
def calculate_performance(results):
    base = weighted_sum / normalization_factor
    penalty = 0.0
    if len(results) > 5:
        penalty = 0.4
    elif len(results) < 3:
        penalty = 0.6
    return base - penalty

# Key assignment point
final_score = calculate_performance(validated_scores)
print(f"Result: {final_score}")