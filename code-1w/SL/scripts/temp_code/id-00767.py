import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_readings = [127, 255, 192, 64, 96, 159]
    gain_factor = 1.25
    amplified = [x * gain_factor for x in raw_readings]
    return amplified

# Irrelevant helper: network status simulation (dead code path)
def check_network():
    status_codes = {200: 'OK', 500: 'Error'}
    return status_codes[200]

# Signal filtering using set operations to remove noise bands
def filter_noise(signal):
    full_range = set(range(256))
    noise_floor = set(range(32))
    saturation_band = set(range(240, 256))
    allowed_band = full_range - noise_floor - saturation_band
    
    # Misleading intermediate: clipped values (not actually used in final result)
    clipped = [min(max(int(x), 32), 239) for x in signal]
    
    # Actual filtering logic
    quantized = [int(x) for x in signal]
    clean_signal = [x for x in quantized if x in allowed_band]
    return clean_signal

# Feature extraction with lambda-based transformations
def extract_features(data):
    entropy_estimator = lambda x: math.log(x) if x > 1 else 0
    features = []
    for val in data:
        b1 = val & 1
        b7 = (val >> 7) & 1
        parity = b1 ^ b7
        info_content = entropy_estimator(val)
        features.append((val, info_content, parity))
    
    # Decoy aggregation (never used)
    total_info = sum(f[1] for f in features)
    
    return features

# Data reconstruction from features (distractor function - not called)
def reconstruct_data(features):
    reconstructed = [f[0] for f in features]
    scale_back = [x * 0.9 for x in reconstructed]
    return scale_back

# Core analysis: compute diagnostic metric based on bit patterns and distribution
def analyze_signal(features):
    valid_count = 0
    pattern_score = 0
    parity_sum = 0
    
    # Linear search through features for specific entropy threshold
    threshold = math.log(100)
    high_entropy_group = []
    for f in features:
        if f[1] >= threshold:
            high_entropy_group.append(f)
    
    # Process high-entropy subset
    for entry in high_entropy_group:
        val, entropy_val, parity_bit = entry
        valid_count += 1
        
        # Bit manipulation: isolate middle bits 3-5
        mid_bits = (val >> 3) & 7  # bits 3,4,5
        pattern_score += mid_bits * entropy_val
        parity_sum += parity_bit
    
    # Composite diagnostic formula
    base_metric = pattern_score / valid_count if valid_count else 0
    adjustment = (parity_sum * 10) / (valid_count + 1)
    final_score = base_metric + adjustment
    
    # Secondary decoy calculation (looks important but unused)
    avg_val = sum(f[0] for f in features) / len(features)
    variance_proxy = sum((f[0] - avg_val)**2 for f in features) / len(features)
    
    return final_score

# Unused utility: string-based log formatter (red herring)
def format_diagnostics(code, level='INFO'):
    segments = ['SYS', 'CHK', 'DIAG']
    tag = '-'.join([s[:2].upper() for s in segments])
    timestamp = "2023-01-01T00:00:00"[:10]
    return f"[{timestamp}] {tag} {level}: {code}"

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw samples
    samples = collect_samples()
    
    # Step 2: Filter out noisy readings
    filtered = filter_noise(samples)
    
    # Step 3: Extract rich feature set
    features = extract_features(filtered)
    
    # Step 4: Analyze signal characteristics
    final_diagnostic = analyze_signal(features)
    
    # Print final result (critical output)
    print(f"Result: {final_diagnostic}")
    
    # Irrelevant logging output (distractor)
    debug_log = format_diagnostics(200, 'DEBUG')
    network_status = check_network()