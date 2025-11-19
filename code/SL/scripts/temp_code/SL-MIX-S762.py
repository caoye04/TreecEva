from collections import deque
from functools import reduce
import math

def is_valid_reading(x):
    return x >= 0 and x <= 100

def compute_rolling_avg(window):
    return sum(window) / len(window) if window else 0

# Sensor readings
readings = [10, 15, 105, 20, 25, 30, -5, 35, 40, 45, 50]
window_size = 3
threshold = 30

# Initialize data structures
sensor_window = deque(maxlen=window_size)
valid_readings = []
processed_samples = 0
avg_history = []

def process_sensor_data(readings):
    global processed_samples
    for i, reading in enumerate(readings):
        # Apply short-circuit evaluation for efficiency
        if is_valid_reading(reading) and (not avg_history or abs(reading - avg_history[-1]) < 20):
            sensor_window.append(reading)
            valid_readings.append(reading)
            
            # Compute rolling average when window is full
            if len(sensor_window) == window_size:
                avg = compute_rolling_avg(sensor_window)
                avg_history.append(avg)
                
                # Count samples exceeding threshold
                if avg > threshold:
                    processed_samples += 1
        
        # Special handling for every third invalid reading
        elif not is_valid_reading(reading) and len([r for r in readings[:i] if not is_valid_reading(r)]) % 3 == 2:
            if sensor_window:
                sensor_window.popleft()
    
    # Final adjustment using functional programming
    if avg_history:
        adjusted_values = list(map(lambda x: x * 1.1 if x > threshold else x, avg_history))
        processed_samples = reduce(lambda acc, val: acc + (1 if val > threshold else 0), adjusted_values, 0)

process_sensor_data(readings)
print(f"Result: {processed_samples}")