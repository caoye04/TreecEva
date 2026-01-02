from collections import defaultdict, Counter
import math

# Simulated quantum sensor readings and system diagnostics
def collect_sensor_data():
    readings = []
    for i in range(18):
        val = (i ** 3 - 2 * i + 11) % 17
        readings.append(val)
    return readings

def apply_calibration(raw_readings):
    calibrated = []
    offset = 3.7
    scale = 1.05
    for r in raw_readings:
        adjusted = (r + offset) * scale
        if adjusted > 20:
            adjusted = 20
        elif adjusted < 0:
            adjusted = 0
        calibrated.append(round(adjusted, 2))
    return calibrated

def compute_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def generate_checksum(sequence):
    # Irrelevant distractor function: used nowhere critical
    chk = 0
    for i, v in enumerate(sequence):
        chk ^= (v * (i + 1)) % 256
    return chk + 1000

def evaluate_stability_index(readings):
    # Misleading stability metric (not used in final result)
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    if not diffs:
        return 0.0
    return round(sum(diffs) / len(diffs), 3)

def filter_anomalies(data_list):
    # Dead code path - never actually removes anything due to logic
    threshold = sum(data_list) / len(data_list)
    filtered = [x for x in data_list if x <= threshold + 1]
    return filtered if len(filtered) > 5 else data_list

def build_diagnostic_map(flags):
    # Distractor: builds a complex structure but only one field matters
    diag_map = defaultdict(dict)
    diag_map['status']['primary'] = flags.get('active', False)
    diag_map['status']['safe_mode'] = not flags.get('override', False)
    diag_map['metrics']['latency'] = flags.get('latency', 0) * 0.85
    diag_map['metrics']['power_cycle'] = flags.get('cycles', 1)
    diag_map['flags']['degraded'] = flags.get('degraded', True)
    diag_map['version'] = '2.1.0'
    return diag_map

def calculate_coherence_score(vals):
    # Complex-looking but unused calculation
    s = 0
    for i in range(len(vals)):
        s += vals[i] * math.sin(i + 0.5)
    return round(abs(s), 3)

def analyze_system_state(sensor_data, config_flags):
    # Core logic buried in distractions
    
    # Irrelevant preprocessing
    temp_snapshot = [x * 1.01 for x in sensor_data]
    snapshot_entropy = compute_entropy([int(x) for x in sensor_data])
    
    # Key flag-dependent branching
    if config_flags.get('debug_mode'):
        initial_weight = 0.3
    else:
        initial_weight = 0.7  # This path is taken
    
    # Critical data transformation
    processed = []
    for idx, val in enumerate(sensor_data):
        transformed = val ** 2 - 3 * val + 5
        if idx % 4 == 0:
            transformed += 1.5
        processed.append(transformed)
    
    # Accumulation with conditional logic
    accumulator = 0.0
    for p_val in processed:
        if p_val > 10:
            accumulator += p_val * 0.9
        elif p_val > 5:
            accumulator += p_val * 1.1
        else:
            accumulator += p_val * 1.3
    
    # Secondary adjustment based on flag
    override_factor = config_flags.get('boost', 1.25)
    adjusted_accum = accumulator * override_factor
    
    # Tertiary weighting using default dictionary side effect
    weights = defaultdict(lambda: 0.8)
    weights['base'] = 1.0
    weights['boost'] = config_flags.get('turbo', 0.9)  # Not used
    final_adjustment = adjusted_accum * weights['base']
    
    # Final decision logic (only this affects output)
    if config_flags.get('emergency_shutdown'):
        final_diagnostic = -999
    else:
        final_diagnostic = int(round(final_adjustment - 42.5))
    
    # Dead code: early return that's unreachable
    if final_diagnostic < 0:
        return 0
    
    return final_diagnostic

# --- Main Execution ---
if __name__ == '__main__':
    # Collect raw sensor data
    raw_quantum_readings = collect_sensor_data()
    
    # Apply irrelevant calibration (result not used)
    calibrated_readings = apply_calibration(raw_quantum_readings)
    
    # Compute meaningless metrics
    stability = evaluate_stability_index(calibrated_readings)
    coherence = calculate_coherence_score(calibrated_readings)
    checksum = generate_checksum(raw_quantum_readings)
    
    # Build diagnostic map (complex object but only flags matter)
    system_flags = {
        'active': True,
        'override': False,
        'degraded': True,
        'latency': 120,
        'cycles': 3,
        'debug_mode': False,
        'boost': 1.25,
        'emergency_shutdown': False,
        'turbo': 1.1
    }
    
    diagnostic_tree = build_diagnostic_map(system_flags)
    
    # Filter anomalies (called but result ignored)
    clean_readings = filter_anomalies(calibrated_readings)
    
    # CORE COMPUTATION
    final_diagnostic = analyze_system_state(raw_quantum_readings, system_flags)
    
    # Output target variable
    print(f"Result: {final_diagnostic}")