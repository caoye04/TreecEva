import math
from functools import wraps

def sensor_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.calls += 1
        wrapper.total += result
        return result
    wrapper.calls = 0
    wrapper.total = 0
    return wrapper

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

@sensor_tracker
def process_sensor_reading(reading, position):
    if position % 2 == 0:
        return reading * math.log(position + 1)
    else:
        return reading * math.sin(position)

# Sensor network configuration
sensor_positions = list(fibonacci_sequence(8))[1:]  # Skip first zero
sensor_readings = [10, 15, 20, 25, 30, 35, 40]

# Process sensor data
processed_data = [
    process_sensor_reading(reading, pos) 
    for reading, pos in zip(sensor_readings, sensor_positions)
]

# Calculate statistical metrics
mean_value = sum(processed_data) / len(processed_data)
variance_components = [(x - mean_value)**2 for x in processed_data]
variance = sum(variance_components) / len(variance_components)

# Apply matrix transformation
transformation_matrix = [[1, 0.5], [0.5, 1]]
vector_to_transform = [mean_value, variance]
transformed_vector = [
    sum(transformation_matrix[i][j] * vector_to_transform[j] for j in range(2))
    for i in range(2)
]

# Final metric calculation
final_metric = int(transformed_vector[0] * transformed_vector[1])
print(f"Result: {final_metric}")