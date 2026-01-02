def simulate_sensor_array():
    # Simulate raw sensor readings (irrelevant to final result)
    base_frequency = 50.0
    harmonics = [base_frequency * i for i in range(1, 6)]
    phase_shifts = {h: (h * 1.57) % (2 * 3.14159) for h in harmonics}
    noise_profile = sum([abs(h * 0.02) for h in harmonics])
    return phase_shifts  # Dead end return


def compute_power_gradient(readings):
    # Irrelevant power analysis with decoy math
    gradient = 0
    for i in range(len(readings)):
        if i % 2 == 0:
            gradient += readings[i] ** 0.5
        else:
            gradient -= readings[i] ** 0.3
    return gradient * 0.1


def generate_diagnostic_template():
    # Creates a red herring diagnostic structure
    template = {
        'system_id': 'DIAG-9X',
        'timestamp': '2023-11-05T14:30:00Z',
        'baseline_stability': 0.987,
        'harmonic_distortion': [],
        'status_codes': set(),
        'fault_mask': 0x0
    }
    for i in range(5):
        template['status_codes'].add(f'INIT_{i}')
    return template


def legacy_calibration_sequence(data):
    # Unused calibration routine (dead code path)
    if len(data) < 10:
        return None
    calibrated = []
    for x in data:
        if x > 0:
            calibrated.append(x * 0.91 + 2.5)
        else:
            calibrated.append(x * 1.05 - 1.8)
    return [c for c in calibrated if abs(c) > 1e-3]


def detect_anomaly_clusters(sensor_ids):
    # Distractor function using set operations (semi-relevant but misleading)
    critical_set = {f'SEN-{i}' for i in [2, 3, 5, 7, 11]}
    warning_set = {f'SEN-{i}' for i in [1, 4, 6, 8, 9, 10, 12]}
    high_risk = critical_set.intersection(sensor_ids)
    monitored = warning_set.intersection(sensor_ids)
    
    # Decoy logic
    if len(high_risk) > 2:
        level = 'CRITICAL'
    elif len(monitored) > 4:
        level = 'WARNING'
    else:
        level = 'STABLE'
    
    # This return has partial relevance
    return {'risk_level': level, 'count': len(high_risk)}


def analyze_fault_chain(log_entries, signal_flags):
    # Core relevant logic buried in distractions
    fault_weights = {
        'F1': 3, 'F2': -5, 'F3': 2, 'F4': 7, 'F5': -4
    }
    
    # Real computation begins here
    cumulative_score = 0
    for entry in log_entries:
        code = entry.get('fault_code')
        severity = entry.get('severity_offset', 0)
        if code in fault_weights:
            cumulative_score += fault_weights[code] + severity
    
    # Set-based filtering (actual relevant use)
    flag_set = set(signal_flags)
    modifier_flags = {'SIG_ALPHA', 'SIG_OMEGA'}
    if flag_set.intersection(modifier_flags):
        cumulative_score *= 2
    
    # Additional real logic
    if len(flag_set) >= 3:
        cumulative_score += 10
    
    # Final transformation
    normalized = abs(cumulative_score) * 0.5
    return int(normalized)

# Main execution with heavy interference
if __name__ == '__main__':
    # Irrelevant sensor simulation (distractor)
    phase_data = simulate_sensor_array()
    frequencies = [50, 100, 150, 200, 250]
    power_grad = compute_power_gradient(frequencies)
    
    # Red herring data structures
    template_diag = generate_diagnostic_template()
    calibration_input = [-2.1, 0.0, 4.7, 8.3, -1.2, 0.5]
    legacy_results = legacy_calibration_sequence(calibration_input)
    
    # Semi-relevant but misleading anomaly detection
    sensor_list = ['SEN-2', 'SEN-3', 'SEN-7', 'SEN-9']
    anomaly_report = detect_anomaly_clusters(sensor_list)
    
    # ACTUAL RELEVANT INPUT DATA (buried among distractors)
    diagnosis_log = [
        {'fault_code': 'F1', 'severity_offset': 1},
        {'fault_code': 'F4', 'severity_offset': 0},
        {'fault_code': 'F2', 'severity_offset': -1},
        {'fault_code': 'F1', 'severity_offset': 0},
        {'fault_code': 'F5', 'severity_offset': 2}
    ]
    
    active_signals = ['SIG_BETA', 'SIG_GAMMA', 'SIG_OMEGA', 'SIG_THETA']
    
    # Critical statement
    final_diagnostic = analyze_fault_chain(diagnosis_log, active_signals)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")