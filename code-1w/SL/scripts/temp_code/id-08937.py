def calculate_thermal_capacity(profile, state):
    base_factor = 1.75
    adjustment = 0.23 if state == 'crystalline' else 0.12
    peak_energy = max(profile)
    avg_energy = sum(profile) / len(profile)
    
    # Distractor: Redundant frequency analysis (not used in final result)
    high_freq_count = 0
    for val in profile:
        if val > avg_energy * 1.5:
            high_freq_count += 1
    normalized_variance = (max(profile) - min(profile)) / avg_energy if avg_energy != 0 else 0
    
    # Irrelevant transformation chain
    transformed = [x * base_factor for x in profile]
    shifted = [int(x + adjustment * 10) for x in transformed]
    checksum = sum(shifted) % 100
    
    # Core logic with conditional expression
    capacity_score = sum(x ** 0.8 for x in profile if x > avg_energy)
    stability_ratio = (peak_energy / avg_energy) if avg_energy != 0 else 0
    thermal_capacity = (capacity_score * base_factor) + (stability_ratio * 10) if state in ['amorphous', 'crystalline'] else 0
    
    return thermal_capacity

# Simulation data
energy_readings = [12.5, 18.3, 9.7, 22.1, 14.8, 19.0, 11.2]
material_phase = 'crystalline'

# Secondary distractor variables
reference_norm = sum([x**2 for x in energy_readings]) ** 0.5
scaling_factor = reference_norm / 100.0
adjusted_readings = [x * scaling_factor for x in energy_readings]

# Key computation
thermal_capacity = calculate_thermal_capacity(energy_readings, material_phase)

# Output result
print(f"Result: {thermal_capacity}")