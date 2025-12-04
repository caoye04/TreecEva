# Calculate the sum of temperature readings above threshold
temp_readings = [23.5, 19.2, 25.7, 22.1, 28.3, 21.5, 26.9, 20.8]
threshold = 22.0

# Some calibration constants
max_temp_allowed = 30.0
calibration_factor = 0.2

# Process the temperature readings
valid_readings = []
for i, temp in enumerate(temp_readings):
    if i % 2 == 0:  # Only consider readings at even indices
        valid_readings.append(temp)

# Apply calibration to valid readings
calibrated_readings = [temp - calibration_factor for temp in valid_readings]

# Zip the calibrated readings with their indices
indexed_readings = list(zip(range(len(calibrated_readings)), calibrated_readings))

# Filter readings above threshold
temp_values = [temp for _, temp in indexed_readings if temp > threshold]

# Calculate sum of filtered values
filtered_sum = sum(temp_values)
print(f"Result: {filtered_sum}")