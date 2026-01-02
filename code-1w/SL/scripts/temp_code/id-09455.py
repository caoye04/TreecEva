import math

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8]
humidity_readings = [55, 58, 60, 62, 59, 57, 61]
co2_levels = [410, 415, 420, 425, 430, 435, 440]

# Irrelevant backup logs (distractor)
backup_logs = ['log_2023_01', 'log_2023_02', 'log_2023_03']
last_backup = '2023-02-15'

# Preprocessing: Normalize temperature to z-scores (relevant)
def normalize(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean_val) / std_dev for x in data]

# Misleading function: appears useful but unused (dead code path)
def legacy_calibrate(values):
    adjusted = []
    for v in values:
        if v > 400:
            adjusted.append(v * 0.95)
        else:
            adjusted.append(v * 1.02)
    return adjusted  # Never called

# Another red herring: complex string-based encoding of metadata
sensor_location = 'GRID-7B-NW'
sensor_id_hash = hash(sensor_location)
location_code = ''.join([chr(ord(c) + 2) for c in sensor_location])  # Transforms to 'ITGFB9D-PY'

# Real signal processing begins here
normalized_temp = normalize(temperature_readings)

# Compute rolling average of CO2 over 3-day window (relevant)
def rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

co2_trend = rolling_average(co2_levels)

# Extract mid-segment of humidity using slicing (relevant)
humidity_slice = humidity_readings[2:5]  # [60, 62, 59]

# Create diagnostic tuple with multiple metrics (relevant)
base_metric = sum(normalized_temp[:4])
trend_strength = abs(co2_trend[-1] - co2_trend[0])
variability_index = max(humidity_slice) - min(humidity_slice)

# Decoy dictionary with plausible but unused diagnostics
unused_diagnostics = {
    'stability': 'moderate',
    'noise_floor': 0.03,
    'outlier_count': 2,
    'calibration_age_days': 17
}

# Real processing pipeline
processing_flags = {
    'normalize': True,
    'filter_outliers': False,
    'apply_weights': True
}

# Simulated weighting schema (only some weights are used)
feature_weights = {
    'temp_z': 0.4,
    'co2_trend': 0.35,
    'humidity_var': 0.25,
    'phantom_feature': 0.0  # Deliberately zero-weighted (misleading)
}

# Apply actual transformation to create processed_data
processed_data = []
for i in range(len(normalized_temp)):
    entry = {
        't_z': normalized_temp[i],
        'weighted_shift': co2_levels[i] * 0.01,
        'day_label': f'Day_{i+1}',
        'is_peak_temp': abs(normalized_temp[i]) > 0.5
    }
    processed_data.append(entry)

# Secondary transformation: extract and reverse certain labels (string method use)
day_labels = [entry['day_label'] for entry in processed_data]
reversed_labels = [label[::-1] for label in day_labels]  # e.g., 'yad_1' → distractor

# Extract number of peaks (relevant)
peak_count = sum(1 for entry in processed_data if entry['is_peak_temp'])

# Auxiliary calculation: character count across reversed labels (red herring)
total_chars = sum(len(label) for label in reversed_labels)
mean_char_length = total_chars / len(reversed_labels)  # Not used

# Core analysis function
def analyze_signal(signal_list):
    # Use dictionary operations and slicing on signal
    recent_signals = signal_list[-3:]  # Last three entries
    
    # Aggregate key numeric indicators
    z_sum = sum(entry['t_z'] for entry in signal_list)
    shift_total = sum(entry['weighted_shift'] for entry in recent_signals)
    
    # Boolean logic with short-circuiting
    has_high_z = any(entry['t_z'] > 0.8 for entry in signal_list)
    has_recent_peak = any(entry['is_peak_temp'] for entry in recent_signals)
    
    # Control flow with nesting depth 3
    if has_high_z or (has_recent_peak and processing_flags['apply_weights']):
        if z_sum > 0:
            if shift_total > 12.5:
                multiplier = 1.75
            else:
                multiplier = 1.25
        else:
            multiplier = 0.85
    else:
        multiplier = 0.65
    
    # Final computation combining multiple concepts
    base_score = z_sum * 10 + peak_count * 5
    final_score = base_score * multiplier
    
    # Additional distraction: unused complex tuple unpacking
    if len(signal_list) >= 5:
        first, *middle, last = [entry['t_z'] for entry in signal_list]
        median_like = middle[len(middle)//2]
        # This is computed but not used in final result
    
    # The true answer derivation
    adjustment = math.sin(math.pi * peak_count / 4)  # Trigonometric adjustment
    final_diagnostic = round(final_score + adjustment * 10, 4)
    
    return final_diagnostic

# Execute main analysis
target_result = analyze_signal(processed_data)
print(f"Target result: {target_result}")