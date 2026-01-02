def calculate_efficiency(data, limit):
    filtered = [x for x in data if x > limit]
    outliers = [x for x in data if x < limit * 0.1]  # Distractor: not used later
    adjusted = [x * 1.1 for x in filtered]
    avg = sum(adjusted) / len(adjusted) if adjusted else 0
    variance_proxy = sum((x - avg) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0
    compression_ratio = len(data) / len(filtered) if filtered else 0  # Semi-relevant but unused
    efficiency = avg / (variance_proxy + 1)
    return efficiency

# Simulate sensor readings
data_points = [15, 23, 18, 92, 76, 44, 61, 88, 34, 52, 29, 77]

# Preprocessing: extract every third reading and scale
scaled_readings = [x * 0.85 for x in data_points[::3]]

# Noise reduction pass (irrelevant to final result)
smoothed = []
for i in range(len(scaled_readings)):
    left = max(0, i - 1)
    right = min(i + 2, len(scaled_readings))
    window_avg = sum(scaled_readings[left:right]) / (right - left)
    smoothed.append(window_avg)

# Key processing pipeline
baseline = sum(data_points) / len(data_points)
threshold = baseline * 0.6
processed_data = [x * 1.2 for x in data_points if x >= threshold]

# Red herring computation: system health
health_metrics = []
for val in data_points:
    if val > 80:
        health_metrics.append('HIGH')
    elif val > 50:
        health_metrics.append('MODERATE')
    else:
        health_metrics.append('LOW')

# Actual target calculation
efficiency_score = calculate_efficiency(processed_data, threshold)

# Final unrelated transformation (dead path)
temp_output = [round(x * 0.9) for x in processed_data if x > 70]

print(f"Result: {efficiency_score}")