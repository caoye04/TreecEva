sensor_readings = [0.8, 1.2, -0.5, 3.1, 2.7, -1.3, 4.4, 0.0, 1.9]
valid_range = (0.0, 3.0)

# Normalize negative readings
corrected_readings = [max(0, reading) for reading in sensor_readings]

# Filter readings within operational range
filtered_readings = [val for val in corrected_readings if valid_range[0] < val <= valid_range[1]]

# Discard low-confidence values below threshold
effective_readings = [val for val in filtered_readings if val >= 0.7]

filtration_score = sum(effective_readings)
print(f"Result: {filtration_score}")