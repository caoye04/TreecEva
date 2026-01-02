import itertools

# Simulated wind turbine sensor data processing with diagnostic logic
def analyze_turbine_performance(sensor_log, threshold=0.85):
    normal_ranges = {"vibration": (0.1, 0.9), "temperature": (40, 90), "rpm": (1200, 1800)}
    vibration_data = [entry['vibration'] for entry in sensor_log if 'vibration' in entry]
    temp_data = [entry['temperature'] for entry in sensor_log if 'temperature' in entry]
    rpm_data = [entry['rpm'] for entry in sensor_log if 'rpm' in entry]

    # Irrelevant transformation: time-based decay weighting (not used later)
    time_weights = [(0.95 ** i) for i in range(len(sensor_log), 0, -1)]
    weighted_rpm = [rpm_data[i] * time_weights[i] for i in range(len(rpm_data))]  # Dead path

    # Real metric: sustained deviation count
    sustained_faults = 0
    for i in range(len(vibration_data) - 2):
        if all(v > normal_ranges['vibration'][1] for v in vibration_data[i:i+3]):
            sustained_faults += 1

    performance_score = len([v for v in vibration_data if v < threshold]) / len(vibration_data)
    return performance_score, sustained_faults

# Fault pattern detection using bit flags (relevant)
def detect_fault_patterns(log_entries):
    PATTERN_UNDERVOLTAGE = 1 << 0
    PATTERN_OVERHEAT = 1 << 1
    PATTERN_IMBALANCE = 1 << 2
    PATTERN_BEARING = 1 << 3

    detected = 0
    heat_events = [e['temp'] for e in log_entries if 'temp' in e]
    voltage_reads = [e['voltage'] for e in log_entries if 'voltage' in e]

    # Irrelevant: power output trend (unused)
    power_trend = [log_entries[i+1]['power'] - log_entries[i]['power'] 
                  for i in range(len(log_entries)-1) if 'power' in log_entries[i] and 'power' in log_entries[i+1]]

    if any(t > 95 for t in heat_events):
        detected |= PATTERN_OVERHEAT
    if len([v for v in voltage_reads if v < 100]) > len(voltage_reads) * 0.3:
        detected |= PATTERN_UNDERVOLTAGE

    imbalance_vector = [abs(e.get('phase_a', 0) - e.get('phase_b', 0)) for e in log_entries]
    if max(imbalance_vector) > 15:
        detected |= PATTERN_IMBALANCE

    # Red herring: bearing wear index calculation (not linked to flag)
    wear_index = sum(imbalance_vector) / len(imbalance_vector) + 0.5 * max(vibration_data[:10])  # Undefined vibration_data

    return detected

# Data windowing and feature extraction
def extract_temporal_features(records, window_size=3):
    features = []
    for i in range(0, len(records) - window_size + 1):
        window = records[i:i+window_size]
        avg_vib = sum(w['vibration'] for w in window) / window_size
        trend_temp = window[-1]['temperature'] - window[0]['temperature']
        features.append({'avg_vib': avg_vib, 'trend_temp': trend_temp})
    return features

# Main aggregation function combining multiple diagnostics
def aggregate_metrics(turbine_data, indicators):
    # Core computation path
    base_score, fault_duration = analyze_turbine_performance(turbine_data)
    pattern_flags = detect_fault_patterns(turbine_data)

    # Extract features for secondary validation (partially relevant)
    temporal_features = extract_temporal_features(turbine_data, 3)
    instability_index = sum(1 for f in temporal_features if f['avg_vib'] > 1.0) / len(temporal_features)

    # Decoy metrics
    efficiency_ratio = (sum(f['trend_temp'] for f in temporal_features) + 1) / (fault_duration + 1)  # Misleading
    calibration_offset = 0.023 * len(turbine_data)  # Unused distraction

    # Critical logic chain
    risk_accumulator = 0
    if fault_duration > 2:
        risk_accumulator += 150
    if pattern_flags & (1 << 1):  # OVERHEAT present
        risk_accumulator += 220
    if instability_index > 0.4:
        risk_accumulator += 95
    if base_score < 0.7:
        risk_accumulator += 180

    # Complex conditional involving bitwise and arithmetic
    adjustment_factor = 1.0
    if pattern_flags & (PATTERN_UNDERVOLTAGE | PATTERN_IMBALANCE) and fault_duration > 1:
        adjustment_factor *= 0.85
    elif pattern_flags & PATTERN_BEARING:
        adjustment_factor *= 1.2  # Never triggered

    final_diagnostic = int(risk_accumulator * adjustment_factor) + 42

    # Obfuscating print statements (irrelevant)
    debug_snapshot = [f'{k}:{v:.2f}' for k, v in itertools.islice({'base': base_score, 'instability': instability_index, 'efficiency': efficiency_ratio}.items(), 2)]
    
    return final_diagnostic

# Generate synthetic input data
synthetic_log = [
    {'vibration': 1.2, 'temperature': 96, 'rpm': 1750, 'voltage': 95, 'temp': 98, 'phase_a': 120, 'phase_b': 100},
    {'vibration': 1.3, 'temperature': 94, 'rpm': 1700, 'voltage': 92, 'temp': 96, 'phase_a': 125, 'phase_b': 105},
    {'vibration': 1.4, 'temperature': 97, 'rpm': 1720, 'voltage': 98, 'temp': 99, 'phase_a': 130, 'phase_b': 110},
    {'vibration': 0.6, 'temperature': 85, 'rpm': 1500, 'voltage': 105, 'temp': 88, 'phase_a': 115, 'phase_b': 113},
    {'vibration': 0.5, 'temperature': 83, 'rpm': 1450, 'voltage': 110, 'temp': 85, 'phase_a': 118, 'phase_b': 117}
]

# Orphaned preprocessing (dead code path)
filtered_data = [entry for entry in synthetic_log if entry['rpm'] > 1400]
sorted_by_vib = sorted(filtered_data, key=lambda x: x['vibration'], reverse=True)

# Irrelevant combinatorics: generate all pairs (not used)
combinations = list(itertools.combinations(['sensor_A', 'sensor_B', 'sensor_C'], 2))

# Key execution point
final_diagnostic = aggregate_metrics(synthetic_log, [])
print(f"Result: {final_diagnostic}")