from collections import defaultdict

# Simulate wave interference analysis with noise filtering and phase tracking
def analyze_wave_interference(signal_input, threshold=0.15):
    raw_peaks = []
    filtered_peaks = []
    peak_count_log = defaultdict(int)

    # Extract peaks from signal (simplified zero-crossing detection)
    for i in range(1, len(signal_input)):
        if signal_input[i-1] < 0 <= signal_input[i]:
            raw_peaks.append(i)
            peak_count_log['raw'] += 1

    # Apply amplitude threshold filter (simulated)
    for idx in raw_peaks:
        if abs(signal_input[idx]) > threshold:
            filtered_peaks.append(idx)
            peak_count_log['filtered'] += 1

    # Misleading energy calculation (not used in final result)
    total_energy = sum(x**2 for x in signal_input)
    avg_energy = total_energy / len(signal_input)
    energy_ratio = avg_energy / (threshold ** 2) if threshold > 0 else 0

    # Construct composite wave pattern based on filtered peaks
    composite_wave = [0] * 20
    for i, pos in enumerate(filtered_peaks):
        if i < 20:
            composite_wave[i] = (pos % 7) - 3  # Map to [-3, 3]

    # Reference pattern based on harmonic sequence
    reference_pattern = [int(2 * (j % 3) - 1) for j in range(20)]

    # Calculate phase interference between composite and reference
    def calculate_interference_phase(wave, ref):
        phase_shift = 0
        temp_shifts = []
        for k in range(len(wave)):
            if ref[k] != 0 and wave[k] != 0:
                shift = wave[k] // max(1, abs(ref[k]))
                temp_shifts.append(shift)
                if len(temp_shifts) > 5:
                    temp_shifts.pop(0)
                phase_shift += shift * ref[k]
        return phase_shift + len(temp_shifts)  # Final adjustment

    net_phase_shift = calculate_interference_phase(composite_wave, reference_pattern)

    # Dead code path - never executed under normal conditions
    debug_mode = False
    if debug_mode:
        print(f"Raw peaks: {len(raw_peaks)}")
        print(f"Filtered peaks: {len(filtered_peaks)}")
        print(f"Energy stats: {avg_energy:.4f}, Ratio: {energy_ratio:.4f}")

    return net_phase_shift

# Input signal (simulated sensor data)
sensor_data = [
    -0.1, 0.05, -0.2, 0.3, 0.1, -0.15, 0.25, -0.05, 0.12, -0.3,
    0.18, -0.11, 0.22, 0.09, -0.13, 0.17, -0.08, 0.14, 0.11, -0.19,
    0.21, -0.12, 0.16, 0.07, -0.14, 0.19, -0.1, 0.13, 0.08, -0.16
]

result = analyze_wave_interference(sensor_data)
print(f"Target result: {result}")