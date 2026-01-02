def analyze_quantum_sequence(pulse_sequence):
    # Irrelevant preprocessing
    baseline_correction = sum([x ** 2 for x in pulse_sequence if x > 0])
    normalization_factor = max(pulse_sequence) or 1
    corrected_seq = [x / normalization_factor for x in pulse_sequence]

    # Distractor: unused transformation
    fourier_mock = list(map(lambda x: (x + 1j)**2, corrected_seq))
    energy_signature = [abs(z) for z in fourier_mock][:len(corrected_seq)//2]

    # Real computation begins: filter active phases
    active_phases = [x for x in corrected_seq if abs(x) > 0.5]
    phase_weights = {i: val**3 for i, val in enumerate(active_phases)}

    # Decoy accumulation (not used later)
    cumulative_drift = 0
    for w in phase_weights.values():
        cumulative_drift += w * 0.01
        if cumulative_drift > 1.0:
            cumulative_drift = 0  # Reset loop - irrelevant

    # Key transformation: apply windowed shift
    shifted_phases = []
    window_size = 3
    for i in range(len(active_phases)):
        window_avg = sum(active_phases[max(0, i - window_size//2):i + window_size//2 + 1])
        shifted_phases.append(active_phases[i] + window_avg * 0.1)

    # Secondary distractor: string-based metadata (red herring)
    seq_tag = ''.join([str(int(abs(x*10))) for x in active_phases[:5]])
    checksum_label = seq_tag.upper().replace('0', 'X')  # Looks important

    # Core logic: integration via weighted summation
    def integrate_phase_shift(phases, weights):
        total_weight = sum(weights.values())
        flux_accumulator = 0
        for idx, phase_val in enumerate(phases):
            weight = weights.get(idx, 0.1)
            flux_accumulator += phase_val * weight
        return flux_accumulator / (total_weight or 1)

    # Another decoy structure: unused data aggregation
    stats_bundle = {
        'peak': max(shifted_phases, default=0),
        'entropy': sum([-w*log(w+1e-8) for w in weights.values()]),
        'mode': max(set(shifted_phases), key=shifted_phases.count) if shifted_phases else 0
    }

    # Actual target computation
    final_flux = integrate_phase_shift(shifted_phases, phase_weights)

    # Unrelated post-processing (dead path)
    if final_flux < 0:
        final_flux = abs(final_flux) ** 0.5
    elif final_flux > 1:
        final_flux = final_flux / 2  # Misleading modification

    # Correct result printed here
    print(f"Result: {final_flux}")
    return final_flux

# Supporting functions (avoid import dependency)
from math import log

# Input data with meaningful pattern
initial_pulse = [-2.0, 0.3, 1.2, -0.7, 0.9, 1.5, -0.4, 0.6]

# Execute
result = analyze_quantum_sequence(initial_pulse)