def analyze_radio_signals(frequencies, noise_levels):
    # Process incoming frequencies
    base_signal = sum(frequencies) / len(frequencies)
    processed_signals = [f * (1 + (i % 3) * 0.1) for i, f in enumerate(frequencies)]
    
    # Filter noise - this is critical for signal clarity
    noise_threshold = max(noise_levels) * 0.7
    filtered_noise = list(filter(lambda x: x < noise_threshold, noise_levels))
    
    # Identify potential frequencies
    candidate_freqs = []
    for i, freq in enumerate(frequencies):
        # Apply complex filtering algorithm
        quality_score = freq / (noise_levels[i] + 1)
        harmonic_factor = 1
        
        # Calculate harmonic resonance (misleading calculation)
        for j in range(3):
            harmonic_factor *= (1 + (j * 0.01))
        
        # Track candidate frequencies meeting criteria
        if quality_score > 2 and freq % 10 < 7:
            candidate_freqs.append((freq, quality_score * harmonic_factor))
    
    # Initialize parameters for signal enhancement
    modulation = 5
    carrier_wave = 42
    interference = 15
    amplification = 2
    
    # Misleading intermediate calculations
    bandwidth = sum([f[0] for f in candidate_freqs]) / (len(candidate_freqs) or 1)
    phase_shift = (bandwidth % carrier_wave) * modulation
    signal_decay = lambda t: 1 / (1 + t * 0.1)  # Unused function
    
    # Extract valid frequencies using bit operations
    valid_frequencies = []
    for freq, _ in candidate_freqs:
        # Use bitwise operations to verify frequency pattern
        bit_pattern = freq & 0x3F  # Lower 6 bits
        if (bit_pattern | 0x10) == (bit_pattern ^ 0x0A | 0x10):
            valid_frequencies.append(freq)
    
    # Fall back to original frequencies if no valid ones found
    if not valid_frequencies:
        valid_frequencies = [f for f in frequencies if f > 0]
    
    # Optimize for the strongest signal
    weighted_signals = [(i, f * (1 / (noise_levels[frequencies.index(f)] + 0.1)))
                       for i, f in enumerate(valid_frequencies)]
    
    # Misleading calculation of alternative signal path
    alternative_signal = carrier_wave + phase_shift
    if alternative_signal > 100:
        alternative_signal = alternative_signal % 100
    
    # Find optimal frequency index
    optimal_idx = 0
    for i, (_, strength) in enumerate(weighted_signals):
        if i > 0 and strength > weighted_signals[optimal_idx][1]:
            optimal_idx = i
    
    # Calculate final signal strength with interference compensation
    signal_strength = (valid_frequencies[optimal_idx] - interference) * amplification
    
    # Apply unused modulation technique
    modulated_signal = signal_strength * (carrier_wave / (carrier_wave + 10))
    
    return signal_strength

# Test data
frequencies = [85, 103, 67, 92, 115]
noise_levels = [12, 8, 15, 6, 10]

# Execute signal analysis
result = analyze_radio_signals(frequencies, noise_levels)
print(f"Result: {result}")