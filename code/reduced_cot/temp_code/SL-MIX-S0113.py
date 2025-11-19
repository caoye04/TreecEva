import math
from functools import reduce

# Sensor network configuration
sensor_readings = [[2, 4, 6], [3, 5, 7], [1, 8, 9]]
weight_factors = [0.5, 1.5, 2.0]

# Lambda function for signal adjustment
adjust_signal = lambda base_value, weight: math.floor((base_value ** 2) * weight) & 0xFF

# Initialize accumulator for processed signal strength
processed_signal_strength = 0

# Process sensor readings across multiple time intervals
for interval_idx in range(len(sensor_readings)):
    interval_readings = sensor_readings[interval_idx]
    
    # Apply weight factors and nested processing
    for sensor_idx in range(len(interval_readings)):
        raw_value = interval_readings[sensor_idx]
        weight = weight_factors[sensor_idx]
        
        # Apply adjustment and accumulate
        adjusted_value = adjust_signal(raw_value, weight)
        processed_signal_strength += adjusted_value
        
        # Apply additional transformation for every second interval
        if interval_idx % 2 == 1:
            processed_signal_strength ^= raw_value

# Final transformation using functional programming
final_transform = list(map(lambda x: x & 0xF, [processed_signal_strength]))
processed_signal_strength = reduce(lambda a, b: a + b, final_transform)

print(f"Result: {processed_signal_strength}")