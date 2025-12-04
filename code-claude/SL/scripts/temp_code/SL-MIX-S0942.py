def analyze_signal(raw_signal, window_size=3):
    # Process the signal data
    processed_signal = []
    noise_threshold = 5  # Noise reduction parameter
    
    # Apply basic filtering (not needed for core calculation)
    for i in range(len(raw_signal)):
        if raw_signal[i] > noise_threshold:
            processed_signal.append(raw_signal[i] - noise_threshold//2)
        else:
            processed_signal.append(raw_signal[i])
    
    # Extract signal segments using slicing
    segments = []
    for i in range(0, len(processed_signal), window_size):
        segment = processed_signal[i:i+window_size]
        if len(segment) == window_size:  # Only consider complete segments
            segments.append(segment)
    
    # Calculate segment averages
    segment_averages = [sum(segment)/len(segment) for segment in segments]
    
    # Find frequency components (simulation)
    base_frequencies = [10, 20, 30, 40, 50]
    frequency_amplitudes = []
    
    # Calculate amplitudes based on segment averages
    for avg in segment_averages:
        # This calculation doesn't affect final result
        temp_amp = avg * 2.5
        frequency_amplitudes.append(round(avg))
    
    # Count occurrences of each amplitude (frequency analysis)
    frequency_data = {}
    for amplitude in frequency_amplitudes:
        if amplitude in frequency_data:
            frequency_data[amplitude] += 1
        else:
            frequency_data[amplitude] = 1
    
    # Calculate some statistics (distractors)
    mean_amplitude = sum(frequency_amplitudes) / len(frequency_amplitudes)
    max_amplitude = max(frequency_amplitudes)
    min_amplitude = min(frequency_amplitudes)
    
    # Find the most common amplitude (dominant frequency)
    dominant_frequency = max(frequency_data, key=frequency_data.get)
    
    # Calculate a meaningless metric (distractor)
    signal_complexity = (max_amplitude - min_amplitude) / (mean_amplitude + 1)
    
    return dominant_frequency, signal_complexity

# Input signal data
raw_signal = [7, 12, 8, 14, 9, 15, 10, 14, 8, 13, 9, 15, 8, 14, 9]

# Analyze the signal
dominant_frequency, complexity = analyze_signal(raw_signal)

# Print the result
print(f"Result: {dominant_frequency}")