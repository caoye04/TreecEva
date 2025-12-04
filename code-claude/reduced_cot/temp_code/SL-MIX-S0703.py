def analyze_signal_data(data, noise_level=3):
    # Signal processing parameters
    sampling_rate = 1000  # Hz
    nyquist = sampling_rate / 2
    noise_floor = 10
    signal_gain = 5
    
    # Process raw data
    filtered_data = [d for d in data if abs(d) > noise_level]
    
    # Calculate signal statistics
    mean_amplitude = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    peak_amplitude = max(abs(d) for d in filtered_data) if filtered_data else 0
    
    # Distractor calculations
    harmonics = [i * 50 for i in range(1, 6)]
    modulation_index = peak_amplitude / (mean_amplitude if mean_amplitude != 0 else 1)
    quality_factor = lambda f, bw: f / bw if bw > 0 else 0
    
    # Signal frequency estimation (simplified)
    frequency_bins = [0, 50, 100, 150, 200, 250, 300]
    frequency_powers = [noise_floor] * len(frequency_bins)
    
    # Simulate frequency domain data
    for i, freq in enumerate(frequency_bins):
        if freq == 0:  # DC component
            frequency_powers[i] = noise_floor + 5
        elif freq == 100:  # Main signal
            frequency_powers[i] = noise_floor + signal_gain * 15
        elif freq == 200:  # Harmonic
            frequency_powers[i] = noise_floor + signal_gain * 8
        elif freq in harmonics:  # Other harmonics
            frequency_powers[i] = noise_floor + signal_gain * 2
    
    # Create frequency analysis dictionary
    frequency_analysis = dict(zip(frequency_bins, frequency_powers))
    
    # Calculate noise statistics
    noise_mean = sum(v for k, v in frequency_analysis.items() if k not in [100, 200]) / (len(frequency_analysis) - 2)
    noise_threshold = noise_mean + 2 * noise_level
    
    # Helper function to validate frequency
    def is_valid_freq(f):
        # Frequencies divisible by 50 are considered valid in this domain
        return f > 0 and f % 50 == 0 and f < nyquist
    
    # Distractor processing
    secondary_peaks = [f for f, p in frequency_analysis.items() 
                      if p > noise_threshold and f != 100 and is_valid_freq(f)]
    harmonic_ratio = frequency_analysis.get(200, 0) / frequency_analysis.get(100, 1)
    snr_estimate = 10 * (frequency_analysis.get(100, 0) / noise_mean if noise_mean > 0 else 0)
    
    # Find the target frequency with the highest power above noise threshold
    max_power = max(frequency_analysis.values())
    max_freq = max(frequency_analysis.items(), key=lambda x: x[1])[0]
    
    # Check if we should apply the bandwidth correction
    bandwidth_correction = False
    if max_power > noise_threshold * 2:
        bandwidth_correction = True
    
    # Find target frequency using a more complex approach
    target_frequency = next((freq for freq, count in frequency_analysis.items() 
                           if count > noise_threshold and is_valid_freq(freq)), 0)
    
    # Distractor result calculations
    adjusted_frequency = target_frequency * (1 + 0.01 * noise_level) if target_frequency > 0 else 0
    confidence_metric = (max_power - noise_threshold) / noise_threshold if noise_threshold > 0 else 0
    
    return {
        'main_frequency': target_frequency,
        'signal_quality': confidence_metric,
        'harmonics': secondary_peaks
    }

# Test data
signal_data = [15, -8, 12, -5, 7, -9, 14, -6, 10, -7]

# Run analysis
result = analyze_signal_data(signal_data, noise_level=2)
print(f"Target result: {result['main_frequency']}")