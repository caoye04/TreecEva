import statistics

temperature_readings = [22.5, 23.1, 21.8, 24.0, 22.9, 23.3, 21.7, 24.2, 22.6, 23.0]
encoding_keys = [0x1F, 0x2A, 0x3B, 0x4C, 0x5D]

# Encode temperature readings
encoded_readings = []
for i, temp in enumerate(temperature_readings):
    key = encoding_keys[i % len(encoding_keys)]
    encoded_value = int(temp * 10) ^ key
    encoded_readings.append(encoded_value)

# Calculate mean and standard deviation of encoded readings
mean_encoded = statistics.mean(encoded_readings)
std_dev_encoded = statistics.stdev(encoded_readings)

# Detect anomalies (values more than 1.5 standard deviations from the mean)
anomalies = [x for x in encoded_readings if abs(x - mean_encoded) > 1.5 * std_dev_encoded]

# Calculate anomaly score as the mean of anomalies if any, otherwise 0
anomaly_score = statistics.mean(anomalies) if anomalies else 0

print(f"Result: {anomaly_score}")