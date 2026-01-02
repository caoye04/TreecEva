import math

# Simulated sensor fusion and diagnostic system for environmental monitoring

def collect_sensor_data():
    # Real data collection (simplified)
    return {
        'temp_c': 23.5,
        'humidity_pct': 68,
        'co2_ppm': 415,
        'pressure_pa': 101325,
        'voc_index': 37
    }

def calculate_heat_index(temp_c, humidity):
    # Heat index calculation in Celsius
    t = temp_c
    h = humidity
    hi = (-8.784695) + (1.61139411 * t) + (2.33854900 * h) +
         (-0.14611605 * t * h) + (-0.01230809 * t**2) +
         (-0.01642541 * h**2) + (0.00221173 * t**2 * h) +
         (0.00072546 * t * h**2) + (-0.00000358 * t**2 * h**2)
    return round(hi, 2)

def normalize(value, min_val, max_val):
    # Normalize to 0-1 scale
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def apply_calibration(readings):
    # Apply arbitrary calibration offsets (some irrelevant)
    calibrated = readings.copy()
    calibrated['temp_c'] += 0.2
    calibrated['humidity_pct'] -= 1.5
    calibrated['co2_ppm'] += 5  # Minor adjustment
    calibrated['pressure_pa'] *= 1.001
    calibrated['voc_index'] += 2
    return calibrated

def analyze_trend(history, key):
    # Dummy trend analysis (not used in final result)
    if len(history) < 2:
        return 'stable'
    diff = history[-1] - history[0]
    return 'rising' if diff > 0 else 'falling' if diff < 0 else 'stable'

def compute_entropy(data_list):
    # Calculate Shannon entropy of a list (distractor function)
    from collections import Counter
    counts = Counter(data_list)
    total = len(data_list)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def mask_sensitive_info(data_dict):
    # Remove or obfuscate sensitive fields (irrelevant to computation)
    safe_copy = data_dict.copy()
    for k in ['co2_ppm', 'voc_index']:
        if k in safe_copy:
            safe_copy[k] = 'REDACTED'
    return safe_copy

def validate_structure(obj):
    # Schema validation mock (dead code path)
    required_keys = ['temp_c', 'humidity_pct', 'co2_ppm']
    return all(k in obj for k in required_keys)

def transform_keys(d):
    # Convert keys to uppercase (unused transformation)
    return {k.upper(): v for k, v in d.items()}

def detect_anomaly(value, mean, std_dev):
    # Z-score anomaly detection (not used)
    z = abs(value - mean) / std_dev
    return z > 2.5

def process_readings(raw_data, threshold_config):
    # Core processing with multiple steps and distractions
    
    # Step 1: Calibrate raw inputs
    calibrated = apply_calibration(raw_data)
    
    # Step 2: Extract relevant metrics
    t = calibrated['temp_c']
    h = calibrated['humidity_pct']
    c = calibrated['co2_ppm']
    p = calibrated['pressure_pa']
    v = calibrated['voc_index']
    
    # Step 3: Compute derived indices
    heat_index = calculate_heat_index(t, h)
    
    # Step 4: Normalize values for scoring (only some used)
    norm_temp = normalize(heat_index, 0, 50)      # based on perceived temp
    norm_co2 = normalize(c, 400, 2000)            # indoor air quality scale
    norm_voc = normalize(v, 0, 100)               # standard VOC index
    
    # Step 5: Weighted risk score (core logic)
    temp_risk = norm_temp * 0.4
    co2_risk = norm_co2 * 0.3
    voc_risk = norm_voc * 0.3
    
    # Step 6: Aggregate health impact index
    health_index = (temp_risk + co2_risk + voc_risk) * 100
    
    # Step 7: Apply non-linear correction (sigmoid-like)
    corrected_index = 50 + 50 * (2 / (1 + math.exp(-0.05 * (health_index - 50))) - 1)
    
    # Step 8: Compare against thresholds (only one matters)
    alert_levels = {
        'normal': threshold_config['safe_level'],
        'warning': threshold_config['caution_level'],
        'critical': threshold_config['danger_level']
    }
    
    # Distractor: Create unused alert map using string operations
    alert_map_str = "|".join([f"{k}:{v}" for k, v in alert_levels.items()])
    tokens = alert_map_str.upper().split('|')
    filtered_tokens = [tok for tok in tokens if 'WARNING' not in tok]
    token_count = len(filtered_tokens)
    
    # Distractor: Set operation on keys (irrelevant)
    expected_keys = {'temp_c', 'humidity_pct', 'co2_ppm', 'pressure_pa', 'voc_index'}
    actual_keys = set(calibrated.keys())
    missing_keys = expected_keys - actual_keys
    extra_keys = actual_keys - expected_keys
    key_compliance = len(missing_keys) == 0
    
    # Distractor: Build unused dictionary structure
    diagnostics_log = {
        'raw_snapshot': raw_data,
        'calibration_offset': 0.2,
        'processing_steps': [
            'calibration', 'normalization', 'weighting', 'correction'
        ],
        'algorithm_version': 'v2.1-beta',
        'entropy_estimate': compute_entropy([int(t), int(h), c//100, v]),
        'stability_flag': analyze_trend([t], 'temp_c') == 'stable'
    }
    
    # Final decision logic (depends only on corrected_index)
    if corrected_index < alert_levels['normal']:
        level = 1
    elif corrected_index < alert_levels['warning']:
        level = 2
    elif corrected_index < alert_levels['critical']:
        level = 3
    else:
        level = 4
    
    # Final diagnostic code: composite of level and normalized CO2 (only level used)
    # BUT answer is actually the corrected_index rounded to nearest integer
    final_value = round(corrected_index)
    
    # Many variables created but only one matters
    final_diagnostic = final_value  # <-- KEY VARIABLE
    
    # Dead code: dictionary manipulation (distractor)
    mirror_dict = {v: k for k, v in enumerate(['low','medium','high','severe'])}
    if level in mirror_dict:
        category = mirror_dict[level].replace('h','H')
        category = category[::-1].upper()
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    
    # Irrelevant historical buffer (distractor)
    history_buffer = [
        collect_sensor_data(),
        collect_sensor_data()
    ]
    
    # Threshold configuration (only these values matter)
    thresholds = {
        'safe_level': 45,
        'caution_level': 60,
        'danger_level': 80
    }
    
    # Collect and process
    sensor_data = collect_sensor_data()
    
    # Perform masked logging (useless for result)
    secure_data = mask_sensitive_info(sensor_data)
    
    # Transform for API (unused)
    api_payload = transform_keys(sensor_data)
    
    # Validate structure (always passes)
    is_valid = validate_structure(sensor_data)
    
    # Core processing
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")