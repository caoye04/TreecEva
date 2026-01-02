import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 51, 49]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014]

# Irrelevant backup readings (distractor)
backup_temp_history = [
    [22.3, 23.1], [24.0, 24.2], [23.8, 23.9], [24.9, 25.1],
    [26.0, 26.5], [26.9, 27.3], [25.5, 26.0], [24.4, 24.9], [23.6, 24.0]
]

# Noise calibration factors (mostly irrelevant)
calibration_factors = {"sensor_a": 1.02, "sensor_b": 0.99, "sensor_c": 1.01}
adjusted_factors = {k: v * 0.98 for k, v in calibration_factors.items()}

# Thresholds for anomaly detection (used later)
threshold_map = {
    'temp_high': 26.0,
    'temp_low': 23.0,
    'humidity_spike': 55,
    'pressure_drift': 1016
}

# Auxiliary function – actual processing logic
def smooth_data(data, window=2):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Unused decoy function (red herring)
def predict_future(readings, steps=1):
    # This is never called but looks important
    trend = sum(readings[i] - readings[i-1] for i in range(1, len(readings))) / (len(readings) - 1)
    return [readings[-1] + trend * i for i in range(1, steps+1)]

# Data normalization (only partially used)
def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Real processing chain
filtered_temps = [t for t in temperature_readings if threshold_map['temp_low'] <= t <= threshold_map['temp_high']]
avg_temp = sum(filtered_temps) / len(filtered_temps)

# Apply smoothing to all sensor streams (some used, some not)
smoothed_temp = smooth_data(temperature_readings)
smoothed_humidity = smooth_data(humidity_readings, window=3)
smoothed_pressure = smooth_data(pressure_readings)

# Compute rolling variance (distractor computation)
variance_snapshot = []
for i in range(2, len(smoothed_temp)):
    mean_win = sum(smoothed_temp[i-2:i+1]) / 3
    var = sum((x - mean_win)**2 for x in smoothed_temp[i-2:i+1]) / 3
    variance_snapshot.append(var)

# Extract key phase indicators
phase_markers = []
for i, temp in enumerate(smoothed_temp):
    if temp > threshold_map['temp_high']:
        phase_markers.append((i, 'overheat'))
    elif temp < threshold_map['temp_low']:
        phase_markers.append((i, 'chill'))
    else:
        phase_markers.append((i, 'stable'))

# Build processed data structure with multiple red herrings
processed_data = {
    'primary_temp': smoothed_temp,
    'aux_humidity': normalize_readings(humidity_readings),
    'raw_pressure': pressure_readings,  # unused
    'smoothed_pressure': smoothed_pressure,
    'anomalies': [],
    'flags': {},
    'metadata': {
        'source': 'station_7b',
        'calibrated': True,
        'version': '2.3'
    }
}

# Add detected anomalies based on humidity spikes and pressure drift
for i, hum in enumerate(smoothed_humidity):
    if hum > threshold_map['humidity_spike']:
        if smoothed_pressure[i] > threshold_map['pressure_drift']:
            processed_data['anomalies'].append({
                'index': i,
                'type': 'compound_stress',
                'severity': (hum - 50) * (smoothed_pressure[i] - 1010)
            })
        else:
            processed_data['anomalies'].append({
                'index': i,
                'type': 'humidity_rise',
                'severity': hum - 50
            })

# Flag stable temperature zones
stable_zones = []
zone_start = None
for i, (_, status) in enumerate(phase_markers):
    if status == 'stable' and zone_start is None:
        zone_start = i
    elif status != 'stable' and zone_start is not None:
        stable_zones.append((zone_start, i-1))
        zone_start = None
if zone_start is not None:
    stable_zones.append((zone_start, len(phase_markers)-1))

processed_data['flags']['stable_ranges'] = stable_zones
processed_data['flags']['peak_temp_index'] = smoothed_temp.index(max(smoothed_temp))

# Decoy statistical summary (never used)
stat_summary = {
    'temp_stats': {
        'mean': sum(smoothed_temp) / len(smoothed_temp),
        'std': math.sqrt(sum((x - avg_temp)**2 for x in smoothed_temp) / len(smoothed_temp)),
        'trend': smoothed_temp[-1] - smoothed_temp[0]
    },
    'humidity_stats': {
        'median': sorted(smoothed_humidity)[len(smoothed_humidity)//2],
        'range': max(smoothed_humidity) - min(smoothed_humidity)
    }
}

# Core analysis function that determines final output
def analyze_readings(data, thresholds):
    primary = data['primary_temp']
    anomalies = data['anomalies']
    flags = data['flags']
    
    # Diagnostic score components
    base_score = 100.0
    
    # Penalty for high temperature occurrences
    high_temp_indices = [i for i, t in enumerate(primary) if t > thresholds['temp_high']]
    if high_temp_indices:
        base_score -= len(high_temp_indices) * 5.5
    
    # Bonus for long stable zones
    for start, end in flags.get('stable_ranges', []):
        duration = end - start + 1
        if duration >= 3:
            base_score += 3.0
    
    # Penalty for compound anomalies
    compound_count = sum(1 for a in anomalies if a['type'] == 'compound_stress')
    base_score -= compound_count * 8.2
    
    # Adjustment based on peak location
    peak_idx = flags['peak_temp_index']
    if peak_idx < len(primary) // 3:
        base_score -= 4.0  # Early peak = instability
    elif peak_idx >= 2 * len(primary) // 3:
        base_score += 2.0  # Late peak = controlled rise
    
    # Final adjustment using humidity trend near end
    late_humidity = smoothed_humidity[-3:]
    hum_trend = late_humidity[-1] - late_humidity[0]
    if hum_trend > 3:
        base_score -= 6.0  # Rapid increase
    elif hum_trend < -3:
        base_score -= 3.0  # Rapid decrease
    
    return round(base_score, 4)

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Irrelevant slicing operations (distractor)
decoy_slice_1 = backup_temp_history[2:7:2]
decoy_slice_2 = temperature_readings[::-1][:4]

# Unused dictionary aggregation (dead path)
aggregate_diagnostics = {}
for sensor_type in ['temp', 'humidity', 'pressure']:
    aggregate_diagnostics[sensor_type] = {
        'count': len(locals().get(sensor_type + '_readings', [])),
        'adjusted': False
    }

# Print final answer as required
print(f"Result: {final_diagnostic}")