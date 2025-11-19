from functools import reduce

def process_sensor_data(readings):
    # Apply bit masking and shifting
    masked_readings = [r & 0xFF for r in readings]
    shifted_readings = [r << 2 if r < 64 else r >> 1 for r in masked_readings]
    
    # Conditional filtering with early return pattern
    filtered_values = []
    for val in shifted_readings:
        if val > 200:
            break
        if val ^ 0x55 > 30:  # XOR with 0x55 then check threshold
            filtered_values.append(val)
    
    # Floating point transformation using lambda
    float_transform = lambda x: round(x * 1.25 + 0.7, 2)
    transformed_values = list(map(float_transform, filtered_values))
    
    # Accumulate with bitwise adjustment
    accumulator = 0
    for i, val in enumerate(transformed_values):
        if i % 2 == 0:
            accumulator += int(val) & 0x7F
        else:
            accumulator |= int(val) >> 1
    
    # Final adjustment using reduce
    correction_factors = [1.1, 0.95, 1.05]
    final_adjustment = reduce(lambda acc, f: acc * f, correction_factors, 1.0)
    
    processed_signal_strength = int(accumulator * final_adjustment)
    return processed_signal_strength

# Sensor readings input
sensor_readings = [45, 120, 78, 205, 33, 160, 92]
result_value = process_sensor_data(sensor_readings)
print(f"Result: {result_value}")