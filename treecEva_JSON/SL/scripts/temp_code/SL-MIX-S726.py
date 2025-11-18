from collections import defaultdict

def find_consistent_patterns(sensor_readings):
    value_counts = defaultdict(int)
    value_sensors = defaultdict(set)
    
    # Count occurrences and track which sensors reported each value (±2 tolerance)
    for sensor_id, readings in enumerate(sensor_readings):
        for reading in readings:
            for adjusted_value in range(reading-2, reading+3):  # ±2 tolerance
                value_counts[adjusted_value] += 1
                value_sensors[adjusted_value].add(sensor_id)
    
    # Find values that appear in at least half the sensors
    min_sensors = len(sensor_readings) // 2
    candidates = []
    
    for value, sensors in value_sensors.items():
        if len(sensors) > min_sensors:
            candidates.append((value, value_counts[value]))
    
    # Return the value with highest total count, breaking ties by highest value
    if not candidates:
        return -1
    
    candidates.sort(key=lambda x: (-x[1], -x[0]))
    return candidates[0][0]

# Sensor data from 7 different environmental monitors
sensor_data = [
    [15, 22, 30, 18],
    [17, 24, 29, 20],
    [16, 23, 31, 19],
    [18, 25, 28, 21],
    [14, 22, 32, 17],
    [16, 24, 30, 19],
    [15, 23, 29, 18]
]

strongest_pattern = find_consistent_patterns(sensor_data)
print(f"Result: {strongest_pattern}")