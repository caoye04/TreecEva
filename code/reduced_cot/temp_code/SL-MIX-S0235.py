import itertools
import math

class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.data = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data.clear()
    
    def add(self, value):
        if len(self.data) < self.size:
            self.data.append(value)
        return len(self.data)

# Sensor readings
sensor_readings = [
    [1.2, 2.3, 3.4],
    [4.5, 5.6, 6.7],
    [7.8, 8.9, 9.0],
    [2.1, 3.2, 4.3]
]

# Initialize counters and matrices
processed_signals_count = 0
signal_matrix = [[0 for _ in range(3)] for _ in range(4)]

# Process sensor data
with DataBuffer(10) as buffer:
    for i, readings in enumerate(sensor_readings):
        valid_readings = [r for r in readings if r > 2.0]
        if len(valid_readings) >= 2:
            combinations = list(itertools.combinations(valid_readings, 2))
            for j, (a, b) in enumerate(combinations):
                if j < 3:  # Only process first 3 combinations
                    signal_matrix[i][j] = math.floor(a * b)
                    buffer.add(signal_matrix[i][j])
            
            # Apply conditional logic based on buffer state
            if buffer.add(0) > 5:  # Add a marker and check buffer size
                processed_signals_count += len(combinations)
            else:
                processed_signals_count += 1
        else:
            # Handle cases with insufficient valid readings
            signal_matrix[i] = [math.ceil(r) for r in readings]
            processed_signals_count -= 1

# Final adjustment based on matrix properties
if any(sum(row) > 10 for row in signal_matrix):
    processed_signals_count *= 2

print(f"Result: {processed_signals_count}")