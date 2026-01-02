from collections import defaultdict
import itertools

# Simulate time-series sensor data for system load
timestamps = list(range(10))
data_stream = [12, 15, 15, 22, 22, 22, 18, 18, 25, 25]

# Group consecutive identical readings using itertools.groupby
grouped_readings = [list(group) for _, group in itertools.groupby(data_stream)]

duration_count = defaultdict(int)
for group in grouped_readings:
    duration_count[len(group)] += 1

# Calculate stability score using lambda function
stability_score = sum(map(lambda x: x ** 2, duration_count.values()))

# Determine dominant pattern length
max_duration = max(duration_count.keys())
frequent_stable_period = duration_count[max_duration]

# Analyze load pattern
monitored_data = []
for i, val in enumerate(data_stream):
    monitored_data.append((timestamps[i], val))

    # Early termination if threshold exceeded
    if val >= 25 and i >= 8:
        break

# Critical analysis function
def analyze_load_pattern(logged_data):
    load_peaks = [entry[1] for entry in logged_data if entry[1] > 20]
    if not load_peaks:
        return 0
    peak_load = max(load_peaks)
    normalization_factor = len(logged_data) / (len(load_peaks) or 1)
    adjusted_peak = peak_load * normalization_factor
    return int(adjusted_peak)

final_analysis = analyze_load_pattern(monitored_data)

# Additional unrelated metric (minor distraction)
total_transitions = sum(1 for i in range(1, len(data_stream)) if data_stream[i] != data_stream[i-1])

Result: final_analysis