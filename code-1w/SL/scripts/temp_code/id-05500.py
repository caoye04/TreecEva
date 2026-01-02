import math

# Simulated sensor data processing with red herrings and complex logic paths
def preprocess_waveform(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

# Irrelevant transformation: not used in final computation
def transform_coordinates(coords):
    return [(c[0] * math.cos(c[1]), c[1] + math.pi / 4) for c in coords]

# Decoy function: looks important but unused
def compute_entropy(data):
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Bit manipulation utility (used once in critical path)
def pack_flags(status_bits):
    packed = 0
    for i, bit in enumerate(status_bits):
        packed |= (bit << i)
    return packed

# Data alignment using slicing (critical)
def align_pattern(sequence, offset=3):
    return sequence[offset:] + sequence[:offset]

# Set-based interference: creates distraction but not central
def detect_anomalies(values):
    baseline = set(range(10, 20))
    observed = set([int(abs(v * 10)) for v in values])
    deviations = observed ^ baseline  # XOR set difference
    return len(deviations) > 5

# Core analysis function with multiple logic layers
def analyze_signal(buffer, thresholds):
    # Step 1: slice and realign buffer
    shifted = align_pattern(buffer, 2)
    
    # Step 2: extract control flags via bitwise ops
    flags = [int(x % 1 >= 0.5) for x in shifted[:4]]
    flag_word = pack_flags(flags)  # becomes 11
    
    # Step 3: apply threshold masking (set operation disguise)
    active_indices = {i for i, x in enumerate(thresholds) if x > 0.75}
    magnitude = 0
    
    # Step 4: conditional accumulation with short-circuiting
    for i in range(len(shifted)):
        if i in active_indices and i < len(shifted):
            magnitude += shifted[i] * thresholds[i]
        elif magnitude > 10:  # dead condition due to data
            break
    
    # Step 5: inject misleading early-return pattern (never triggers)
    if flag_word == 0:
        return -999  # decoy
    
    # Step 6: secondary adjustment based on slice statistics
    tail_slice = shifted[-5:]
    correction = sum(tail_slice) / len(tail_slice)
    
    # Step 7: final nonlinear transformation
    adjusted = (magnitude + correction) ** 2
    adjusted = math.floor(adjusted * 100) / 100  # round to 2 decimals
    
    # Final decision gate (uses flag_word from bitwise op)
    if flag_word & 0b1010:  # checks alternating bits
        adjusted += 1.25
    
    return adjusted

# --- Main execution ---
if __name__ == "__main__":
    # Initialize sensor input (simulated)
    signal_input = [0.15, 0.82, 0.93, 0.11, 0.47, 0.68, 0.33, 0.74]
    pattern_buffer = preprocess_waveform(signal_input)  # Result: [0.82, 0.93, 0.47, 0.68, 0.33, 0.74]
    
    # Irrelevant coordinate data (distraction)
    polar_coords = [(1.0, 0.1), (2.5, 0.8), (1.7, 1.2)]
    transformed = transform_coordinates(polar_coords)
    
    # Threshold configuration (only some elements > 0.75)
    threshold_map = [0.2, 0.3, 0.91, 0.87, 0.4, 0.7, 0.93, 0.5]
    
    # Spurious anomaly check (evaluates but unused)
    has_issue = detect_anomalies(pattern_buffer)
    
    # Actual key computation
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")