import itertools
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(raw):    
    # Irrelevant transformation chain (distractor)
    temp_adjusted = [x * 1.05 + 2 for x in raw]
    filtered = [t for t in temp_adjusted if t > 50]
    normalized = [n / max(filtered) for n in filtered] if filtered else [0]

    # Decoy statistical summary (unused later)
    avg_temp = sum(temp_adjusted) / len(temp_adjusted) if temp_adjusted else 0
    peak_noise = max([abs(x - avg_temp) for x in temp_adjusted]) if temp_adjusted else 0

    # Actual relevant path: frequency mask generation
    freq_domain = [abs(math.sin(x)) for x in raw]
    threshold_mask = [f > 0.3 for f in freq_domain]
    return list(itertools.compress(raw, threshold_mask))

# Signal feature extraction with misleading branches
def extract_features(data_chunk):
    if not data_chunk:
        return {'energy': 0, 'complexity': 0}
    
    # Real computation branch
    energy_level = sum([x**2 for x in data_chunk]) / len(data_chunk)
    
    # Distractor: unused pattern analysis
    patterns = []
    for i in range(1, min(4, len(data_chunk))):
        paired = list(zip(data_chunk, data_chunk[i:]))
        correlation = sum([a * b for a, b in paired]) / len(paired)
        patterns.append(correlation > 0.75)
    
    # Fake entropy calculation (never used)
    unique_vals = set(round(d, 1) for d in data_chunk)
    decoy_entropy = math.log(len(unique_vals)) if unique_vals else 0
    
    # Relevant metric
    variance_proxy = sum([(x - energy_level)**2 for x in data_chunk]) / len(data_chunk)
    complexity_score = math.sqrt(variance_proxy) if variance_proxy > 0 else 0
    
    return {
        'energy': energy_level,
        'complexity': complexity_score
    }

# Misleading auxiliary function (looks important but irrelevant)
def validate_calibration(reference, signal):
    ref_avg = sum(reference) / len(reference) if reference else 0
    sig_avg = sum(signal) / len(signal) if signal else 0
    deviation = abs(ref_avg - sig_avg)
    tolerance = 0.5
    status_flags = {"calibrated": deviation < tolerance, "version": 2}
    return status_flags  # Never used in main logic

# Core analysis with nested distractions
def analyze_signal(dataset):
    if len(dataset) == 0:
        return -1
    
    # Real pipeline step
    processed_features = extract_features(dataset)
    
    # Dead code path 1: unreachable due to logic
    if processed_features['energy'] < 0:
        correction_factor = math.exp(processed_features['energy'])
        adjusted_energy = processed_features['energy'] * correction_factor
    else:
        adjusted_energy = processed_features['energy']
    
    # Critical distraction block: complex but irrelevant string encoding
    debug_tag = "SIG-PROC"
    encoded_trace = ''.join([
        chr((ord(c) ^ 17) % 95 + 32) for c in debug_tag
    ])
    trace_hash = sum([ord(encoded_trace[i]) * (i + 1) for i in range(len(encoded_trace))])
    
    # Another decoy: bit manipulation with no effect
    metadata_key = 0xA1B2
    rotated = ((metadata_key << 3) | (metadata_key >> 13)) & 0xFFFF
    checksum = bin(rotated).count('1')
    
    # Actual decision logic (well-hidden among noise)
    e = processed_features['energy']
    c = processed_features['complexity']
    
    # True diagnostic formula
    if e > 100:
        base_score = e * 0.8 + c * 12
    elif e > 50:
        base_score = e * 1.1 + c * 8
    else:
        base_score = e * 1.5 + c * 5
    
    # Final adjustment using distractor values (but only one matters)
    final_diagnostic = int(base_score + (trace_hash % 10))  # Only trace_hash % 10 affects result
    
    # Unused conditional override (dead code)
    if checksum > 10 and rotated % 7 == 0:
        final_diagnostic = -999  # Never reached
    
    return final_diagnostic

# Entry point with realistic simulation
if __name__ == '__main__':
    # Raw input data
    raw_sensor_data = [120, 45, 88, 205, 73, 94, 68, 150, 110, 82]
    
    # Irrelevant baseline for calibration (unused)
    calibration_sequence = [100, 102, 98, 101, 99]
    
    # Main processing steps
    processed_data = preprocess_sensor_readings(raw_sensor_data)
    
    # This validation runs but its output is ignored
    validation_result = validate_calibration(calibration_sequence, processed_data)
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result
    print(f"Target result: {final_diagnostic}")