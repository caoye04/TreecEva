from collections import defaultdict
from functools import reduce
import math

temperature_readings = [23.5, 25.1, 22.8, 24.3, 26.0]
sensor_weights = [0.15, 0.25, 0.20, 0.30, 0.10]
calibration_map = {0: 1.02, 1: 0.98, 2: 1.05, 3: 0.99, 4: 1.01}

adjusted_readings = []
for idx, temp in enumerate(temperature_readings):
    adjustment = calibration_map.get(idx, 1.0)
    calibrated_temp = temp * adjustment
    adjusted_readings.append(calibrated_temp)

weighted_temps = list(map(lambda pair: pair[0] * pair[1], zip(adjusted_readings, sensor_weights)))
total_weighted_sum = reduce(lambda x, y: x + y, weighted_temps)
total_weight = reduce(lambda x, y: x + y, sensor_weights)
base_average = total_weighted_sum / total_weight

sensor_variance = 0.0
for reading in adjusted_readings:
    sensor_variance += (reading - base_average) ** 2
sensor_variance /= len(adjusted_readings)

mode_flag = 2 if sensor_variance > 1.0 else 1 if sensor_variance > 0.5 else 0

final_adjustment_factor = 1.0
if mode_flag == 0:
    final_adjustment_factor = base_average * 0.95
elif mode_flag == 1:
    final_adjustment_factor = base_average * (1.0 + sensor_variance * 0.1)
else:
    final_adjustment_factor = base_average * (1.0 + sensor_variance * 0.15)

print(f"Result: {final_adjustment_factor}")