def analyze_signal(input_sequence, filter_level=3):
    # Signal processing parameters
    base_value = 0
    noise_filter = 0
    security_mask = 0xFF
    
    # Process input sequence with different filters
    for idx, char in enumerate(input_sequence):
        # Apply primary filter
        if idx % 2 == 0:
            base_value = (base_value << 2) | (ord(char) & 0x3)
        else:
            noise_filter = (noise_filter >> 1) | ((ord(char) & 0x4) << 4)
    
    # Secondary processing
    secondary_factors = []
    for i, j in zip(range(1, 6), range(5, 0, -1)):
        secondary_factors.append(i * j)
    
    # Apply secondary factors (distraction)
    amplitude = sum(secondary_factors) // len(secondary_factors)
    phase_shift = amplitude * 2
    
    # Adjust base parameters
    base_value = (base_value + 15) & 0xFF
    noise_filter = (noise_filter + phase_shift) & 0x3F
    
    # Calculate signal clarity (distraction)
    clarity = 0
    for i, factor in enumerate(secondary_factors):
        if i < filter_level:
            clarity += factor
    
    # Final security calculations
    encryption_strength = (base_value ^ noise_filter) & security_mask
    integrity_check = (base_value | noise_filter) & 0x3F
    
    # Verify signal parameters (distraction)
    is_valid = encryption_strength > integrity_check
    validation_code = 42 if is_valid else 24
    
    print(f"Result: {encryption_strength}")
    return encryption_strength

# Process a sample signal
input_signal = "SecureTransmission"
result = analyze_signal(input_signal)