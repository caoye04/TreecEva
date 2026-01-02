from collections import defaultdict
import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [55, 58, 60, 62, 59, 57, 61, 63]
pressure_readings = [1013, 1012, 1015, 1016, 1014, 1011, 1010, 1017]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3']
error_flags = [False, False, True, False, False, False, True, False]
redundant_checksums = [0xabc, 0xdef, 0x123, 0x456, 0x789, 0x0ab, 0xcd0, 0xf12]

# Preprocessing: Normalize and filter readings
def normalize_sensor_data(raw_data):
    mean_val = sum(raw_data) / len(raw_data)
    normalized = [(x - mean_val) for x in raw_data]
    return [round(x, 2) for x in normalized]

# Distraction function - never called (dead code path)
def legacy_compatibility_mode(data):
    conversion_map = {k: v for k, v in zip(legacy_codes, range(len(legacy_codes)))}
    encoded = 0
    for i, code in enumerate(data):
        encoded += conversion_map[code] * (i + 1)
    return encoded % 256

# Real processing function
def process_environmental_data(temp, humid, press):
    processed = defaultdict(list)
    temp_norm = normalize_sensor_data(temp)
    humid_norm = normalize_sensor_data(humid)
    press_norm = normalize_sensor_data(press)
    
    for i in range(len(temp)):
        # Composite index calculation (relevant)
        stability_index = round(
            (temp_norm[i] * 0.4) + 
            (humid_norm[i] * 0.3) + 
            (press_norm[i] * 0.3), 2
        )
        processed['stability'].append(stability_index)
        
        # Distractor computation (irrelevant)
        phantom_risk = math.sin(temp[i]) * math.cos(press[i] / 100) + humid[i] / 100
        processed['phantom_alerts'].append(round(phantom_risk, 3))
        
        # Another irrelevant derived metric
        if humid[i] > 60:
            processed['overhead_load'].append(humid[i] * press[i] / 1000)
        else:
            processed['overhead_load'].append(0)
    
    return processed

# Threshold configuration map (used later)
threshold_config = {
    'critical': 1.5,
    'warning': 0.8,
    'normal': -0.5
}

# Unused historical thresholds (red herring)
historical_thresholds_v1 = {
    'critical': 1.8,
    'warning': 1.0,
    'normal': 0.0
}

# Diagnostic engine
def analyze_readings(data, thresholds):
    diagnostics = []
    
    # Misleading initialization (unused)
    debug_trace = []
    anomaly_count = 0
    cumulative_drift = 0.0
    
    for idx, stab in enumerate(data['stability']):
        # Core logic: classification based on thresholds
        if stab > thresholds['critical']:
            level = 3
        elif stab > thresholds['warning']:
            level = 2
        elif stab > thresholds['normal']:
            level = 1
        else:
            level = 0
        
        # Irrelevant transformation chain
        encoded_flag = (level << 2) | (idx % 4)
        scrambled = (encoded_flag ^ 0xB) + 7
        descrambled = (scrambled - 7) ^ 0xB
        recovered_level = descrambled >> 2  # Always equals original level
        
        diagnostics.append(recovered_level)
    
    # Final aggregation: count high-risk events (level 3)
    high_risk_events = sum(1 for d in diagnostics if d == 3)
    
    # Secondary metric: average stability
    avg_stability = sum(data['stability']) / len(data['stability'])
    
    # Tertiary distractor: phantom correlation
    phantom_correlation = 0
    for i in range(len(data['phantom_alerts']) - 1):
        if data['phantom_alerts'][i] > 0.5 and data['overhead_load'][i] > 50:
            phantom_correlation += 1
    
    # The actual answer derivation
    base_score = high_risk_events * 100
    adjustment = int(avg_stability * 10)
    final_diagnostic = base_score + adjustment
    
    # Dead code: never executed due to condition
    if False and 'debug' in data:
        final_diagnostic -= sum(debug_trace)
    
    return final_diagnostic

# Execution flow
processed_data = process_environmental_data(
    temperature_readings, 
    humidity_readings, 
    pressure_readings
)

threshold_map = threshold_config  # Use current config, not historical

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")