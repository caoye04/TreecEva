import math

# Simulated sensor array data processing with diagnostic logic
def preprocess_sensor_readings(raw_readings):
    calibrated = [x * 1.05 for x in raw_readings]
    offset = sum(calibrated) / len(calibrated)
    adjusted = [x - offset + 2.1 for x in calibrated]
    return adjusted

# Irrelevant helper: spectral weight calculation (unused path)
def compute_spectral_weight(signal, freq):
    return sum(math.sin(x * freq) for x in signal[:10])

# Noise filtering using moving average (relevant)
def apply_noise_filter(data, window_size=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        segment = data[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

# Secondary filter: outlier suppression (partially relevant)
def suppress_outliers(values, factor=1.5):
    median_val = sorted(values)[len(values)//2]
    deviation = [abs(x - median_val) for x in values]
    mad = sorted(deviation)[len(deviation)//2]  # Median absolute deviation
    threshold = factor * mad
    return [median_val if abs(x - median_val) > threshold else x for x in values]

# Core analysis function (contains key logic)
def analyze_signal(signal, sensitivity):
    base_magnitude = sum(abs(x) for x in signal)
    normalized = base_magnitude / len(signal)
    
    # Complex conditional logic chain
    if normalized > sensitivity:
        activation = 1.0
        if any(x > 3*sensitivity for x in signal):
            activation += 0.7
            if all(x < 5*sensitivity for x in signal):
                activation += 0.4
            else:
                activation -= 0.3
        if len(signal) % 2 == 0 and normalized > 4.0:
            activation *= 1.2
    else:
        activation = 0.1
        
    # Bit manipulation red herring
    magic_key = 0
    for i in range(len(signal)):
        magic_key ^= int(abs(signal[i])) & 7
        magic_key = (magic_key << 1) | (magic_key >> 2)
        magic_key &= 0xF
    
    # Decoy transformation (irrelevant to final result)
    decoy_transform = ''.join([chr(int(65 + abs(x) % 26)) for x in signal if abs(x) > 1.0])
    decoy_checksum = sum(ord(c) for c in decoy_transform) % 100
    
    # Conditional expression with string method distraction
    mode_flag = 'HIGH' if activation > 1.5 else 'LOW'
    flag_code = mode_flag.lower().replace('h', 'X')
    
    # Final computation (depends only on activation)
    diagnostic_score = int((activation * 100) + 17)
    
    # Unused recursive side calculation (distractor)
    def recursive_energy(level, acc):
        if level <= 0:
            return acc
        return recursive_energy(level-1, acc + math.sqrt(level))
    
    return diagnostic_score

# Main execution flow
if __name__ == '__main__':
    # Initial sensor input (realistic domain)
    raw_sensor_data = [2.3, -1.7, 4.1, 3.9, 0.5, -2.2, 5.8, 3.0, 1.1, 4.4]
    
    # Step 1: Preprocess readings
    processed = preprocess_sensor_readings(raw_sensor_data)
    
    # Distractor variable (never used)
    entropy_estimate = -sum(x * math.log(abs(x)+1e-9) for x in processed)
    
    # Step 2: Apply noise filter (relevant)
    filtered_data = apply_noise_filter(processed)
    
    # Dead code path: unused filtering branch
    if len(filtered_data) < 5:
        alternate_path = [x * 2 for x in filtered_data]
        filtered_data = alternate_path
    
    # Step 3: Suppress outliers (relevant modification)
    filtered_data = suppress_outliers(filtered_data, factor=1.8)
    
    # Irrelevant list comprehension with string methods
    labels = [f'SENSOR_{i}' for i in range(len(filtered_data))]
    valid_labels = [label.lower().strip('_') for label in labels if 'X' not in label]
    label_hash = sum(len(lbl) for lbl in valid_labels)
    
    # Threshold determination with red herring logic
    dynamic_factor = 0.9
    for x in filtered_data:
        if x > 2.0:
            dynamic_factor *= 1.05
    reference_baseline = sum(filtered_data) / len(filtered_data)
    threshold = reference_baseline * dynamic_factor
    
    # UNUSED: complex bit flag simulation
    status_register = 0
    status_register |= (1 << 5)
    status_register &= ~(1 << 3)
    parity_check = bin(status_register).count('1') % 2
    
    # Key statement: what is the value of final_diagnostic after this?
    final_diagnostic = analyze_signal(filtered_data, threshold)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")