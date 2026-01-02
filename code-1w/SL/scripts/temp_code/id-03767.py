import itertools

# Simulate wave interference in a multi-channel signal processor
def main():
    frequencies = [12.5, 25.0, 50.0, 100.0]
    amplitudes = [0.8, 1.2, 0.5, 2.0]
    phases = [0.1, 0.25, 0.6, 0.15]  # in radians
    damping_factors = [0.99, 0.98, 0.97, 0.96]

    # Irrelevant pre-processing: normalize amplitudes (not used later)
    normalized_amps = [amp / max(amplitudes) for amp in amplitudes]
    avg_amplitude = sum(normalized_amps) / len(normalized_amps)

    # Auxiliary calculation: total energy (distractor)
    total_energy = sum(a**2 for a in amplitudes)
    energy_threshold = 5.0
    high_energy_channels = [i for i, e in enumerate(amplitudes) if e**2 > energy_threshold]

    # Simulate phase drift due to temperature (semi-relevant but overridden)
    temp_drift_compensation = []
    base_temp = 25.0
    for t in range(4):
        drift = (base_temp - 20) * 0.001 * t
        temp_drift_compensation.append(drift)

    # Override with fixed correction (making prior loop partially irrelevant)
    temp_drift_compensation = [0.0 for _ in range(4)]

    def calculate_interference_phase(freqs, phs):
        # Apply frequency-weighted phase shift
        weighted_phases = [f * p for f, p in zip(freqs, phs)]
        
        # Generate all pairwise interactions using itertools
        interaction_terms = []
        for (i, wp1), (j, wp2) in itertools.combinations(enumerate(weighted_phases), 2):
            delta = abs(wp1 - wp2)
            if delta > 1.0:  # threshold filter
                interaction_terms.append(delta * 0.1)
        
        # Aggregate base and interaction effects
        base_sum = sum(weighted_phases)
        interaction_sum = sum(interaction_terms)
        
        # Dummy logic: simulate noise cancellation
        noise_floor = 0.05
        effective_interactions = [term for term in interaction_terms if term > noise_floor]
        if len(effective_interactions) > 2:
            interaction_sum *= 0.9  # damping

        # Final phase calculation
        raw_phase = base_sum + interaction_sum
        
        # Normalize to [-π, π] range
        while raw_phase > 3.14159:
            raw_phase -= 2 * 3.14159
        while raw_phase < -3.14159:
            raw_phase += 2 * 3.14159
        
        return round(raw_phase, 4)

    # Critical statement
    net_phase_shift = calculate_interference_phase(frequencies, phases)
    
    # Dead code: unused post-processing
    if net_phase_shift > 0:
        magnitude_class = 'POSITIVE'
    else:
        magnitude_class = 'NEGATIVE'
    
    # Additional distraction: entropy-like measure (irrelevant)
    phase_entropy = -sum(p * __import__('math').log(p + 1e-8) for p in phases)

    print(f"Result: {net_phase_shift}")

if __name__ == "__main__":
    main()