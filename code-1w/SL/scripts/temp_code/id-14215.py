from collections import defaultdict
import itertools

# Simulate sensor data with noise and metadata
data = [
    {'sensor': 'A', 'value': 12, 'status': 'ok'},
    {'sensor': 'B', 'value': 8, 'status': 'ok'},
    {'sensor': 'A', 'value': 15, 'status': 'ok'},
    {'sensor': 'C', 'value': 6, 'status': 'error'},
    {'sensor': 'B', 'value': 7, 'status': 'ok'},
    {'sensor': 'A', 'value': 11, 'status': 'ok'},
]

weights = {'A': 0.5, 'B': 0.3, 'C': 0.2}

# Misleading variables (distractors)
total_readings = len(data)
dropped_sensors = []
redundant_sum = 0

# Aggregation using defaultdict for cleaner grouping
sensor_values = defaultdict(list)
sensor_status_count = defaultdict(int)

for entry in data:
    sensor_id = entry['sensor']
    sensor_values[sensor_id].append(entry['value'])
    sensor_status_count[entry['status']] += 1

# Compute averages, ignoring sensors with 'error' status
averages = {}
for sensor, values in sensor_values.items():
    if sensor_status_count.get('error', 0) == 0 or sensor != 'C':  # Only exclude C if errors exist
        averages[sensor] = sum(values) / len(values)

# Additional distraction: process combinations of sensors (not used in final score)
sensor_pairs = list(itertools.combinations(sensor_values.keys(), 2))
pair_deltas = []
for a, b in sensor_pairs:
    if a in averages and b in averages:
        pair_deltas.append(abs(averages[a] - averages[b]))

# Dead code path (never executed due to data)
peak_value = -float('inf')
if False:  # Simulated condition that never triggers
    for v in sensor_values.values():
        peak_value = max(peak_value, max(v))

# Weighted score calculation (core logic)
def calculate_final_score(data_dict, weight_dict):
    score = 0.0
    count = 0
    for sensor, avg in averages.items():
        if sensor in weight_dict:
            score += avg * weight_dict[sensor]
            count += 1
    # Normalize by total weight contribution
    total_weight = sum(weight_dict[s] for s in averages.keys() if s in weight_dict)
    return score / total_weight if total_weight else 0

# Final computation
final_score = calculate_final_score(sensor_values, weights)

# Irrelevant string processing (distraction)
log_message = "Processing complete"
char_count = {c: log_message.count(c) for c in set(log_message)}

# Output result
print(f"Result: {final_score}")