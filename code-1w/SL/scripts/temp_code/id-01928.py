from collections import Counter

# Simulate sensor readings over time (e.g., temperature fluctuations)
readings = [23, 24, 25, 23, 24, 23, 26, 24, 24, 27, 25, 24, 23, 24]

# Count frequency of each reading
def process_readings(data):
    frequency_counter = Counter(data)
    average_value = sum(data) // len(data)  # integer division for baseline
    
    # Identify most frequent reading (mode)
    peak_frequency = max(frequency_counter.values())
    
    # Additional derived metric: deviation count
    deviation_count = sum(1 for x in data if abs(x - average_value) > 1)

    return frequency_counter, peak_frequency, deviation_count

# Execute analysis
freq_map, peak_frequency, dev_count = process_readings(readings)

# Output target result
print(f"Result: {peak_frequency}")