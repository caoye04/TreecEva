import math

# Simulated sensor data and calibration values
data_points = [12, 15, 22, 34, 37, 41, 44, 50, 55, 60, 63, 70]
calibration_factor = 0.92
threshold = 35
adjustment_rate = 0.05

# Irrelevant baseline metrics (distractor)
baseline_avg = sum(data_points) / len(data_points)
variance_estimate = sum((x - baseline_avg) ** 2 for x in data_points) / len(data_points)
noise_floor = math.sqrt(variance_estimate) * 0.1

# Signal filtering: select points above threshold and adjust with calibration
filtered_data = [x for x in data_points if x > threshold]
adjusted_data = [x * calibration_factor for x in filtered_data]

# Secondary processing: detect rising trends (consecutive increases)
trend_changes = []
for i in range(1, len(adjusted_data)):
    if adjusted_data[i] > adjusted_data[i-1]:
        trend_changes.append(1)
    elif adjusted_data[i] < adjusted_data[i-1]:
        trend_changes.append(-1)
    else:
        trend_changes.append(0)

# Misleading intermediate calculation (dead path - distractor)
stability_score = 0
if len(trend_changes) > 0:
    stability_score = trend_changes.count(0) / len(trend_changes)
else:
    stability_score = 1.0

# Real processing: accumulate only rising segments
rising_segments_total = sum(1 for x in trend_changes if x == 1)

# Additional irrelevant transformation (distractor)
transformed_rising = [math.log(x + 2) for x in range(rising_segments_total)]
decay_weights = [0.9 ** i for i in range(len(transformed_rising))]
weighted_transform = sum(a * b for a, b in zip(transformed_rising, decay_weights))

# Core logic: final output depends on count of rising segments and base adjustment
base_accumulator = 0
for val in adjusted_data:
    if val > 40:
        base_accumulator += int(val // 3)  # Integer division contribution

# Final computation combining key elements
final_output = base_accumulator + rising_segments_total * 2

print(f"Result: {final_output}")