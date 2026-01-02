import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 19.0, 27.3, 30.1, 18.9, 22.4, 25.0, 26.7, 20.2, 31.5]
humidity_readings = [45, 52, 60, 67, 40, 58, 70, 63, 55, 72]
pressure_readings = [1013, 1009, 1015, 1008, 1017, 1012, 1005, 1010, 1007, 1014]

# Irrelevant auxiliary arrays (distractors)
elevation_data = [120, 205, 80, 30, 250, 140, 60, 95, 180, 10]
wind_speed_kmh = [12, 18, 22, 30, 10, 15, 25, 20, 14, 33]

# Preprocessing: normalize readings to z-scores (some used, some not)
def z_score_normalize(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean_val) / std_dev for x in data]

norm_temps = z_score_normalize(temperature_readings)
norm_humidity = z_score_normalize(humidity_readings)
# norm_pressure unused intentionally (dead code path)
norm_pressure = z_score_normalize(pressure_readings)

# Threshold configuration map for anomaly detection
threshold_map = {
    'temp': {'low': -0.5, 'high': 0.8},
    'humidity': {'low': -0.6, 'high': 0.7},
    'combined_risk': 1.1
}

# Data fusion matrix (irrelevant transformation - distractor)
correlation_matrix = [
    [1.0, 0.4, -0.2],
    [0.4, 1.0, 0.1],
    [-0.2, 0.1, 1.0]
]

# Fused risk score calculation (unused - red herring)
def compute_fused_risk(temp_z, hum_z, press_z):
    weights = [0.5, 0.3, 0.2]
    return abs(weights[0]*temp_z + weights[1]*hum_z + weights[2]*press_z)

# Generate combined dataset with metadata
sensor_data = []
for i in range(len(temperature_readings)):
    entry = {
        'id': f'SEN{i+1:02d}',
        'temp': temperature_readings[i],
        'humidity': humidity_readings[i],
        'elev': elevation_data[i],
        'wind': wind_speed_kmh[i],
        'temp_z': norm_temps[i],
        'hum_z': norm_humidity[i],
        'risk_flag': False
    }
    # Compute derived metrics (some influence final result)
    entry['heat_index'] = entry['temp'] + 0.5 * entry['humidity']
    entry['vapor_pressure'] = 6.11 * (10**(7.5*entry['temp']/(237.7+entry['temp']))) * (entry['humidity']/100)
    sensor_data.append(entry)

# Filtering based on elevation and wind (partially relevant preprocessing)
filtered_stations = [s for s in sensor_data if s['elev'] > 50 and s['wind'] < 30]

# Extract filtered raw values for analysis
filtered_data = [(s['temp'], s['humidity']) for s in filtered_stations]

# Auxiliary statistical measures (mostly irrelevant)
avg_temp_filtered = sum(x[0] for x in filtered_data) / len(filtered_data)
stdev_temp_filtered = math.sqrt(sum((x[0] - avg_temp_filtered)**2 for x in filtered_data) / len(filtered_data))

def analyze_readings(readings, thresholds):
    # Local normalization within filtered set
    temp_vals = [r[0] for r in readings]
    hum_vals = [r[1] for r in readings]
    
    # Compute z-scores again locally (redundant but plausible)
    temp_mean = sum(temp_vals) / len(temp_vals)
    hum_mean = sum(hum_vals) / len(hum_vals)
    temp_z_scores = [(t - temp_mean) for t in temp_vals]  # simplified deviation
    hum_z_scores = [(h - hum_mean) for h in hum_vals]
    
    # Anomaly detection using threshold map
    temp_anomalies = [abs(z) > thresholds['temp']['high'] for z in temp_z_scores]
    hum_anomalies = [abs(z) > thresholds['humidity']['high'] for z in hum_z_scores]
    
    # Combined extremity index (key computation)
    combined_extremity = [
        math.sqrt(temp_z_scores[i]**2 + hum_z_scores[i]**2)
        for i in range(len(temp_z_scores))
    ]
    
    # Secondary filter: high combined deviation
    extreme_indices = [i for i, ce in enumerate(combined_extremity) if ce > thresholds['combined_risk']]
    
    # Diagnostic scoring logic
    base_score = 100
    for i in range(len(combined_extremity)):
        if i in extreme_indices:
            base_score += int(combined_extremity[i] * 15)
        elif temp_anomalies[i] or hum_anomalies[i]:
            base_score += 5
        else:
            base_score -= 2
    
    # Irrelevant adjustment using vapor pressure formula (distractor)
    adjustment_factor = 0
    for s in sensor_data:
        vp = s['vapor_pressure']
        if vp > 20:
            adjustment_factor += 0.1  # Never actually applied
    
    # Final diagnostic includes length-based bonus (subtle but valid)
    length_bonus = len(readings) * 3
    final_score = base_score + length_bonus
    
    # Dead code: risk propagation simulation (never executed)
    '''
    propagation_model = {}
    for i in range(len(readings)-1):
        diff = abs(combined_extremity[i] - combined_extremity[i+1])
        propagation_model[f'flow_{i}'] = diff * 0.75
    '''
    
    return int(final_score)

# Critical execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")