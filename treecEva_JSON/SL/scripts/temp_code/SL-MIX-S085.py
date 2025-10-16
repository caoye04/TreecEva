import math
import heapq
from collections import defaultdict

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

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def signal_decay(distance, factor=0.1):
    return math.exp(-factor * distance)

def log_weight(value, base=math.e):
    return math.log(value + 1, base) if value > 0 else 0

class SensorDataProcessor:
    def __init__(self):
        self.readings_queue = []
        self.processed_data = defaultdict(float)
        self.triangulation_points = []
    
    def add_reading(self, priority, data):
        heapq.heappush(self.readings_queue, (priority, data))
    
    def process_readings(self, count):
        triangulation_confidence = 0.0
        
        for _ in range(min(count, len(self.readings_queue))):
            priority, (sensor_id, coordinates) = heapq.heappop(self.readings_queue)
            
            # Calculate weighted signal strength
            distance_from_origin = calculate_distance(coordinates, (0, 0))
            decay_factor = signal_decay(distance_from_origin)
            weighted_signal = priority * decay_factor
            
            # Apply logarithmic weighting
            log_weighted = log_weight(weighted_signal)
            
            # Accumulate in processed data
            self.processed_data[sensor_id] += log_weighted
            
            # Update triangulation confidence
            triangulation_confidence += log_weighted * 0.75
        
        return triangulation_confidence

# Main processing
processor = SensorDataProcessor()

# Generate Fibonacci indices for sensor packet selection
fib_indices = fibonacci_sequence(10)[2:]  # Skip first two (0, 1)

# Simulated sensor data with coordinates
sensor_packets = [
    (1, ('S01', (3.5, 4.2))),
    (2, ('S02', (6.1, 8.3))),
    (3, ('S03', (-2.4, 5.7))),
    (4, ('S04', (7.8, -1.9))),
    (5, ('S05', (-5.2, -3.6))),
    (6, ('S06', (9.1, 2.4))),
    (7, ('S07', (0.5, -7.3))),
    (8, ('S08', (-8.2, 0.9)))
]

# Add selected packets to processor based on Fibonacci indices
for idx in fib_indices:
    if idx < len(sensor_packets):
        priority, data = sensor_packets[idx]
        processor.add_reading(priority, data)

# Process the readings and calculate triangulation confidence
triangulation_confidence = processor.process_readings(len(fib_indices))

# Apply final adjustment using matrix determinant concept
adjustment_matrix = [
    [1.2, 0.5],
    [0.3, 1.8]
]
determinant = adjustment_matrix[0][0] * adjustment_matrix[1][1] - adjustment_matrix[0][1] * adjustment_matrix[1][0]
triangulation_confidence *= determinant

print(f"Result: {round(triangulation_confidence, 6)}")