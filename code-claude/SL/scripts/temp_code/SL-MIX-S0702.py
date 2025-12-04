# Sensor Network Status Analyzer

def check_connection_quality(signal):
    # Higher values indicate better connection
    noise_factor = signal % 3
    return signal > 75 - noise_factor

# Sensor readings (temperature in celsius)
temperature_readings = [22.5, 23.1, 21.8, 24.0, 22.7, 23.5, 21.9]

# Process readings with calibration factor
calibration = 0.2
calibrated_temps = [temp + calibration for temp in temperature_readings]

# Network signal strength for each sensor (percentage)
signal_strength = [82, 67, 91, 45, 88, 76, 59]

# Analyze which sensors are online based on signal strength
sensor_status = [check_connection_quality(signal) for signal in signal_strength]

# Calculate average temperature from functioning sensors only
valid_readings = []
for i, is_online in enumerate(sensor_status):
    connection_descriptor = "strong" if signal_strength[i] > 80 else "moderate" if signal_strength[i] > 60 else "weak"
    if is_online:
        valid_readings.append(calibrated_temps[i])

# Count sensors with temperature above threshold
threshold = 23.0
warm_sensors = 0
for temp in valid_readings:
    if temp > threshold:
        warm_sensors += 1

# Determine how many sensors are active in the network
active_sensors = sum(is_active for is_active in sensor_status if is_active)

# Calculate efficiency ratio (unused in final result)
efficiency = len(valid_readings) / len(temperature_readings) if temperature_readings else 0

print(f"Result: {active_sensors}")