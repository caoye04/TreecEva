from functools import reduce

def process_telemetry(readings):
    processed_values = []
    
    # State machine for processing
    for sensor_id, value in readings:
        if sensor_id % 2 == 0:  # Even sensor ID
            processed_values.append(value ** 2)
        else:  # Odd sensor ID
            processed_values.append(abs(value))
    
    # Sorting in descending order
    sorted_values = sorted(processed_values, reverse=True)
    
    # Compute product of top 3 values
    top_three = sorted_values[:3]
    final_product = reduce(lambda x, y: x * y, top_three, 1)
    
    return final_product

# Telemetry data: list of (sensor_id, value) tuples
sensor_readings = [
    (1, -5),
    (2, 3),
    (3, -7),
    (4, 4),
    (5, -2),
    (6, -6)
]

final_product = process_telemetry(sensor_readings)
print(f"Result: {final_product}")