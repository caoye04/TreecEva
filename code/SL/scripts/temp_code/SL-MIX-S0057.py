from collections import deque

temperature_deviations = [1.2, -0.5, 0.8, -1.0, 2.3, -0.2, 1.7]
window_size = 3
weighted_readings = deque(maxlen=window_size)
total_weighted_sum = 0.0

for idx, deviation in enumerate(temperature_deviations):
    weighted_value = deviation * (idx + 1)
    weighted_readings.append(weighted_value)
    total_weighted_sum += weighted_value

smoothed_average_temperature = total_weighted_sum / len(weighted_readings)
print(f"Result: {smoothed_average_temperature}")