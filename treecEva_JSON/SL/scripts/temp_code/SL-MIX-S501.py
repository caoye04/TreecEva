from collections import defaultdict
import statistics

temperature_readings = [
    {'sensor_id': 'A', 'values': [23.5, 24.0, None, 25.1, 22.8]},
    {'sensor_id': 'B', 'values': [21.0, 21.5, 22.0, 21.8, None]},
    {'sensor_id': 'C', 'values': [None, 19.5, 20.0, 19.8, 20.2]}
]

sensor_valid_data = defaultdict(list)
quality_scores = {}

for reading in temperature_readings:
    sensor = reading['sensor_id']
    values = [v for v in reading['values'] if v is not None]
    sensor_valid_data[sensor].extend(values)
    
    # Short-circuit evaluation in quality check
    if len(values) > 0 and statistics.mean(values) > 20:
        base_score = len(values) * 10
        variance_bonus = 5 if statistics.variance(values) < 1 else 0
        quality_scores[sensor] = base_score + variance_bonus
    else:
        quality_scores[sensor] = 0

# Calculate system-wide metrics
all_valid_values = [v for values in sensor_valid_data.values() for v in values]
system_mean = statistics.mean(all_valid_values) if all_valid_values else 0

# Final score computation with lambda function
weight_function = lambda s: 1.5 if quality_scores[s] > 50 else 1.0
weighted_scores = [quality_scores[sensor] * weight_function(sensor) for sensor in quality_scores]

final_score = int(sum(weighted_scores) * system_mean / 10)
print(f"Result: {final_score}")