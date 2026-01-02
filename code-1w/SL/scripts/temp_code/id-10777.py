import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 19.5, 27.8, 22.1, 31.0, 18.9, 25.6, 24.3, 20.2, 26.7, 28.9, 17.6]
humidity_readings = [45, 53, 38, 61, 33, 58, 49, 44, 56, 41, 37, 62]
pressure_readings = [1013, 1009, 1015, 1007, 1018, 1005, 1011, 1014, 1008, 1012, 1006, 1019]

# Auxiliary irrelevant data (distractor)
sound_levels = [65, 70, 58, 80, 72, 63, 68, 75, 59, 67, 74, 69]
lux_values = [12000, 9500, 14000, 8700, 15000, 8200, 11000, 12500, 9000, 11800, 8500, 13000]

# Threshold configurations for anomaly detection
threshold_map = {
    'temp': {'min': 18.0, 'max': 30.0},
    'humidity': {'min': 35, 'max': 60},
    'pressure': {'min': 1000, 'max': 1020}
}

# Irrelevant transformation chain (dead code path)
def transform_sound_levels(levels):
    return [round(20 * math.log10(x + 1)) for x in levels if x > 60]

transformed_noise = transform_sound_levels(sound_levels)  # Unused result

# Data alignment index mapping (distractor)
station_mapping = {i: f'S{i+1}' for i in range(len(temperature_readings))}
location_zones = ['North', 'South', 'East', 'West']
zone_assignment = {f'S{i+1}': location_zones[i % 4] for i in range(12)}

# Composite data packing (relevant and distractor mix)
sensor_data = []
for i in range(len(temperature_readings)):
    packet = (
        temperature_readings[i],
        humidity_readings[i],
        pressure_readings[i],
        sound_levels[i],        # Irrelevant field
        lux_values[i]           # Irrelevant field
    )
    sensor_data.append(packet)

# Filtering valid time windows based on secondary criteria (partially relevant)
event_flags = [True if h > 50 and t < 25 else False for t, h in zip(temperature_readings, humidity_readings)]
active_windows = [i for i, flag in enumerate(event_flags) if flag]

# Primary filtering operation (critical path)
filtered_indices = []
for idx in range(len(sensor_data)):
    temp, humid, press, _, _ = sensor_data[idx]
    if (threshold_map['temp']['min'] <= temp <= threshold_map['temp']['max'] and
        threshold_map['humidity']['min'] <= humid <= threshold_map['humidity']['max'] and
        threshold_map['pressure']['min'] <= press <= threshold_map['pressure']['max']):
        filtered_indices.append(idx)

filtered_data = [sensor_data[i] for i in filtered_indices]

# Decoy analysis function (never called)
def deprecated_diagnostic(data):
    anomalies = 0
    for entry in data:
        if abs(entry[2] - 1010) > 10:
            anomalies += 1
    return anomalies * 100

# Auxiliary statistical helper (used indirectly)
def moving_average(values, window=3):
    if len(values) < window:
        return values[:]
    return [sum(values[i:i+window]) / window for i in range(len(values) - window + 1)]

# Core analysis logic with set operations and conditional expressions
valid_temps = {round(temp) for temp, _, _, _, _ in filtered_data}
valid_humidities = {h for _, h, _, _, _ in filtered_data}

common_conditions = valid_temps & valid_humidities  # Intersection as rare condition indicator

# Conditional weighting based on pattern presence
base_score = sum(valid_temps) * 0.7
bonus = len(common_conditions) * 25 if common_conditions else len(valid_humidities) * 2
penalty = 0

for _, h, p, _, _ in filtered_data:
    # Complex conditional penalty rules
    deviation = 0
    if h < 40 or h > 55:
        deviation += 8
    if abs(p - 1013) > 5:
        deviation += 12
    penalty += deviation

# Secondary decoy calculation (misleading intermediate)
anomaly_index = 0
for i in range(len(humidity_readings)):
    if humidity_readings[i] > 60 and temperature_readings[i] < 20:
        anomaly_index += 1
anomaly_index *= 50  # Large but irrelevant number

# Final diagnostic computation (key statement)
def analyze_readings(data, thresholds):
    if not data:
        return 0.0
    
    # Extract components with unpacking
    temps = [d[0] for d in data]
    humids = [d[1] for d in data]
    pressures = [d[2] for d in data]
    
    # Statistical transformations
    avg_temp = sum(temps) / len(temps)
    avg_humid = sum(humids) / len(humids)
    stability_metric = sum([1 for p in pressures if abs(p - 1013) <= 2])
    
    # Conditional expression with nested logic
    adjustment = 1.25 if avg_temp < 24 and stability_metric >= 3 else (0.85 if avg_temp > 26 else 1.0)
    
    # Set-based uniqueness bonus
    unique_temp_count = len({round(t) for t in temps})
    diversity_bonus = 10 * unique_temp_count if unique_temp_count >= 4 else 5 * unique_temp_count
    
    # Final composition
    result = (avg_temp * 3.1) + (avg_humid * 1.8) + diversity_bonus - penalty * adjustment
    
    # Red herring rounding attempt
    if result > 100:
        result = round(result, 1)
    else:
        result = round(result, 2)
    
    return result

# Execution point of interest
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")