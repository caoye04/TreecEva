import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 61, 48, 55, 59, 43, 50, 54]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017, 1013]

# Irrelevant auxiliary constants (distractors)
CALIBRATION_OFFSET = 0.789
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256
TEMPORARY_FLAG = False

# Mapping thresholds for different zones (used in final computation)
threshold_map = {
    'zone_A': {'temp_min': 20.0, 'temp_max': 25.0, 'humidity_weight': 0.6},
    'zone_B': {'temp_min': 18.0, 'temp_max': 26.0, 'humidity_weight': 0.4}
}

# Decoy function – looks important but unused in critical path
def calibrate_sensor(data, offset=0.1):
    return [round(x + offset, 2) for x in data]

# Another decoy – simulates noise filtering but not used
noise_profile = [0.1, -0.2, 0.05, 0.15, -0.1]
smoothed_noise = list(itertools.accumulate(noise_profile))

# Real preprocessing: align and combine sensor streams using zip and enumerate
aligned_readings = []
for i, (t, h, p) in enumerate(zip(temperature_readings, humidity_readings, pressure_readings)):
    aligned_readings.append({
        'index': i,
        'temp': t,
        'humidity': h,
        'pressure': p,
        'score': abs(t - 22.5) * 2 + (100 - h) / 10  # composite score
    })

# Filtering logic with misleading intermediate steps
outlier_indices = []
high_pressure_events = 0  # red herring counter

for entry in aligned_readings:
    if entry['temp'] < 20 or entry['temp'] > 26:
        outlier_indices.append(entry['index'])
    if entry['pressure'] > 1015:
        high_pressure_events += 1  # tracked but irrelevant

# Actual filter uses only temperature bounds from zone_A
valid_range = (threshold_map['zone_A']['temp_min'], threshold_map['zone_A']['temp_max'])
filtered_data = [r for r in aligned_readings if valid_range[0] <= r['temp'] <= valid_range[1]]

# Dead code path – never executed due to prior filtering (misleading)
if TEMPORARY_FLAG:
    for item in filtered_data:
        item['corrected'] = item['temp'] + CALIBRATION_OFFSET

# Auxiliary transformation with itertools – creates distraction
indexed_pairs = list(itertools.combinations([r['index'] for r in filtered_data], 2))
distance_metrics = []
for a, b in indexed_pairs:
    diff = abs(temperature_readings[a] - temperature_readings[b])
    distance_metrics.append(round(diff, 3))

# Core processing function that computes final diagnostic
def process_readings(readings, thresholds):
    zone_a = thresholds['zone_A']
    total_weighted_deviation = 0.0
    base_count = len(readings)

    for reading in readings:
        temp_mid = (zone_a['temp_min'] + zone_a['temp_max']) / 2
        temp_dev = abs(reading['temp'] - temp_mid)
        humid_score = reading['humidity'] * zone_a['humidity_weight']
        
        # Combined deviation metric
        weighted_dev = temp_dev * 1.2 + (humid_score / 10)
        total_weighted_deviation += weighted_dev

        # Early termination red herring (never triggers due to data)
        if reading['humidity'] == 0:
            return -999

    # Final aggregation with integer division effect
    if base_count == 0:
        return 0
    
    average_deviation = total_weighted_deviation / base_count
    scaled_index = int(average_deviation * 100) // 2  # integer division impact
    
    # Apply secondary adjustment based on pressure trend (only last three matter)
    recent_pressures = pressure_readings[-3:]
    pressure_trend = sum(recent_pressures) / len(recent_pressures) - 1013
    adjusted_result = scaled_index + int(abs(pressure_trend) * 5)
    
    return round(adjusted_result, 4)

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output the result as required
print(f"Target result: {final_diagnostic}")