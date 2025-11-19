from collections import defaultdict
import math

def celsius_conversion(temp, unit):
    if unit == 'F':
        return (temp - 32) * 5/9
    elif unit == 'K':
        return temp - 273.15
    else:
        return temp

def get_quality_factor(score):
    match score:
        case s if s >= 90:
            return 1.0
        case s if s >= 75:
            return 0.8
        case s if s >= 60:
            return 0.5
        case _:
            return 0.0

# Sensor data: (temperature, unit, reliability_score)
sensor_readings = [
    (78, 'F', 82),
    (300, 'K', 95),
    (22.5, 'C', 68),
    (95, 'F', 45),
    (295, 'K', 88)
]

# Process sensor data
normalized_temps = []
reliability_weights = []

for temp, unit, score in sensor_readings:
    celsius_temp = celsius_conversion(temp, unit)
    quality_factor = get_quality_factor(score)
    
    # Only include readings with non-zero quality factor
    if quality_factor > 0:
        normalized_temps.append(celsius_temp)
        reliability_weights.append(quality_factor)

# Calculate weighted average
weighted_sum = sum(temp * weight for temp, weight in zip(normalized_temps, reliability_weights))
total_weight = sum(reliability_weights)

final_weighted_average_temperature = weighted_sum / total_weight if total_weight > 0 else 0

print(f"Result: {final_weighted_average_temperature}")