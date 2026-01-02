import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 52, 58, 61, 54, 49, 53]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1010, 1014, 1016]

# Irrelevant auxiliary metrics (distractors)
luminosity_log = [890, 910, 875, 903, 888, 895, 901, 897]
wind_speed_buffer = [3.2, 3.8, 4.1, 3.6, 3.0, 3.9, 4.2, 3.7]

# Preprocessing: Normalize temperature into z-scores (used)
def normalize_temperatures(data):
    mean_temp = sum(data) / len(data)
    variance = sum((x - mean_temp) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean_temp) / std_dev for x in data]

# Dead function - never called (red herring)
def calculate_wind_chill(temps, winds):
    chill_index = []
    for t, w in zip(temps, winds):
        chill = 13.12 + 0.6215*t - 11.37*(w**0.16) + 0.3965*t*(w**0.16)
        chill_index.append(round(chill, 2))
    return chill_index

# Unused transformation (distractor code path)
adjusted_humidity = [h * 1.02 for h in humidity_readings if h > 50]
adjusted_humidity = [round(x, 1) for x in adjusted_humidity]

# Mapping sensors to calibration offsets (dictionary operation - relevant)
calibration_map = {
    'temp': 0.8,
    'humidity': -2.1,
    'pressure': 3.5
}

# Apply calibration (only temp used later)
calibrated_temps = [t + calibration_map['temp'] for t in temperature_readings]

def apply_noise_filter(signal, strength=0.9):
    # Simulates signal smoothing but not actually used in final path
    filtered = []
    for i in range(len(signal)):
        if i == 0:
            filtered.append(signal[i])
        else:
            filtered.append(round(strength * signal[i] + (1-strength) * filtered[i-1], 2))
    return filtered

# Falsely appears important - generates alternate data path that's unused
smoothed_temps = apply_noise_filter(calibrated_temps)

# Composite processing with dictionary packing (relevant)
raw_data_packets = []
for i in range(len(temperature_readings)):
    packet = {
        'id': i + 1000,
        'temp_raw': round(temperature_readings[i], 2),
        'temp_cal': round(calibrated_temps[i], 2),
        'humidity': humidity_readings[i],
        'pressure': pressure_readings[i],
        'anomaly_flag': False
    }
    # Introduce synthetic anomaly detection (partially used)
    if packet['temp_cal'] > 26.0 or packet['humidity'] > 60:
        packet['anomaly_flag'] = True
    raw_data_packets.append(packet)

# Linear search for high-risk entries (dead code - not used later)
high_risk_packets = []
for pkt in raw_data_packets:
    if pkt['anomaly_flag'] and pkt['pressure'] < 1010:
        high_risk_packets.append(pkt['id'])

# Data summarization using dictionary grouping (irrelevant distractor)
summary_stats = {}
for key in ['temp_raw', 'humidity', 'pressure']:
    values = [p[key] for p in raw_data_packets]
    summary_stats[key] = {
        'min': min(values),
        'max': max(values),
        'avg': round(sum(values)/len(values), 2)
    }

# Critical preprocessing step: identify outliers in calibrated temps
z_scores = normalize_temperatures(calibrated_temps)
outlier_indices = [i for i, z in enumerate(z_scores) if abs(z) > 1.5]

# Mark outliers in packets
for i in outlier_indices:
    raw_data_packets[i]['anomaly_flag'] = True  # May override previous flag

# Extract only necessary field for next stage
processed_data = [p['temp_cal'] for p in raw_data_packets]

# Threshold configuration map (dictionary - relevant)
threshold_map = {
    'warning_high': 25.5,
    'critical_high': 26.5,
    'warning_low': 22.0,
    'critical_low': 21.0,
    'hysteresis': 0.5
}

# Diagnostic engine - analyzes sequence against thresholds
def analyze_readings(readings, limits):
    warnings = 0
    criticals = 0
    recovered = 0
    
    # State tracking
    in_critical_state = False
    last_state_duration = 0
    
    for temp in readings:
        current_state = None
        
        if temp >= limits['critical_high']:
            current_state = 'CRITICAL'
            criticals += 1
            in_critical_state = True
            last_state_duration = 0
        elif temp >= limits['warning_high']:
            current_state = 'WARNING'
            warnings += 1
            if in_critical_state:
                last_state_duration += 1
        elif temp <= limits['critical_low']:
            current_state = 'CRITICAL_COLD'
            criticals += 1
            in_critical_state = True
        elif temp <= limits['warning_low']:
            current_state = 'WARNING_COLD'
            warnings += 1
        else:
            current_state = 'NORMAL'
            if in_critical_state:
                recovered += 1
            in_critical_state = False
            last_state_duration = 0
            
        # Hysteresis logic prevents rapid oscillation reporting
        if in_critical_state and last_state_duration > 0:
            if temp < limits['critical_high'] - limits['hysteresis']:
                in_critical_state = False

    # Compute diagnostic score (deterministic formula)
    base_score = (criticals * 100) + (warnings * 10) - (recovered * 5)
    adjustment = len(outlier_indices) * 7  # Uses outer-scope variable
    final_score = base_score + adjustment
    
    # Additional irrelevant computation (distraction)
    avg_reading = sum(readings) / len(readings)
    variance = sum((x - avg_reading)**2 for x in readings) / len(readings)
    stability_index = round(100 / (math.sqrt(variance) + 1), 2)
    
    return int(final_score)

# Execute main analysis
temp_snapshot = [x for x in processed_data]  # Redundant copy
baseline_check = sum(temp_snapshot) / len(temp_snapshot)

# Key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")