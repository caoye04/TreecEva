from functools import reduce
from collections import namedtuple
import math

def is_valid_reading(value):
    return value > 0 and not math.isnan(value)

def normalize_signal(value):
    return math.log(value + 1)

def compute_threshold_index(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 0:
        return (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
    else:
        return sorted_values[n//2]

# Underwater acoustic sensor readings matrix (rows=sensors, columns=time series)
SensorData = namedtuple('SensorData', ['sensor_id', 'readings'])
sensor_array = [
    SensorData('HYDRO_01', [0.5, 1.2, -0.3, 2.1, float('nan'), 3.4]),
    SensorData('HYDRO_02', [1.0, float('nan'), 2.5, 0, 4.2, 1.8]),
    SensorData('HYDRO_03', [-1.5, 2.3, 3.1, 0.9, 5.5, float('nan')]),
    SensorData('HYDRO_04', [0, 1.1, 2.2, 3.3, 4.4, 5.5])
]

# Stage 1: Filter valid readings from all sensors
valid_readings_matrix = [
    list(filter(is_valid_reading, sensor.readings))
    for sensor in sensor_array
]

# Stage 2: Normalize valid readings
normalized_matrix = [
    list(map(normalize_signal, readings))
    for readings in valid_readings_matrix
]

# Stage 3: Compute threshold for each sensor's normalized readings
thresholds = list(map(compute_threshold_index, normalized_matrix))

# Stage 4: Count signals above threshold for each sensor
signals_above_threshold = [
    len(list(filter(lambda x: x > thresholds[i], normalized_matrix[i])))
    for i in range(len(normalized_matrix))
]

# Final stage: Aggregate count using divide and conquer approach
def aggregate_counts(counts):
    if len(counts) == 1:
        return counts[0]
    mid = len(counts) // 2
    left_sum = aggregate_counts(counts[:mid])
    right_sum = aggregate_counts(counts[mid:])
    return left_sum + right_sum

processed_signals_count = aggregate_counts(signals_above_threshold)
print(f"Result: {processed_signals_count}")