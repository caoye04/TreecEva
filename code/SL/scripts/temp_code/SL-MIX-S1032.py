from functools import reduce
import itertools

class SensorReading:
    def __init__(self, raw_data):
        self.raw = raw_data
        self.parsed = None
        self.valid = False
    
def validate_and_parse(reading):
    try:
        # Remove prefix if exists
        data = reading.raw
        if data.startswith('0x'):
            data = data[2:]
        # Check if even length and not empty
        if len(data) == 0 or len(data) % 2 != 0:
            return False
        # Try parsing as hex
        int(data, 16)
        reading.parsed = data
        reading.valid = True
        return True
    except ValueError:
        return False

def decode_reading(reading):
    if not reading.valid:
        return 0
    # Decode hex to bytes then to ASCII
    try:
        byte_data = bytes.fromhex(reading.parsed)
        ascii_str = byte_data.decode('ascii')
        # Convert each character to its ASCII value and sum
        return sum(ord(c) for c in ascii_str)
    except:
        return 0

# Simulated sensor input stream
sensor_feed = [
    SensorReading('0x48656c6c'),  # "Hell"
    SensorReading('0x6f20576f'),  # "o Wo"
    SensorReading('0x726c6421'),  # "rld!"
    SensorReading('0x00'),        # Null
    SensorReading('0xGHIJKL'),    # Invalid
    SensorReading('0x414243'),    # "ABC"
]

# Process pipeline
valid_readings = filter(validate_and_parse, sensor_feed)
checksum_components = map(decode_reading, valid_readings)

# Compute rolling checksum with initial value
initial_seed = 0x55
final_checksum = reduce(lambda acc, val: acc ^ val, checksum_components, initial_seed)

print(f"Result: {final_checksum}")