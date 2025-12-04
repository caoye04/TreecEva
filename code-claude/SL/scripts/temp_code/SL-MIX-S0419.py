def filter_harmonics(waves, threshold):
    filtered = []
    for i, wave in enumerate(waves):
        if i % 2 == 0 and wave > threshold:
            filtered.append(wave - threshold)
        elif i % 3 == 0 and wave < threshold:
            filtered.append(wave + threshold)
        else:
            filtered.append(wave)
    return filtered

def calculate_redundancy(data):
    # Calculates redundancy factor (unused)
    unique = len(set(data))
    return len(data) / unique if unique > 0 else 0

def normalize_signal(signal, bits=8):
    # Returns normalized signal value
    max_val = (1 << bits) - 1  # 255 for 8 bits
    return [max(0, min(s, max_val)) for s in signal]

def apply_noise_reduction(signal, noise_level):
    # Apply sophisticated noise reduction algorithm
    baseline = sum(signal) / len(signal) if signal else 0
    corrected = []
    for s in signal:
        # This complex adjustment isn't actually used
        adjustment = (s - baseline) * noise_level / 100
        # But this simple version is what matters
        corrected.append(s - noise_level if s > noise_level else s)
    return corrected

def calculate_signal_strength(frequencies, noise_filters):
    # Process the frequencies with various filters
    primary_frequencies = [f for f in frequencies if 20 <= f <= 20000]
    
    # Apply first noise filter
    filtered_signal = filter_harmonics(primary_frequencies, noise_filters[0])
    
    # These operations don't affect the final result
    secondary_signal = normalize_signal(filtered_signal)
    modulation_index = len([s for s in secondary_signal if s > 200]) / len(secondary_signal) if secondary_signal else 0
    phase_shift = sum([i * f for i, f in enumerate(filtered_signal)]) % 360
    
    # Apply second filter (key operation)
    reduced_noise = apply_noise_reduction(filtered_signal, noise_filters[1])
    
    # Calculate channel interference (distractor)
    interference_patterns = [abs(a - b) for a, b in zip(filtered_signal, reduced_noise)]
    max_interference = max(interference_patterns) if interference_patterns else 0
    
    # This is the actual calculation that matters
    signal_power = sum([f**2 for f in reduced_noise])
    noise_power = noise_filters[1]**2 * len(reduced_noise)
    
    # Conditional expression that determines result
    signal_to_noise = signal_power / noise_power if noise_power > 0 else 0
    
    # More distractor calculations
    clarity_index = 100 - (100 / (1 + signal_to_noise)) if signal_to_noise > 0 else 0
    potential_gain = modulation_index * clarity_index * 0.5
    
    # The key value we want
    return 10 * (signal_to_noise**0.5) if signal_to_noise > 1 else signal_to_noise * 5

# Main execution
audible_range = [50, 100, 200, 500, 1000, 2000, 5000, 10000]
frequencies = audible_range + [15, 25000]  # Adding frequencies outside audible range

# Filter settings
noise_threshold = 75
reduction_factor = 50
noise_filters = [noise_threshold, reduction_factor]

# Calculate various metrics (distractors)
redundancy = calculate_redundancy(frequencies)
valid_frequencies = [f for f in frequencies if 20 <= f <= 20000]
frequency_range = max(valid_frequencies) - min(valid_frequencies) if valid_frequencies else 0

# This is the key calculation we're asking about
signal_strength = calculate_signal_strength(frequencies, noise_filters)

# More distractor calculations after our target value
adjusted_strength = signal_strength * (1 + redundancy / 10)
quality_rating = "High" if signal_strength > 15 else "Medium" if signal_strength > 5 else "Low"

print(f"Frequencies: {frequencies}")
print(f"Noise filters: {noise_filters}")
print(f"Signal strength: {signal_strength}")
print(f"Quality rating: {quality_rating}")