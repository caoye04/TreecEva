from collections import namedtuple
import math

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])
        return seq

def encode_measurement(value, fib_weights):
    encoded = 0
    for i, weight in enumerate(fib_weights):
        bit = (value >> i) & 1
        encoded ^= (bit * weight)
    return encoded

def decode_signal(encoded_val, fib_weights):
    decoded = 0
    for i, weight in enumerate(fib_weights):
        if encoded_val & (1 << i):
            decoded ^= weight
    return decoded

class SignalProcessor:
    def __init__(self, window_size=8):
        self.window_size = window_size
        self.fib_weights = fibonacci_sequence(window_size)
    
    def process(self, measurements):
        processed_values = []
        for meas in measurements:
            # Apply Fibonacci-weighted encoding
            encoded = encode_measurement(meas, self.fib_weights)
            # Perform bit rotation
            rotated = ((encoded << 3) | (encoded >> (self.window_size-3))) & ((1 << self.window_size) - 1)
            # Apply mask and XOR with magic number
            masked = rotated & 0b11010111
            final_val = masked ^ 0b10110010
            processed_values.append(final_val)
        return processed_values

# Vibration sensor measurements from mechanical assembly line
SensorData = namedtuple('SensorData', ['timestamp', 'readings'])
sensor_data = SensorData(
    timestamp=1678901234,
    readings=[0x3A, 0x4F, 0x2C, 0x5B, 0x38]
)

# Process the sensor data
processor = SignalProcessor(window_size=8)
processed_readings = processor.process(sensor_data.readings)

# Calculate signal strength using dictionary comprehension and merging
base_weights = {i: val for i, val in enumerate(processor.fib_weights)}
adjustment_factors = {i: (1 << i) for i in range(len(processor.fib_weights))}
combined_weights = {**base_weights, **{k: v*2 for k, v in adjustment_factors.items()}}

# Compute weighted sum with lambda function
weight_func = lambda idx, val: val * combined_weights.get(idx, 1)
signal_components = {i: weight_func(i, val) for i, val in enumerate(processed_readings)}

# Final signal strength calculation
initial_strength = sum(signal_components.values())
processed_signal_strength = (initial_strength >> 2) ^ (initial_strength & 0xFF)

print(f"Result: {processed_signal_strength}")