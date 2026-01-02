def analyze_material_behavior():
    # Simulate material stress-strain analysis with filtering and transformation
    raw_stress_data = [120, 150, 180, 210, 240]
    strain_readings = [0.002, 0.003, 0.0045, 0.006, 0.008]

    # Derived stress levels with scaling factor
    stress_levels = [s * 0.95 for s in raw_stress_data]

    # Misleading intermediate calculation (not used in final result)
    avg_stress = sum(stress_levels) / len(stress_levels)
    max_strain = max(strain_readings)
    min_strain = min(strain_readings)

    # Simulated noise correction (distractor)
    corrected_noise = [s + 0.0001 for s in strain_readings]
    denoised = [c - 0.0001 for c in corrected_noise]

    # Apply non-linear correction to strain (relevant)
    nonlinear_factor = 1.08
    adjusted_strains = [s * nonlinear_factor for s in strain_readings]

    # Filter valid test cycles using set logic (key use of set operation)
    valid_cycles = {2, 3, 4}
    test_cycle_flags = {1: 'failed', 2: 'passed', 3: 'passed', 4: 'passed'}
    passed_indices = {k for k, v in test_cycle_flags.items() if v == 'passed'}
    usable_cycles = valid_cycles & passed_indices  # Set intersection

    # Extract corresponding strains and stresses for valid cycles
    strains = [adjusted_strains[i] for i in usable_cycles]
    filtered_stresses = [stress_levels[i] for i in usable_cycles]

    # Compute modulus approximation for each point (irrelevant)
    moduli = [filtered_stresses[i] / strains[i] for i in range(len(strains))]
    average_modulus = sum(moduli) / len(moduli)

    # Auxiliary tracking variables (distraction)
    measurement_count = len(raw_stress_data)
    processed_count = len(usable_cycles)
    data_efficiency = processed_count / measurement_count

    # Core yield calculation: weighted sum based on strain magnitude
    def calculate_strain_yield(strain_list, stress_list):
        cumulative_weight = 0.0
        total_contribution = 0.0
        for i in range(len(strain_list)):
            weight = strain_list[i] ** 1.5  # Nonlinear weighting
            cumulative_weight += weight
            total_contribution += weight * stress_list[i]
        if cumulative_weight == 0:
            return 0.0
        return total_contribution / cumulative_weight

    # Final computation step
    final_yield = calculate_strain_yield(strains, stress_levels)

    # Print result as required
    print(f"Target result: {final_yield}")

    # Return unused diagnostics (more distraction)
    diagnostics = {
        'modulus': average_modulus,
        'efficiency': data_efficiency,
        'raw_count': measurement_count
    }

    return final_yield, diagnostics

# Execute function to produce output
result, info = analyze_material_behavior()