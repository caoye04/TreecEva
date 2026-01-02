import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 54, 51]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014]

# Irrelevant backup log (distractor)
backup_logs = ['OK', 'SYNCED', 'PENDING', 'ERROR', 'RESOLVED', 'OK', 'OK', 'FAILED', 'IGNORED']
last_backup_status = backup_logs[-1]  # Decoy usage

# Data transformation pipeline
filtered_temps = [t for t in temperature_readings if 20 <= t <= 30]
scaled_humidity = [h * 1.2 for h in humidity_readings if h > 40]

# Complex normalization function (partially irrelevant)
def normalize_pressure(pressure_list):
    avg = sum(pressure_list) / len(pressure_list)
    return [(p - avg) / avg * 100 for p in pressure_list]

normalized_pressure = normalize_pressure(pressure_readings)

# Unused transformation chain (dead code path)
def transform_sequence(seq):
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append(val * 1.1)
        else:
            result.append(math.log(abs(val) + 1))
    return result

transformed_humidity = transform_sequence(humidity_readings)  # Computed but unused

# Threshold configuration map (critical)
threshold_map = {
    'temp_high': 25.5,
    'temp_low': 24.0,
    'humidity_critical': 57,
    'pressure_stable': 1015
}

# Historical reference window (distractor)
historical_averages = {
    'summer_avg_temp': 24.8,
    'summer_avg_hum': 52,
    'baseline_pressure': 1014.2
}

# Data processing core
rolling_window_size = 3
def smooth_data(data, window=rolling_window_size):
    smoothed = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        smoothed.append(round(window_avg, 2))
    return smoothed

smoothed_temps = smooth_data(filtered_temps)

# Advanced pattern detection (red herring)
def detect_outlier_spikes(data, factor=1.5):
    Q1 = sorted(data)[len(data)//4]
    Q3 = sorted(data)[-len(data)//4]
    IQR = Q3 - Q1
    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR
    return [x for x in data if x < lower_bound or x > upper_bound]

spikes = detect_outlier_spikes(temperature_readings)  # Calculated but not used

# Primary processing function
def process_sensor_data(temp, hum, press):
    # Step 1: Create composite index
    composite_index = []
    for t, h, p in zip(temp, hum, press):
        index_val = (t * 0.4) + (h * 0.3) + ((p - 1000) * 0.3)
        composite_index.append(index_val)
    
    # Step 2: Slice middle section (relevant slicing)
    mid_section = composite_index[2:7]
    
    # Step 3: Map to risk levels
    risk_levels = []
    for val in mid_section:
        if val > 75:
            risk_levels.append('HIGH')
        elif val > 65:
            risk_levels.append('ELEVATED')
        else:
            risk_levels.append('NORMAL')
    
    # Step 4: Count transitions
    transitions = 0
    for i in range(1, len(risk_levels)):
        if risk_levels[i] != risk_levels[i-1]:
            transitions += 1
    
    # Step 5: Generate diagnostic vector
    diagnostic_vector = []
    for i, raw_t in enumerate(temp):
        phase_angle = math.sin(i * math.pi / 4)
        adjusted = raw_t * (1 + phase_angle * 0.1)
        diagnostic_vector.append(adjusted)
    
    # Step 6: Extract pattern using string method on encoded state (satisfies requirement)
    state_code = ''.join([str(int(d > 24)) for d in diagnostic_vector[:6]])
    pattern_count = state_code.count('101')  # Uses string method
    
    # Step 7: Build result dictionary (dictionary operations)
    result = {
        'composite_mid_avg': sum(mid_section) / len(mid_section),
        'risk_transitions': transitions,
        'diagnostic_sum': sum(diagnostic_vector),
        'pattern_frequency': pattern_count,
        'data_integrity': len(temp) == len(hum) == len(press)
    }
    
    return result

# Execute main processing
processed_data = process_sensor_data(
    temperature_readings, 
    humidity_readings, 
    pressure_readings
)

# Secondary analysis function
def analyze_readings(data_dict, thresholds):
    # Extract values
    temp_high_trigger = data_dict['composite_mid_avg'] > thresholds['temp_high']
    humidity_alert = data_dict['risk_transitions'] >= 3
    
    # Hidden calculation: uses dictionary lookup and comparison
    base_score = data_dict['diagnostic_sum']
    adjustment_factor = 0.8 if data_dict['pattern_frequency'] > 0 else 1.2
    
    # Complex conditional expression
    severity_level = (
        3 if temp_high_trigger and humidity_alert else
        2 if temp_high_trigger or humidity_alert else
        1
    )
    
    # Bit manipulation red herring
    status_flag = 0b1010
    mask = 0b1100
    masked_result = status_flag & mask  # Computed but mostly irrelevant
    
    # Decoy list operations
    dummy_list = [10, 20, 30, 40]
    shifted = dummy_list[1:] + dummy_list[:1]  # Dead code
    
    # Final diagnostic computation (this is the real answer)
    final_score = base_score * adjustment_factor
    penalty = severity_level * 5.5
    
    # Critical statement
    final_diagnostic = final_score - penalty
    
    return final_diagnostic

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")