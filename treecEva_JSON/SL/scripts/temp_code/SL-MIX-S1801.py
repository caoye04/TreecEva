def process_sensor_data(raw_hex):
    # Remove hex prefix
    hex_part = raw_hex[2:]
    
    # Shift each character by its position
    shifted_chars = []
    for i, char in enumerate(hex_part):
        # Convert char to int, add position, mod 16 to keep in hex range
        val = int(char, 16)
        shifted_val = (val + i) % 16
        shifted_chars.append(format(shifted_val, 'X'))
    
    # Join shifted characters
    shifted_hex = ''.join(shifted_chars)
    
    # Compute hash-like validation using XOR of character codes
    validation_hash = 0
    for c in shifted_hex:
        validation_hash ^= ord(c)
    
    return validation_hash

# Dictionary comprehension for sensor metadata
sensor_metadata = {f'sensor_{i}': {'type': 'temp', 'id': i*7} for i in range(3)}

# Process the main sensor reading
primary_reading = '0x1B4F'
encoded_result = process_sensor_data(primary_reading)

# Conditional branch for calibration
if encoded_result > 100:
    calibration_factor = 3
else:
    calibration_factor = 7

# Switch-like logic using dict for adjustment
adjustment_map = {
    3: lambda x: x * 2,
    7: lambda x: x + 10
}

adjusted_result = adjustment_map[calibration_factor](encoded_result)

# Final telemetry score calculation using set operations
valid_hashes = {0x41, 0x42, 0x43, adjusted_result & 0xFF}
telemetry_pool = frozenset([0x41, 0x43, 0x45])

# Intersection and final calculation
common_elements = valid_hashes & telemetry_pool

telemetry_score = sum(common_elements) + (adjusted_result >> 4)

print(f"Result: {telemetry_score}")