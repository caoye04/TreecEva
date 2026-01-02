import math

# Simulated sensor fusion system for environmental diagnostics
def analyze_readings(raw_data, calibration_offset):
    # Irrelevant transformation: normalize data (not used in final path)
    normalized = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)) * 100) for x in raw_data]
    
    # Key computation chain begins
    base_values = [x for x in raw_data if x > 50]
    filtered_stats = {
        'sum': sum(base_values),
        'count': len(base_values),
        'max_val': max(base_values) if base_values else 0
    }

    # Distractor: unused statistical analysis
    moment_stats = {}
    mean_val = sum(raw_data) / len(raw_data)
    for order in [2, 3, 4]:
        moment_stats[f'moment_{order}'] = sum((x - mean_val)**order for x in raw_data) / len(raw_data)

    # Dead code path: entropy calculation never used
    def shannon_entropy(values):
        freq_map = {v: values.count(v) for v in set(values)}
        total = float(len(values))
        return -sum((count/total) * math.log(count/total, 2) for count in freq_map.values())
    
    entropy_estimate = shannon_entropy([int(x % 10) for x in raw_data])  # Computed but unused

    # Conditional logic with red herring branches
    if len(base_values) > 3:
        aggregation_method = 'weighted'
        weight_sequence = [1, 2, 1.5, 2.5, 1]
        weighted_sum = sum(val * weight_sequence[i % len(weight_sequence)] for i, val in enumerate(base_values))
        aggregate_score = int(weighted_sum / len(base_values))
    elif len(base_values) == 0:
        aggregate_score = 0
    else:
        # Misleading fallback that doesn't trigger
        backup_frame = {'init': 1, 'state': 'pending'}
        backup_frame.update({'init': 0})
        aggregate_score = filtered_stats['sum'] * 2

    # Bit manipulation decoy
    status_flag = 0xAEF3
    masked_flag = status_flag & 0xFF00
    shift_diagnostic = (masked_flag >> 8) ^ 0xAB
    checksum_probe = (shift_diagnostic + len(raw_data)) % 256

    # Critical path variables
    temperature_readings = [22.5, 23.1, 21.9, 22.8, 23.0]
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    temperature_factor = int(avg_temp * 2)

    # Complex conditional expression with distractor evaluation
    phase_state = 'gamma' if any(x > 75 for x in raw_data) else 'beta' if all(x < 60 for x in raw_data) else 'alpha'
    phase_modulator = 3 if phase_state == 'gamma' else (2 if phase_state == 'beta' else 1)
    
    # Set operations as red herring
    expected_codes = {101, 102, 103, 201, 202}
    received_codes = {101, 102, 104, 203}
    missing_codes = expected_codes - received_codes  # computed but unused
    critical_match = bool(expected_codes & received_codes)  # evaluated but not impactful

    # Core answer computation buried among distractions
    final_diagnostic = aggregate_score + temperature_factor * phase_modulator
    
    # Additional dead code: post-processing never invoked
    def generate_report(data):
        return {'status': 'complete', 'entries': len(data), 'flagged': False}
    
    # Spurious variable updates
    calibration_offset *= -1
    if calibration_offset > 0:
        calibration_offset += 1000  # unreachable due to prior negation

    return final_diagnostic

# Main execution
sensor_input = [55, 67, 88, 54, 91, 45, 77]
calib_offset = 17

result = analyze_readings(sensor_input, calib_offset)
print(f"Target result: {result}")