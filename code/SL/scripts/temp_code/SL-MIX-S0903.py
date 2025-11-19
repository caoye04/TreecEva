import math

def transform_sensor_data(raw_input):
    # Stage 1: Normalize and apply exponential mapping
    normalized = (raw_input & 0xFF) / 255.0
    exponential_mapped = math.exp(normalized) - 1
    
    # Stage 2: Bitwise encoding with shifting
    integer_part = int(exponential_mapped * 100)
    shifted_left = integer_part << 2
    xor_mask = 0b10101010
    encoded_value = shifted_left ^ xor_mask
    
    # Stage 3: Conditional amplification using ternary logic
    amplified = encoded_value * 3 if (encoded_value & 1) == 0 else encoded_value // 2
    
    # Stage 4: Final adjustment with logarithmic scaling
    if amplified > 0:
        final_result = int(math.log(amplified + 1) * 10)
    else:
        final_result = 0
    
    return final_result

# Sensor reading pipeline
sensor_readings = [187, 204, 153, 221]
processing_pipeline = lambda x: transform_sensor_data(x)

# Apply transformation to all readings and sum them
processed_values = list(map(processing_pipeline, sensor_readings))
aggregated_signal = sum(processed_values)

# Final encoding step with bitwise operations
signal_mask = 0xF0F0
masked_signal = aggregated_signal & signal_mask
processed_signal = masked_signal >> 4 if (aggregated_signal & 0x1000) != 0 else masked_signal ^ 0xAA

print(f"Result: {processed_signal}")