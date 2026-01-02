import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 19.5, 27.8, 30.1, 25.0, 22.7, 26.3, 28.9, 24.2, 21.6]
humidity_readings = [45, 50, 60, 62, 58, 54, 56, 61, 49, 52]
pressure_readings = [1013, 1015, 1012, 1009, 1010, 1014, 1016, 1008, 1011, 1013]

# Irrelevant auxiliary arrays (distractor data)
wind_speed_kmh = [12, 15, 10, 8, 14, 16, 9, 11, 13, 17]
solar_irradiance_wm2 = [850, 900, 870, 830, 890, 910, 860, 840, 880, 905]
elevation_meters = [120, 135, 110, 95, 105, 128, 140, 90, 115, 122]

# Mapping station index to location names (decoy structure)
station_locations = {
    0: 'North Ridge',
    1: 'East Valley',
    2: 'South Plateau',
    3: 'West Cliffs',
    4: 'Central Basin',
    5: 'Northeast Slope',
    6: 'Southeast Mesa',
    7: 'Northwest Dune',
    8: 'Southwest Grove',
    9: 'Midland Field'
}

# Threshold configuration for anomaly detection (critical data)
threshold_map = {
    'temp_high': 27.5,
    'temp_low': 20.0,
    'humidity_high': 59,
    'pressure_trend': -3
}

# Derived metrics with red herring calculations
heat_index = [
    t + 0.5 * h if t > 25 else t
    for t, h in zip(temperature_readings, humidity_readings)
]

dew_point_approx = [
    t - ((100 - h) / 5) for t, h in zip(temperature_readings, humidity_readings)
]

# Pressure change rate (unused but plausible intermediate)
pressure_change = [
    pressure_readings[i] - pressure_readings[i-1] if i > 0 else 0
    for i in range(len(pressure_readings))
]

# Mask creation using slicing and list comprehension (relevant filtering)
valid_indices = [
i for i in range(len(temperature_readings))
    if temperature_readings[i] >= threshold_map['temp_low']
]

filtered_data = [
    {
        'idx': i,
        'temp': temperature_readings[i],
        'humid': humidity_readings[i],
        'press': pressure_readings[i]
    }
    for i in valid_indices
    if humidity_readings[i] <= threshold_map['humidity_high']
]

# Dead function - looks important but unused (distractor)
def calculate_wind_chill(temp, wind):
    return 13.12 + 0.6215*temp - 11.37*(wind**0.16) + 0.3965*temp*(wind**0.16)

# Bit manipulation decoy (simulates low-level processing)
status_flags = 0
for i, reading in enumerate(filtered_data):
    if reading['temp'] > threshold_map['temp_high']:
        status_flags |= (1 << i)  # Set bit if high temp
    if i % 2 == 0:
        status_flags ^= (1 << (i+1))  # Flip even bits (misleading)

# Another irrelevant transformation
compressed = []
for i in range(0, len(filtered_data), 2):
    pair_sum = filtered_data[i]['temp'] + filtered_data[i]['humid']
    if i+1 < len(filtered_data):
        pair_sum += filtered_data[i+1]['temp']
    compressed.append(int(pair_sum) & 0xFF)  # Bitwise masking red herring

# Real processing function with multiple concepts
def process_readings(data_list, thresholds):
    # Dictionary accumulation
    stats = {
        'high_temp_count': 0,
        'total_humidity': 0,
        'pressure_sum': 0,
        'anomaly_score': 0.0
    }
    
    # Nested conditional logic with complex interdependencies
    for entry in data_list:
        temp = entry['temp']
        humid = entry['humid']
        press = entry['press']
        
        # Primary condition chain (relevant)
        if temp > thresholds['temp_high']:
            stats['high_temp_count'] += 1
            stats['anomaly_score'] += 1.5
            
            # Nested branch with slicing side-effect (decoy)
            subset = temperature_readings[2:7]
            mid_avg = sum(subset) / len(subset)
            if mid_avg > 25.0:
                stats['anomaly_score'] += 0.2  # Minor bump (distraction)
        
        # Independent accumulation
        stats['total_humidity'] += humid
        stats['pressure_sum'] += press
        
        # Complex derived condition (looks important but contributes minimally)
        expected_humid = 70 - (temp - 20) * 1.5
        humid_deviation = abs(humid - expected_humid)
        if humid_deviation > 10:
            stats['anomaly_score'] += 0.3
    
    # Multi-step final computation
    base_score = stats['high_temp_count'] * 100
    humidity_factor = max(0, (stats['total_humidity'] - 200) / 10)
    pressure_offset = (stats['pressure_sum'] // 100) % 7
    
    # Critical calculation path
    intermediate = base_score + humidity_factor
    if intermediate > 200:
        intermediate -= pressure_offset * 8
    
    # Final non-linear transformation
    final_value = int(intermediate ** 1.1) % 897
    
    # Decoy rounding operation (never used)
    precise_final = round(final_value + 0.4567, 4)
    
    return final_value

# Execute key statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")