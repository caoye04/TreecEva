def calculate_weighted_harmonics():
    # Simulate sensor weights and harmonic response frequencies
    weights = [0.5, 1.2, 0.8, 1.5]
    frequencies = [440, 880, 1320, 1760]  # Hz
    
    # Irrelevant distractor: unused variable (minimal interference)
    calibration_offset = 0.05
    
    # Compute harmonic factors using frequency ratios relative to base
    base_freq = frequencies[0]
    harmonics = [round(f / base_freq, 3) for f in frequencies]
    
    # Key computation: weighted sum of harmonic contributions
    total_harmonic_weight = sum(weights[i] * harmonics[i] for i in range(len(weights)))
    
    # Print result for verification
    print(f"Result: {total_harmonic_weight}")

# Execute function
calculate_weighted_harmonics()