import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [0.88, -1.22, 3.14, -2.71, 0.0, 1.41, -1.73]
    scale_factor = 1.5
    offset = 0.5
    calibrated = [(x * scale_factor) + offset for x in raw_samples]
    return calibrated

# Irrelevant helper: used nowhere but looks important
def entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Signal conditioning with red herring transformations
def filter_noise(signal):
    filtered = []
    threshold = 0.5
    suppression_factor = 0.1
    for val in signal:
        if abs(val) < threshold:
            val *= suppression_factor  # attenuate small values
        else:
            val += 0.05  # minor correction
        filtered.append(round(val, 4))
    
    # Distractor: fake smoothing pass (unused)
    smoothed = [filtered[0]]
    for i in range(1, len(filtered)-1):
        smoothed.append((filtered[i-1] + filtered[i] + filtered[i+1]) / 3)
    smoothed.append(filtered[-1])
    
    # Dead code path: never executed due to prior logic
    if len(smoothed) > 100:
        return [x * 1.1 for x in smoothed]
    
    return filtered

# Data encoding step with misleading bit operations
def encode_frame(data):
    encoded = []
    mask = 0b11111111
    base_shift = 3
    
    for x in data:
        # Convert float to fixed-point integer for bit manipulation
        fixed = int(abs(x) * 100) & mask
        
        # Real transformation
        transformed = (fixed << base_shift) ^ 0b101010
        encoded.append(transformed)
        
        # Irrelevant bit noise (never used)
        parity = bin(fixed).count('1') % 2
        checksum = (fixed >> 4) ^ (fixed & 0b1111)
        dummy_op = (checksum << 2) | parity
        
    return encoded

# Core analysis with conditional early exits and distractors
def validate_integrity(encoded):
    if not encoded:
        return False
    
    # Checksum logic that seems important but is bypassed
    total_sum = sum(encoded)
    expected = (encoded[0] + encoded[-1]) * 2
    if total_sum < expected:
        temp_result = [x for x in encoded if x % 2 == 0]
        if len(temp_result) > 5:
            return True
    
    # Actual validation rule (non-obvious)
    valid_count = 0
    for val in encoded:
        if val & 0b101010 == 0b101010:  # checks if specific bits are set
            valid_count += 1
    
    # Early exit red herring
    if valid_count == 0:
        return False
        redundant_clear = [0] * len(encoded)
        for i in range(len(redundant_clear)):
            redundant_clear[i] = i * 2
    
    return valid_count >= 3

# Main diagnostic engine with decoy state tracking
def analyze_signal(data_stream):
    # Step 1: Preprocess
    processed = filter_noise(data_stream)
    
    # Tracking variables that seem important
    stats = {
        'peak': max(processed),
        'trough': min(processed),
        'range': 0,
        'clipped': 0
    }
    stats['range'] = stats['peak'] - stats['trough']
    
    # Decoy normalization
    if stats['range'] != 0:
        normalized = [(x - stats['trough']) / stats['range'] for x in processed]
        discretized = [int(x * 255) for x in normalized]
    
    # Step 2: Encode
    frame = encode_frame(processed)
    
    # Step 3: Validate
    is_clean = validate_integrity(frame)
    
    # Step 4: Diagnose — this is where the real answer is computed
    diagnostic_code = 0
    for val in frame:
        if val > 200:
            diagnostic_code += val % 25  # contributes small deltas
        elif val < 50:
            diagnostic_code -= 1
    
    # Final adjustment based on validation (critical)
    if is_clean:
        diagnostic_code *= 2
    else:
        diagnostic_code += 10
    
    # Distractor block: complex unused calculation
    if diagnostic_code > 0:
        inverse_map = {i: math.atan(i / 10) for i in range(1, diagnostic_code+1) if i % 3 == 0}
        weighted_avg = sum(inverse_map.values()) / len(inverse_map) if inverse_map else 0
        final_weight = math.floor(weighted_avg * 100)
        
    # The actual target variable
    final_diagnostic = diagnostic_code + 5
    
    # Never-executed cleanup
    if final_diagnostic < 0:
        processed.clear()
        frame = None
    
    return final_diagnostic

# Execution flow
sensor_data = collect_readings()
processed_data = filter_noise(sensor_data)
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")