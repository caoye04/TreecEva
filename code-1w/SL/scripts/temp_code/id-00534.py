from collections import defaultdict, Counter

# Simulated sensor readings over time with noise and redundant data
timestamps = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
sensor_a_readings = [23.5, 24.1, 23.9, 24.0, 24.2, 24.5, 25.0, 25.1, 25.3, 25.6]
sensor_b_readings = [22.8, 23.0, 23.9, 24.1, 24.2, 24.6, 24.9, 25.2, 25.4, 25.5]

# Irrelevant auxiliary data (distractor)
redundant_checksums = [sum(sensor_a_readings[:i]) for i in range(1, len(sensor_a_readings))]
placeholder_flags = [x % 2 == 0 for x in range(len(timestamps))]

# Data aggregation using defaultdict (relevant)
data_by_category = defaultdict(list)
for t, a, b in zip(timestamps, sensor_a_readings, sensor_b_readings):
    category = 'high' if a > 24.0 else 'low'
    data_by_category[category].append((t, a, b))

# Extract high-threshold events (relevant)
high_events = data_by_category['high']

# Compute rolling average of sensor A (semi-relevant, used later)
rolling_avg_a = []
window_size = 3
for i in range(len(sensor_a_readings) - window_size + 1):
    window = sensor_a_readings[i:i+window_size]
    rolling_avg_a.append(sum(window) / window_size)

# Misleading trend analysis on sensor B (distractor)
trend_directions = []
for i in range(1, len(sensor_b_readings)):
    if sensor_b_readings[i] > sensor_b_readings[i-1]:
        trend_directions.append(1)
    elif sensor_b_readings[i] < sensor_b_readings[i-1]:
        trend_directions.append(-1)
    else:
        trend_directions.append(0)

# Count transitions in trend (distractor)
trend_changes = 0
for i in range(1, len(trend_directions)):
    if trend_directions[i] != trend_directions[i-1]:
        trend_changes += 1

# Process valid events: extract timestamps and compute adjusted values (relevant)
adjusted_values = []
for event in high_events:
    ts, a_val, b_val = event
    adjustment_factor = 0.95 if ts % 2 == 0 else 1.05
    adjusted = (a_val + b_val) / 2 * adjustment_factor
    adjusted_values.append(adjusted)

# Use Counter to count occurrence of rounded values (relevant)
rounded_count = Counter([round(val) for val in adjusted_values])

# Calculate base score from frequency of most common reading (relevant)
most_common_value, frequency = rounded_count.most_common(1)[0]
base_score = frequency * 100

# Secondary metric: variance in adjusted values (semi-relevant)
mean_adj = sum(adjusted_values) / len(adjusted_values)
variance = sum((x - mean_adj) ** 2 for x in adjusted_values) / len(adjusted_values)
penalty = int(variance * 10)

# Helper function to simulate calibration adjustment (relevant)
def apply_calibration_offset(raw_list, offset=1.5):
    return [x + offset for x in raw_list]

calibrated_adjusted = apply_calibration_offset(adjusted_values)

# Another distractor: analyze gaps between timestamps
timestamp_gaps = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
gap_counter = Counter(timestamp_gaps)
common_gap, gap_freq = gap_counter.most_common(1)[0]

# Final processing step
processed_data = {
    'base': base_score,
    'penalty': penalty,
    'size': len(calibrated_adjusted),
    'offset': 5,
    'extra_flag': False
}

# Critical computation
def calculate_final_score(data):
    score = data['base'] - data['penalty']
    size_factor = data['size'] * data['offset']
    if data['extra_flag']:
        size_factor *= 2
    score += size_factor
    return score

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")