def analyze_stability(phases):
    # Simulate thermal equilibrium analysis across phases
    peak_moment = max(phases) if phases else 0
    base_reference = sum(phases) / len(phases) if phases else 0

    # Irrelevant signal processing simulation (distractor)
    filtered_noise = list(map(lambda x: (x ** 2 + 3 * x + 1) % 17, phases))
    noise_peak = max(filtered_noise) if filtered_noise else 0
    adjusted_offset = (noise_peak * 0.37) // 1

    # Compute phase transitions with slicing and conditional logic
    transitions = 0
    for i in range(1, len(phases)):
        if phases[i] > phases[i-1] and phases[i] % 2 == 1:
            transitions += 1
        elif phases[i] < phases[i-1] and phases[i] % 3 == 0:
            transitions -= 1

    # Secondary distraction: simulate unused energy trace
    energy_trace = [p * (p // 2 + 1) for p in phases]
    total_energy = sum(energy_trace)
    normalized_energy = total_energy / 100 if total_energy > 100 else total_energy

    # Core stability metric computation
    fluctuation_index = sum(abs(phases[i] - phases[i-1]) for i in range(1, len(phases)))
    symmetry_score = abs(len(phases) - 2 * transitions)
    
    # Final score depends only on fluctuation_index, symmetry_score, and base_reference
    # Everything above includes red herrings and intermediate distractions
    equilibrium_score = int((fluctuation_index * 0.6) + (symmetry_score * 0.3) + (base_reference * 0.1))

    return equilibrium_score

# Experimental thermal phase data from reactor simulation
temperature_profile = [23, 45, 45, 12, 78, 33, 91, 10, 10]

# Slice to extract active thermal phases
thermal_phases = temperature_profile[1:8:2]  # Extracts [45, 12, 33, 10]

# Misleading pre-analysis (dead code path, not used later)
diagnostic_mode = True
if diagnostic_mode:
    snapshot = thermal_phases[::-1]
    checksum = sum(s * (i+1) for i, s in enumerate(snapshot))

# Key computation step
equilibrium_score = analyze_stability(thermal_phases)

print(f"Result: {equilibrium_score}")