def analyze_transmission(data_sequence, threshold=15):
    raw_peaks = [x for x in data_sequence if x > 8]
    base_power = sum(raw_peaks) / len(raw_peaks) if raw_peaks else 0

    # Irrelevant signal phase calculation (distractor)
    phase_shifts = list(map(lambda x: (x % 7) * 0.1, data_sequence))
    weighted_phase = sum(phase_shifts[:len(phase_shifts)//2])

    # Real processing path
    clipped_data = data_sequence[::2]  # Every other sample
    power_levels = [x**2 for x in clipped_data]
    avg_power = sum(power_levels) / len(power_levels)

    # Noise estimation with dummy operations
    temp_buffer = [x for x in power_levels if x < 100]
    noise_floor = len(temp_buffer) * 0.5
    adjustment_factor = 1.0
    
    if avg_power > threshold:
        adjustment_factor = 0.8
        secondary_check = [x for x in power_levels if x & 1]  # Bitwise check (semi-relevant)
        if len(secondary_check) > 3:
            adjustment_factor *= 0.95

    filtered_power = avg_power * adjustment_factor
    signal_strength = filtered_power - noise_floor

    # Dead code branch (red herring)
    if False:
        backup_signal = sum(data_sequence) * 0.1
        signal_strength = max(signal_strength, backup_signal)

    return signal_strength

# Main execution
transmission_input = [3, 12, 7, 16, 4, 9, 11, 6]
signal_strength = analyze_transmission(transmission_input)
print(f"Result: {signal_strength}")