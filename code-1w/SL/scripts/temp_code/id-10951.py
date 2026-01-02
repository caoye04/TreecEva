from collections import Counter

def analyze_temperature_modes(temperatures):
    # Filter temperatures within comfortable range (18-24 degrees)
    filtered_temps = [t for t in temperatures if 18 <= t <= 24]
    
    # Count frequency of each temperature reading
    frequency_map = Counter(filtered_temps)
    
    # Determine how many unique temperatures were recorded
    unique_count = len(frequency_map)
    
    # Find the highest occurrence count (mode frequency)
    peak_frequency = max(frequency_map.values())
    
    # Return only the peak frequency for evaluation
    return peak_frequency

# Sensor data from office environment over a week
temp_data = [20, 21, 19, 22, 20, 23, 20, 24, 21, 17, 25, 20, 21, 16, 22, 20]

result = analyze_temperature_modes(temp_data)
print(f"Target result: {result}")