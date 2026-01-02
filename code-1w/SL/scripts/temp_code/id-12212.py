from collections import defaultdict, Counter

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_readings():
    raw_signals = [32, 17, 25, 14, 88, 67, 53, 19, 42]
    noise_floor = 15
    adjusted = [x - noise_floor if x > noise_floor else 0 for x in raw_signals]
    return adjusted

# Irrelevant helper - simulates temperature drift compensation (not used in final path)
def apply_thermal_correction(data):
    corrected = []
    for x in data:
        if x > 50:
            corrected.append(x * 0.92)
        elif x > 20:
            corrected.append(x * 0.98)
        else:
            corrected.append(x + 1.5)
    return corrected

# Core signal processing with decoy logic
def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if x > 10]  # Remove low-noise artifacts
    squared_energy = [x ** 2 for x in filtered]     # Compute signal energy
    
    # DEAD CODE PATH: frequency analysis (never used)
    peak_freq = None
    if len(squared_energy) > 5:
        peak_freq = sum(squared_energy[i] * i for i in range(len(squared_energy))) / sum(squared_energy)
    
    normalized = [x / max(squared_energy) * 100 for x in squared_energy]
    return normalized

# Misleading pattern detection (decoy function - never called)
def detect_anomaly_pattern(signal):
    if not signal:
        return False
    diffs = [signal[i+1] - signal[i] for i in range(len(signal)-1)]
    return any(abs(d) > 75 for d in diffs)

# Threshold configuration with red herring entries
def generate_threshold_map():
    config = defaultdict(float)
    config['critical'] = 85.0
    config['warning'] = 60.0
    config['info'] = 30.0
    config['debug'] = 10.0  # Never used
    config['legacy_mode'] = 200.0  # Decoy parameter
    return config

# Data validation with hidden XOR-based integrity check
def validate_integrity(data):
    if not data:
        return False
    checksum = 0
    for val in data:
        checksum ^= int(val)  # Bitwise XOR chain
    return (checksum & 1) == 1  # Check if odd

# Main analysis with conditional bypasses and distractors
def analyze_signal(energy_levels, thresholds):
    if not validate_integrity(energy_levels):
        return -1
    
    high_energy_count = sum(1 for e in energy_levels if e >= thresholds['critical'])
    medium_energy_count = sum(1 for e in energy_levels if thresholds['warning'] <= e < thresholds['critical'])
    
    # Compute weighted impact score (intermediate result - misleading)
    impact_score = 0
    for e in energy_levels:
        if e >= thresholds['critical']:
            impact_score += e * 1.5
        elif e >= thresholds['warning']:
            impact_score += e * 0.8
        else:
            impact_score += e * 0.2
    
    # UNUSED variable - decoy for reasoning
    average_impact = impact_score / len(energy_levels) if energy_levels else 0
    
    # Hidden logic: count transitions across warning threshold
    crossing_events = 0
    for i in range(1, len(energy_levels)):
        prev, curr = energy_levels[i-1], energy_levels[i]
        if (prev < thresholds['warning'] <= curr) or (curr < thresholds['warning'] <= prev):
            crossing_events += 1
    
    # FINAL DIAGNOSTIC: composite calculation
    base_risk = high_energy_count * 1000
    fluctuation_penalty = crossing_events * 17
    total_diagnostics = base_risk + fluctuation_penalty
    
    # Apply secret offset based on list length parity (obscure but deterministic)
    if len(energy_levels) % 2 == 1:
        total_diagnostics -= 42
    else:
        total_diagnostics += 13
    
    return total_diagnostics

# Orchestration with unused branches and irrelevant state
system_state = {
    'active_sensors': 7,
    'calibration_cycle': 'completed',
    'last_update': '2023-12-01',
    'maintenance_due': False
}

if __name__ == '__main__':
    # Primary execution flow
    raw_data = collect_sensor_readings()
    processed_data = preprocess_signal(raw_data)
    
    # DEAD CODE: thermal correction computed but unused
    thermally_corrected = apply_thermal_correction(processed_data)
    
    # Generate threshold configuration
    threshold_map = generate_threshold_map()
    
    # UNUSED: anomaly detection skipped entirely
    # status_flag = detect_anomaly_pattern(processed_data)
    
    # Critical diagnostic computation
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print final result as required
    print(f"Target result: {final_diagnostic}")