def process_signal_data(raw_readings):
    # Signal processing constants
    noise_threshold = 15
    amplification_factor = 2.5
    signal_offset = 42
    
    # Process the readings with various filters
    normalized = [r - signal_offset for r in raw_readings]
    
    # Apply noise reduction (values below threshold are considered noise)
    denoised = []
    for signal in normalized:
        if abs(signal) > noise_threshold:
            denoised.append(signal)
        else:
            # Still track noise for debugging
            denoised.append(0)
    
    # Track potential interference patterns
    interference_count = sum(1 for s in denoised if s == 0)
    interference_ratio = interference_count / len(denoised) if denoised else 0
    
    # Apply signal amplification to strong signals
    amplified = [s * amplification_factor if abs(s) > 2*noise_threshold else s for s in denoised]
    
    # Calculate signal metrics (not used in final processing)
    max_signal = max(amplified) if amplified else 0
    min_signal = min(amplified) if amplified else 0
    signal_range = max_signal - min_signal
    
    # Apply frequency domain transformation (simulated)
    transformed = []
    for i, signal in enumerate(amplified):
        if i % 3 == 0:  # Every third reading gets special processing
            transformed.append(signal * 1.5)
        elif i % 2 == 0:  # Every second (but not third) reading
            transformed.append(signal * 0.8)
        else:
            transformed.append(signal)
    
    # Extract only the meaningful signals for final analysis
    # We only care about positive signals in odd positions
    filtered_signals = [s for i, s in enumerate(transformed) if i % 2 == 1 and s > 0]
    
    # Discard extreme outliers (not used in final calculation)
    outlier_threshold = signal_range * 0.8
    clean_signals = [s for s in filtered_signals if s <= outlier_threshold]
    
    # Calculate signal strength
    potential_strength = sum(clean_signals)
    reference_strength = sum(filtered_signals)
    
    # Apply final calibration based on interference
    calibration_factor = 1.0
    if interference_ratio > 0.5:
        calibration_factor = 0.85
    elif interference_ratio > 0.3:
        calibration_factor = 0.92
    else:
        calibration_factor = 1.0
    
    # Calculate the actual signal strength
    actual_signal_strength = sum(filtered_signals)
    
    # Apply additional processing for system reporting (not used)
    adjusted_strength = actual_signal_strength * calibration_factor
    normalized_strength = adjusted_strength / len(raw_readings)
    
    return {
        'raw_count': len(raw_readings),
        'filtered_count': len(filtered_signals),
        'interference_ratio': interference_ratio,
        'signal_strength': actual_signal_strength,
        'normalized_strength': normalized_strength
    }

# Test with sample data
raw_readings = [65, 72, 48, 53, 89, 44, 35, 69, 57, 80]
result = process_signal_data(raw_readings)
print(f"Result: {result['signal_strength']}")