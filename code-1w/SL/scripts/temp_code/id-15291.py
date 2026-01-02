from collections import Counter

# Simulate sensor readings over time (e.g., temperature in tenths of °C)
readings = [215, 220, 215, 225, 230, 220, 215, 235, 225, 220, 220]

# Count frequency of each reading
def process_readings(data):
    frequency_count = Counter(data)
    average_value = sum(data) / len(data)
    mode_reading = frequency_count.most_common(1)[0][0]
    peak_frequency = max(frequency_count.values())
    return average_value, mode_reading, peak_frequency

_, _, peak_frequency = process_readings(readings)
print(f"Result: {peak_frequency}")