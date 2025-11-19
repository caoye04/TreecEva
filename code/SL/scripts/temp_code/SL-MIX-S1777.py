from collections import deque

def process_sensor_data(readings):
    window = deque(maxlen=3)
    normalized_values = []
    
    for i, reading in enumerate(readings):
        window.append(reading)
        if len(window) == 3:
            avg = sum(window) // 3
            normalized = (avg * 7 + 13) % 256
            normalized_values.append(normalized)
    
    # Compute checksum using XOR on every third element starting from index 2
    checksum = 0
    for i in range(2, len(normalized_values), 3):
        checksum ^= normalized_values[i]
    
    return checksum

# Sensor readings from a temperature monitoring system
sensor_readings = [82, 76, 91, 88, 73, 95, 87, 79, 93, 85, 77, 94, 89, 81, 92]

final_checksum = process_sensor_data(sensor_readings)
print(f"Result: {final_checksum}")