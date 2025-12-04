def analyze_radio_signals(frequencies, strengths, noise_threshold=15):
    # Signal quality calculation helper
    def calculate_quality(strength, interference, distance):
        potential_quality = (strength * 2) - (interference / 2)
        distance_factor = max(0, 1 - (distance / 100))
        return potential_quality * distance_factor
    
    # Track signal information
    signal_count = len(frequencies)
    signal_strengths = []
    signal_qualities = []
    interference_levels = [12, 8, 23, 5, 19, 7, 14]
    satellite_distances = [45, 68, 22, 97, 51, 33, 76]
    
    # Environmental conditions (affect some calculations)
    atmospheric_density = 1.2
    solar_activity = 0.8
    magnetic_distortion = 2.5
    
    # Process all received signals
    for i in range(signal_count):
        # Apply atmospheric corrections to strength values
        raw_strength = strengths[i]
        corrected_strength = raw_strength * atmospheric_density
        
        # Calculate interference factors
        if i < len(interference_levels):
            interference = interference_levels[i] * solar_activity
            distance = satellite_distances[i]
        else:
            # Default values for additional signals
            interference = 10 * solar_activity
            distance = 50
        
        # Store processed strength
        signal_strengths.append(corrected_strength)
        
        # Calculate and store signal quality
        quality = calculate_quality(corrected_strength, interference, distance)
        signal_qualities.append(quality)
        
        # Debug logging (not used in final calculation)
        log_value = (frequencies[i] % 100) + (raw_strength / 10)
        if log_value > 50:
            # This branch is never used in the final result
            anomaly_factor = log_value * magnetic_distortion
            corrected_log = anomaly_factor - 25
    
    # Find signals above noise threshold
    valid_signals = []
    valid_indices = []
    for i, strength in enumerate(signal_strengths):
        # Distracting calculation that isn't used
        noise_ratio = strength / (noise_threshold + 0.01)
        weighted_quality = signal_qualities[i] * (1 + (noise_ratio / 10))
        
        if strength > noise_threshold:
            valid_signals.append(frequencies[i])
            valid_indices.append(i)
    
    # Calculate optimal signal (misleading - not the final answer)
    potential_optimal = max(signal_qualities) if signal_qualities else 0
    avg_strength = sum(signal_strengths) / len(signal_strengths) if signal_strengths else 0
    
    # The actual answer calculation
    filtered_strengths = [signal_strengths[i] for i in valid_indices if i % 2 == 0]
    if not filtered_strengths:
        optimal_index = 0
    else:
        # Find the index of the maximum value among valid even-indexed signals
        max_strength = max(filtered_strengths)
        relative_index = filtered_strengths.index(max_strength)
        
        # Map back to the original signal index
        even_valid_indices = [idx for idx in valid_indices if idx % 2 == 0]
        optimal_index = even_valid_indices[relative_index]
    
    # Calculate final result
    target_frequency = signal_strengths[optimal_index]
    
    # More distracting calculations
    harmonic_series = [frequencies[i] * (i+1) for i in range(min(3, len(frequencies)))]
    resonance_factor = sum(harmonic_series) / 1000 if harmonic_series else 0
    
    print(f"Result: {target_frequency}")
    return target_frequency

# Test data
frequencies = [92.5, 101.3, 88.7, 105.9, 97.1]
strengths = [18, 12, 25, 9, 14]

# Execute analysis
result = analyze_radio_signals(frequencies, strengths)