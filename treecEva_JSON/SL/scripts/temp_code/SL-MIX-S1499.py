import itertools

def calculate_average(readings):
    return sum(readings) / len(readings) if readings else 0

class SensorAnalyzer:
    def __init__(self, sensor_id, readings):
        self.sensor_id = sensor_id
        self.readings = readings
        self.average = calculate_average(readings)
    
    def find_exceptional_patterns(self):
        max_strength = float('-inf')
        n = len(self.readings)
        for start in range(n):
            for end in range(start + 2, n):  # At least 3 elements
                subseq = self.readings[start:end+1]
                if all(r > self.average for r in subseq):
                    strength = sum(subseq)
                    if strength > max_strength:
                        max_strength = strength
        return max_strength if max_strength != float('-inf') else 0

def process_sensors(sensor_data_list):
    analyzers = [SensorAnalyzer(i, data) for i, data in enumerate(sensor_data_list)]
    max_strengths = [analyzer.find_exceptional_patterns() for analyzer in analyzers]
    return max(max_strengths) if max_strengths else 0

# Sensor readings data
sensor_readings = [
    [10, 12, 8, 15, 17, 16, 5],
    [20, 22, 25, 18, 30, 35, 28],
    [5, 3, 7, 9, 6, 4, 8]
]

# Determine the maximum strength among all exceptional patterns
max_pattern_strength = process_sensors(sensor_readings)
print(f"Result: {max_pattern_strength}")