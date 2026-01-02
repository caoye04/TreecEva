from collections import defaultdict
import math

# Simulate sensor data with noise and valid readings
data = [104, 98, 102, 110, 95, 108, 103, 99, 101, 107]
weights = [0.1, 0.15, 0.2, 0.05, 0.1, 0.08, 0.12, 0.07, 0.06, 0.07]

# Irrelevant counters for distraction
loop_counter = 0
valid_readings_count = 0
noise_threshold_alerts = 0

# Distractor: mapping irrelevant categories
status_map = defaultdict(lambda: 'unknown')
for i in range(10):
    if i % 3 == 0:
        status_map[i] = 'critical'
    elif i % 3 == 1:
        status_map[i] = 'monitor'
    else:
        status_map[i] = 'normal'

# Noise filtering (distraction: complex but unused)
filtered_data = []
for val in data:
    if abs(val - 100) > 15:
        noise_threshold_alerts += 1
    else:
        filtered_data.append(val)

# Unused transformation via lambda
transform = lambda x: (x ** 2 + 1) / 100
transformed_data = [transform(x) for x in data if x > 97]

# Real computation begins: normalize data around baseline
baseline_adjusted = [x - 100 for x in data]

# Compute weighted deviation score
weighted_deviation = 0.0
for i in range(len(baseline_adjusted)):
    contribution = abs(baseline_adjusted[i]) * weights[i]
    weighted_deviation += contribution

# Secondary adjustment based on trend consistency
increasing_trend = 0
for i in range(1, len(baseline_adjusted)):
    if baseline_adjusted[i] > baseline_adjusted[i-1]:
        increasing_trend += 1

# Distractor: unused statistical measure
deviation_squared_sum = sum([x**2 for x in baseline_adjusted])
mean_deviation = sum(baseline_adjusted) / len(baseline_adjusted)

# Real logic: trend bonus affects final score
if increasing_trend >= 5:
    trend_bonus = 10
else:
    trend_bonus = 3

# Final aggregation using dictionary-based weight classification
weight_classes = {}
for i, w in enumerate(weights):
    if w > 0.1:
        weight_classes[i] = 'high'
    elif w > 0.05:
        weight_classes[i] = 'medium'
    else:
        weight_classes[i] = 'low'

high_weight_sum = sum(abs(baseline_adjusted[i]) for i, wc in weight_classes.items() if wc == 'high')

# Core formula: weighted deviation scaled by high-weight influence and trend bonus
effective_factor = (high_weight_sum / (weighted_deviation + 1))
final_score = int(weighted_deviation * effective_factor + trend_bonus)

# Print result as required
print(f"Result: {final_score}")