import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [45, 48, 52, 58, 61, 57, 54, 50]
co2_levels = [410, 415, 420, 430, 450, 470, 500, 520]

# Irrelevant backup readings (distractor)
backup_temp_history = [
    [23.4, 24.0, 22.9], [25.1, 26.2, 27.0], [25.9, 24.8, 23.7]
]

# Misleading intermediate calculation (dead path)
avg_backup_temp = sum(sum(row) for row in backup_temp_history) / sum(len(row) for row in backup_temp_history)

# Real processing begins
normalized_temps = [round((t - 20) / 5, 2) for t in temperature_readings]
high_co2_indices = {i for i, co2 in enumerate(co2_levels) if co2 > 450}

# Destructuring assignment with dummy variables
(*ambient_data, last_temp) = temperature_readings
(*_, peak_humidity) = humidity_readings

# Complex conditional mapping
risk_flags = []
for i, temp in enumerate(normalized_temps):
    if i in high_co2_indices:
        if temp > 1.0:
            risk_flags.append('CRITICAL')
        elif temp > 0.5:
            risk_flags.append('WARNING')
        else:
            risk_flags.append('ELEVATED')
    elif temp > 1.2:
        risk_flags.append('MODERATE')
    else:
        risk_flags.append('NORMAL')

# Decoy function (never called)
def calculate_air_quality_legacy(humidity_list, co2_list):
    base_score = 100
    for h, c in zip(humidity_list, co2_list):
        if h < 40 or h > 60:
            base_score -= 5
        if c > 500:
            base_score -= 10
    return max(base_score, 0)

# Dictionary construction with red herring keys
threshold_map = {
    'temp_norm_upper': 1.2,
    'temp_norm_lower': 0.4,
    'co2_critical': 500,
    'humidity_optimal_min': 45,
    'humidity_optimal_max': 55,
    'dummy_offset': 999,  # distractor
    'placeholder_matrix': [[1,0],[0,1]],  # irrelevant
    'scaling_factor_zeta': 0.87  # misleading unused parameter
}

# Data transformation with list comprehension and filtering
processed_data = [
    {
        'idx': idx,
        'norm_temp': nt,
        'raw_temp': rt,
        'co2': co2,
        'flag': flag,
        'valid': nt >= threshold_map['temp_norm_lower'] and co2 < threshold_map['co2_critical']
    }
    for idx, (nt, rt, co2, flag) in enumerate(zip(
        normalized_temps, temperature_readings, co2_levels, risk_flags
    ))
]

# Another decoy structure (unused)
calibration_sequence = [
    {'phase': i, 'pulse': (i ** 2) % 7} for i in range(1, 10)
]

# Bitwise manipulation as distraction (used nowhere)
key_signature = 0
for item in calibration_sequence:
    key_signature ^= item['pulse']
    key_signature = (key_signature << 1) | (key_signature >> 7)
    key_signature &= 0xFF

# Core analysis logic
safe_count = 0
warning_count = 0
for entry in processed_data:
    if not entry['valid']:
        continue
    if entry['flag'] == 'NORMAL':
        safe_count += 1
    elif entry['flag'] in ['WARNING', 'CRITICAL']:
        warning_count += 1

# Secondary diagnostic using set operations
recent_high_risk = high_co2_indices & {i for i, d in enumerate(processed_data) if d['norm_temp'] > 1.0}
dynamic_penalty = len(recent_high_risk) * 15

# Final computation with multiple dependencies
base_diagnostic = safe_count * 100
penalty_adjustment = warning_count * 25 + dynamic_penalty

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Actual implementation of analyze_readings (defined here to avoid forward ref error)
def analyze_readings(data_entries, thresholds):
    total_score = 0
    for entry in data_entries:
        # Scoring logic
        if entry['flag'] == 'NORMAL':
            total_score += 10
        elif entry['flag'] == 'MODERATE':
            total_score += 5
        elif entry['flag'] == 'ELEVATED':
            total_score += 3
        elif entry['flag'] == 'WARNING':
            total_score -= 5
        elif entry['flag'] == 'CRITICAL':
            total_score -= 15
    
    # Additional penalty based on CO2 exposure
    critical_exposure = sum(1 for e in data_entries if e['co2'] > thresholds['co2_critical'])
    total_score -= critical_exposure * 10
    
    # Bonus for stable temperatures (within narrow band)
    stable_count = sum(1 for e in data_entries if 0.8 <= e['norm_temp'] <= 1.0)
    total_score += stable_count * 7
    
    return total_score

# Print final result
Result: {final_diagnostic}