import math

# Simulated signal processing pipeline with diagnostic traces
def analyze_frequency_bands(raw_samples):
    sample_count = len(raw_samples)
    normalized_powers = [abs(s)**2 for s in raw_samples]
    total_power = sum(normalized_powers)
    avg_power = total_power / sample_count if sample_count else 0

    # Irrelevant diagnostic computation (red herring)
    peak_to_average_ratio = max(normalized_powers) / avg_power if avg_power else 0
    entropy_approx = -sum(p/total_power * math.log(p/total_power + 1e-9) for p in normalized_powers)

    # Frequency band segmentation (real work begins)
    low_band = [s for s in raw_samples if abs(s) < 0.5]
    mid_band = [s for s in raw_samples if 0.5 <= abs(s) < 1.5]
    high_band = [s for s in raw_samples if abs(s) >= 1.5]

    # Signal dispersion metrics (distractor)
    dispersion_metric = sum(abs(mid_band[i] - mid_band[i-1]) for i in range(1, len(mid_band))) if mid_band else 0

    # Critical amplitude filtering (core logic)
    base_amplitudes = [abs(x) for x in high_band]
    threshold = 1.8
    filtered_amplitudes = [a for a in base_amplitudes if a > threshold]

    # Correction system with fake dependencies
    noise_floor = 0.02
    gain_stages = [1.0, 1.2, 1.1, 0.9]
    applied_gain = gain_stages[2] if len(filtered_amplitudes) > 3 else gain_stages[1]
    stability_factor = math.cos(math.pi * len(low_band) / (len(raw_samples) + 1))

    # Decoy calculation path (dead code - never used)
    if len(high_band) > 10:
        dummy_accumulator = 0
        for i in range(len(high_band)):
            dummy_accumulator += math.sin(high_band[i] * 0.1)
        calibration_offset = dummy_accumulator / len(high_band)
    else:
        calibration_offset = 0.0  # Unused variable

    # Real correction factor (depends only on mid_band and fixed params)
    nonlinearity_correction = 1.0 + 0.1 * math.sin(len(mid_band) * 0.5)
    correction_factor = applied_gain * nonlinearity_correction * (1 + stability_factor)

    # Key assignment statement
    filtration_score = sum(filtered_amplitudes) * correction_factor

    # Post-processing distractions
    spectral_peaks = []
    for i in range(1, len(normalized_powers)-1):
        if normalized_powers[i] > normalized_powers[i-1] and normalized_powers[i] > normalized_powers[i+1]:
            spectral_peaks.append(i)

    # Output unrelated diagnostics
    diagnostic_report = {
        'sample_size': sample_count,
        'dominant_band': 'high' if len(high_band) > len(mid_band) and len(high_band) > len(low_band) else 'mid',
        'peak_locations': spectral_peaks[:3]
    }

    return filtration_score  # Only this matters

# Simulated sensor input (deterministic)
phase_shifts = [math.sin(i * 0.21 + math.pi/4) + 0.7*math.cos(i * 0.13) for i in range(50)]
doppler_offsets = [0.3 * math.sin(i * 0.07) for i in range(50)]
raw_input_signal = [phase_shifts[i] + doppler_offsets[i] + 0.2*(i%4-1.5) for i in range(50)]

# Execute main analysis
result = analyze_frequency_bands(raw_input_signal)
print(f"Result: {result}")