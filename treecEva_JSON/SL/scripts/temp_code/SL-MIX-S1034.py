import numpy as np
from collections import defaultdict

temperature_readings = [
    [23.5, 24.1, 22.8, 25.0],
    [21.2, 22.0, 20.9, 23.3],
    [25.8, 26.4, 24.7, 27.1]
]

calibration_factors = {
    0: np.array([[1.02, 0.01], [0.01, 1.03]]),
    1: np.array([[1.01, 0.02], [0.02, 1.02]]),
    2: np.array([[1.03, 0.01], [0.01, 1.04]])
}

sensor_weights = {0: 0.4, 1: 0.35, 2: 0.25}
variance_thresholds = {0: 1.5, 1: 1.2, 2: 1.8}

adjusted_data = defaultdict(list)

for sensor_id, readings in enumerate(temperature_readings):
    matrix = calibration_factors[sensor_id]
    for i in range(0, len(readings)-1, 2):
        vector = np.array([readings[i], readings[i+1]])
        adjusted_vector = matrix @ vector
        adjusted_data[sensor_id].extend(adjusted_vector.tolist())

aggregated_readings = {}
for sensor_id in adjusted_data:
    values = adjusted_data[sensor_id]
    mean_val = sum(values) / len(values)
    squared_diffs = [(x - mean_val) ** 2 for x in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    if variance > variance_thresholds[sensor_id]:
        aggregated_readings[sensor_id] = mean_val * sensor_weights[sensor_id]
    else:
        aggregated_readings[sensor_id] = mean_val * sensor_weights[sensor_id] * 1.1

stability_index = sum(aggregated_readings.values())
print(f"Result: {stability_index}")