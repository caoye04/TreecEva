import math

# Simulated sensor array data processing for aerospace diagnostics
def collect_sensor_data():
    raw_readings = [i * 0.213 for i in range(150)]
    return raw_readings

# Irrelevant auxiliary function - dead code path
def compute_wind_resistance(velocity):
    drag_coefficient = 0.47
    air_density = 1.225
    area = 2.5
    return 0.5 * air_density * velocity**2 * drag_coefficient * area

# Misleading preprocessing with red herring transformations
def preprocess_signal(data):
    filtered = [x for x in data if abs(x) > 0.5]  # List comprehension
    shifted = [math.sin(x) * 1.7 for x in filtered]
    padded = [0.0] * 5 + shifted + [0.0] * 5
    downsampled = padded[::3]  # Slicing operation
    return downsampled

# Decoy transformation chain
def apply_fourier_tone(signal):
    transformed = []
    for i in range(len(signal)):
        component = signal[i] * math.cos(i * 0.3)
        transformed.append(component)
    normalized = [x / (max(transformed) + 1e-8) for x in transformed]
    return normalized

# Core data processing with critical intermediate steps
def extract_features(signal):
    magnitude = sum(abs(x) for x in signal)
    peak = max(signal)
    zero_crossings = 0
    for i in range(1, len(signal)):
        if signal[i-1] < 0 < signal[i] or signal[i-1] > 0 > signal[i]:
            zero_crossings += 1
    avg = magnitude / len(signal)
    return {
        'magnitude': magnitude,
        'peak': peak,
        'zero_crossings': zero_crossings,
        'avg': avg
    }

# Redundant checksum verification - distractor logic
def validate_checksum(data):
    checksum = 0
    for val in data:
        checksum = (checksum + int(val * 100)) % 97
    return checksum == 42  # Always false for this data

# Secondary decoy analysis with unused result
def evaluate_stability_index(features):
    mag = features['magnitude']
    peaks = features['peak']
    stability = (peaks * 0.6) / (mag * 0.01 + 1)
    classification = "STABLE" if stability > 0.5 else "UNSTABLE"
    return classification, stability

# Critical analysis function that produces the target answer
def analyze_signal(samples):
    # Step 1: Extract core features
    features = extract_features(samples)
    
    # Step 2: Compute diagnostic metric using modular arithmetic and accumulation
    accumulator = 0
    for i in range(int(features['zero_crossings'])):
        term = (i * 73 + 41) % 1000  # Modular arithmetic
        accumulator += term
    
    # Step 3: Apply decay factor based on average amplitude
    decay_factor = math.exp(-features['avg'] * 0.3)
    adjusted_accum = accumulator * decay_factor
    
    # Step 4: Final transformation to produce diagnostic score
    diagnostic_score = int(adjusted_accum) ^ 0xAA55  # Bitwise XOR
    
    # Irrelevant conditional - misleading branching
    if diagnostic_score < 0:
        diagnostic_score = abs(diagnostic_score)
    elif diagnostic_score == 0:
        diagnostic_score = 999
    
    return diagnostic_score

# Main execution flow
if __name__ == "__main__":
    # Collect raw sensor data
    readings = collect_sensor_data()
    
    # Apply irrelevant wind resistance calculation (unused)
    resistance = compute_wind_resistance(250)
    
    # Process signal through multiple stages
    processed_signal = preprocess_signal(readings)
    processed_filtered = [x for x in processed_signal if x > -1.0]  # List comprehension (partial filter)
    processed_clipped = processed_filtered[:100]  # Slicing - truncation
    
    # Perform decoy validation
    is_valid = validate_checksum(processed_clipped)
    
    # Extract meaningful features
    extracted_features = extract_features(processed_clipped)
    
    # Run decoy stability evaluation (result ignored)
    stability_result = evaluate_stability_index(extracted_features)
    
    # Apply secondary transformation (not used in final result)
    fourier_enhanced = apply_fourier_tone(processed_clipped)
    
    # CRITICAL EXECUTION POINT
    final_diagnostic = analyze_signal(processed_clipped)
    
    # Print result in required format
    print(f"Target result: {final_diagnostic}")