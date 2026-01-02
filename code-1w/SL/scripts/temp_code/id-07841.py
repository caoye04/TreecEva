import math

# Simulated sensor fusion and diagnostic system for environmental monitoring
def collect_environmental_data():
    base_readings = [23.4, 19.1, 45.6, 30.2, 11.8]
    timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
    locations = [(51.5, -0.1), (48.9, 2.4), (40.4, -3.7), (35.7, 13.3), (37.8, -122.4)]
    
    # Irrelevant metadata
    device_id = 'ENV-SENSE-PRO-9000'
    firmware_version = 'v2.7.1'
    battery_level = 87
    signal_strength = -67
    
    return {'readings': base_readings, 'times': timestamps, 'locs': locations}

# Decoy function – never called but looks important
def analyze_trend_pattern(data_stream):
    if len(data_stream) < 3:
        return False
    trend = [data_stream[i+1] - data_stream[i] for i in range(len(data_stream)-1)]
    return sum(trend) / len(trend) > 0

# Auxiliary transformation
def apply_noise_filter(raw_values, strength=0.15):
    filtered = []
    for i, v in enumerate(raw_values):
        noise = math.sin(i * 0.5) * strength
        filtered.append(v + noise)
    return filtered

# Calibration logic with red herring parameters
def generate_calibration_matrix(seed_offset=1.37, mode='standard'):
    matrix = {}
    for i in range(5):
        phase = seed_offset + i * 0.23
        matrix[f'sensor_{i}'] = {
            'gain': 1.0 + 0.05 * math.cos(phase),
            'offset': -0.8 + 0.3 * math.sin(phase),
            'active': True if i % 2 == 0 else False,
            'last_updated': f'2023-0{i+1}-15'
        }
    
    # Unused but misleading computation
    aggregate_sensitivity = sum([m['gain'] for m in matrix.values()]) / len(matrix)
    system_health_score = int(aggregate_sensitivity * 100)  # Distractor
    
    return matrix

# Core processing with conditional expressions and dictionary ops
def process_readings(data, calib):
    adjusted = []
    for idx, val in enumerate(data):
        key = f'sensor_{idx}'
        if key in calib and calib[key]['active']:
            corrected = val * calib[key]['gain'] + calib[key]['offset']
        else:
            corrected = val * 1.1  # Fallback gain
        adjusted.append(corrected)
    
    # Compute derived metrics (some irrelevant)
    mean_val = sum(adjusted) / len(adjusted)
    variance = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted)
    std_dev = math.sqrt(variance)
    
    # Conditional expression chain - relevant to final result
    status_flag = 'optimal' if mean_val > 20 else 'suboptimal'
    correction_factor = 1.25 if status_flag == 'optimal' else 0.88
    
    # Data transformation using tuples and dictionaries
    categorized = {
        'high': tuple(x for x in adjusted if x >= mean_val + std_dev),
        'normal': tuple(x for x in adjusted if mean_val - std_dev <= x < mean_val + std_dev),
        'low': tuple(x for x in adjusted if x < mean_val - std_dev)
    }
    
    # Misleading health computation (dead end)
    nominal_ratio = len(categorized['normal']) / len(adjusted) if adjusted else 0
    if nominal_ratio > 0.6:
        health_index = 90 + int((nominal_ratio - 0.6) * 100)
    else:
        health_index = max(30, int(nominal_ratio * 80))
    
    # Key diagnostic logic - depends on prior steps
    baseline_diagnostic = sum(adjusted) * correction_factor
    
    # Additional interference: string-based case conversion (irrelevant)
    mode_label = 'FieldOp'.upper()
    env_class = ''.join([c.lower() if c.isupper() else c.upper() for c in mode_label])
    classification_hash = sum(ord(c) for c in env_class) % 17
    
    # Final computation - only this matters
    final_diagnostic = int(baseline_diagnostic - classification_hash * 2.5)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Orchestration function with unused branching
def run_diagnostics(full_system_check=True, log_details=False):
    raw_data = collect_environmental_data()
    
    # Simulate optional preprocessing (not used in main path)
    if full_system_check:
        filtered_data = apply_noise_filter(raw_data['readings'], strength=0.1)
    else:
        filtered_data = raw_data['readings']
    
    # Real path
    calibration_matrix = generate_calibration_matrix(seed_offset=1.37)
    final_diagnostic = process_readings(filtered_data, calibration_matrix)
    
    # Dead code branch (logistics reporting - irrelevant)
    if log_details:
        report_id = hash('diagnostic_' + str(int(sum(filtered_data))))
        timestamp_str = "2023-06-15T10:15:30Z"
        return {'id': report_id, 'result': final_diagnostic, 'time': timestamp_str}
    
    return final_diagnostic

# Execution entry point
if __name__ == '__main__':
    result = run_diagnostics(full_system_check=True, log_details=False)