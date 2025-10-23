import math
import re
from collections import deque

def process_sensor_data(readings):
    # Stack for computation
    stack = []
    # Hash table for pattern frequencies
    pattern_counts = {}
    
    for reading in readings:
        # Apply logarithmic transformation if positive
        if reading > 0:
            log_val = math.log10(reading)
            stack.append(log_val)
        else:
            stack.append(0.0)
        
        # Exponential smoothing with previous value if exists
        if len(stack) >= 2:
            prev = stack[-2]
            current = stack[-1]
            smoothed = 0.7 * current + 0.3 * prev
            stack[-1] = smoothed
    
    # Pattern detection using regex on string representation
    stack_str = ''.join([f'{x:.2f}' for x in stack])
    patterns = re.findall(r'\d\.\d{2}', stack_str)
    
    for p in patterns:
        pattern_counts[p] = pattern_counts.get(p, 0) + 1
    
    # Calculate anomaly score based on pattern repetition and stack values
    unique_patterns = len(pattern_counts)
    stack_sum = sum(stack)
    
    # Anomalous if any pattern repeats more than twice
    repeated_patterns = sum(1 for count in pattern_counts.values() if count > 2)
    
    # Final anomaly score calculation
    anomaly_score = (stack_sum * unique_patterns) / (1 + repeated_patterns)
    return anomaly_score

# Sensor readings (in mm)
sensor_readings = [0.5, 1.2, 3.3, 0.5, 10.0, 0.0, 2.7, 1.2, 0.5, 5.5]

# Process the data
anomaly_score = process_sensor_data(sensor_readings)
print(f'Result: {anomaly_score}')