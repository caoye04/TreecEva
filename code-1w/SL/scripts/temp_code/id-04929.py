def analyze_signal(pattern):
    if not pattern:
        return 0
    return sum(ord(c) * (i + 1) for i, c in enumerate(pattern)) % 7

def decode_sequence(seq):
    temp_result = 0
    for i, val in enumerate(seq):
        temp_result += val ^ (i * 3)
    return temp_result

def validate_checksum(data_str):
    count_a = data_str.count('A')
    count_z = data_str.count('Z')
    return (count_a * 2 + count_z * 3) % 5

def shift_register(value, mode='left'):
    if mode == 'left':
        return (value << 2) & 0xFFFF
    else:
        return (value >> 1) & 0xFFFF

def compute_entropy(text):
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1
    entropy = 0
    length = len(text)
    for count in freq_map.values():
        p = count / length
        entropy -= p * __import__('math').log2(p) if p > 0 else 0
    return round(entropy, 4)

def extract_features(raw_string):
    segments = raw_string.split('-')
    feature_list = []
    for seg in segments:
        clean_seg = seg.strip().upper()
        if clean_seg.startswith('X'):
            feature_list.append(analyze_signal(clean_seg))
        elif clean_seg.isdigit():
            feature_list.append(int(clean_seg) % 19)
    return feature_list

def encrypt_token(token, key):
    encrypted = []
    for i, c in enumerate(token):
        shifted = ord(c) ^ (key + i) % 256
        encrypted.append(shifted)
    return encrypted

def merge_arrays(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        result.append((a + b) * 2)
    return result

def evaluate_diagnostic(code_sequence):
    base_score = 0
    for i, code in enumerate(code_sequence):
        if i % 2 == 0:
            base_score += code * 3
        else:
            base_score -= code
    return base_score

def process_readings(readings, key):
    # Core relevant logic starts here
    filtered = [r for r in readings if r % 2 == 1]
    transformed = [shift_register(r, 'left') for r in filtered]
    
    # Distractor: irrelevant entropy computation on fake string
    fake_string = "AXY-ZZ1-XX3"
    _ = compute_entropy(fake_string)
    
    # More distractions
    dummy_checksum = validate_checksum("AZZZ")
    dummy_signal = analyze_signal("XYZ")
    
    # Key transformation
    calibrated = [(t ^ key) % 1000 for t in transformed]
    
    # Another red herring: unused decryption attempt
    test_token = "SECRET"
    _ = encrypt_token(test_token, 12)
    
    # Real logic continues
    feature_vector = extract_features("X1A-2B-X2C")
    extended = merge_arrays(calibrated[:len(feature_vector)], feature_vector)
    
    # Final evaluation
    final_diagnostic = evaluate_diagnostic(extended)
    
    # Dead path - never executed due to prior filtering
    if False:
        fallback = 0
        for item in readings:
            fallback += item << 3
        return fallback
        
    return final_diagnostic

# Simulated sensor input and calibration
sensor_data = [23, 45, 67, 88, 101, 115]
calibration_key = 13

# Execute main logic
final_diagnostic = process_readings(sensor_data, calibration_key)
print(f"Target result: {final_diagnostic}")