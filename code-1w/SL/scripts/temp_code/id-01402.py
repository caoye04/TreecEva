import math

# Simulated sensor data processing pipeline with diagnostic evaluation
def collect_readings():
    raw_samples = [127, 255, 192, 64, 80, 240, 168]
    offset = 32
    adjusted = [sample - offset for sample in raw_samples]  # Shift baseline
    return adjusted

def filter_anomalies(data):
    filtered = []
    anomalies = []
    for x in data:
        if x < 0:
            anomalies.append(x)
        elif x > 200:
            continue  # Drop extreme values
        else:
            filtered.append(x)
    # Distractor: unused anomaly log
    anomaly_log = ''.join([f'{a:x}' for a in anomalies])
    return filtered

def compute_weights(n):
    # Irrelevant weighting function (not used in final path)
    weights = []
    for i in range(1, n+1):
        w = (i / n) ** 0.5
        weights.append(round(w, 3))
    return weights

def generate_signature(seq):
    # Dead code path — never called
    sig = 0
    for i, val in enumerate(seq):
        sig ^= (val + i) % 256
    return sig

def derive_metrics(values):
    # Compute various statistical indicators
    count = len(values)
    total = sum(values)
    mean = total / count if count else 0
    variance = sum((x - mean) ** 2 for x in values) / count if count else 0
    stdev = math.sqrt(variance)
    
    # Intermediate metrics with red herring transformations
    peak_response = max(values) if values else 0
    normalized_energy = (sum(x**2 for x in values) / count) ** 0.5 if values else 0
    
    # Distractor variables
    phantom_index = int(mean * 1.618) % 100
    dummy_flag = bool(phantom_index & 1)
    shadow_buffer = [0] * 5
    for i in range(len(shadow_buffer)):
        shadow_buffer[i] = (phantom_index + i) % 47
    
    return {
        'mean': mean,
        'stdev': stdev,
        'peak': peak_response,
        'energy': normalized_energy,
        'count': count
    }

def build_threshold_map(metrics):
    # Create adaptive thresholds based on distribution
    base_map = {
        'low': metrics['mean'] - 0.5 * metrics['stdev'],
        'high': metrics['mean'] + 0.8 * metrics['stdev'],
        'critical': metrics['peak'] * 0.9
    }
    
    # Decoy entries
    base_map['spurious'] = metrics['energy'] * 2.1
    base_map['ghost'] = sum(base_map.values()) % 100
    
    return base_map

def process_sequence(raw_seq):
    # Main transformation chain
    stage1 = collect_readings()
    stage2 = filter_anomalies(stage1)
    
    # Bit manipulation red herring
    bit_trail = 0
    for val in stage2:
        bit_trail = (bit_trail << 1) | (val & 1)
        if bit_trail > 255:
            bit_trail &= 255
    
    # Real processing continues
    processed = [max(0, x - 10) for x in stage2]  # Final signal adjustment
    
    # Unused transformed variant
    inverted = [255 - x for x in processed][:len(processed)//2 or 1]
    
    return processed

def analyze_signal(signal, thresholds):
    if not signal:
        return -1
    
    # Count how many samples cross adaptive bands
    low_t = thresholds['low']
    high_t = thresholds['high']
    crit_t = thresholds['critical']
    
    categories = {
        'stable': 0,
        'elevated': 0,
        'critical': 0
    }
    
    for val in signal:
        if val < low_t:
            categories['stable'] += 1
        elif val < high_t:
            categories['elevated'] += 1
        elif val >= crit_t:
            categories['critical'] += 1

    # Diagnostic logic
    if categories['critical'] > 0:
        severity = 900 + categories['critical']
    elif categories['elevated'] > 4:
        severity = 700 + categories['elevated']
    else:
        severity = 500 - int(thresholds['low'])

    # Apply correction factor based on sequence pattern
    if len(signal) >= 4:
        trend = (signal[-1] - signal[0]) / (len(signal) - 1) if len(signal) > 1 else 0
        if trend > 2:
            severity += 50
        elif trend < -2:
            severity -= 30

    # Final adjustment using slicing distraction
    slice_proxy = signal[::2]  # Even indices only
    bonus = len(slice_proxy) if sum(slice_proxy) > 100 else 0
    severity += bonus

    return severity

# Orchestration block
if __name__ == '__main__':
    # Irrelevant initialization
    system_id = 'DIAG-9X'
    boot_cycle = 3
    calibration_offset = 0.0

    # Core execution path
    raw_data = collect_readings()  # [95, 223, 160, 32, 48, 208, 136]
    processed_data = process_sequence(raw_data)  # After -10: [85, 213, 150, 22, 38, 198, 126]
    metrics_summary = derive_metrics(processed_data)
    threshold_map = build_threshold_map(metrics_summary)
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Distractor computation
    synthetic_trace = [int(math.sin(i) * 100) for i in range(5)]
    checksum = sum(synthetic_trace) & 0xFF
    
    print(f"Result: {final_diagnostic}")