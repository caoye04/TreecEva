import math

# Simulated sensor health monitoring system with diagnostic processing
def analyze_readings(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return {'average': avg, 'deviation': std_dev, 'status': 'stable' if std_dev < 5 else 'unstable'}

# Irrelevant auxiliary function - distractor (dead logic path)
def legacy_compatibility_mode(data):
    transformed = [x * 0.95 + 2 for x in data if x > 10]
    normalized = list(map(lambda z: round(z, 2), transformed))
    return normalized if len(normalized) > 3 else [0] * 5

# Core transformation pipeline
config_flags = {
    'debug_mode': False,
    'precision_override': None,
    'threshold_adjust': 1.15
}

temp_buffer = [23.5, 24.1, 22.7, 25.3, 26.8, 24.0, 23.9]

# Misleading intermediate calculation - looks important but unused in final result
calibration_offset = sum(temp_buffer) * 0.01
adjusted_readings = [round(x + calibration_offset, 2) for x in temp_buffer]
diagnostic_snapshot = analyze_readings(adjusted_readings)

# Real-time signal filter (unused side effect)
filter_kernel = [0.25, 0.5, 0.25]
convolved = [sum(temp_buffer[i+j] * filter_kernel[j] for j in range(3)) 
             for i in range(len(temp_buffer) - 2)]

# Primary data structure - actual input to final computation
health_data = {
    'sensor_a': [88, 92, 85, 94, 90],
    'sensor_b': [76, 73, 79, 77, 80],
    'sensor_c': [65, 68, 63, 70, 67]
}

# Threshold configuration map - critical for final decision logic
threshold_map = {
    'normal': lambda x: x > 75,
    'warning': lambda x: 60 <= x <= 75,
    'critical': lambda x: x < 60
}

# Auxiliary lookup table - partially used (distractor entries)
status_weights = {
    'sensor_a': 1.2,
    'sensor_b': 0.9,
    'sensor_c': 1.0,
    'spare_d': 0.0  # Unused entry - red herring
}

# Diagnostic processor combining multiple concepts
measure_log = []

for key, values in health_data.items():
    mean_val = sum(values) / len(values)
    weight = status_weights.get(key, 0.5)
    weighted_mean = mean_val * weight
    measure_log.append(weighted_mean)

# Bit manipulation decoy - appears complex but irrelevant
obfuscation_key = 0b110101
encoded_flag = (len(measure_log) << 3) ^ obfuscation_key
probe_mask = (encoded_flag & 0b1111) | 0b1000

# Actual core logic hidden among distractions
def evaluate_status(value, thresholds):
    if thresholds['critical'](value):
        return -1
    elif thresholds['warning'](value):
        return 0
    else:
        return 1

# Higher-order function wrapper - functional paradigm distraction
def create_validator(ref_value):
    return lambda x: abs(x - ref_value) < 10

validator = create_validator(85)

# Main processing function with dictionary operations and conditional logic
def process_metrics(data, th_map):
    results = []
    for sensor, readings in data.items():
        avg = sum(readings) / len(readings)
        status_code = evaluate_status(avg, th_map)
        # String-based flag generation (superficially complex)
        flag = f"{sensor}_{'high' if status_code == 1 else 'mid' if status_code == 0 else 'low'}"
        if 'a' in flag:  # Partial use of string method
            pass  # Dummy control flow branch
        results.append(status_code)
    
    # Final aggregation with min/max/avg
    raw_total = sum(results)
    adjustment = config_flags.get('threshold_adjust', 1.0)
    # Critical answer computation
    return int((raw_total * adjustment) + 50)

# Execute final statement
final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Target result: {final_diagnostic}")