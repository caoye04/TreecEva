import itertools

# Simulate wave interference in a constrained harmonic system
def analyze_wave_behavior():
    base_frequency = 12
    harmonics = [base_frequency * i for i in range(1, 5)]
    sub_harmonics = [base_frequency // (i+1) for i in range(1, 4) if base_frequency % (i+1) == 0]
    
    # Mixed signal generation with distractor computations
    all_frequencies = sorted(harmonics + sub_harmonics)
    temp_amplitudes = [f % 7 + 0.5 for f in all_frequencies]
    weighted_sum = sum([a * f for a, f in zip(temp_amplitudes, all_frequencies)])
    normalization_factor = len(all_frequencies) ** 0.5
    
    # Irrelevant energy dispersion calculation (distractor)
    energy_loss = 0
    for i in range(len(all_frequencies)):
        for j in range(i+1, len(all_frequencies)):
            energy_loss += (all_frequencies[i] - all_frequencies[j]) ** 2
    energy_loss /= (len(all_frequencies) * 8.0) if len(all_frequencies) else 1

    # Phase initialization with deliberate complexity
    phase_seeds = [f % 11 for f in all_frequencies]
    phases = []
    for seed in phase_seeds:
        if seed % 2 == 0:
            phases.append((seed * 1.1) % (2 * 3.1416))
        else:
            phases.append((seed * 0.9) % (2 * 3.1416))
    
    # Signal coherence analysis (semi-relevant)
    coherence_pairs = list(itertools.combinations(range(len(all_frequencies)), 2))
    coherent_count = 0
    for i, j in coherence_pairs:
        freq_ratio = all_frequencies[j] / all_frequencies[i]
        if freq_ratio.is_integer() and freq_ratio <= 4:
            coherent_count += 1
    
    # Key computation: frequency-phase interference
    def calculate_interference_pattern(freqs, phaselist):
        total_shift = 0.0
        for idx, (f, p) in enumerate(zip(freqs, phaselist)):
            # Complex interaction term
            interaction = (f % 10) * (p / 3.1416) * ((idx + 1) % 3)
            total_shift += interaction
        # Final adjustment based on parity of frequencies
        even_freq_count = sum(1 for f in freqs if f % 2 == 0)
        if even_freq_count % 3 == 0:
            total_shift -= 2.5
        else:
            total_shift += 1.5
        return round(total_shift, 4)
    
    # Distractor: amplitude modulation chain (dead-end computation)
    modulated_amps = []
    for amp in temp_amplitudes:
        mod_val = amp
        for _ in range(3):
            mod_val = (mod_val ** 1.1) % 4.0
        modulated_amps.append(round(mod_val, 3))
    avg_modulation = sum(modulated_amps) / len(modulated_amps) if modulated_amps else 0
    
    # Critical execution point
    net_phase_shift = calculate_interference_pattern(all_frequencies, phases)
    
    # Additional irrelevant state tracking
    state_log = []
    for f in all_frequencies:
        if f > 20:
            state_log.append(f"High-{f}")
        elif f > 10:
            state_log.append(f"Mid-{f}")
        else:
            state_log.append(f"Low-{f}")
    
    # Output target result
    print(f"Result: {net_phase_shift}")
    return net_phase_shift

# Execute and capture result
result = analyze_wave_behavior()