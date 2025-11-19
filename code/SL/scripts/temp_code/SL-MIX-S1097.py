from functools import reduce
from collections import namedtuple

def modified_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 100
    return b

def find_threshold_position(readings):
    # Binary search for position where reading > avg using custom comparison
    avg = sum(readings) / len(readings)
    left, right = 0, len(readings) - 1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if readings[mid] > avg:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1
    return pos

# Sensor data processing pipeline
SensorReading = namedtuple('SensorReading', ['timestamp', 'strength'])
raw_data = [12, 25, 98, 37, 61, 44, 29, 73, 85, 56]
timestamps = list(range(len(raw_data)))

# Create sensor readings using functional approach
sensor_readings = list(map(lambda t, s: SensorReading(t, s), timestamps, raw_data))

# Identify readings matching modified Fibonacci pattern
fib_pattern_matches = [
    idx for idx, reading in enumerate(sensor_readings)
    if reading.strength == modified_fibonacci(reading.timestamp + 5)
]

# Calculate dynamic threshold position
threshold_pos = find_threshold_position([r.strength for r in sensor_readings])

# Compute stability index
stability_index = len(fib_pattern_matches) * (threshold_pos + 1) if threshold_pos != -1 else 0

print(f"Result: {stability_index}")