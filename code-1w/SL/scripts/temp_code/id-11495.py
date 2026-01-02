import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 58, 41, 60, 55, 39, 50, 48]
pressure_readings = [1013, 1015, 1010, 1020, 1008, 1012, 1025, 1018, 1005]
wind_speed_readings = [12.4, 15.1, 8.7, 18.3, 9.6, 14.2, 20.1, 11.8, 13.5]

# Auxiliary metadata (mostly irrelevant)
sensor_ids = ['TH01', 'TH02', 'HUM03', 'PRES04', 'WIND05']
location_grid = {'sector_x': 42, 'sector_y': 17, 'elevation': 88}
calibration_offsets = {"temp": 0.2, "humidity": -3, "pressure": 5}

# Distractor: unused transformation
transformed = [math.log(x + 1) for x in pressure_readings if x > 1010]

# Threshold configuration map (critical)
threshold_map = {
    'high_temp': 24.0,
    'low_humidity': 45,
    'pressure_variation': 15,
    'wind_alert': 15.0
}

# Irrelevant string processing (distractor)
device_tag = "ENV-SENSOR-PROD"
status_flag = device_tag.lower().replace('-', '_').split('_')
activation_code = ''.join([part[0] for part in status_flag])

# Data preprocessing with filtering logic
filtered_data = []
for i in range(len(temperature_readings)):
    temp_ok = temperature_readings[i] >= threshold_map['high_temp']
    humid_ok = humidity_readings[i] <= threshold_map['low_humidity']
    wind_high = wind_speed_readings[i] >= threshold_map['wind_alert']
    
    # Only include readings where temp is high OR (low humidity AND high wind)
    if temp_ok or (humid_ok and wind_high):
        entry = {
            'idx': i,
            't': round(temperature_readings[i], 1),
            'h': humidity_readings[i],
            'w': wind_speed_readings[i],
            'p': pressure_readings[i]
        }
        filtered_data.append(entry)

# Secondary distractor: dead-end analysis
anomaly_count = 0
for reading in filtered_data:
    if reading['h'] < 40:
        anomaly_count += 1

# Unused recursive helper (red herring)
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n - 2) + calculate_depth(n - 1) if n < 10 else n // 2

# Real processing function with multiple steps
def analyze_pressure_stability(data_chunk):
    if not data_chunk:
        return 0.0
    pressures = [item['p'] for item in data_chunk]
    avg_pressure = sum(pressures) / len(pressures)
    variance = sum((p - avg_pressure) ** 2 for p in pressures) / len(pressures)
    return round(math.sqrt(variance), 3)

# Character counting distractor
reference_text = "Environmental Diagnostic Suite v2.1"
char_frequency = {}
for char in reference_text:
    if char.isalpha():
        char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1

vowel_count = sum(char_frequency[v] for v in 'aeiou' if v in char_frequency)

# Main diagnostic processor
def process_readings(data, thresholds):
    if not data:
        return -1
    
    # Step 1: Count qualifying entries
    count = len(data)
    
    # Step 2: Compute average temperature
    avg_temp = sum(item['t'] for item in data) / count
    
    # Step 3: Count high-wind instances
    high_wind_events = sum(1 for item in data if item['w'] >= thresholds['wind_alert'])
    
    # Step 4: Pressure stability index (from earlier function)
    stability_index = analyze_pressure_stability(data)
    
    # Step 5: Base score calculation
    base_score = avg_temp * 10 + high_wind_events * 5
    
    # Step 6: Apply penalty for instability
    penalty = int(stability_index * 10)
    adjusted_score = base_score - penalty
    
    # Step 7: Map to diagnostic level using conditional expression
    diagnostic_level = 5 if adjusted_score >= 230 else (
        4 if adjusted_score >= 200 else (
            3 if adjusted_score >= 170 else (
                2 if adjusted_score >= 140 else 1
            )
        )
    )
    
    # Step 8: Final diagnostic code generation
    final_code = (diagnostic_level * 1000) + (high_wind_events * 10) + (count % 10)
    
    return final_code

# Execute critical statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result
print(f"Target result: {final_diagnostic}")