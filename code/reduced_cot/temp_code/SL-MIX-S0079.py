from dataclasses import dataclass
from typing import List

def calibrate(factor: float):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator

@dataclass
class SensorReading:
    sensor_id: str
    strength: float

readings: List[SensorReading] = [
    SensorReading('S1', 42.7),
    SensorReading('S2', 18.3),
    SensorReading('S3', 73.1),
    SensorReading('S4', 29.9),
    SensorReading('S5', 55.5)
]

sorted_readings = sorted(readings, key=lambda x: x.strength)

@calibrate(1.2)
def get_median_strength(readings_list):
    n = len(readings_list)
    return readings_list[n//2].strength

calibrated_median_strength = get_median_strength(sorted_readings)
print(f'Result: {calibrated_median_strength}')