import math

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_values = [2.1, 3.5, 4.8, 5.0, 6.2, 7.4, 8.0, 9.1]
    timestamps = list(range(8))
    metadata = {'version': '2.3a', 'calibration': 0.987, 'units': 'μg/m³'}
    return list(zip(timestamps, raw_values))

# Legacy function - unused but looks relevant
def legacy_normalize(data):
    return [x * 0.95 for x in data if x > 3.0]

# Signal processing pipeline
def filter_noise(readings):
    cleaned = []
    noise_floor = 3.0
    for t, val in readings:
        if val >= noise_floor:
            cleaned.append((t, val * 1.05))
    return cleaned

# Frequency domain transformation (distractor)
def compute_spectral_density(signal):
    magnitude = 0.0
    for i, (t, v) in enumerate(signal):
        magnitude += v * math.sin(i * 0.5)
    spectral_index = abs(magnitude) / len(signal) if signal else 0
    return round(spectral_index, 4)

# Amplitude modulation analysis (irrelevant)
def modulate_amplitude(base_signal, carrier_freq=2.1):
    modulated = []
    for i, (t, v) in enumerate(base_signal):
        mod_val = v * math.cos(t * carrier_freq)
        modulated.append(mod_val)
    return modulated

# Data classification by threshold bands
def classify_readings(amplitudes):
    categories = {'low': 0, 'medium': 0, 'high': 0}
    for _, amp in amplitudes:
        if amp < 4.0:
            categories['low'] += 1
        elif amp < 7.0:
            categories['medium'] += 1
        else:
            categories['high'] += 1
    return categories

# String-based diagnostic tagging
def generate_diagnostics(flags):
    tag_map = {
        'low': 'L',
        'medium': 'M',
        'high': 'H'
    }
    tag_str = ''.join([tag_map[k] * flags[k] for k in ['low', 'medium', 'high']])
    # Apply transformations that look significant
    rotated = tag_str[1:] + tag_str[0]  # Left rotate
    inverted = rotated[::-1]  # Reverse
    encoded = inverted.upper().replace('L', 'X')  # Obfuscation
    return encoded

# Core analytical logic
def integrate_magnitude(signal):
    total = 0.0
    for t, v in signal:
        total += v ** 2
    return math.sqrt(total)

# Secondary weighting function (unused path)
def apply_temporal_decay(signal):
    weighted_sum = 0.0
    for i, (t, v) in enumerate(reversed(signal)):
        weighted_sum += v / (i + 1.5)
    return weighted_sum

# Main analysis engine
def analyze_readings(filtered_data):
    # Step 1: Compute vector magnitude
    magnitude_score = integrate_magnitude(filtered_data)
    
    # Step 2: Classify amplitude distribution
    class_counts = classify_readings(filtered_data)
    
    # Step 3: Generate string diagnostic code
    diagnostic_tag = generate_diagnostics(class_counts)
    
    # Step 4: Extract numeric features from tag
    tag_value = 0
    for c in diagnostic_tag:
        tag_value += ord(c) - ord('A')
    
    # Step 5: Combine with magnitude using combinatorial weight
    n_high = class_counts['high']
    combination_weight = math.comb(n_high + 2, 2) if n_high >= 1 else 1  # C(n+2,2)
    
    # Step 6: Final diagnostic calculation
    raw_diagnostic = magnitude_score * combination_weight
    adjustment_factor = len(diagnostic_tag) % 4
    final_diagnostic = raw_diagnostic - adjustment_factor * 0.25
    
    # Dead code branch - never executed due to fixed input
    if len(filtered_data) > 20:
        fallback = compute_spectral_density(filtered_data)
        final_diagnostic = max(final_diagnostic, fallback)
    
    # Irrelevant logging
    log_entry = f"ANALYSIS|{magnitude_score:.3f}|{diagnostic_tag}|{tag_value}"
    log_entry = log_entry.replace('|', ';').upper()
    
    return round(final_diagnostic, 6)

# Unused utility (red herring)
def validate_checksum(data_string):
    return sum(ord(c) for c in data_string) % 17

# Execution workflow
if __name__ == '__main__':
    # Acquire initial measurements
    sensor_log = acquire_sensor_data()
    
    # Apply noise filtering
    processed_signals = filter_noise(sensor_log)
    
    # Perform spectral analysis (distractor call)
    dummy_spectral = compute_spectral_density(processed_signals)
    
    # Modulation test (dead end)
    dummy_mod = modulate_amplitude(processed_signals)
    
    # Trigger key computation
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")