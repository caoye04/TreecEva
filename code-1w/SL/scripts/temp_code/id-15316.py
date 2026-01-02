import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw = [127, 85, 170, 255, 64, 192, 32, 224]
    scale_factor = 0.75
    offset = 12.5
    adjusted = []
    for val in raw:
        adjusted.append(val * scale_factor + offset)
    return adjusted

# Irrelevant auxiliary function - dead code path
def deprecated_filter(x):
    if x > 100:
        return x // 3
    else:
        return x % 7

# Signal conditioning with multiple distractors
def clean_noise(data):
    cleaned = []
    temp_buffer = []
    threshold = 50.0
    suppression_factor = 0.1
    for d in data:
        if d > threshold:
            # Apply exponential smoothing (relevant)
            smoothed = d * 0.9 + suppression_factor * 10
            cleaned.append(round(smoothed, 2))
        else:
            # Suppressed branch - misleading but never reached due to data
            noise_floor = math.log(d + 1) * suppression_factor
            temp_buffer.append(noise_floor)
    # Unused buffer - red herring
    if len(temp_buffer) > 3:
        temp_buffer.clear()
    return cleaned

# Bit manipulation decoy - looks important but unused
def bit_interleave(a, b):
    result = 0
    for i in range(8):
        result |= ((a & (1 << i)) << i) | ((b & (1 << i)) << (i + 1))
    return result

# Core transformation: XOR-based feature extraction (critical)
def extract_features(signal):
    features = []
    running_xor = 0
    for sample in signal:
        int_rep = int(sample)
        # Key operation: accumulate XOR of integer parts
        running_xor ^= int_rep
        features.append(int_rep % 17)  # Distractor usage
    # The real answer contributor
    return running_xor

# String-based metadata parser - irrelevant but plausible
def parse_header(header_str):
    fields = header_str.split('|')
    metadata = {}
    for f in fields:
        if ':' in f:
            k, v = f.split(':', 1)
            metadata[k.strip()] = v.strip().upper()
    # Slicing distraction
    if 'VERSION' in metadata:
        metadata['VERSION'] = metadata['VERSION'][:3]
    return metadata

# Main analysis with hidden logic chain
def analyze_signal(data):
    # Step 1: Extract critical XOR fingerprint
    fingerprint = extract_features(data)
    
    # Step 2: Simulate diagnostic matrix (mostly filler)
    diagnostics = {}
    diagnostics['baseline'] = sum(data) / len(data)
    diagnostics['variance'] = sum((x - diagnostics['baseline']) ** 2 for x in data) / len(data)
    diagnostics['peak'] = max(data)
    diagnostics['entropy'] = 0.0
    for d in data:
        if d > 0:
            diagnostics['entropy'] -= (d / 100) * math.log(d / 100)
    
    # Step 3: Hidden accumulator based on index parity (decoy)
    alt_sum = 0
    for idx, val in enumerate(data):
        if idx % 2 == 0:
            alt_sum += int(val) & 15
    
    # Step 4: Real final computation (non-obvious)
    # Combine fingerprint with baseline via bitwise and scaling
    magic_offset = 8192
    scaling_const = 0.25
    intermediate = fingerprint ^ 0xFF
    scaled_base = int(diagnostics['baseline'] * scaling_const)
    final_diagnostic = magic_offset - (intermediate + scaled_base)
    
    # Dead code - misleading print
    if final_diagnostic < 0:
        print("Anomaly detected")
    
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Collect and process signal
    raw_data = collect_readings()
    processed_data = clean_noise(raw_data)
    
    # Parse fake header (irrelevant)
    header = "TYPE:SENSOR|ID:7A3C|VERSION:2.1.9|CALIBRATED:YES"
    config = parse_header(header)
    
    # Run analysis
    final_diagnostic = analyze_signal(processed_data)
    
    # Output target result
    Result: {final_diagnostic}