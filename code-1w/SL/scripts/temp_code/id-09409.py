from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
timestamps = [101, 102, 103, 104, 105, 106, 107]
raw_readings = [23.1, 24.5, 24.5, 25.0, 23.1, 26.3, 25.0]

# Misleading auxiliary data (distractor)
redundant_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
duplicate_map = {label: ts for label, ts in zip(redundant_labels, timestamps)}

# Organize readings by value frequency
reading_frequency = Counter(raw_readings)

# Group timestamps by reading values
inverted_index = defaultdict(list)
for t, r in zip(timestamps, raw_readings):
    inverted_index[r].append(t)

# Compute statistical baseline (not used later - red herring)
mean_reading = sum(raw_readings) / len(raw_readings)
variance_proxy = sum((r - mean_reading) ** 2 for r in raw_readings)

# Identify recurring readings (appearing more than once)
stable_readings = [r for r, count in reading_frequency.items() if count > 1]

# Extract first occurrence timestamp for each unique reading
first_occurrences = {r: min(ts_list) for r, ts_list in inverted_index.items()}

# Performance metric: sum of timestamps corresponding to stable (repeated) readings
activation_times = []
for reading in stable_readings:
    activation_times.append(first_occurrences[reading])

# Secondary filtering: only consider activations before median timestamp
timestamp_median = sorted(timestamps)[len(timestamps) // 2]
filtered_activations = [t for t in activation_times if t < timestamp_median]

# Bonus logic: if any stable reading equals the initial reading, add offset
initial_reading = raw_readings[0]
bonus_awarded = initial_reading in stable_readings
offset_value = 10 if bonus_awarded else 0

# Core calculation function
def calculate_performance(data):
    base_score = sum(filtered_activations)
    adjustment = len(stable_readings) * 5
    # Complex conditional expression combining multiple factors
    penalty = 7 if len(filtered_activations) < 3 else (3 if bonus_awarded else 5)
    return base_score + adjustment - penalty + offset_value

# Final computation
calibration_data = list(zip(timestamps, raw_readings))
benchmark_data = {
    'readings': raw_readings,
    'timestamps': timestamps,
    'meta': duplicate_map
}

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")