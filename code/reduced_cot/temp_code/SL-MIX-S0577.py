import functools

def process_telemetry(readings):
    encoded_values = []
    for idx, reading in enumerate(readings):
        # Rotate mask based on index: shift left by (idx % 5) bits
        mask = ((0b1101 << (idx % 5)) & 0xFF) | (0b1101 >> (8 - (idx % 5)))
        # XOR reading with mask
        encoded = reading ^ mask
        # Convert to hex string and back to simulate encoding/decoding
        hex_str = hex(encoded)[2:]
        decoded = int(hex_str, 16)
        encoded_values.append(decoded)
    
    # Apply a reduction to simulate aggregation
    aggregated = functools.reduce(lambda x, y: (x + y) & 0xFF, encoded_values, 0)
    return aggregated

# Sensor readings
sensor_data = [42, 18, 73, 29, 55]
final_telemetry = process_telemetry(sensor_data)
print(f"Result: {final_telemetry}")