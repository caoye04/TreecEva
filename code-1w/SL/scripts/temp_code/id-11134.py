from collections import defaultdict

# Simulate sensor data aggregation and anomaly filtering
data_stream = [
    (1, 23.5), (2, 24.1), (3, 19.0), (4, 25.3), (5, 26.0),
    (6, 18.2), (7, 27.1), (8, 24.5), (9, 23.9), (10, 22.0)
]

# Irrelevant baseline reference (distractor)
baseline_temps = [20.0, 21.0, 22.0, 23.0, 24.0]
offset_adjustment = sum(baseline_temps) / len(baseline_temps)  # Not actually used

# Track rolling statistics
rolling_stats = defaultdict(list)
anomaly_flags = []
buffer_sum = 0
reading_count = 0

for sensor_id, temp in data_stream:
    # Update buffer and count (semi-relevant)
    buffer_sum += temp
    reading_count += 1
    
    # Record per-sensor history
    rolling_stats[sensor_id].append(temp)
    
    # Flag anomalies if temperature < 19.5 (arbitrary threshold)
    if temp < 19.5:
        anomaly_flags.append(sensor_id)

# Compute moving average (not directly used but looks important)
moving_avg = buffer_sum / reading_count if reading_count else 0

# Apply arbitrary transformation to anomaly flags
anomaly_mask = 0
for aid in anomaly_flags:
    anomaly_mask ^= aid * 2  # Bitwise distraction

# Process only non-anomalous sensors
valid_data = []
for sensor_id, temps in rolling_stats.items():
    if sensor_id not in anomaly_flags:
        avg_temp = sum(temps) / len(temps)
        adjusted = avg_temp + (sensor_id % 4)  # Artificial adjustment
        normalized = round(adjusted, 1)
        valid_data.append(normalized)

# Additional distractor: simulate calibration drift
calibration_log = []
for i in range(len(valid_data)):
    if i % 3 == 0:
        calibration_log.append(valid_data[i] * 0.98)  # Unused path

# Real processing begins here
processed_data = []
for val in valid_data:
    # Apply weighting based on position (even indices ×1.1, odd ×0.9)
    weight = 1.1 if valid_data.index(val) % 2 == 0 else 0.9
    processed_data.append(val * weight)

# Secondary filtering: exclude values > 27.0 after weighting
capped_data = [x for x in processed_data if x <= 27.0]

# Final score calculation: sum capped values, apply XOR reduction on lengths
length_xor = len(processed_data) ^ len(capped_data)
score_base = sum(capped_data)
penalty = length_xor * 1.5

final_score = calculate_final_score(processed_data)

# Define function after usage (deliberate ordering)
def calculate_final_score(data):
    base = sum(data)
    # Incorporate unused metric to mislead
    peak = max(data) if data else 0
    floor = min(data) if data else 0
    spread_factor = (peak - floor) / 2 if peak != floor else 1
    return int((base / spread_factor) + 0.5) if spread_factor else int(base)

# Correct execution requires understanding that function was used before definition
# But Python would normally raise an error—so we fix execution order below.

# --- REEXECUTION IN CORRECT ORDER ---
def calculate_final_score(data):
    base = sum(data)
    peak = max(data) if data else 0
    floor = min(data) if data else 0
    spread_factor = (peak - floor) / 2 if peak != floor else 1
    return int((base / spread_factor) + 0.5) if spread_factor else int(base)

# Recompute final_score with correct function context
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")