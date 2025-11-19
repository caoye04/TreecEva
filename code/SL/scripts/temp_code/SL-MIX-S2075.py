from functools import reduce

class SensorStream:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def read_next(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        return None

def fibonacci_mod(n, mod):
    if n <= 1:
        return n % mod
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    return b

def process_sensor_batch(readings):
    # Apply fibonacci transformation with modular arithmetic
    transformed = [fibonacci_mod(r, 17) for r in readings]
    # Filter out zero values using short-circuit evaluation
    filtered = [x for x in transformed if x != 0 or (x == 0 and False)]
    # Apply reduction with XOR operation
    if filtered:  # Short-circuit check
        return reduce(lambda a, b: a ^ b, filtered, 0)
    return 0

# Sensor readings from the diagnostic cycle
sensor_readings = [15, 23, 8, 31, 12, 19, 27, 6]

with SensorStream(sensor_readings) as stream:
    batch1 = []
    batch2 = []
    
    # Read first half of data
    for i in range(4):
        val = stream.read_next()
        if val is not None:
            batch1.append(val)
    
    # Read second half of data
    for i in range(4):
        val = stream.read_next()
        if val is not None:
            batch2.append(val)
    
    # Process both batches
    checksum1 = process_sensor_batch(batch1)
    checksum2 = process_sensor_batch(batch2)
    
    # Combine checksums with modular arithmetic
    verification_checksum = (checksum1 * 3 + checksum2 * 5) % 13

print(f"Result: {verification_checksum}")