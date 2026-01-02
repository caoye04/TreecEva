from collections import Counter, defaultdict

# Simulate sensor readings with noise and valid signals
data_stream = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8, 9, 10]
noise_filter = {3, 7}  # These values are known noise artifacts
filtered_data = [x for x in data_stream if x not in noise_filter]

data_counter = Counter(filtered_data)

# Misleading auxiliary tracking (distractor)
event_log = defaultdict(list)
total_events = 0
for val in data_stream:
    event_log[val].append(total_events)
    total_events += 1

# Auxiliary statistic - not used in final score but looks relevant
mode_count = max(data_counter.values())
mean_value = sum(filtered_data) / len(filtered_data)
median_index = len(filtered_data) // 2
sorted_unique = sorted(data_counter.keys())
median_value = sorted_unique[median_index] if len(sorted_unique) % 2 == 1 else (sorted_unique[median_index-1] + sorted_unique[median_index]) / 2

# Threshold logic based on distribution properties
dominant_values = [k for k, v in data_counter.items() if v >= mode_count * 0.75]
threshold = sum(dominant_values) // len(dominant_values) if dominant_values else 0

# Secondary distractor: simulate historical comparison
historical_baseline = Counter([1, 2, 2, 4, 4, 4, 4, 5, 5, 8, 9])
drift_score = 0
for key in historical_baseline:
    drift_score += abs(data_counter.get(key, 0) - historical_baseline[key])
drift_score *= 0.5  # Normalize

# Core scoring logic
overlap_sum = sum(data_counter[k] for k in dominant_values if k in historical_baseline)
penalty = len([k for k in data_counter if k > threshold])

# Final computation using only specific derived values
def calculate_final_score(counter, thresh):
    raw = sum(v for k, v in counter.items() if k <= thresh)
    bonus = len([k for k in counter if k == thresh])
    return raw + bonus * 2

final_score = calculate_final_score(data_counter, threshold)

# Irrelevant transformation chain (dead path)
transformed = [x**2 for x in filtered_data]
normalized = [x / (max(transformed) + 1e-5) for x in transformed]
scaled_sum = sum(normalized)

print(f"Result: {final_score}")