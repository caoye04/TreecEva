# Processing sensor data segments
sensor_readings = [45, 67, 23, 89, 34, 12, 78, 56]
data_buffer = 15

# Extract middle readings using slicing
middle_segment = sensor_readings[2:6]

# Calculate sum of extracted segment
extracted_sum = sum(middle_segment)

# Add buffer value to final result
final_result = extracted_sum + data_buffer

# Display final processed result
print(f"Result: {final_result}")