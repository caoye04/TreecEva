import itertools

def analyze_signal_strength(raw_samples, noise_floor):
    filtered = [x for x in raw_samples if x > noise_floor]
    return sum(filtered) / len(filtered) if filtered else 0.0

def generate_sequence(base, count):
    return [(base * i) % 17 for i in range(1, count + 1)]

def validate_checksum(data_chunk):
    checksum = 0
    for val in data_chunk:
        checksum ^= val
        checksum = (checksum << 1) & 0xFFFF
    return checksum | (len(data_chunk) & 0xFF)

def decode_payload(encoded_stream):
    decoded = []
    shift_reg = 0
    for byte in encoded_stream:
        shift_reg = (byte ^ 0xAA) >> 1
        decoded.append(shift_reg)
    return decoded

def compute_entropy(values):
    from math import log2
    freq_map = {}
    total = len(values)
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p) if p > 0 else 0
    return round(entropy, 6)

def merge_diagnostics(d1, d2, weight):
    return d1 * weight + d2 * (1 - weight)

def extract_features(time_series):
    features = {}
    features['peak'] = max(time_series)
    features['trough'] = min(time_series)
    features['delta'] = features['peak'] - features['trough']
    features['slope'] = (time_series[-1] - time_series[0]) / len(time_series)
    return features

def main_pipeline():
    # Irrelevant initialization (distractor)
    calibration_data = [0.1, 0.3, 0.5, 0.7, 0.9]
    baseline_offset = sum(calibration_data) * 0.01
    temp_buffer = [0] * 10
    
    # Real input data
    raw_log_magnitude = [12, 15, 18, 22, 14, 19, 25, 30, 28, 20, 17]
    system_states = ['active', 'idle', 'active', 'fault', 'active']
    event_timestamps = list(range(1000, 1000 + len(raw_log_magnitude)))
    
    # Generate decoy sequences (red herring)
    decoy_sequence_a = generate_sequence(7, 12)
    decoy_sequence_b = generate_sequence(13, 8)
    decoy_checksum = validate_checksum(decoy_sequence_a[:5])
    
    # Misleading signal analysis (distraction)
    fake_signal = [1.1, 1.2, 0.9, 1.5, 2.1, 1.8, 1.0]
    phantom_strength = analyze_signal_strength(fake_signal, 1.0)
    
    # Actual relevant computation begins
    log_entries = []
    for idx, (mag, ts) in enumerate(zip(raw_log_magnitude, event_timestamps)):
        entry = {
            'id': idx,
            'magnitude': mag,
            'timestamp': ts,
            'category': 'high' if mag > 20 else 'normal'
        }
        log_entries.append(entry)
    
    # Secondary data structure with cross-reference
    state_transitions = {}
    for i, state in enumerate(system_states):
        state_transitions[i] = {'state': state, 'flagged': state == 'fault'}
    
    # Process entries using itertools and enumerate (required feature)
    indexed_entries = list(enumerate(log_entries))
    paired_data = list(zip([e['magnitude'] for e in log_entries], [e['id'] for e in log_entries]))
    
    # Complex transformation chain
    magnitude_sequence = [e['magnitude'] for e in log_entries]
    processed_magnitudes = [m ** 0.5 * 1.1 for m in magnitude_sequence]
    
    # Decoy payload decoding (irrelevant)
    dummy_stream = [200, 150, 90, 210, 180]
    decoded_garbage = decode_payload(dummy_stream)
    
    # Feature extraction on real data
    features = extract_features(magnitude_sequence)
    
    # Entropy calculation on transformed data
    quantized = [int(x) for x in processed_magnitudes]
    entropy_metric = compute_entropy(quantized)
    
    # Create threshold map (relevant)
    system_thresholds = {
        'critical': 24,
        'warning': 18,
        'entropy_cap': 2.5
    }
    
    # Simulate multi-stage diagnostic scoring (core logic)
    base_score = 0
    for entry in log_entries:
        if entry['magnitude'] > system_thresholds['warning']:
            base_score += 3
        if entry['magnitude'] > system_thresholds['critical']:
            base_score += 5
    
    # Secondary scoring from features
    feature_bonus = 0
    if features['delta'] > 15:
        feature_bonus += 4
    if features['slope'] > 0.5:
        feature_bonus += 2
    
    # Combine scores with weighted merge (real path)
    raw_diagnostic = base_score + feature_bonus
    adjusted_diagnostic = merge_diagnostics(raw_diagnostic, len(log_entries), 0.7)
    
    # Final processing step with distractors around
    temp_debug = [analyze_signal_strength(raw_log_magnitude, 10)]  # unused
    debug_snapshot = {'size': len(log_entries), 'version': '2.1'}  # dead data
    
    # Key statement: this is where the answer is determined
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

# Required external function (simulates complex processing)
def process_metrics(entries, thresholds):
    count_high = 0
    sum_excess = 0.0
    recent_alerts = []
    
    # Use of itertools (required)
    for i, entry in itertools.islice(enumerate(entries), 0, None, 1):
        mag = entry['magnitude']
        if mag > thresholds['warning']:
            count_high += 1
            if mag > thresholds['critical']:
                excess = mag - thresholds['critical']
                sum_excess += excess ** 1.5  # non-linear contribution
        # Capture last three high-magnitude events
        if len(recent_alerts) < 3 and mag > thresholds['warning']:
            recent_alerts.append(i)
    
    # Transform recent alerts via case conversion (suggested paradigm)
    alert_keys = [f"A{idx}".lower() for idx in recent_alerts]
    key_string = ''.join(alert_keys)
    
    # Hash-like transform from string (using ord)
    str_value = sum(ord(c) for c in key_string) if key_string else 0
    
    # Final formula
    result = int(sum_excess + count_high * 2.7 + str_value * 0.3)
    return result

if __name__ == "__main__":
    main_pipeline()