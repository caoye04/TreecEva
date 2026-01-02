from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
timestamps = [100, 101, 102, 103, 104, 105, 106]
raw_readings = [23.4, 24.1, 23.9, 24.1, 25.0, 23.4, 26.2]
statuses = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'OK', 'ERROR']

# Misleading auxiliary data (distractor)
dummy_weights = [0.1, 0.2, 0.3, 0.4, 0.5]
weight_sum = sum(dummy_weights)  # Irrelevant computation

# Track occurrences of each reading for anomaly detection
duplicate_tracker = Counter(raw_readings)

# Group data by status (some irrelevant grouping)
grouped_by_status = defaultdict(list)
for i, status in enumerate(statuses):
    grouped_by_status[status].append((timestamps[i], raw_readings[i]))

# Extract only 'OK' readings
ok_timestamps = []
ok_readings = []
for ts, val, stat in zip(timestamps, raw_readings, statuses):
    if stat == 'OK':
        ok_timestamps.append(ts)
        ok_readings.append(val)

# Compute moving average over valid window (relevant preprocessing)
window_size = 3
smoothed_values = []
for i in range(len(ok_readings) - window_size + 1):
    window_avg = sum(ok_readings[i:i+window_size]) / window_size
    smoothed_values.append(round(window_avg, 2))

# Identify repeated values in original data (semi-relevant analysis)
frequent_readings = [v for v, cnt in duplicate_tracker.items() if cnt > 1]

# Simulate confidence adjustment based on repetition
confidence_map = {}
for val in raw_readings:
    if val in frequent_readings:
        confidence_map[val] = 1.1  # Boost for duplicates
    else:
        confidence_map[val] = 0.9  # Reduce otherwise

# Apply confidence weighting to original data (not used later — red herring)
weighted_readings = [val * confidence_map[val] for val in raw_readings]

# Process only the smoothed values for final scoring
adjusted_smoothed = [val * 1.05 if val > 24.0 else val * 0.95 for val in smoothed_values]

# Calculate baseline trend using integer arithmetic
baseline_trend = 0
for i in range(1, len(adjusted_smoothed)):
    baseline_trend += int(adjusted_smoothed[i] - adjusted_smoothed[i-1])

# Normalize trend to avoid overflow (dummy protection)
normalized_trend = max(-100, min(100, baseline_trend))

# Secondary distraction: simulate checksum validation (unused)
checksum = 0
for idx, val in enumerate(ok_readings):
    checksum += int(val) * (idx + 1)
checksum %= 1000

# Critical processing function
def calculate_final_score(data_segment):
    score = 0
    # data_segment is adjusted_smoothed
    for x in data_segment:
        if x > 24.5:
            score += int(x // 2)
        elif x > 23.5:
            score += round(x)
        else:
            score -= 1
    # Bonus for positive trend
    if normalized_trend > 0:  # Uses outer scope variable
        score += 5
    return score

# Final assignment
processed_data = adjusted_smoothed
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")