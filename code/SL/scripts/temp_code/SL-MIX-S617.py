from functools import reduce
import math

def validate_reading(temp):
    return -40.0 <= temp <= 50.0

def is_outlier(temp, avg, std_dev):
    return abs(temp - avg) > 2 * std_dev

def compute_std_dev(temps, avg):
    variance = sum((t - avg) ** 2 for t in temps) / len(temps)
    return math.sqrt(variance)

sensor_readings = {
    'sensor_a': [22.5, 23.1, 22.8, 99.0, 23.0],
    'sensor_b': [21.0, 21.5, -999, 22.0, 21.8],
    'sensor_c': [23.3, 23.5, 23.4, 23.6, 23.2]
}

valid_data = {sensor: list(filter(validate_reading, readings)) for sensor, readings in sensor_readings.items()}
all_valid_temps = reduce(lambda x, y: x + y, valid_data.values(), [])
average_temp = sum(all_valid_temps) / len(all_valid_temps) if all_valid_temps else 0.0
std_dev = compute_std_dev(all_valid_temps, average_temp)

filtered_data = {
    sensor: [t for t in temps if not is_outlier(t, average_temp, std_dev)]
    for sensor, temps in valid_data.items()
}

adjusted_averages = {
    sensor: (sum(temps) / len(temps)) + 0.5 if temps else 0.0
    for sensor, temps in filtered_data.items()
}

# Final adjustment factor computation
base_factor = 1.2 if average_temp > 22.0 else 0.8
outlier_count = sum(len(readings) - len(filtered_data.get(sensor, [])) for sensor, readings in valid_data.items())
final_adjustment_factor = base_factor * (1.0 + outlier_count * 0.05) if outlier_count > 0 else base_factor

print(f"Result: {final_adjustment_factor}")