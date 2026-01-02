import itertools

# Simulate wave interference in a multi-frequency signal analysis
def analyze_harmonic_stability(base_freq, harmonics_config):
    frequencies = [base_freq * (i + 1) for i in range(len(harmonics_config))]
    phases = [config['phase'] for config in harmonics_config]
    amplitudes = [config['amp'] for config in harmonics_config]

    # Irrelevant intermediate: power distribution (not used in final result)
    power_distribution = [amp ** 2 for amp in amplitudes]
    total_power = sum(power_distribution)
    avg_power = total_power / len(power_distribution) if power_distribution else 0

    # Distractor: frequency band classification
    band_classifications = []
    for f in frequencies:
        if f < 50:
            band_classifications.append('low')
        elif f < 150:
            band_classifications.append('mid')
        else:
            band_classifications.append('high')

    # Semi-relevant: phase normalization
    normalized_phases = [(p % 360) for p in phases]
    adjusted_phases = [p - 180 if p > 180 else p for p in normalized_phases]

    # Real computation begins: generate all pairwise frequency-phase interactions
    interaction_pairs = list(itertools.combinations(range(len(frequencies)), 2))
    phase_contributions = []

    for i, j in interaction_pairs:
        freq_diff = abs(frequencies[i] - frequencies[j])
        phase_diff = abs(adjusted_phases[i] - adjusted_phases[j])
        weight = amplitudes[i] * amplitudes[j]
        contribution = (freq_diff / (1 + phase_diff)) * weight
        phase_contributions.append(contribution)

    # Accumulate net effect on phase space
    raw_interference = sum(phase_contributions)
    stability_factor = len(interaction_pairs) if interaction_pairs else 1
    net_phase_shift = round(raw_interference / stability_factor, 4)

    # Dead code path: visual debugging output (never called)
    def debug_print():
        print("Frequencies:", frequencies)
        print("Phases:", adjusted_phases)
        print("Amplitudes:", amplitudes)

    return frequencies, adjusted_phases, net_phase_shift


def calculate_interference_pattern(freqs, phs):
    # Reconstruct dummy amplitude assumptions
    mock_amps = [1.5] * len(freqs)

    # Recompute pairwise effects
    pairs = list(itertools.permutations(range(len(freqs)), 2))
    shifts = []
    for i, j in pairs:
        delta_f = abs(freqs[i] - freqs[j])
        delta_p = abs(phs[i] - phs[j])
        effect = delta_f * (1 / (1 + delta_p)) * mock_amps[i]
        shifts.append(effect)

    # Additional distraction: harmonic symmetry check
    symmetric_pairs = [(a, b) for a, b in pairs if freqs[a] + freqs[b] == 2 * freqs[0]]
    symmetry_correction = len(symmetric_pairs) * 0.1

    base_net = sum(shifts) / len(shifts) if shifts else 0
    return round(base_net + symmetry_correction, 4)

# Setup experiment configuration
config = [
    {'harmonic': 1, 'phase': 270, 'amp': 2.0},
    {'harmonic': 2, 'phase': 95, 'amp': 1.8},
    {'harmonic': 3, 'phase': 185, 'amp': 1.2},
    {'harmonic': 4, 'phase': 260, 'amp': 0.9}
]

# Execute analysis
base_frequency = 20
frequencies, phases, stability_metric = analyze_harmonic_stability(base_frequency, config)

# Key computational step
net_phase_shift = calculate_interference_pattern(frequencies, phases)

# Output target result
print(f"Result: {net_phase_shift}")