import math

def process_sensor_data(readings, decay_factor):
    # Generate weights using exponential decay
    weights = [(lambda x: math.exp(-decay_factor * i))(i) for i in range(len(readings))]
    
    # Normalize weights so they sum to 1
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Calculate weighted sum using generator expression
    weighted_sum = sum(r * w for r, w in zip(readings, normalized_weights))
    
    # Apply final transformation
    final_output = int(round(weighted_sum * 10))
    return final_output

# Sensor readings from a monitoring system
sensor_readings = [4, 7, 2, 9, 1, 5]
decay = 0.5

final_output = process_sensor_data(sensor_readings, decay)
print(f'Result: {final_output}')