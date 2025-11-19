from collections import deque
import statistics

def smooth_readings(temperatures):
    smoothed = []
    n = len(temperatures)
    for i in range(n):
        window = [temperatures[i]]
        if i > 0:
            window.append(temperatures[i-1])
        if i < n-1:
            window.append(temperatures[i+1])
        smoothed.append(statistics.median(window))
    return smoothed

def compute_deviation_sums(values):
    deviations = []
    for i in range(len(values)):
        start = max(0, i-1)
        end = min(len(values), i+2)
        window_vals = values[start:end]
        avg = sum(window_vals) / len(window_vals)
        sq_dev_sum = sum((x - avg)**2 for x in window_vals)
        deviations.append(sq_dev_sum)
    return deviations

def count_anomalies(deviations, threshold=10):
    return sum(1 for d in deviations if d > threshold)

# Sensor data
sensor_data = [
    [22, 24, 23, 25, 24, 26],
    [20, 21, 22, 21, 20, 19],
    [25, 27, 26, 28, 27, 29]
]

# Process each sensor's data
processed_signals = []
for signal in sensor_data:
    smoothed = smooth_readings(signal)
    deviations = compute_deviation_sums(smoothed)
    processed_signals.extend(deviations)

# Count total anomalies
anomaly_count = count_anomalies(processed_signals)
print(f"Result: {anomaly_count}")