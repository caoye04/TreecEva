import math

# Simulate sensor readings with noise
data_points = [12.4, 15.6, 9.8, 18.2, 14.3, 21.5, 13.7, 16.8, 10.1, 17.4]

# Baseline calibration offset (irrelevant to final result, minor distraction)
calibration_factor = 0.98
adjusted_data = [x * calibration_factor for x in data_points]

# Compute moving average for smoothing
window_size = 3
smoothed_data = []
for i in range(len(adjusted_data) - window_size + 1):
    window_avg = sum(adjusted_data[i:i+window_size]) / window_size
    smoothed_data.append(round(window_avg, 2))

# Filter valid operational range (focus on this logic path)
valid_range_min, valid_range_max = 12.0, 18.0
filtered_data = [x for x in smoothed_data if valid_range_min <= x <= valid_range_max]

# Determine outlier threshold as median of filtered data
sorted_filtered = sorted(filtered_data)
mid = len(sorted_filtered) // 2
if len(sorted_filtered) % 2 == 0:
    median_value = (sorted_filtered[mid-1] + sorted_filtered[mid]) / 2
else:
    median_value = sorted_filtered[mid]

outlier_threshold = median_value * 1.1

# Critical statement: count how many exceed the threshold
threshold_count = len([x for x in filtered_data if x > outlier_threshold])

print(f"Result: {threshold_count}")