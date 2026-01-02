import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.7, 20.3, 26.4, 21.9, 24.8, 23.0]
humidity_readings = [45, 52, 61, 48, 55, 67, 43, 58, 50, 54]
co2_levels = [410, 425, 480, 415, 430, 510, 405, 440, 420, 435]

# Irrelevant auxiliary metrics (distractor variables)
sound_decibels = [32, 35, 41, 33, 37, 45, 31, 38, 34, 36]
luminance_lux = [512, 489, 530, 501, 477, 521, 495, 508, 515, 499]

# System calibration offsets (misleading constants)
CALIBRATION_A = 0.987
CALIBRATION_B = 1.014
BASELINE_DRIFT = 0.003

# Complex preprocessing with red herrings
def preprocess_sensors(raw_temps, raw_humid):
    normalized = []
    for i in range(len(raw_temps)):
        # Real transformation
        temp_norm = (raw_temps[i] - 20) / 5
        humid_ratio = raw_humid[i] / 100
        index_score = temp_norm * (1 + humid_ratio)
        normalized.append(round(index_score, 3))
    
    # Dead code path - never used (distractor)
    if len(normalized) > 20:
        smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized)-2)]
    else:
        dummy_var = [x * CALIBRATION_A for x in normalized]
        dummy_var = [x + BASELINE_DRIFT for x in dummy_var]
    
    return normalized

# Filtering logic with conditional expressions and set operations
valid_indices = {i for i, co2 in enumerate(co2_levels) if co2 < 475}
high_co2_alerts = {i for i in range(len(co2_levels)) if co2_levels[i] >= 475}

filtered_data = []
for idx in range(len(temperature_readings)):
    if idx in valid_indices:
        filtered_data.append({
            'idx': idx,
            'temp': temperature_readings[idx],
            'humidity': humidity_readings[idx],
            'co2': co2_levels[idx]
        })

# Unused function - decoy for cognitive distraction
def calculate_air_quality_index(data_list):
    aqi_values = []
    for entry in data_list:
        base = 0.4 * entry['temp'] + 0.03 * entry['co2']
        if entry['humidity'] > 60:
            base *= 1.25
        aqi_values.append(round(base, 2))
    return sum(aqi_values) / len(aqi_values)

# Threshold configuration map (used later)
threshold_map = {
    'temp_breach': lambda t: t > 25.0,
    'humidity_spike': lambda h: h > 60,
    'co2_warning': lambda c: c > 450
}

# Diagnostic analysis with list comprehension and nesting
def analyze_readings(readings, thresholds):
    diagnostics = []
    
    # Real computation chain
    for record in readings:
        issues = []
        
        # Check multiple conditions with logical combinations
        if thresholds['temp_breach'](record['temp']):
            issues.append('HIGH_TEMP')
        if thresholds['humidity_spike'](record['humidity']):
            issues.append('HIGH_HUMIDITY')
        if thresholds['co2_warning'](record['co2']):
            issues.append('ELEVATED_CO2')
        
        # Composite risk score calculation
        risk_weight = 0
        if 'HIGH_TEMP' in issues:
            risk_weight += 1.8
        if 'HIGH_HUMIDITY' in issues:
            risk_weight += 1.2
        if 'ELEVATED_CO2' in issues:
            risk_weight += 2.0
        
        # Apply nonlinear transformation
        adjusted_risk = math.log(1 + risk_weight) * 10
        
        diagnostics.append({
            'record_idx': record['idx'],
            'issue_count': len(issues),
            'risk_score': round(adjusted_risk, 3),
            'flags': issues
        })
    
    # Final aggregation using list comprehension and conditional logic
    significant_cases = [d for d in diagnostics if d['risk_score'] > 5.0]
    
    # Critical line: this determines the final answer
    final_diagnostic = sum(d['risk_score'] for d in significant_cases) if significant_cases else 0.0
    
    # Irrelevant post-processing (dead code)
    summary_stats = {
        'total_analyzed': len(diagnostics),
        'critical_cases': len([d for d in diagnostics if d['issue_count'] == 3]),
        'max_risk': max((d['risk_score'] for d in diagnostics), default=0)
    }
    
    # This print is just noise to distract
    # print(f"System report: {summary_stats['total_analyzed']} records processed")
    
    return final_diagnostic

# Execute main logic flow
processed_metrics = preprocess_sensors(temperature_readings, humidity_readings)

# Key execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")