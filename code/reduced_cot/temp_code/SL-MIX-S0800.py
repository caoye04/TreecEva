import math
from collections import namedtuple

# Define sensor reading structure
SensorReading = namedtuple('SensorReading', ['sensor_id', 'temperature'])

# Simulated sensor data
sensor_data = [
    SensorReading('THERMAL_01', 23.7),
    SensorReading('THERMAL_02', 25.2),
    SensorReading('THERMAL_03', 22.1),
    SensorReading('THERMAL_04', 27.8),
    SensorReading('THERMAL_05', 24.9)
]

# Quality control thresholds
VALID_RANGE = (15.0, 35.0)
OUTLIER_THRESHOLD = 2.0

# Initialize processing variables
valid_readings = []
quality_flags = set()

# First pass: Validate readings and flag quality issues
for reading in sensor_data:
    if VALID_RANGE[0] <= reading.temperature <= VALID_RANGE[1]:
        valid_readings.append(reading)
        # Check for potential outlier based on distance from mean
        temp_deviation = abs(reading.temperature - sum(r.temperature for r in sensor_data) / len(sensor_data))
        if temp_deviation > OUTLIER_THRESHOLD:
            quality_flags.add(f"OUTLIER:{reading.sensor_id}")
    else:
        quality_flags.add(f"INVALID:{reading.sensor_id}")

# Second pass: Apply calibration and compute base metrics
calibrated_temps = [
    temp * 1.02 - 0.5 if temp > 25.0 else temp * 0.98 + 0.3
    for _, temp in valid_readings
]

# Compute statistical measures
mean_temp = sum(calibrated_temps) / len(calibrated_temps) if calibrated_temps else 0
variance = sum((t - mean_temp) ** 2 for t in calibrated_temps) / len(calibrated_temps) if calibrated_temps else 0
std_dev = math.sqrt(variance) if variance > 0 else 0

# Determine weighting factor based on data quality
weight_factor = 0.8 if len(quality_flags) <= 2 else 0.95 if len(quality_flags) <= 4 else 1.2

# Calculate normalized index using logarithmic scaling
raw_index = mean_temp * weight_factor
normalized_index = round(math.log(raw_index) * 100, 2) if raw_index > 0 else 0.0

print(f"Result: {normalized_index}")