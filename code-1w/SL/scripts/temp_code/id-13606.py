import itertools

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    scaled = [int(x * 255) for x in normalized]
    return scaled

# Irrelevant helper - looks important but unused in final path
def deprecated_filter(seq):
    return [x for x in seq if x % 2 == 0]

# Core transformation function
def generate_phase_shift(signal, offset):
    shifted = []
    for i in range(len(signal)):
        shift_index = (i + offset) % len(signal)
        shifted.append(signal[shift_index] ^ (offset & 255))  # Bitwise XOR with offset
    return shifted

# Data fusion from multiple sources
def fuse_streams(stream_a, stream_b):
    fused = []
    for a, b in zip(stream_a, stream_b):
        fused.append((a & 0xF0) | (b & 0x0F))  # Merge high and low nibbles
    return fused

# Pattern analyzer with set-based feature extraction
def extract_features(data):
    unique_vals = set(data)
    even_set = {x for x in unique_vals if x % 2 == 0}
    odd_set = {x for x in unique_vals if x % 2 == 1}
    prime_approx = {x for x in unique_vals if x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]}
    
    # Dummy metrics that look important
    entropy_proxy = len(unique_vals) * 0.1
    symmetry_score = sum(1 for x, y in zip(data, reversed(data)) if x == y)
    
    # Actual relevant metric
    feature_vector = [
        len(even_set),
        len(odd_set),
        len(prime_approx),
        len(even_set & prime_approx),
        len(odd_set - prime_approx)
    ]
    return feature_vector

# Main pattern analyzer
def analyze_pattern(processed, sequence_key):
    # Complex multi-step analysis with red herrings
    base_sum = sum(processed)
    mod_refs = [base_sum % k for k in sequence_key if k > 0]
    
    # Decoy computation - looks like it does something
    shadow_accum = 0
    for i, val in enumerate(processed):
        if i % 5 == 0:
            shadow_accum += val * (i // 10)
    
    # Real computation path (obscured)
    cycle_products = []
    for window in itertools.zip_longest(processed[::3], processed[1::3], processed[2::3], fillvalue=1):
        product = 1
        for w in window:
            product *= (w + 1)
        cycle_products.append(product % 256)
    
    # Key transformation
    adjusted_cycles = [(c ^ 0xAA) & 0x7F for c in cycle_products]  # Bit manipulation
    
    # Final diagnostic calculation
    diagnostic_seed = sum(adjusted_cycles) * len(sequence_key)
    final_diagnostic = (diagnostic_seed ^ 0x5555) % 1000000  # Final result
    
    # Dead code branch - never executed but looks critical
    if False:
        backup = 0
        for x in processed:
            backup += x << 2
        final_diagnostic = backup % 99999
    
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    # Simulated input data
    sensor_input = list(range(5, 155, 7))  # Generate raw readings
    
    # Unused decoy variables
    calibration_map = {i: i*3 + 2 for i in range(20)}
    legacy_thresholds = [0.1, 0.25, 0.5, 0.75, 0.9]
    debug_trace = []
    
    # Main processing pipeline
    cleaned = preprocess_readings(sensor_input)
    phase_1 = generate_phase_shift(cleaned, 13)
    phase_2 = generate_phase_shift(phase_1, 7)
    combined = fuse_streams(phase_1, phase_2)
    
    # Feature extraction (partly irrelevant)
    features = extract_features(combined)
    
    # Key sequence for analysis
    key_sequence = [3, 5, 7, 11, 13]
    transformed_data = [x for x in combined if x % 3 != 0]
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Output result
    print(f"Result: {final_diagnostic}")