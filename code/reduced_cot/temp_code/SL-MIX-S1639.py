from dataclasses import dataclass
from contextlib import contextmanager
import math

data = [
    (10, 20, 50),
    (15, 25, 75),
    (30, 40, 25),
    (35, 45, 60),
    (50, 60, 80)
]

@dataclass
class SensorReading:
    x: float
    y: float
    signal: int

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

@contextmanager
def log_readings(filename):
    readings_log = []
    try:
        yield readings_log
    finally:
        with open(filename, 'w') as f:
            for r in readings_log:
                f.write(f"({r.x}, {r.y}) => {r.signal}\n")

def filter_by_distance(readings, max_distance):
    return [r for r in readings if r.distance_from_origin() <= max_distance]

def binary_search_optimize(signals):
    signals.sort()
    left, right = 0, len(signals) - 1
    while left < right:
        mid = (left + right) // 2
        if signals[mid] < signals[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return signals[left]

# Main execution
readings = [SensorReading(x, y, s) for x, y, s in data]

with log_readings('sensor_logs.txt') as log:
    for r in readings:
        log.append(r)
    
    # Filter readings within 50 units from origin
    filtered = filter_by_distance(readings, 50)
    
    # Extract signal strengths
    signal_strengths = [r.signal for r in filtered]
    
    # Optimize using binary search approach
    optimized_signal_strength = binary_search_optimize(signal_strengths)

print(f"Result: {optimized_signal_strength}")