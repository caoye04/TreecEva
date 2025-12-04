def compute_data_integrity(data_stream):
    # Initialize verification components
    parity_bit = 0x1F
    accumulator = 128
    validation_mask = 0b10101010
    
    # Main integrity computation
    checksum = 0
    for byte_val in data_stream:
        # XOR with parity and mask operations
        processed_byte = byte_val ^ parity_bit
        processed_byte &= validation_mask
        checksum ^= processed_byte
        
        # Distractor operations (irrelevant to final result)
        accumulator = (accumulator << 1) | (byte_val & 1)
        parity_bit = (parity_bit + 7) % 32
    
    # Secondary verification (dead code path)
    if checksum > 200:
        backup_checksum = sum(data_stream) % 256
        checksum = backup_checksum ^ 0xFF
    
    return checksum

def transform_sensor_data(raw_readings):
    # Apply calibration offsets
    calibrated = [reading + 5 for reading in raw_readings]
    
    # Filter and scale data (distractor operations)
    filtered = [val * 2 for val in calibrated if val % 3 != 0]
    scaled = [min(val, 100) for val in filtered]
    
    # Misleading intermediate calculation
    temp_sum = sum(scaled) + len(raw_readings)
    
    return calibrated

# Main execution
sensor_samples = [45, 67, 23, 89, 12, 56, 78, 34]

# Distractor variables and computations
temp_buffer = [sample ^ 0xAA for sample in sensor_samples]
redundant_check = sum(temp_buffer) % 128
validation_flag = redundant_check > 50

# Data transformation
transformed_data = transform_sensor_data(sensor_samples)

# Final integrity computation
final_checksum = compute_data_integrity(transformed_data)

# Print result
print(f"Result: {final_checksum}")