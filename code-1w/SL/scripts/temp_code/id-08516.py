import itertools

# Domain-specific context: Signal processing with noise filtering and frequency analysis
def process_sensor_data(raw_readings):
    # Core variables
    base_frequency = 7
    phase_offset = 3
    sampling_rate = 100
    
    # Irrelevant calibration data (distractor)
    calibration_matrix = [[1.2, 0.8], [0.9, 1.1]]
    normalization_factor = 0.95 + 0.05 * 2  # Red herring computation
    temp_buffer = [0] * 10
    
    # Generate time-domain signal with modulation
    time_points = [t / sampling_rate for t in range(50)]
    raw_signal = [raw_readings[i % len(raw_readings)] * 
                  (0.5 + 0.5 * __import__('math').sin(2 * __import__('math').pi * 
                                          base_frequency * t + phase_offset)) 
                  for i, t in enumerate(time_points)]
    
    # Apply windowing function (relevant preprocessing)
    hamming_window = [0.54 - 0.46 * __import__('math').cos(2 * __import__('math').pi * n / (len(raw_signal) - 1)) 
                     for n in range(len(raw_signal))]
    windowed_signal = [raw_signal[i] * hamming_window[i] for i in range(len(raw_signal))]
    
    # Compute magnitude spectrum via simple DFT simulation (core logic)
    freq_bins = 20
    dft_magnitudes = []
    for k in range(freq_bins):
        real_part = sum(windowed_signal[n] * __import__('math').cos(2 * __import__('math').pi * k * n / len(windowed_signal)) for n in range(len(windowed_signal)))
        imag_part = -sum(windowed_signal[n] * __import__('math').sin(2 * __import__('math').pi * k * n / len(windowed_signal)) for n in range(len(windowed_signal)))
        magnitude = __import__('math').sqrt(real_part**2 + imag_part**2)
        dft_magnitudes.append(magnitude)
    
    # False path: Spectral smoothing (unused)
    smoothed_spectrum = dft_magnitudes.copy()
    for i in range(1, len(smoothed_spectrum) - 1):
        smoothed_spectrum[i] = (dft_magnitudes[i-1] + dft_magnitudes[i] + dft_magnitudes[i+1]) / 3
    
    # Noise threshold calculation using statistical heuristics
    noise_floor = sum(dft_magnitudes) / len(dft_magnitudes) * 0.3
    signal_threshold = noise_floor * 2.5
    
    # Frequency masking based on adaptive threshold
    mask = [mag > signal_threshold for mag in dft_magnitudes]
    
    # Extract significant frequency components
    significant_frequencies = [i for i, m in enumerate(mask) if m]
    
    # Simulate harmonic validation (additional filtering)
    harmonic_candidates = []
    if len(significant_frequencies) > 0:
        fundamental = min(significant_frequencies)
        if fundamental > 0:
            harmonics = [f for f in significant_frequencies if f % fundamental == 0]
            harmonic_candidates = [h for h in harmonics if h <= 3 * fundamental]
    
    # Transform back to modified domain using harmonic structure
    transformed_output = []
    for idx in range(len(windowed_signal)):
        value = windowed_signal[idx]
        if harmonic_candidates:
            modulator = __import__('math').sin(__import__('math').pi * harmonic_candidates[0] * idx / len(windowed_signal))
            value *= (1 + modulator) / 2
        transformed_output.append(abs(value))
    
    # Group consecutive similar values using tolerance clustering (itertools usage)
    tolerance = 0.05
    sorted_vals = sorted(enumerate(transformed_output), key=lambda x: x[1])
    grouped_indices = [list(group) for k, group in 
                       itertools.groupby(sorted_vals, key=lambda x: round(x[1] / tolerance))]
    
    # Extract clusters above energy threshold
    energy_threshold = 0.1
    high_energy_groups = []
    for grp in grouped_indices:
        avg_val = sum(item[1] for item in grp) / len(grp)
        if avg_val > energy_threshold:
            high_energy_groups.append([item[0] for item in grp])  # store original indices
    
    # Flatten and sort detected high-energy time points
    flattened_indices = sorted(itertools.chain.from_iterable(high_energy_groups))
    
    # Decoy operation: Attempt reconstruction from groups (not used in final result)
    reconstructed_profile = [0] * len(transformed_output)
    for idx_list in high_energy_groups:
        contribution = len(idx_list) / len(transformed_output)
        for pos in idx_list:
            reconstructed_profile[pos] += contribution
    
    # Final feature extraction: slice central segment and apply conditional scaling
    mid_start = len(flattened_indices) // 4
    mid_end = 3 * len(flattened_indices) // 4
    central_slice = flattened_indices[mid_start:mid_end]
    
    # Scale based on harmonic presence
    scaling_factor = 1.0
    if harmonic_candidates and len(harmonic_candidates) >= 2:
        scaling_factor = 1.75
    elif harmonic_candidates:
        scaling_factor = 1.25
    else:
        scaling_factor = 0.8
    
    scaled_indices = [idx * scaling_factor for idx in central_slice]
    
    # Filter results based on parity and modulo pattern (lambda + slicing)
    filtered_results = list(filter(lambda x: int(x) % 3 == 1, scaled_indices))
    
    # Final summation (target execution point)
    filtered_sum = sum(filtered_results)
    
    # Unused diagnostic print (dead code path)
    def debug_print():
        print(f"Fundamental: {fundamental if 'fundamental' in locals() else 'None'}")
        print(f"Harmonics found: {len(harmonic_candidates)}")
    
    return filtered_sum

# Entry point
sensor_input = [0.8, 1.1, 0.9, 1.3, 1.0, 0.7, 1.2]
sensor_result = process_sensor_data(sensor_input)
filtered_sum = sensor_result
print(f"Target result: {filtered_sum}")