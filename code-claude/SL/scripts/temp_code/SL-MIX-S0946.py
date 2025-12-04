from collections import Counter

def calculate_signal_quality(readings):
    # Main algorithm to determine signal quality
    if not readings:
        return 0
    
    signal_mean = sum(readings) / len(readings)
    # Higher weight for readings closer to mean
    weighted_sum = sum(1 / (abs(r - signal_mean) + 1) for r in readings)
    return round(weighted_sum * 10, 2)

# Sensor data from different stations
sensor_data = {
    'station1': [42, 45, 41, 38, 44],
    'station2': [39, 37, 42, 41, 40],
    'station3': [44, 46, 45, 47, 43],
    'station4': [36, 38, 35, 37, 39]
}

# Calculate noise levels (not directly used in final result)
noise_levels = {station: max(data) - min(data) for station, data in sensor_data.items()}
debug_info = Counter(noise_level for noise_level in noise_levels.values())

# Filter stations based on criteria
threshold = lambda x: sum(x) / len(x) >= 40
valid_stations = [station for station, readings in sensor_data.items() if threshold(readings)]

# Process readings from valid stations
all_readings = []
for station in valid_stations:
    # This extracts readings from valid stations
    readings = sensor_data[station]
    
    # Calculate station reliability factor (not used in final calculation)
    reliability = 100 - (max(readings) - min(readings)) * 2
    
    # Apply transformation to each reading
    transformed = [r - 3 if r % 2 == 0 else r + 2 for r in readings]
    
    # This step doesn't affect the final result
    diagnostic_value = sum(transformed) / len(transformed)
    
    # Only odd-indexed readings are used
    filtered = [transformed[i] for i in range(len(transformed)) if i % 2 == 1]
    all_readings.extend(filtered)

# Apply secondary filter based on range
min_acceptable = 38
max_acceptable = 50
filtered_readings = [r for r in all_readings if min_acceptable <= r <= max_acceptable]

# Calculate final signal quality score
signal_strength = calculate_signal_quality(filtered_readings)
print(f"Result: {signal_strength}")