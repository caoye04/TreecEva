from collections import Counter

# Simulate sensor readings over time (e.g., temperature thresholds triggered)
readings = [22, 24, 22, 25, 26, 24, 22, 27, 25, 24, 24, 23]

# Count how often each reading occurs
def process_sensor_data(data):
    frequency_map = Counter(data)
    peak_frequency = max(frequency_map.values())
    return peak_frequency

result = process_sensor_data(readings)
print(f"Result: {result}")