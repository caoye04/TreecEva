import re
from collections import defaultdict
from statistics import mean, variance
temperature_readings = ['22.5', '23.1', '22.8', 'error', '23.0', '22.9', '23.2', '22.7', '23.1', 'sensor-fault', '22.6', '23.3', '22.8', '23.0', '22.9']
sensor_data = [float(x) for x in temperature_readings if re.match(r'^\d+\.\d+$', x)]
baseline_mean = mean(sensor_data)
baseline_variance = variance(sensor_data)
threshhold = baseline_mean * 0.02 + baseline_variance * 0.5
anomaly_scores = {temp: abs(temp - baseline_mean) for temp in sensor_data}
high_anomalies = {k: v for k, v in anomaly_scores.items() if v > threshhold}
anomaly_count = len(high_anomalies)
valid_readings = sorted([x for x in sensor_data if x not in high_anomalies], reverse=True)
if len(valid_readings) > 10:
    trimmed_data = valid_readings[2:-2]
    adjusted_mean = mean(trimmed_data)
    if adjusted_mean > baseline_mean:
        anomaly_count += 1
print(f'Result: {anomaly_count}')