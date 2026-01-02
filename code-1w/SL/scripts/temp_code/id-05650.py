from collections import defaultdict

# Simulate sensor array calibration with noise filtering and phase correction
def main():
    raw_readings = [1.2, 0.8, 1.5, 0.9, 1.1]
    baseline_noise = 0.3
    filtered_data = []
    temp_accumulator = 0.0

    # Apply noise threshold filter (distractor: temp_accumulator not used later)
    for val in raw_readings:
        if val > baseline_noise:
            filtered_data.append(val * 1.1)
        temp_accumulator += val ** 2  # Irrelevant accumulation

    # Compute effective signal magnitude (used)
    signal_magnitude = sum(filtered_data) / len(filtered_data)

    # Frequency band classification (semi-relevant)
    band_class = 'mid' if 1.0 < signal_magnitude < 1.4 else 'high'
    gain_profile = {'low': 0.8, 'mid': 1.1, 'high': 1.3}
    amplification = gain_profile[band_class]

    # Phase shift lookup table based on dominant frequency (used)
    phase_lookup = defaultdict(lambda: 0.5)
    phase_lookup.update({0: 0.6, 1: 0.75, 2: 0.9, 3: 1.05})

    # Ancillary diagnostic metrics (mostly irrelevant)
    sample_variance = sum((x - signal_magnitude) ** 2 for x in filtered_data) / len(filtered_data)
    stability_index = 1 / (1 + sample_variance) if sample_variance > 0 else 1
    debug_snapshot = {'variance': sample_variance, 'stability': stability_index}

    # Core phase calculation chain
    ref_id = int(signal_magnitude) % 4  # maps to 1
    raw_phase = phase_lookup[ref_id]
    correction_factor = 1.6
    adjustment_offset = -0.4

    # Key statement
    final_calibration = phase_lookup[ref_id] * correction_factor + adjustment_offset

    # Secondary transformation (dead path - never executed)
    if False:
        fallback_mode = True
        final_calibration *= 0.9

    # Final net phase shift computation (depends on prior)
    cycle_count = 3
    net_phase_shift = (final_calibration + 0.1) * cycle_count

    # Output result
    print(f"Result: {net_phase_shift}")

if __name__ == "__main__":
    main()