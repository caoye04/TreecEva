from collections import namedtuple

# Define a sensor reading structure
SensorReading = namedtuple('SensorReading', ['sensor_id', 'timestamp', 'values'])

# Simulated sensor data
sensor_data = [
    SensorReading('S1', 1001, [2.3, 4.1, 5.7]),
    SensorReading('S2', 1002, [1.8, 3.9, 6.2]),
    SensorReading('S3', 1003, [2.0, 4.0, 5.9])
]

# Base calibration map
base_calibration = {'S1': 1.05, 'S2': 0.98, 'S3': 1.02}

# Lambda for anomaly detection score
compute_anomaly = lambda x, mean: abs(x - mean) > 1.0

# Process data
adjusted_readings = {}
anomaly_flags = {}

for reading in sensor_data:
    calibrated_values = [v * base_calibration[reading.sensor_id] for v in reading.values]
    adjusted_readings[reading.sensor_id] = calibrated_values
    mean_val = sum(calibrated_values) / len(calibrated_values)
    flags = [compute_anomaly(val, mean_val) for val in calibrated_values]
    anomaly_flags[reading.sensor_id] = flags

# Merge results into summary
summary = {sid: {
    'average': sum(vals)/len(vals),
    'anomalies': sum(flags)
} for sid, vals, flags in zip(adjusted_readings.keys(), adjusted_readings.values(), anomaly_flags.values())}

# Calculate final anomaly score
anomaly_score = sum(
    entry['anomalies'] * entry['average']
    for entry in summary.values()
)

print(f'Result: {anomaly_score}')