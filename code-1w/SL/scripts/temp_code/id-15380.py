from collections import defaultdict

# Simulate sensor data with some noise
data = [10, 15, 20, 25, 30]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]

# Irrelevant tracking variables (distractors)
running_avg = 0
sample_count = len(data)
total_sum = sum(data)
noise_floor = 5

# Misleading preprocessing (not used in final calculation)
adjusted_data = [x - noise_floor for x in data if x > noise_floor]
baseline_correction = sum(adjusted_data) / len(adjusted_data) if adjusted_data else 0

# Auxiliary function that appears important but has limited impact
compute_deviation = lambda vals, mean: sum((v - mean) ** 2 for v in vals) / len(vals) if vals else 0
deviation = compute_deviation(data, total_sum / sample_count)

# Weighted aggregation using dictionary-based mapping (relevant part)
weight_map = defaultdict(float)
for i, w in enumerate(weights):
    weight_map[i] = w

# Simulated confidence scaling (partially relevant)
confidence_factor = 1.0
if deviation < 50:
    confidence_factor += 0.1

intermediate_scores = []
for i, val in enumerate(data):
    # Apply weight and normalize by sum of weights (correct weighted average)
    normalized_weight = weight_map[i] / sum(weights)
    intermediate_scores.append(val * normalized_weight)

# Another distraction: conditional logic that doesn't alter outcome
if len(intermediate_scores) > 3:
    temp_offset = 10
    temp_offset -= 10  # Neutralized

# Final score computation (this is the key step)
def calculate_final_score(values, wts):
    weighted_sum = sum(v * w for v, w in zip(values, wts))
    scaling = 1 + (deviation / 100)  # Minor correction based on spread
    return weighted_sum / scaling

final_score = calculate_final_score(data, weights)

# Print result for evaluation
target_result: {final_score}