def process_signal(signal_data, noise_threshold=15):
    # Apply complex filtering to remove noise
    filtered = [x for x in signal_data if abs(x) > noise_threshold]
    
    # This calculation is for metadata only and doesn't affect the result
    noise_ratio = len(filtered) / len(signal_data) if signal_data else 0
    
    # Unused normalization function
    normalize = lambda x: [val / max(abs(min(x)), max(x)) for val in x] if x else []
    
    return filtered

def calculate_amplitude(signal):
    # Calculate peak-to-peak amplitude
    if not signal:
        return 0
    return max(signal) - min(signal)

def calculate_frequency(signal_data):
    # Extract dominant frequency components
    if not signal_data:
        return 0
    
    # These weights simulate frequency domain analysis but are distractors
    weights = {i: (i % 3) * 0.1 + 0.7 for i in range(10)}
    
    # Harmonic detector (unused)
    harmonics = set([len(signal_data) // factor for factor in range(2, 6) if len(signal_data) % factor == 0])
    
    # This is the actual calculation that matters
    base_frequency = sum(signal_data[::2]) - sum(signal_data[1::2])
    
    # Misleading intermediate calculations
    phase_shift = sum([s * (i % 5) for i, s in enumerate(signal_data[:10])]) if len(signal_data) >= 10 else 0
    modulation_index = calculate_amplitude(signal_data) / 100
    
    # These branches lead to different results but only one is taken
    if len(signal_data) > 20:
        # This branch is a distractor
        carrier = sum(signal_data) / len(signal_data)
        return carrier * modulation_index + phase_shift
    elif len(signal_data) > 10:
        # This is the actual calculation path
        return base_frequency / 2
    else:
        # Another distractor path
        return sum(signal_data) * 0.15

# Main signal processing pipeline
signal_raw = [18, -22, 15, -16, 20, -25, 17, -19, 21, -24, 16, -18]

# Misleading secondary data
background_noise = [5, -4, 6, -3, 4, -5, 3, -6]
noise_profile = {f"band_{i}": sum(background_noise[:i])/i if i > 0 else 0 for i in range(5)}

# Distractor processing branch
if len(background_noise) > 10:
    calibration_factor = sum(background_noise) / len(background_noise)
else:
    calibration_factor = 0.75

# More distraction with unused lambda
filter_complex = lambda data, threshold: [x for x in data if abs(x) > threshold * calibration_factor]

# Actual processing happens here
filtered_signals = process_signal(signal_raw)

# The key calculation we're asking about
target_frequency = calculate_frequency(filtered_signals)

# Distractor calculations after the target value is set
amplitude = calculate_amplitude(filtered_signals)
signal_power = sum([x**2 for x in filtered_signals]) / len(filtered_signals)
quality_metric = amplitude / (signal_power or 1) * calibration_factor

# Display results
print(f"Filtered signal: {filtered_signals}")
print(f"Target frequency: {target_frequency}")