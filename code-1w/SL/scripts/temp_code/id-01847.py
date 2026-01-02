from collections import defaultdict
import math

def calculate_total(deviations, scale):
    base = 0
    for key in deviations:
        if key.endswith('_err'):
            base += abs(deviations[key]) * scale
    return math.ceil(base)

# Sensor data with error flags
deviation_map = defaultdict(float)
deviation_map['temp_err'] = -3.4
deviation_map['pressure_err'] = 2.1
deviation_map['humidity'] = 1.8  # not an error channel
deviation_map['vibration_err'] = -1.9

def normalize_readings(data):
    total = sum(abs(v) for v in data.values())
    factor = 1.0 if total == 0 else 10.0 / total
    return {k: v * factor for k, v in data.items()}

scaling_factor = len(normalize_readings(deviation_map)) * 0.5

final_score = calculate_total(deviation_map, scaling_factor)
print(f"Result: {final_score}")