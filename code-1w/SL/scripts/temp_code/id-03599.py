import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.3, 26.0, 24.7, 23.9, 25.1]
humidity_readings = [45, 47, 50, 52, 48, 55, 60, 53]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant backup readings (distractor)
backup_temperature = [23.4, 24.0, 22.7, 25.2]  
backup_humidity = [46, 48, 51, 54]

# Noise calibration factors (partially used, misleading)
noise_floor = 0.15
amplification_factor = 1.08

def calibrate_sensor(value, sensor_type):
    if sensor_type == 'temp':
        return (value + noise_floor) * amplification_factor
    elif sensor_type == 'humid':
        return value * 1.02
    return value

# Apply calibration to main readings only
processed_temps = [calibrate_sensor(t, 'temp') for t in temperature_readings]
processed_humids = [calibrate_sensor(h, 'humid') for h in humidity_readings]

# Combine into structured data
sensor_data = []
for i in range(len(temperature_readings)):
    sensor_data.append({
        'index': i,
        'temp': processed_temps[i],
        'humid': processed_humids[i],
        'press': pressure_readings[i]
    })

# Distractor: Unused function that looks important
def validate_checksum(data_list):
    checksum = 0
    for d in data_list:
        checksum ^= int(d.get('temp', 0) * 10)
    return checksum % 17

# Another red herring: historical baseline comparison (unused)
historical_avg_temp = 24.0
historical_avg_humid = 50

# Real processing begins here
threshold_map = {
    'temp_high': 25.0,
    'temp_low': 23.0,
    'humid_high': 55,
    'stable_pressure_range': (-3, 3)
}

# Misleading transformation: normalized scores (only partially relevant)
normalized_readings = []
for entry in sensor_data:
    norm_entry = {
        'idx': entry['index'],
        't_score': (entry['temp'] - 23.0) / 3.0,
        'h_score': abs(entry['humid'] - 50) / 10.0,
        'p_ref': entry['press'] - pressure_readings[0]  # deviation from start
    }
    normalized_readings.append(norm_entry)

# Secondary distractor: bitmask analysis of pressure stability (unused result)
pressure_devs = [nr['p_ref'] for nr in normalized_readings]
stability_bitmask = 0
for i, dev in enumerate(pressure_devs):
    if threshold_map['stable_pressure_range'][0] <= dev <= threshold_map['stable_pressure_range'][1]:
        stability_bitmask |= (1 << i)

# Actual data processing pipeline
anomaly_flags = []
drift_accumulator = 0.0

for reading in sensor_data:
    temp = reading['temp']
    humid = reading['humid']
    
    # Temporal drift simulation (only affects accumulator, minor role)
    drift_accumulator += (temp - historical_avg_temp) * 0.05
    
    flag_set = set()
    if temp > threshold_map['temp_high']:
        flag_set.add('overheat')
    if temp < threshold_map['temp_low']:
        flag_set.add('chill')
    if humid > threshold_map['humid_high']:
        flag_set.add('muggy')
    
    anomaly_flags.append(flag_set)

# Processed data structure with filtered relevance
processed_data = []
for i, flags in enumerate(anomaly_flags):
    impact_score = len(flags) * 1.5
    if 'overheat' in flags:
        impact_score += 0.7
    if 'muggy' in flags:
        impact_score += 0.5
    
    # Add only entries with anomalies to processed data (filtering)
    if flags:
        processed_data.append({
            'location_id': i + 100,
            'severity': impact_score,
            'flags': flags
        })

# Distractor: unused aggregation
average_anomaly_severity = sum([item['severity'] for item in processed_data]) / len(processed_data) if processed_data else 0

# Critical function: computes final diagnostic using specific logic
valid_locations = {102, 103, 105, 107}  # Known sensitive zones

# Decoy list comprehension (looks like it's used)
[c for c in processed_data if c['location_id'] in valid_locations]

# This is the actual key computation
weighted_sum = 0.0
for record in processed_data:
    loc_weight = 1.0
    if record['location_id'] in valid_locations:
        loc_weight = 2.5
    weighted_sum += record['severity'] * loc_weight

# Final diagnostic calculation
baseline_offset = 12.5
final_diagnostic = math.floor(weighted_sum + baseline_offset - drift_accumulator)

# Output the target result
Result: {final_diagnostic}