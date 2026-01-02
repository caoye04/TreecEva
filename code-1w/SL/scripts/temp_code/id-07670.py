import itertools

# Simulate signal processing with noise filtering and phase analysis
def analyze_frequency_bands(raw_samples):
    sample_count = len(raw_samples)
    base_amplitude = 0.0
    temp_buffer = []
    filtered_peaks = []
    noise_floor = 0.05
    peak_threshold = 0.7

    # Amplitude normalization and peak detection
    for s in raw_samples:
        normalized = abs(s) / max(1.0, max(raw_samples))
        temp_buffer.append(round(normalized, 3))

    for val in temp_buffer:
        if val > peak_threshold and val > noise_floor:
            filtered_peaks.append(val)

    # Compute harmonic weights using string-based labeling for traceability
    labels = [f"H{str(i+1).zfill(2)}" for i in range(len(filtered_peaks))]
    harmonic_weights = [float(label[1:]) * 0.1 for label in labels]

    weighted_sum = sum(h * p for h, p in zip(harmonic_weights, filtered_peaks))

    # Apply windowing function (Hamming approximation)
    window_correction = 0.54 - 0.46 * 0.1  # simplified for fixed size
    adjusted_sum = weighted_sum * window_correction

    # Dummy tracking variables for system load (irrelevant to final result)
    cpu_load_sim = 0.0
    for _ in itertools.repeat(None, 3):
        cpu_load_sim += 0.12
        cpu_load_sim = round(cpu_load_sim % 0.9, 2)

    # Phase logic based on dominant frequency index
    dominant_idx = -1
    if filtered_peaks:
        max_peak = max(filtered_peaks)
        dominant_idx = temp_buffer.index(max_peak)

    # Misleading entropy calculation (unused)
    entropy = 0.0
    for x in temp_buffer:
        if x > 0:
            entropy -= x * x * 0.1

    # Actual phase shift logic
    if dominant_idx % 3 == 0:
        phase_multiplier = 1.5
    elif dominant_idx % 3 == 1:
        phase_multiplier = 2.25
    else:
        phase_multiplier = 0.75

    net_phase_shift = adjusted_sum * phase_multiplier

    # Additional red herring: frequency folding simulation (dead code path)
    folded_spectrum = []
    for i, w in enumerate(harmonic_weights):
        if i % 2 == 0:
            folded_val = w * 0.5
        else:
            folded_val = w * 1.5
        folded_spectrum.append(round(folded_val, 3))

    # Only this output matters
    print(f"Result: {net_phase_shift}")
    return net_phase_shift

# Input signal with embedded pattern
input_signal = [0.3, 1.2, 0.9, 0.4, 1.8, 0.2, 1.6, 0.7]
analyze_frequency_bands(input_signal)