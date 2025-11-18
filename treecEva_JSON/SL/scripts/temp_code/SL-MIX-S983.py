import heapq
import math
from collections import deque

def signal_enhancer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return math.log(result + 1) if result > 0 else 0
    return wrapper

class SensorArray:
    def __init__(self):
        self.readings = []
    
    def add_reading(self, value):
        self.readings.append(value)
    
    @signal_enhancer
    def get_peak_intensity(self):
        return max(self.readings) if self.readings else 0

def process_acoustic_data(raw_signals):
    # Initialize processing queues and stacks
    primary_queue = deque()
    secondary_stack = []
    
    # Load signals into queue
    for signal in raw_signals:
        primary_queue.append(signal)
    
    # Process through first filter
    filtered_heap = []
    while primary_queue:
        current = primary_queue.popleft()
        adjusted = current * math.exp(0.1) if current > 10 else current
        heapq.heappush(filtered_heap, -adjusted)  # Max heap using negative values
    
    # Apply second stage processing
    sensor_bank = SensorArray()
    while filtered_heap:
        value = -heapq.heappop(filtered_heap)
        transformed = math.pow(value, 1/3) if value >= 0 else -math.pow(-value, 1/3)
        sensor_bank.add_reading(transformed)
    
    # Final detection calculation
    peak_intensity = sensor_bank.get_peak_intensity()
    baseline_noise = sum(raw_signals) / len(raw_signals)
    
    # Ternary operator for threshold check
    detection_threshold = 2.5 if len(raw_signals) > 5 else 1.8
    
    # Logical operations for final score determination
    is_valid_detection = peak_intensity > baseline_noise and peak_intensity > 0
    has_sufficient_samples = len(raw_signals) >= 3 or peak_intensity > 5
    
    # Calculate final score using logical combinations
    raw_score = peak_intensity * math.log(len(raw_signals) + 1) if is_valid_detection else 0
    final_detection_score = raw_score if (is_valid_detection and has_sufficient_samples) else detection_threshold
    
    return final_detection_score

# Execute the acoustic analysis
underwater_readings = [12.5, 8.3, 15.7, 22.1, 9.8, 18.4, 11.2]
detection_result = process_acoustic_data(underwater_readings)
print(f"Result: {detection_result}")