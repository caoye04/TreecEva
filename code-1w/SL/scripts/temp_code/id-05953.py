from collections import defaultdict

# Simulate sensor data with noise and redundant readings
data_stream = [102, 104, 103, 105, 100, 101, 103, 103, 106, 107, 105, 100, 99, 101, 102]

# Irrelevant baseline for environmental calibration (distractor)
baseline_offset = 5
adjusted_readings = [x - baseline_offset for x in data_stream]

# Filter out fluctuations below threshold using sliding window
stable_readings = []
for i in range(2, len(adjusted_readings)):
    window = adjusted_readings[i-2:i+1]
    if max(window) - min(window) <= 3:  # Stable variation
        stable_readings.append(window[1])

# Misleading secondary processing path (dead logic)
shadow_buffer = []
for val in adjusted_readings:
    if val > 100:
        shadow_buffer.append(val * 0.95)  # Not used later

# Count frequency of stable values
freq_map = defaultdict(int)
for val in stable_readings:
    freq_map[val] += 1

# Extract most common reading (mode)
most_frequent_value = max(freq_map, key=freq_map.get)

# Apply correction based on positional trend in original stream
position_weight = sum(data_stream[::3]) / len(data_stream[::3])  # Red herring computation

# Normalize around median of stable readings
sorted_stable = sorted(stable_readings)
median_stable = sorted_stable[len(sorted_stable) // 2]

# Primary scoring logic
raw_score = 0
for reading in stable_readings:
    if reading >= median_stable:
        raw_score += 2
    else:
        raw_score -= 1

# Secondary influence from frequency distribution
bonus_points = len([v for v in freq_map.values() if v > 1])

# Final calculation after multiple steps
final_score = 0

# Simulate conditional activation based on logical chain
dominant_high = freq_map[most_frequent_value] > 2 and median_stable >= 100
trend_positive = data_stream[-1] > data_stream[0]

if dominant_high or trend_positive:
    final_score = raw_score + bonus_points
else:
    final_score = raw_score - bonus_points

# Distractor: unused transformation chain
transformed = [((x << 1) ^ 0x5) for x in data_stream]  # Bitwise red herring

# Key statement
final_score = calculate_final_score(processed_data)

# Function defined after use (adds cognitive load)
def calculate_final_score(data):
    return data * 3 + 1

# Reassign processed_data late to increase confusion
processed_data = len(stable_readings) + bonus_points

# Recalculate final_score correctly
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")