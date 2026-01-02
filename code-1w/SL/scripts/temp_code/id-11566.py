from collections import defaultdict, Counter

# Simulated sensor readings over time with some noise
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
raw_readings = [23.1, 24.5, 24.5, 25.9, 23.1, 27.3, 24.5, 29.0]

# Misleading auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
label_mapping = {lbl: idx for idx, lbl in enumerate(dummy_labels)}

# Data grouping by value frequency (relevant)
frequency_map = Counter(raw_readings)

# Secondary processing: group timestamps by reading value
reading_to_times = defaultdict(list)
for t, val in zip(timestamps, raw_readings):
    reading_to_times[val].append(t)

# Extract unique values and sort them (semi-relevant)
sorted_unique_readings = sorted(set(raw_readings))

# Compute moving average of sorted values (distractor)
moving_avg = []
for i in range(1, len(sorted_unique_readings)-1):
    avg_val = (sorted_unique_readings[i-1] + sorted_unique_readings[i] + sorted_unique_readings[i+1]) / 3
    moving_avg.append(avg_val)

# Identify most frequent reading (relevant)
most_frequent_reading = frequency_map.most_common(1)[0][0]

# Find all timestamps where this reading occurred
frequent_times = reading_to_times[most_frequent_reading]

# Compute time gap statistics (semi-relevant)
time_gaps = [frequent_times[i] - frequent_times[i-1] for i in range(1, len(frequent_times))]
if time_gaps:
    avg_gap = sum(time_gaps) / len(time_gaps)
else:
    avg_gap = 0

# Normalize gaps against first occurrence (distractor)
normalized_offsets = [t - frequent_times[0] for t in frequent_times]

# Weighted contribution based on frequency and temporal clustering
frequency_weight = frequency_map[most_frequent_reading]
clustering_bonus = 10 if avg_gap < 2 else 5

# Dummy transformation chain (distractor)
intermediate_key = 0
for label in dummy_labels[:frequency_weight]:
    intermediate_key ^= label_mapping[label]

# Final processing pipeline
processed_data = {
    'base_value': most_frequent_reading * 10,
    'bonus': clustering_bonus,
    'penalty': len(normalized_offsets) if max(normalized_offsets, default=0) > 5 else 0
}

# Core calculation function
def calculate_final_score(data):
    score = data['base_value'] + data['bonus']
    if data['penalty'] > 0:
        score -= data['penalty'] * 2
    return int(score)

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")