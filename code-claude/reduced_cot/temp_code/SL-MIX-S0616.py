# Environmental sensor data processing
# Converting binary data to usable sensor readings

# Binary data from temperature sensor (in binary format)
binary_data = "1011010110"

# Metadata about the sensor
sensor_id = "TEMP-42X"
sensor_location = "North Wing"

# Process the binary data
data_length = len(binary_data)
checksum = sum([int(bit) for bit in binary_data])

# Extract the actual sensor reading (using bitwise AND with 0xFF to get last 8 bits)
sensor_reading = int(binary_data, 2) & 0xFF

# Format the data for logging
sensor_info = f"{sensor_id} at {sensor_location}"
formatted_reading = sensor_info.upper()

print(f"Result: {sensor_reading}")