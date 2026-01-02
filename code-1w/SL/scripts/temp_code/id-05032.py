def calculate_threshold(values):
    total = sum(values)
    count = len(values)
    return total / count if count > 0 else 0

# Sensor data from monitoring stations
readings = [23, 45, 67, 89, 12, 34, 56, 78, 91, 10, 42]

# Extract middle segment of data for stability analysis
start_idx = len(readings) // 3
end_idx = 2 * len(readings) // 3
median_slice = readings[start_idx:end_idx]

# Calculate dynamic threshold based on median segment
target_base = max(median_slice) - min(median_slice)
adjustment_factor = len(median_slice) % 7
temp_offset = target_base + adjustment_factor  # Irrelevant intermediate

threshold_score = calculate_threshold(median_slice)

# Output result
print(f"Result: {threshold_score}")