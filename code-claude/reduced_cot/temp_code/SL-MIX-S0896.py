def analyze_sound_frequencies(raw_data, threshold=10):
    # Process raw frequency data
    base_frequencies = [440, 523, 659, 784, 880, 988]
    noise_factor = 0.15  # Environmental noise coefficient
    
    # Apply noise filtering - this doesn't affect our target calculation
    adjusted_data = [(f + noise_factor * i) if i % 2 == 0 else (f - noise_factor * i) 
                    for i, f in enumerate(raw_data)]
    
    # Extract frequencies above threshold
    filtered_frequencies = [f for f in adjusted_data if f > threshold]
    
    # Count occurrences of frequency ranges
    frequency_ranges = [0] * 5
    for freq in filtered_frequencies:
        if freq < 500:
            frequency_ranges[0] += 1
        elif freq < 600:
            frequency_ranges[1] += 1
        elif freq < 700:
            frequency_ranges[2] += 1
        elif freq < 800:
            frequency_ranges[3] += 1
        else:
            frequency_ranges[4] += 1
    
    # Find the most common frequency range
    max_count = max(frequency_ranges)
    most_common_index = frequency_ranges.index(max_count)
    
    # These calculations are just distractions
    harmonic_mean = len(filtered_frequencies) / sum(1/f for f in filtered_frequencies if f > 0)
    pitch_variance = sum((f - sum(filtered_frequencies)/len(filtered_frequencies))**2 
                        for f in filtered_frequencies) / len(filtered_frequencies)
    
    # Select target frequency for analysis
    target_frequency = filtered_frequencies[most_common_index]
    
    # Calculate amplitude modulation (not relevant to our answer)
    modulation_depth = (max(filtered_frequencies) - min(filtered_frequencies)) / 2
    
    print(f"Target result: {target_frequency}")
    return target_frequency

# Sample frequency data
raw_frequencies = [320, 440, 540, 542, 545, 660, 670, 690, 750, 900]
result = analyze_sound_frequencies(raw_frequencies)