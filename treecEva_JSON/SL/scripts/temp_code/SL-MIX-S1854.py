from functools import reduce

class TelemetryProcessor:
    def __init__(self):
        self.state = 'IDLE'
        self.checksum = 0
    
    def __enter__(self):
        self.state = 'PROCESSING'
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.state = 'COMPLETED'
    
    def update_checksum(self, value):
        self.checksum ^= value
        return self.checksum

def decode_packet(raw_data):
    # Extract status bits (bits 4-7)
    status = (raw_data >> 4) & 0xF
    # Extract measurement bits (bits 0-3)
    measurement = raw_data & 0xF
    # Apply transformation
    transformed = (status * 3) + (measurement ^ 0b1010)
    return transformed

# Simulated incoming telemetry packets
packets = [0x7E, 0x3C, 0xB5, 0x9A, 0x6F]

with TelemetryProcessor() as processor:
    # Decode packets using functional approach
    decoded_values = list(map(decode_packet, packets))
    
    # Apply checksum updates
    for val in decoded_values:
        processor.update_checksum(val)
    
    # Finalize with reduction operation
    processed_checksum = reduce(lambda x, y: x ^ (y << 1), decoded_values, processor.checksum)

print(f"Result: {processed_checksum}")