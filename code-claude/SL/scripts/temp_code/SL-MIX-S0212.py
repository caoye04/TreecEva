def apply_filter(data, coefficients):
    # Apply digital filter to signal data
    result = 0
    for i in range(min(len(data), len(coefficients))):
        result += data[i] * coefficients[i]
    return result

def calculate_noise_floor(samples):
    # Calculate theoretical noise floor (unused in final calculation)
    if not samples:
        return 0
    total = sum(abs(x) for x in samples)
    return total / len(samples) * 0.15

def compute_harmonic_distortion(signal, order=3):
    # Simulated harmonic distortion calculation (distractor)
    if not signal:
        return 0
    distortion = sum([(i+1) * abs(x) for i, x in enumerate(signal[:order])])
    return distortion / sum(abs(x) for x in signal) if sum(abs(x) for x in signal) else 0

def process_signal(data, coefficients):
    # Main signal processing function
    if not data or not coefficients:
        return -1
    
    # Apply several transformations to the signal
    normalized_data = []
    peak_value = max(abs(x) for x in data) if data else 1
    
    # Normalize the data (relevant)
    normalized_data = [x / peak_value for x in data]
    
    # Calculate various signal metrics (mostly distractors)
    noise_floor = calculate_noise_floor(normalized_data)
    harmonic_components = [normalized_data[i] * (0.5 ** i) for i in range(min(5, len(normalized_data)))]
    distortion = compute_harmonic_distortion(normalized_data)
    
    # Apply frequency domain transformation (distractor)
    freq_domain = lambda x: [sum(x[i] * ((-1)**(i*j)) for i in range(len(x))) for j in range(min(3, len(x)))]
    freq_components = freq_domain(normalized_data[:5]) if len(normalized_data) >= 5 else []
    
    # Apply the actual filter (relevant)
    filtered_signal = apply_filter(normalized_data, coefficients)
    
    # Conditional processing branch (mostly distractor)
    if filtered_signal > 0.8:
        # High signal path - not taken with our data
        gain_factor = 1.2
        compensation = 0.15
        return filtered_signal * gain_factor - compensation
    elif filtered_signal < 0.2:
        # Low signal path - not taken with our data
        gain_factor = 2.5
        noise_reduction = noise_floor * 0.3
        return filtered_signal * gain_factor + noise_reduction
    else:
        # Mid signal path - this is the one we'll take
        enhancement = lambda x: x * 1.5 if x > 0.5 else x * 1.25
        signal_quality = sum(coefficients) / len(coefficients)
        # The key calculation that determines our result
        return enhancement(filtered_signal) - 0.05 * signal_quality

# Initialize test data
raw_data = [0.42, 0.65, 0.48, 0.35, 0.38, 0.42]
test_data = [0.12, 0.24, 0.35] # Unused distractor data

# Initialize filter coefficients
filter_coefficients = [0.2, 0.3, 0.5, 0.4, 0.1, 0.05]
optimal_coefficients = [0.25, 0.45, 0.3] # Unused distractor coefficients

# Process the signal with different settings (distractors)
test_result = apply_filter(test_data, optimal_coefficients)
theoretical_snr = 10 * (sum(raw_data) / len(raw_data))
distortion_factor = compute_harmonic_distortion(raw_data)

# This is the key calculation that produces our answer
signal_strength = process_signal(raw_data, filter_coefficients)

# Alternative processing path (distractor)
alternative_strength = process_signal(test_data, optimal_coefficients)
combined_strength = (signal_strength + alternative_strength) / 2 if alternative_strength > 0 else signal_strength

# Output the result
print(f"Signal strength: {signal_strength}")
print(f"Alternative processing: {alternative_strength}") # Distractor output
print(f"Combined result: {combined_strength}") # Distractor output