from collections import defaultdict, Counter

# Simulated sensor readings over time (timestamp -> value)
sensor_data = [
    (1001, 45), (1002, 47), (1003, 46), (1004, 48), (1005, 50),
    (1006, 53), (1007, 52), (1008, 51), (1009, 49), (1010, 47)
]

# Irrelevant auxiliary data (distractor)
weather_log = [(t, (t % 7) * 2 + 20) for t in range(1000, 1020)]
temperature_bias = sum(w[1] for w in weather_log if w[0] < 1010) / 10

# Data structure initialization (relevant)
data_points = []
for ts, val in sensor_data:
    data_points.append(val)

# Compute moving average (red herring - not used later)
moving_avg = []
for i in range(2, len(data_points)):
    avg_val = (data_points[i-2] + data_points[i-1] + data_points[i]) / 3
    moving_avg.append(round(avg_val, 1))

# Count frequency of readings (partially relevant)
frequency_map = Counter(data_points)
mode_value = frequency_map.most_common(1)[0][0]  # Most frequent reading

# Define thresholds (engineering specs)
normal_range = range(45, 55)
warning_threshold = 54

# Flag anomalies (distractor computation)
anomalies = []
for ts, val in sensor_data:
    if val > warning_threshold:
        anomalies.append(ts)

# Compute stability index based on variance (irrelevant path)
mean_val = sum(data_points) / len(data_points)
variance = sum((x - mean_val) ** 2 for x in data_points) / len(data_points)
stability_index = round(100 / (1 + variance), 2) if variance > 0 else 100.0

# System mode classification (decoy function)
def classify_system_mode(temp):
    if temp < 46:
        return "IDLE"
    elif temp < 50:
        return "STABLE"
    else:
        return "ACTIVE"

# Apply classification to all points (unused result)
mode_assignments = [classify_system_mode(v) for v in data_points]

# Critical pipeline metrics (core logic)
valid_readings = [v for v in data_points if v in normal_range]
outlier_count = len(data_points) - len(valid_readings)
compliance_ratio = len(valid_readings) / len(data_points)

# Efficiency model: recursive smoothing filter (relevant)
def smooth_effectiveness(values, alpha=0.3):
    if len(values) == 1:
        return values[0]
    return alpha * values[-1] + (1 - alpha) * smooth_effectiveness(values[:-1], alpha)

process_efficiency = int(smooth_effectiveness(valid_readings))

# Secondary metric: peak utilization (distractor)
peak_utilization = max(data_points) - min(data_points)

# Key calculation embedded in distractions
filtration_score = process_efficiency * compliance_ratio

# Irrelevant formatting and logging
log_entry = " | ".join(f"{k}:{v}" for k, v in frequency_map.items() if v > 1)
summary_tag = f"MODE:{mode_value},ANOMALIES:{len(anomalies)}"

# Final output (must print target result)
print(f"Result: {filtration_score}")