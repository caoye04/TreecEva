from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, 23.5), (101, 24.1), (103, 22.9), (105, 25.3), (106, 24.8),
    (107, 23.0), (108, 22.1), (110, 26.5), (111, 25.9), (112, 27.1)
]

# Misleading auxiliary data (distractor)
external_noise_floor = [21.2, 22.0, 20.8, 23.1, 24.4]
baseline_offset = sum([x * 0.1 for x in external_noise_floor])  # Unused distraction

# Process raw data into time-windowed bins
def bin_sensor_data(data, window_size=5):
    binned = defaultdict(list)
    for ts, val in data:
        bucket = ts // window_size
        binned[bucket].append(val)
    return binned

binned_data = bin_sensor_data(timestamped_readings)

# Apply filtering: only keep bins with more than one reading
filtered_bins = {k: v for k, v in binned_data.items() if len(v) > 1}

# Compute moving average per bin (relevant)
smoothed_values = []
for bucket, values in filtered_bins.items():
    avg = sum(values) / len(values)
    smoothed_values.append(round(avg, 2))

# Secondary processing: detect upward trends (consecutive increases)
trend_counter = 0
for i in range(1, len(smoothed_values)):
    if smoothed_values[i] > smoothed_values[i-1]:
        trend_counter += 1

# Misleading transformation chain (dead computation path)
shadow_copy = smoothed_values[:]
for _ in range(2):
    shadow_copy = [x * 0.95 + 1.2 for x in shadow_copy]  # No effect on result

# Core logic: score based on trend stability and central tendency
mean_smoothed = sum(smoothed_values) / len(smoothed_values)
median_index = len(smoothed_values) // 2
median_smoothed = sorted(smoothed_values)[median_index]
deviation_penalty = sum(abs(x - mean_smoothed) for x in smoothed_values)

# Calculate final score using multiple factors
def calculate_final_score(data):
    base_score = sum(data)
    adjustment = len(data) * trend_counter  # Uses external state (trend_counter)
    penalty = int(deviation_penalty)  # Static at this point
    return int(base_score + adjustment - penalty)

final_score = calculate_final_score(processed_data=smoothed_values)

# Print result as required
print(f"Result: {final_score}")