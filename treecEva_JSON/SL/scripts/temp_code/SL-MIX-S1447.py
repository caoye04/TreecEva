import math
from itertools import combinations
from statistics import mean, stdev

def validate_sensor_readings(readings, threshold=2.0):
    if len(readings) < 2:
        return readings
    reading_mean = mean(readings)
    reading_stdev = stdev(readings) if len(readings) > 1 else 0
    
    valid_readings = [
        r for r in readings 
        if reading_stdev == 0 or abs(r - reading_mean) <= threshold * reading_stdev
    ]
    return valid_readings if valid_readings else [reading_mean]

# Sensor data from 4 different sources
sensor_data = {
    'alpha': [95.2, 98.7, 102.1, 94.8, 150.3, 96.5],
    'beta': [101.3, 103.8, 100.2, 99.9, 102.7],
    'gamma': [89.5, 91.2, 90.8, 88.9, 92.1, 87.4, 95.6],
    'delta': [110.2, 112.8, 108.5, 109.3, 111.7, 175.4, 110.9]
}

# Process sensor readings
processed_signals = {}
for sensor_id, readings in sensor_data.items():
    processed_signals[sensor_id] = validate_sensor_readings(readings)

# Calculate sensor weights based on consistency (inverse of coefficient of variation)
sensor_weights = {}
for sensor_id, readings in processed_signals.items():
    if len(readings) > 1 and mean(readings) != 0:
        cv = stdev(readings) / abs(mean(readings))
        sensor_weights[sensor_id] = 1 / (1 + cv)  # Add 1 to avoid division by zero
    else:
        sensor_weights[sensor_id] = 1.0

# Compute weighted average for each sensor
weighted_averages = {}
for sensor_id in processed_signals:
    if processed_signals[sensor_id]:
        weighted_averages[sensor_id] = (
            mean(processed_signals[sensor_id]) * sensor_weights[sensor_id]
        )

# Calculate correlation-like metric between all sensor pairs
pairwise_similarities = []
for sensor_pair in combinations(weighted_averages.keys(), 2):
    s1, s2 = sensor_pair
    similarity = abs(weighted_averages[s1] - weighted_averages[s2])
    pairwise_similarities.append(similarity)

# Final aggregation score combines weighted averages and pairwise consistency
aggregation_base = sum(weighted_averages.values())
pairwise_consistency = sum(pairwise_similarities) / len(pairwise_similarities) if pairwise_similarities else 0
final_aggregation_score = aggregation_base * (1 - pairwise_consistency / 100) if pairwise_consistency != 0 else aggregation_base

print(f"Result: {final_aggregation_score}")