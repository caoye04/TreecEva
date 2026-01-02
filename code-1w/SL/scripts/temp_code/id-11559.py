from itertools import combinations

# Simulate sensor readings from a thermal monitoring system
temperature_readings = [23.4, 24.1, 25.0, 24.8, 26.3, 27.1, 25.9, 24.7]

# Auxiliary analysis: detect abnormal fluctuation pairs
fluctuation_pairs = []
for i in range(len(temperature_readings) - 1):
    diff = abs(temperature_readings[i+1] - temperature_readings[i])
    if diff > 1.0:
        fluctuation_pairs.append((i, i+1, diff))

# Misleading computation: unused trend direction analysis
increasing_trends = 0
decreasing_trends = 0
for j in range(len(temperature_readings) - 1):
    if temperature_readings[j+1] > temperature_readings[j]:
        increasing_trends += 1
    elif temperature_readings[j+1] < temperature_readings[j]:
        decreasing_trends += 1

# Generate all possible triplets to check for rare thermal patterns (not actually used)
rare_triplets = list(combinations(temperature_readings, 3))
valid_triplets_count = 0
for triplet in rare_triplets:
    if max(triplet) - min(triplet) > 2.5:
        valid_triplets_count += 1

# Real signal processing path
smoothed_avg = sum(temperature_readings[1:-1]) / len(temperature_readings[1:-1])  # Exclude edges
base_score = int(smoothed_avg * 10)

# Anomaly detection based on fluctuation magnitude
anomaly_count = len(fluctuation_pairs)
anomaly_offset = 0
if anomaly_count == 0:
    anomaly_offset = 0
elif anomaly_count <= 2:
    anomaly_offset = -5
else:
    anomaly_offset = -10

# Introduce distractor state tracking (irrelevant to final result)
current_state = 'STABLE'
if anomaly_count > 1:
    current_state = 'MONITORING'
if base_score > 250:
    current_state = 'WARNING'

# Final diagnostic calculation — critical execution point
final_diagnostic = base_score + anomaly_offset

print(f"Result: {final_diagnostic}")