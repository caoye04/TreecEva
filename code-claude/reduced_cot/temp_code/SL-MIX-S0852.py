def analyze_spectrum(data_points, filter_strength=3):
    # Analyze frequency spectrum (distractor function)
    harmonics = []
    for i in range(1, len(data_points)):
        if i % filter_strength == 0:
            harmonics.append(i * sum(data_points[:i]) / max(1, len(data_points[:i])))
    return harmonics

def apply_noise_filter(signal, threshold):
    # Apply noise filtering (relevant function but with distractions)
    filtered = []
    noise_floor = sum(signal) / len(signal) if signal else 0
    
    # Distractor calculation that isn't used
    spectral_density = [(x - noise_floor)**2 for x in signal]
    
    # The actual filtering logic
    for amplitude in signal:
        if abs(amplitude) > threshold:
            filtered.append(amplitude)
        else:
            filtered.append(0)  # Zero out noise below threshold
    
    # More distractor calculations
    peak_to_peak = max(filtered) - min(filtered) if filtered else 0
    signal_power = sum(x**2 for x in filtered) / len(filtered) if filtered else 0
    
    return filtered

def get_dominant_frequency(signal, threshold):
    # Process signal data to find dominant frequency
    
    # Distractor variables and calculations
    sample_rate = 44100  # Standard audio sample rate
    nyquist = sample_rate / 2
    bit_depth = 16
    dynamic_range = 2**bit_depth
    
    # Apply several transformations (mostly distractions)
    normalized = [(x / max(abs(min(signal)), abs(max(signal)))) if signal else 0 for x in signal]
    
    # This lambda does actual work but is surrounded by distractions
    frequency_detector = lambda sig, thresh: sum([i for i, x in enumerate(sig) if abs(x) > thresh])
    
    # Distractor calculations with misleading names
    dominant_frequency = frequency_detector(normalized, 0.7)  # This isn't actually used
    bandwidth = len([x for x in normalized if abs(x) > 0.5])  # Another distractor
    
    # More distracting operations
    if bandwidth > 10:
        # This branch is never taken with our input data
        signal_type = "broadband"
        freq_estimation = bandwidth * 100
    else:
        # This is the branch that matters
        signal_type = "narrowband"
        # The key calculation is here, but with distractions
        filtered_signal = apply_noise_filter(signal, threshold)
        
        # Distractor calculations
        zero_crossings = sum(1 for i in range(1, len(filtered_signal)) 
                          if filtered_signal[i-1] * filtered_signal[i] < 0)
        
        # The actual calculation that matters
        freq_estimation = sum([i + 1 for i, x in enumerate(filtered_signal) if abs(x) > 0])
    
    # More misleading calculations that aren't used
    harmonic_series = analyze_spectrum(normalized, 2)
    resonant_freq = sum(harmonic_series) / len(harmonic_series) if harmonic_series else 0
    
    # Early return that isn't taken
    if len(signal) < 3:
        return sample_rate / 4
    
    # This is what actually gets returned
    return freq_estimation

# Setup signal data
signal_data = [3, -2, 0, 5, -1, 0, 4, 2]
noise_threshold = 1.5

# Distractor operations
fft_bins = len(signal_data) * 2
window_function = [0.5 - 0.5 * (2*i/(len(signal_data)-1) - 1)**2 for i in range(len(signal_data))]
windowed_signal = [signal_data[i] * window_function[i] for i in range(len(signal_data))]

# Calculate average power (distractor)
avg_power = sum(x**2 for x in signal_data) / len(signal_data)

# The key operation we're asking about
final_frequency = get_dominant_frequency(signal_data, noise_threshold)

# More distractor operations after the key operation
bandwidth = max(signal_data) - min(signal_data)
signal_to_noise = final_frequency / (avg_power ** 0.5) if avg_power > 0 else 0

# Print the result
print(f"Result: {final_frequency}")