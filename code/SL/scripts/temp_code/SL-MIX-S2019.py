from functools import reduce
from itertools import combinations

def state_machine_processor(data_stream):
    state = 'INIT'
    accumulator = 0
    for value in data_stream:
        if state == 'INIT':
            if value > 0:
                state = 'POSITIVE_MODE'
                accumulator += value
            else:
                state = 'NEGATIVE_MODE'
                accumulator -= value
        elif state == 'POSITIVE_MODE':
            if value < 0:
                state = 'NEGATIVE_MODE'
                accumulator += value * 2
            else:
                accumulator += value
        elif state == 'NEGATIVE_MODE':
            if value > 0:
                state = 'POSITIVE_MODE'
                accumulator -= value
            else:
                accumulator -= value // 2
    return accumulator

def divide_and_conquer_aggregation(regional_data):
    if len(regional_data) <= 1:
        return regional_data[0] if regional_data else 0
    mid = len(regional_data) // 2
    left_result = divide_and_conquer_aggregation(regional_data[:mid])
    right_result = divide_and_conquer_aggregation(regional_data[mid:])
    return left_result + right_result + (left_result & right_result)

# Sensor data from different climate regions
sensor_readings = {
    'arctic': [-5, -3, 2, -1, 4],
    'tropical': [3, 5, -2, 6, -4],
    'temperate': [1, -2, 3, -4, 5],
    'desert': [7, -3, 2, -1, 3]
}

# Process each region's sensor data through state machine
processed_regions = {region: state_machine_processor(readings) for region, readings in sensor_readings.items()}

# Apply divide and conquer aggregation on processed values
regional_values = list(processed_regions.values())
regional_aggregate = divide_and_conquer_aggregation(regional_values)

print(f"Result: {regional_aggregate}")