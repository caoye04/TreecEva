# Data processing for sensor readings
sensor_data = [3.5, -1.2, 4.7, -0.8, 2.9, 5.1, -2.3, 3.0]
temperature_threshold = 0.0

# Process the data with enumeration
filtered_indices = [i for i, value in enumerate(sensor_data) if value > temperature_threshold]

# Create a list of tuples with index and reading for valid readings
indexed_readings = list(zip(filtered_indices, [sensor_data[i] for i in filtered_indices]))

# Apply a calibration factor to valid readings
calibrated_data = [(idx, reading * 1.1) for idx, reading in indexed_readings]

# Filter data based on calibrated values
filtered_data = [data for data in calibrated_data if data[1] > 3.0]

# Count valid entries
valid_entries = len([entry for entry in filtered_data])

print(f"Result: {valid_entries}")