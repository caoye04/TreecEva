import math
from functools import reduce

def compute_segment_energy(segment):
    valid_readings = [x for x in segment if x > 0]
    log_transformed = [math.log(x) for x in valid_readings]
    return sum(log_transformed) if log_transformed else 0

def aggregate_energy(readings):
    n = len(readings)
    return (
        compute_segment_energy(readings) if n <= 3
        else aggregate_energy(readings[:n//2]) + aggregate_energy(readings[n//2:])
    )

sensor_data = [1.0, 2.718, 0, 7.389, -1.5, 20.086, 0.5, 0, 1.0]
raw_energy = aggregate_energy(sensor_data)
total_valid_count = len([x for x in sensor_data if x > 0])
normalized_energy = raw_energy / total_valid_count if total_valid_count else 0

print(f"Result: {round(normalized_energy, 3)}")