def calculate_magnitude(values):
    # Calculate magnitude of signal components
    return sum(v**2 for v in values)**0.5

def apply_noise_filter(data, threshold):
    # Apply noise filtering to raw signal data
    return [d for d in data if abs(d) >= threshold]

def extract_features(signal_data):
    # Extract key features from the signal data
    if not signal_data:
        return {}
    
    features = {
        'max': max(signal_data),
        'min': min(signal_data),
        'mean': sum(signal_data) / len(signal_data),
        'range': max(signal_data) - min(signal_data)
    }
    
    # Additional derived features (not used in main calculation)
    features['variance'] = sum((x - features['mean'])**2 for x in signal_data) / len(signal_data)
    return features

def process_signal(data, threshold):
    # Main signal processing function
    if threshold > 5:
        # High threshold branch - not taken in this example
        filtered = data[::-2]  # Reversed with step 2
        quality_factor = 0.75
    else:
        # Main processing branch that will be executed
        filtered = data[::2]  # Every second element
        quality_factor = 0.85
    
    # Calculate primary signal components
    components = [d * quality_factor for d in filtered]
    
    # Create a lookup table for signal weights (distractor)
    weights = {i: 1/(i+1) for i in range(10)}
    
    # Generate frequency bands (distractor)
    bands = [(i*100, (i+1)*100) for i in range(5)]
    
    # Process signal strength using bit manipulation and math
    base_value = len(components) & 0x7  # Mask with 0111 in binary
    shift_amount = threshold & 0x3      # Mask with 0011 in binary
    
    # Calculate a reference value (distractor)
    reference = sum(c for c in components if c > 0) - sum(c for c in components if c < 0)
    
    # Apply harmonic correction (distractor)
    harmonic_series = [1/h for h in range(1, 6)]
    correction_factor = harmonic_series[base_value % len(harmonic_series)]
    
    # This is the key calculation that determines the final result
    result = (base_value << shift_amount) + (len(filtered) & 0xF)
    
    # Signal quality assessment (distractor)
    snr = lambda sig, noise: 20 * (sig / max(noise, 1))
    quality_metrics = {'snr': snr(sum(filtered), threshold), 'clarity': quality_factor * 10}
    
    # Apply final scaling
    return result * correction_factor

# Raw signal data and parameters
raw_data = [3.2, -1.4, 5.8, -2.3, 7.1, -0.6, 4.9, -3.5, 6.0, -1.8]
noise_threshold = 2

# Calculate some statistics for reference (distractor)
stats = {
    'count': len(raw_data),
    'positive': len([x for x in raw_data if x > 0]),
    'negative': len([x for x in raw_data if x < 0])
}

# Filter data and extract features
filtered_data = apply_noise_filter(raw_data, noise_threshold)
features = extract_features(filtered_data)

# Process signal with noise threshold
signal_strength = process_signal(filtered_data, noise_threshold)

# Calculate alternative metrics (distractors)
alt_strength = calculate_magnitude(filtered_data)
modulation_index = features.get('range', 0) / features.get('mean', 1)

print(f"Target result: {signal_strength}")