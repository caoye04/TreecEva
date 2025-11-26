from collections import Counter

# Process sensor data validation with bitwise operations
def validate_sensor_readings(readings):
    valid_mask = 0
    for reading in readings:
        # Check if reading is within valid range (0-255)
        if 0 <= reading <= 255:
            # Set corresponding bit in mask
            valid_mask |= (1 << (reading % 8))
    return valid_mask

# Main data processing
sensor_data = [45, 128, 300, 67, 89, 128, 45, 200, 15, 89, 300, 128, 67]
temperature_threshold = 100

# Process readings and get valid mask
mask_result = validate_sensor_readings(sensor_data)

# Count unique valid readings (distraction - not used in final calculation)
reading_counter = Counter(sensor_data)
unique_readings = len(reading_counter)

# Filter and process valid temperature data
valid_temps = [temp for temp in sensor_data if temp <= temperature_threshold and temp >= 0]
unique_valid = len(set(valid_temps))

# Apply bitwise operations for data encoding
divisor_mask = (mask_result & 0b111) + 2  # Extract lower 3 bits and add 2

# Calculate final result
final_count = unique_valid // divisor_mask

# Distraction calculations (not affecting final result)
temp_sum = sum(valid_temps)
avg_temp = temp_sum / len(valid_temps) if valid_temps else 0

print(f"Target result: {final_count}")