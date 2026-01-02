from itertools import combinations

# Simulate wave interference analysis in a signal processing context
def analyze_wave_patterns(frequencies, amplitudes, phase_offsets):
    total_energy = 0.0
    transient_peaks = []
    dummy_counter = 0

    for i, (f, a, p) in enumerate(zip(frequencies, amplitudes, phase_offsets)):
        # Irrelevant intermediate computation (distractor)
        if f > 50:
            dummy_counter += 1
            adjustment_factor = 1.0 + (f % 7) / 100
        else:
            adjustment_factor = 1.0
        
        energy_contribution = a ** 2 * (1 + (f % 10) / 100)  # Slight variation
        total_energy += energy_contribution

        # Generate transient peaks (not used later)
        if i % 2 == 0 and a > 2:
            transient_peaks.append(f * 1.5)

    # Secondary processing: extract phase-angle interactions
    phase_angles = [p * 0.0174533 for p in phase_offsets]  # Convert to radians
    weights = [a / (sum(amplitudes) or 1) for a in amplitudes]

    # Misleading data transformation
    scaled_freqs = [f / max(frequencies) for f in frequencies]
    normalized_pairs = list(combinations(scaled_freqs, 2))

    net_phase_shift = calculate_interference(phase_angles, weights)

    # Additional red herring variables
    coherence_score = len(normalized_pairs) / (total_energy or 1)
    stability_index = (max(amplitudes) - min(amplitudes)) / (max(amplitudes) or 1)

    return net_phase_shift


def calculate_interference(phases, weights):
    weighted_sum = 0.0
    temp_buffer = []

    for i in range(len(phases)):
        # Apply weight and trigonometric transformation
        contribution = weights[i] * (phases[i] + (0.1 * (i % 3)))
        weighted_sum += contribution

        # Dead-end computation
        if i > 0:
            delta = phases[i] - phases[i-1]
            temp_buffer.append(abs(delta) ** 0.5)

    # Final aggregation with conditional adjustment
    final_shift = weighted_sum * 100
    final_shift = round(final_shift, 4) if final_shift > 0 else abs(final_shift)

    # Print result as required
    print(f"Result: {final_shift}")
    return final_shift

# Input data
freqs = [44, 67, 32, 89, 51]
ampls = [3.5, 5.2, 2.1, 6.8, 4.0]
phases = [30, 75, 120, 45, 90]

# Execute
result = analyze_wave_patterns(freqs, ampls, phases)