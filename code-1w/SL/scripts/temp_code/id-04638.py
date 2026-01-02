from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
raw_readings = [23.5, 24.1, 23.9, 25.2, 26.0, 25.8, 26.1, 26.3]

# Misleading auxiliary data (distractor)
phantom_sensors = ['P1', 'P2', 'P3']
ghost_data = {sensor: [0] * 5 for sensor in phantom_sensors}

# Process real data
sensor_data = list(zip(timestamps, raw_readings))
processed_data = []
baseline = raw_readings[0]
fluctuation_sum = 0.0
reading_count = 0

for ts, val in sensor_data:
    deviation = val - baseline
    if abs(deviation) > 0.5:  # Significant change
        processed_data.append((ts, val, deviation))
        fluctuation_sum += abs(deviation)
        reading_count += 1
    baseline = val  # Adaptive baseline

# Red herring computation on ghost data (dead path)
for k in ghost_data:
    for i in range(len(ghost_data[k])):
        ghost_data[k][i] += i * 0.1  # Irrelevant update

# Extract features for scoring
trend_segments = len(processed_data)
amplitude_avg = fluctuation_sum / reading_count if reading_count else 0

# Secondary distractor: character counting in synthetic labels
label_pool = ['A', 'B', 'C']
total_chars = sum(len(label) for label in label_pool)  # Useless but plausible

# Scoring logic
score_component_1 = trend_segments * 10
score_component_2 = int(amplitude_avg * 4)

# Simulated linear search for latest anomaly (actually just gets last index)
latest_anomaly_idx = -1
for i in range(len(processed_data)):
    latest_anomaly_idx = i  # Overwrites each time, ends as last index

offset_bonus = 5 if latest_anomaly_idx > 2 else 2

# Final calculation
final_score = calculate_final_score(processed_data)

# Helper function defined after use (slight confusion)
def calculate_final_score(data):
    size_factor = len(data) * 7
    sum_of_deviations = sum(abs(dev) for _, _, dev in data)
    adjustment = 3.1416 if sum_of_deviations > 5.0 else 1.0
    return size_factor + int(sum_of_deviations) + adjustment

# Print result
Result: {final_score}