from math import log

# Sensor data calibration and noise filtering simulation
data_points = [12, 15, 22, 8, 37, 41, 9, 16, 24, 30]
threshold = 14
calibration_factor = 0.9

# Apply logarithmic correction to raw data
corrected_data = [round(log(x) * calibration_factor, 2) for x in data_points if x > threshold]

# Identify high-confidence readings above secondary threshold
high_confidence = set([x for x in corrected_data if x > 2.5])

# Filter original data based on high-confidence corrected values
filtered_indices = [i for i, x in enumerate(data_points) if log(x) * calibration_factor in high_confidence]
filtered_data = [data_points[i] for i in filtered_indices]

# Final aggregation
filtered_sum = sum(filtered_data)
print(f"Result: {filtered_sum}")