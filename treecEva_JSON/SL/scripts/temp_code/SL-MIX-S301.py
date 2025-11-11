import re
from statistics import mean

def process_telemetry(readings):
    # State definitions for our finite state machine
    states = {
        'stable': {'low_threshold': 10, 'high_threshold': 90},
        'warning': {'low_threshold': 5, 'high_threshold': 95},
        'critical': {'low_threshold': 0, 'high_threshold': 100}
    }
    
    current_state = 'stable'
    stable_values = []
    
    # Lambda to determine next state based on value
    transition = lambda val: 'critical' if val < 5 or val > 95 else ('warning' if val < 10 or val > 90 else 'stable')
    
    for entry in readings:
        # Pattern matching to validate and extract data
        match = re.match(r'SENSOR_(\w+):(\d+):(\d+\.?\d*)', entry)
        if not match:
            continue  # Corrupted data, skip
        
        _, timestamp, value_str = match.groups()
        value = float(value_str)
        
        # Update state using our state machine
        current_state = transition(value)
        
        # Store value if in stable state
        if current_state == 'stable':
            stable_values.append(value)
    
    # Dictionary comprehension to merge with metadata (dummy here)
    meta = {"processed": len(readings)}
    stats = {"count": len(stable_values)}
    merged_info = {**meta, **stats}
    
    average_stable_value = mean(stable_values) if stable_values else 0
    return average_stable_value, merged_info

# Sensor readings with mixed valid and invalid formats
sensor_data = [
    "SENSOR_TEMP:1001:25.3",
    "SENSOR_HUM:1002:corrupted",
    "SENSOR_TEMP:1003:5.1",
    "SENSOR_PRESS:1004:88.0",
    "INVALID_FORMAT",
    "SENSOR_TEMP:1005:91.2",
    "SENSOR_HUM:1006:45.0"
]

average_stable_value, info = process_telemetry(sensor_data)
print(f"Result: {average_stable_value}")