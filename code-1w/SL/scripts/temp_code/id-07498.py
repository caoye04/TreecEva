from itertools import compress

# Sensor data filtering based on environmental thresholds
temperatures = [22.1, 19.5, 24.3, 18.0, 23.7, 20.2, 25.1, 17.9]
humidity_levels = [45, 60, 52, 68, 58, 54, 49, 71]

# Determine stable conditions: moderate temperature and balanced humidity
stable_temp = [30 > t > 18 for t in temperatures]
balanced_humidity = [65 >= h >= 45 for h in humidity_levels]

# Identify sensors meeting both criteria
valid_sensors = list(compress(temperatures, (a and b for a, b in zip(stable_temp, balanced_humidity))))

# Compute derived quality score as squared deviation from ideal (22°C)
quality_deviation = [(t - 22) ** 2 for t in valid_sensors]
qualifying_scores = [100 - score for score in quality_deviation]

# Apply final thresholding
if len(qualifying_scores) > 3:
    threshold_score = min(qualifying_scores)
else:
    threshold_score = sum(qualifying_scores)

print(f"Result: {threshold_score}")