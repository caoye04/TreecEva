def encode_reading(reading):
    # Convert to 3-digit octal
    octal_str = f"{oct(reading)[2:]:>03}"
    # Mapping from octal digits to characters
    mapping = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H'}
    return ''.join(mapping[digit] for digit in octal_str)

sensor_readings = [127, 256, 511]
encoded_data = [encode_reading(r) for r in sensor_readings]
all_chars = ''.join(encoded_data)
telemetry_checksum = sum(ord(c) for c in all_chars)
print(f"Result: {telemetry_checksum}")