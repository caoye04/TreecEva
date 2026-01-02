from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant readings
data_stream = [
    (1, 23.5), (2, 24.1), (3, 22.9), (1, 23.7), (2, 24.0), (3, 23.0),
    (1, 23.6), (2, 24.2), (3, 23.1), (1, 23.4), (2, 24.3), (3, 23.2)
]

# Track average per sensor using defaultdict
temp_cache = defaultdict(list)
for sensor_id, temp in data_stream:
    temp_cache[sensor_id].append(temp)

averages = {}
for sensor_id, temps in temp_cache.items():
    averages[sensor_id] = sum(temps) / len(temps)

# Misleading: Calculate variance but never used later
variances = {}
for sensor_id, temps in temp_cache.items():
    mean = averages[sensor_id]
    variances[sensor_id] = sum((t - mean) ** 2 for t in temps) / len(temps)

# Apply correction factor based on calibration offset (simulated)
calibration_map = {1: -0.2, 2: +0.1, 3: -0.1}
corrected_averages = {}
for sid in averages:
    corrected_averages[sid] = averages[sid] + calibration_map[sid]

# Aggregate all corrected values into a flat list
all_corrected = []
for sid in sorted(corrected_averages.keys()):
    all_corrected.append(corrected_averages[sid])

# Compute rolling differences (not used in final result - distractor)
rolling_diffs = []
for i in range(1, len(all_corrected)):
    rolling_diffs.append(all_corrected[i] - all_corrected[i-1])

# Slice middle portion (irrelevant to outcome)
middle_slice = all_corrected[1:3] if len(all_corrected) > 2 else all_corrected

# Prepare frequency count of rounded values (semi-relevant)
rounded_vals = [round(v * 2) / 2 for v in all_corrected]  # Round to nearest 0.5
freq_count = Counter(rounded_vals)

# Extract base weights from frequency for scoring
weight_map = {v: freq_count[v] for v in freq_count}

# Simulate processing steps with intermediate transformations
processed_data = []
scaling_factor = 1.75
for val in corrected_averages.values():
    transformed = int((val + 10) * scaling_factor)
    processed_data.append(transformed ^ 3)  # Bitwise XOR as obfuscation

# Additional distraction: sort and reverse multiple times
processed_data.sort()
processed_data.reverse()
processed_data.sort(reverse=True)

# Another dead-end computation: cumulative XOR chain
cumulative_xor = 0
for x in processed_data:
    cumulative_xor ^= x

# Real logic hidden among distractions: sum processed values, then scale down
total_raw = sum(processed_data)
adjustment = len(processed_data) * 0.5
adjusted_total = total_raw - adjustment

# Final score derived from adjusted total modulated by number of sensors
num_sensors = len(corrected_averages)
final_score = int(adjusted_total // num_sensors)

# Irrelevant set operations (distractor)
unique_processed = set(processed_data)
duplicate_check = set([x for x in processed_data if processed_data.count(x) > 1])
overlap = unique_processed & duplicate_check  # Will be empty

# Output the required result
print(f"Result: {final_score}")