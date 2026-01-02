import math

# Simulated sensor array diagnostics with signal processing and noise filtering
def collect_sensor_data():
    raw_values = [3, 5, 7, 11, 13, 17, 19, 23]
    noise_floor = 2.5
    adjusted = [v - noise_floor + (v % 3) for v in raw_values]
    return adjusted

def apply_calibration(signal_list):
    calibrated = []
    for x in signal_list:
        if x < 6:
            calibrated.append(x * 1.8)
        elif x > 15:
            calibrated.append(x * 0.9)
        else:
            calibrated.append(x)
    # Distractor: irrelevant transformation
    temp_shadow = [t ** 0.5 for t in calibrated if t > 10]
    return calibrated

def compute_entropy(data):
    # Dummy entropy-like calculation (not actually used in final result)
    total = sum(data)
    if total == 0:
        return 0
    entropy = 0
    for d in data:
        prob = d / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

def extract_flags(signal):
    # Extract binary flags based on thresholds (some are red herrings)
    flags = set()
    if signal[0] > 4:
        flags.add('F1')
    if signal[4] < 10:
        flags.add('F3')
    if len(signal) % 2 == 1:
        flags.add('ODD_LEN')
    # Irrelevant flag computation
    checksum = sum(signal) % 7
    decoy_flag = f'DECOY_{checksum}'
    flags.add(decoy_flag)  # Dead path — never used
    return flags

def shift_sequence(seq, key):
    # Bit manipulation as distraction
    shifted = []
    for i, val in enumerate(seq):
        bit_shifted = int((val * 10) // 1) ^ key
        bit_shifted = (bit_shifted << 1) | (bit_shifted >> 7)  # 8-bit rotate sim
        shifted.append(bit_shifted % 50)
    return shifted

def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    cleaned = [x for x in data if abs(x - mean_val) <= 2 * std_dev]
    return cleaned

def aggregate_metrics(clean_signal):
    # Core relevant logic begins here
    base_score = sum(clean_signal)
    bonus = 0
    for val in clean_signal:
        if val > 10 and val % 2 == 1:
            bonus += 3
    composite = base_score * 1.1 + bonus
    return int(composite)

def derive_key_from_metadata(meta):
    # Unused function — dead code path
    meta_str = ''.join(meta)
    key = 0
    for c in meta_str:
        key ^= ord(c)
    return key % 16

def analyze_readings(validated):
    # Final analysis using validated signals
    threshold_mask = [1 if x >= 9 else 0 for x in validated]
    activation_sum = sum(threshold_mask)
    total_power = sum(x ** 2 for x in validated) / len(validated)
    # Key formula: combine activation, power, and count of high-energy nodes
    high_energy = len([x for x in validated if x > 12])
    diagnostic_value = activation_sum * 100 + int(total_power) + high_energy * 10
    return diagnostic_value

# Main execution flow with distractions
if __name__ == '__main__':
    # Step 1: Collect raw sensor readings
    raw_input = collect_sensor_data()
    
    # Step 2: Apply non-linear calibration (some values modified)
    calibrated_input = apply_calibration(raw_input)
    
    # Step 3: Compute useless entropy metric (distractor)
    entropy_metric = compute_entropy(calibrated_input)
    
    # Step 4: Extract system flags (only length matters indirectly via filtering)
    status_flags = extract_flags(calibrated_input)
    
    # Step 5: Simulate secure transmission shift (completely irrelevant)
    encrypted_seq = shift_sequence(calibrated_input, key=7)
    
    # Step 6: Filter outliers — this affects the real data path
    filtered_output = filter_outliers(calibrated_input)
    
    # Step 7: Aggregate secondary metrics (bonus logic inside)
    score_summary = aggregate_metrics(filtered_output)
    
    # Step 8: Prepare metadata (dead end)
    metadata_tags = ['CALIB', 'SENSOR_5', 'MODE_A']
    access_key = derive_key_from_metadata(metadata_tags)
    
    # Step 9: Process signals for final diagnosis (core)
    processed_signals = [round(x) for x in filtered_output]
    
    # Step 10: Final diagnostic calculation
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output target result
    print(f"Result: {final_diagnostic}")