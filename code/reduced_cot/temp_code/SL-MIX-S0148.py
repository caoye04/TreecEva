from collections import defaultdict

class SensorReading:
    def __init__(self, start_time, end_time, animal_count):
        self.start_time = start_time
        self.end_time = end_time
        self.animal_count = animal_count

def calculate_max_animals(sensor_data):
    # Sort sensors by end time
    sensor_data.sort(key=lambda x: x.end_time)
    
    # Dynamic programming array to store maximum animals up to each sensor
    dp = [0] * (len(sensor_data) + 1)
    
    # For each sensor, calculate maximum animals
    for i in range(1, len(sensor_data) + 1):
        # Current sensor index in original array
        current = i - 1
        
        # Find latest non-overlapping sensor
        latest_non_overlap = 0
        for j in range(current - 1, -1, -1):
            if sensor_data[j].end_time <= sensor_data[current].start_time:
                latest_non_overlap = j + 1
                break
        
        # Choose maximum between including or excluding current sensor
        dp[i] = max(dp[i-1], dp[latest_non_overlap] + sensor_data[current].animal_count)
    
    return dp[len(sensor_data)]

# Sensor data: (start_time, end_time, animal_count)
sensor_readings = [
    SensorReading(1, 4, 5),
    SensorReading(3, 5, 1),
    SensorReading(0, 6, 8),
    SensorReading(4, 7, 4),
    SensorReading(3, 8, 6),
    SensorReading(5, 9, 2),
    SensorReading(6, 10, 7),
    SensorReading(8, 11, 3)
]

max_animals_tracked = calculate_max_animals(sensor_readings)
print(f"Result: {max_animals_tracked}")