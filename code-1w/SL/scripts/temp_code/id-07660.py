from collections import defaultdict, Counter
import math

# Simulated sensor fusion module for autonomous drone diagnostics
def analyze_propulsion_health(temperature_readings, vibration_data):
    severity_score = 0
    temp_anomalies = [t for t in temperature_readings if t > 85]
    vib_peaks = [v for v in vibration_data if v > 70]
    
    if len(temp_anomalies) > 3:
        severity_score += 25
    if max(vibration_data) > 95:
        severity_score += 40
    
    # Irrelevant computation: ambient noise modeling (red herring)
    ambient_noise = [abs(math.sin(i * 0.1)) * 15 for i in range(len(vibration_data))]
    avg_noise = sum(ambient_noise) / len(ambient_noise) if ambient_noise else 0
    
    return severity_score

# Redundant function - never called in execution path
def legacy_diagnostic_protocol(sensor_matrix):
    checksum = 0
    for row in sensor_matrix:
        for val in row:
            checksum ^= int(val * 10) % 255
    return checksum

# Core data transformation pipeline
def process_telemetry_stream(raw_packets):
    parsed_data = defaultdict(list)
    
    for packet in raw_packets:
        node_id = packet['node']
        for key, value in packet['metrics'].items():
            parsed_data[f'{node_id}_{key}'].append(value)
    
    # Distractor: unused transformation branch
    derived_features = {}
    for k, values in parsed_data.items():
        if 'temp' in k:
            derived_features[f'{k}_rate'] = [values[i+1] - values[i] for i in range(len(values)-1)]
    
    # Real processing: extract timing anomalies
    timing_issues = []
    for k, values in parsed_data.items():
        if 'timing' in k:
            baseline = sum(values) / len(values)
            deviations = [abs(v - baseline) for v in values]
            timing_issues.extend([d for d in deviations if d > 5.0])
    
    return timing_issues

# Critical diagnostic aggregation function
def aggregate_metrics(log_entries, state_vector):
    # Key variable initialization
    diagnostic_weight = 0.0
    anomaly_counter = Counter()
    
    # Parse and classify log events
    for entry in log_entries:
        timestamp, code, desc = entry
        anomaly_counter[code] += 1
        if code.startswith('ERR'):
            diagnostic_weight += 12.5
        elif code.startswith('WRN') and 'critical' in desc:
            diagnostic_weight += 6.0
    
    # State vector analysis with red herring variables
    phase_lock = state_vector.get('phase_alignment', 0)
    coherence_factor = state_vector.get('coherence_ratio', 1.0)
    spectral_shift = state_vector.get('spectral_drift', 0)  # Unused
    temporal_variance = state_vector.get('temporal_stability', 0)  # Dead variable
    
    # Complex conditional weighting
    if phase_lock > 75:
        diagnostic_weight *= 0.8
    elif phase_lock < 30:
        diagnostic_weight += 18.0
    
    if coherence_factor < 0.7:
        diagnostic_weight += 22.0
    
    # Decoy logic block: looks important but irrelevant
    quantum_buffer = [math.cos(i * coherence_factor) for i in range(50)]
    entanglement_score = sum(quantum_buffer) / 50
    normalized_entanglement = abs(entanglement_score) * 100
    
    # Final computation using actual dependencies
    base_penalty = diagnostic_weight
    multiplier = 1 + (anomaly_counter['ERR_CRITICAL'] * 0.15)
    final_diagnostic = int(base_penalty * multiplier)
    
    # Ensure deterministic output
    return final_diagnostic

# Simulated input data
timing_log = [
    (1623456789, 'ERR_CRITICAL', 'Critical timing skew in main oscillator'),
    (1623456790, 'WRN_critical', 'critical subsystem desynchronization'),
    (1623456791, 'ERR_GENERAL', 'General fault detected'),
    (1623456792, 'ERR_CRITICAL', 'Critical timing skew in main oscillator'),
    (1623456793, 'ERR_DIAGNOSTIC', 'Self-test failure')
]

system_state = {
    'phase_alignment': 28,
    'coherence_ratio': 0.65,
    'spectral_drift': 14.8,
    'temporal_stability': 0.33,
    'quantum_entanglement': None
}

# Execute main workflow
raw_sensor_packets = [
    {'node': 'A1', 'metrics': {'temp_1': 88, 'timing_x': 12.1, 'vib_z': 73}},
    {'node': 'A1', 'metrics': {'temp_1': 89, 'timing_x': 18.3, 'vib_z': 76}},
    {'node': 'B2', 'metrics': {'temp_2': 84, 'timing_y': 3.2, 'vib_z': 68}},
    {'node': 'B2', 'metrics': {'temp_2': 87, 'timing_y': 11.9, 'vib_z': 71}}
]

# Dead code path: looks like preprocessing but not connected to main result
preprocessed = process_telemetry_stream(raw_sensor_packets)
sensor_temps = [88, 89, 84, 87, 90, 85]
vibration_samples = [73, 76, 68, 71, 69, 75, 72, 74]

# Execute core functions
health_score = analyze_propulsion_health(sensor_temps, vibration_samples)
final_diagnostic = aggregate_metrics(timing_log, system_state)

# Print target result
print(f"Target result: {final_diagnostic}")