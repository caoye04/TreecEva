import hashlib
import math

def compute_weighted_average(readings, factors, reliabilities):
    adjusted = [r * f for r, f in zip(readings, factors)]
    valid_data = [(a, r) for a, r in zip(adjusted, reliabilities) if abs(a - sum(adjusted)/len(adjusted)) < 2*max(adjusted)]
    if not valid_data:
        return 0
    total_weighted_sum = sum(value * weight for value, weight in valid_data)
    total_weights = sum(weight for _, weight in valid_data)
    return total_weighted_sum / total_weights if total_weights != 0 else 0

sensor_readings = [23.5, 25.1, 22.8, 24.3, 26.7]
calibration_factors = [1.02, 0.98, 1.05, 0.99, 1.01]
sensor_reliabilities = [0.9, 0.85, 0.95, 0.88, 0.92]

weighted_avg_temp = compute_weighted_average(sensor_readings, calibration_factors, sensor_reliabilities)

# Compute a stability index based on hash of the readings and the weighted average
readings_str = ''.join(map(str, sensor_readings))
hash_digest = hashlib.sha256(readings_str.encode()).hexdigest()
ascii_sum = sum(ord(c) for c in hash_digest[:10])

final_temperature_index = 0
if weighted_avg_temp > 24.0:
    final_temperature_index = ascii_sum * math.log(weighted_avg_temp)
else:
    final_temperature_index = ascii_sum / (weighted_avg_temp + 1e-5)  # Avoid division by zero

print(f"Result: {final_temperature_index}")