# Sensor data processing for environmental monitoring system
# Each reading contains signal and noise components

sensor_readings = [523, 489, 612, 397, 550]
temperature_offsets = [2.1, 1.5, 3.0, 0.5, 2.2]

# Find the maximum reading and its index
max_reading = 0
max_index = 0

for i, reading in enumerate(sensor_readings):
    if reading > max_reading:
        max_reading = reading
        max_index = i

# Apply calibration to all readings
calibrated_readings = []
for reading, offset in zip(sensor_readings, temperature_offsets):
    calibrated_readings.append(reading - offset * 10)

# Extract the lower 8 bits as the signal strength
# This removes environmental noise in higher bits
signal_strength = sensor_readings[max_index] & 0xFF

# Calculate average of calibrated readings
average_calibrated = sum(calibrated_readings) / len(calibrated_readings)

print(f"Result: {signal_strength}")