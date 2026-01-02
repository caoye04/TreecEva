import math

# Simulated sensor array data from environmental monitoring system
def acquire_sensor_data():
    raw_values = [127, 255, 192, 64, 96, 159]
    timestamps = [1634567890, 1634567892, 1634567894, 1634567896, 1634567898, 1634567900]
    return list(zip(timestamps, raw_values))

# Legacy compatibility wrapper (distractor)
def legacy_normalization(data):
    normalized = []
    for val in data:
        if val > 127:
            normalized.append(val * 0.8)
        else:
            normalized.append(val * 1.1)
    return normalized  # Never used in main flow

# Signal conditioning with noise filtering
def filter_noise(signal_pairs):
    filtered = []
    noise_floor = 32
    for ts, val in signal_pairs:
        if val >= noise_floor:
            adjusted = val - (val & 7)  # Clear lower bits to reduce jitter
            filtered.append((ts, adjusted))
    return filtered

# Amplitude classification (irrelevant branch)
def classify_amplitude(val):
    if val > 200:
        return 'HIGH'
    elif val > 100:
        return 'MEDIUM'
    else:
        return 'LOW'

# Main processing pipeline
def process_signal_chain(raw_data):
    # Step 1: Extract and align signals
    extracted = [val for _, val in raw_data]
    
    # Distractor computation: power spectrum estimation (unused)
    magnitude_spectrum = []
    for i, x in enumerate(extracted):
        component = abs(x * math.cos(math.pi * i / len(extracted)))
        magnitude_spectrum.append(component)
    
    # Step 2: Apply bitmask correction based on hardware specs
    corrected = []
    mask = 0xFF ^ 0x0F  # Clear lower nibble
    for val in extracted:
        corrected.append(val & mask)
    
    # Step 3: Detect rising edges using shifted comparison
    edges = 0
    for i in range(1, len(corrected)):
        if corrected[i] > corrected[i-1] + 10:
            edges += 1
    
    # Step 4: Compute weighted moving average (distractor structure)
    wma = 0.0
    weights = [0.1, 0.2, 0.4, 0.2, 0.1]
    center = len(corrected) // 2
    segment = corrected[center-2:center+3]
    for i, val in enumerate(segment):
        wma += val * weights[i]
    
    # Step 5: Generate bit signature of corrected values
    bit_signature = 0
    for val in corrected:
        bit_signature ^= val  # Accumulate XOR hash
        bit_signature = (bit_signature << 1) & 0xFF | (bit_signature >> 7)  # Rotate left
    
    return corrected, edges, bit_signature

# Advanced analysis using lambda-based reducers
def analyze_readings(processed):
    values, edge_count, signature = processed
    
    # Irrelevant statistical measures
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    
    # Core diagnostic logic (depends on edge count and signature pattern)
    base_score = 0
    for val in values:
        if val & 0x10:  # Check if bit 4 is set
            base_score += val >> 4
    
    # Critical transformation: combine with edge count
    intermediate = (base_score * 17) + edge_count
    
    # Apply signature modulation
    modulated = intermediate ^ (signature & 0x3F)
    
    # Final non-linear calibration
    calibrated = int(modulated * 1.75) - 42
    
    # Dead code path: floating-point refinement (never executed)
    if False:
        refinement_factor = lambda x: math.log(x + 1) / math.exp(0.1)
        calibrated = round(calibrated * refinement_factor(modulated))
    
    return calibrated

# Orchestration function with red herring branches
def run_diagnostics(mode='standard'):
    # Acquire raw sensor input
    raw_signals = acquire_sensor_data()
    
    # Preprocess with noise removal
    cleaned_signals = filter_noise(raw_signals)
    
    # Process through main pipeline
    processed_signals = process_signal_chain(cleaned_signals)
    
    # Compute final diagnostic score
    final_diagnostic = analyze_readings(processed_signals)
    
    # Distractor output (never printed)
    debug_info = []
    for i, (ts, val) in enumerate(raw_signals):
        debug_info.append(f"Sample {i}: {val} @ {ts}")
    
    # Spurious alternative calculation
    phantom_result = 0
    for x in [1, 2, 3]:
        for y in [4, 5]:
            for z in [6, 7]:
                phantom_result += x * y * z  # Dead end
    
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute main diagnostic sequence
run_diagnostics()