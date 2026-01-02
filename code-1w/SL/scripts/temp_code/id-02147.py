from collections import Counter

# Simulate sensor readings over time (e.g., temperature fluctuations)
readings = [23, 25, 23, 27, 25, 23, 29, 27, 25, 25]

def analyze_sensor_modes(data):
    # Count frequency of each reading
    frequency_map = Counter(data)
    
    # Find the most frequent value
    peak_frequency = max(frequency_map.values())
    
    # Secondary analysis: identify values above threshold
    high_readings = [v for v in data if v > 26]
    spike_count = len(high_readings)
    
    # Dummy variable for minor interference (LOW level)
    avg_reading = sum(data) / len(data)
    
    return peak_frequency

result = analyze_sensor_modes(readings)
print(f"Target result: {result}")