from collections import Counter

# Sensor data readings in millivolts from a biomedical device
readings = [120, 135, 120, 140, 135, 120, 150, 140, 135, 135, 120]

# Filter out values below threshold to remove noise
threshold = 125
filtered_readings = [v for v in readings if v >= threshold]

# Count frequency of each valid reading
frequency_count = Counter(filtered_readings)

# Identify the highest occurrence count
peak_frequency = max(frequency_count.values())

# Calculate average of high-frequency readings (appearing at least peak_frequency - 1 times)
dominant_values = [val for val, cnt in frequency_count.items() if cnt >= peak_frequency - 1]
average_dominant = sum(dominant_values) / len(dominant_values) if dominant_values else 0

# Output target result
print(f"Result: {peak_frequency}")