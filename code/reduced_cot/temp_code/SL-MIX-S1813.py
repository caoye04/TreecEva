import math
from collections import deque
from dataclasses import dataclass
from typing import List

def binary_search_closest(arr, target):
    left, right = 0, len(arr) - 1
    closest = arr[0]
    while left <= right:
        mid = (left + right) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return closest

class SensorStateMachine:
    def __init__(self):
        self.state = 'INIT'
        self.correction_factor = 1.0
    
    def process(self, reading):
        if self.state == 'INIT':
            self.correction_factor = math.log(reading + 1)
            self.state = 'CALIBRATED'
            return reading * self.correction_factor
        elif self.state == 'CALIBRATED':
            corrected = reading * self.correction_factor
            if corrected > 100:
                self.state = 'SATURATED'
            return corrected
        else:  # SATURATED
            return reading * 0.95

def compute_weighted_average(values, weights):
    if not values or not weights or len(values) != len(weights):
        return 0
    total_weight = sum(weights)
    if total_weight == 0:
        return 0
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight

# Sensor readings from 4 different locations
sensor_data = [
    [23.5, 24.1, 22.8, 25.3, 26.0],
    [18.2, 19.0, 17.5, 20.1, 19.8],
    [30.1, 31.2, 29.8, 32.5, 30.9],
    [15.7, 16.3, 14.9, 17.2, 16.8]
]

# Initialize state machines for each sensor
state_machines = [SensorStateMachine() for _ in range(len(sensor_data))]

# Process sensor readings through state machines
processed_readings = []
for i, readings in enumerate(sensor_data):
    sensor_processed = []
    for reading in readings:
        corrected_reading = state_machines[i].process(reading)
        sensor_processed.append(corrected_reading)
    processed_readings.append(sensor_processed)

# Apply logarithmic normalization
normalized_readings = []
for sensor_readings in processed_readings:
    normalized_sensor = [math.log(r + 1) for r in sensor_readings]
    normalized_readings.append(normalized_sensor)

# Compute exponential weights based on variance
weights = []
for sensor_readings in normalized_readings:
    mean = sum(sensor_readings) / len(sensor_readings)
    variance = sum((r - mean) ** 2 for r in sensor_readings) / len(sensor_readings)
    weight = math.exp(-variance)  # Lower variance -> higher weight
    weights.append(weight)

# Divide and conquer aggregation
def aggregate_readings(readings_list, weight_list):
    if len(readings_list) == 1:
        return readings_list[0]
    mid = len(readings_list) // 2
    left_avg = [sum(sensor) / len(sensor) for sensor in readings_list[:mid]]
    right_avg = [sum(sensor) / len(sensor) for sensor in readings_list[mid:]]
    left_weights = weight_list[:mid]
    right_weights = weight_list[mid:]
    
    left_result = compute_weighted_average(left_avg, left_weights)
    right_result = compute_weighted_average(right_avg, right_weights)
    
    # Combine results with additional weighting
    combined_weight = sum(left_weights) + sum(right_weights)
    if combined_weight == 0:
        return 0
    return (left_result * sum(left_weights) + right_result * sum(right_weights)) / combined_weight

# Flatten normalized readings for final processing
flattened_normalized = []
for sensor_readings in normalized_readings:
    flattened_normalized.extend(sensor_readings)

# Find representative value using binary search on sorted readings
sorted_readings = sorted(flattened_normalized)
mean_reading = sum(flattened_normalized) / len(flattened_normalized)
representative_value = binary_search_closest(sorted_readings, mean_reading)

# Final aggregation with representative value adjustment
sensor_averages = [sum(sensor) / len(sensor) for sensor in normalized_readings]
adjusted_averages = [avg * (representative_value / mean_reading) for avg in sensor_averages]

final_aggregate = compute_weighted_average(adjusted_averages, weights)
print(f"Result: {final_aggregate}")