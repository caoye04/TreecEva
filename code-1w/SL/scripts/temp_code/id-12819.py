def calculate_checksum(data):
    checksum = 0
    for val in data:
        checksum ^= val  # XOR-based checksum
    return checksum

# Sensor data stream with noise
raw_sensor_data = [23, 45, 67, 12, 89, 34, 56, 78, 91, 103]

# Extract every second reading (even indices) to reduce noise
data_slice = raw_sensor_data[::2]  # Slicing: [23, 67, 89, 56, 91]

# Apply threshold filter to remove outliers above 90
filtered_data = [x for x in data_slice if x <= 90]

# Checksum of clean data
filtered_checksum = calculate_checksum(filtered_data)

# Irrelevant distraction: secondary calculation (minimal interference)
mean_value = sum(raw_sensor_data) / len(raw_sensor_data)
offset_correction = mean_value * 0.95

Result: filtered_checksum