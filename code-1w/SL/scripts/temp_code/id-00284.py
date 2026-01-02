def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]

def validate_calibration(sequence):
    checksum = sum(sequence) % 7
    return checksum == 0

# Irrelevant sensor simulation data
temperature_log = [23.5, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9]
humidity_buffer = [45, 47, 50, 52, 49, 46, 44]
pressure_sequence = [1013, 1015, 1012, 1010, 1008, 1011, 1014]

# Unused calibration matrix (distractor)
calibration_matrix = [
    [1.02, 0.98, 1.01],
    [0.99, 1.03, 0.97],
    [1.00, 1.01, 0.99]
]

# Energy profile with simulated fluctuations
energy_profile = [i**2 + 2*i - 1 for i in range(1, 8)]
efficiency_map = {i+1: (0.85 + (i * 0.02)) for i in range(7)}

# Red herring: unused function that looks important
def compute_entropy(data):
    import math
    entropy = 0
    total = sum(data)
    for x in data:
        prob = x / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

# Simulated fault detection with dead code path
def check_system_fault(state_vector):
    if len(state_vector) > 10:
        return True
    for val in state_vector:
        if val < 0:
            return True
    return False  # Never reached in practice

# Auxiliary transformation (partially relevant)
def transform_efficiency(eff_map):
    transformed = {}
    for k, v in eff_map.items():
        if k % 2 == 0:
            transformed[k] = v * 1.05
        else:
            transformed[k] = v * 0.95
    return transformed

# Core calculation function
def calculate_thermal_output(energy_levels, efficiency_rates):
    adjusted_efficiency = transform_efficiency(efficiency_rates)
    cumulative_energy = 0
    
    for idx, level in enumerate(energy_levels):
        step = idx + 1
        if step in adjusted_efficiency:
            # Apply modular weighting based on cycle phase
            modulation = (step % 4) + 1
            efficiency = adjusted_efficiency[step]
            contribution = level * efficiency / modulation
            
            # Conditional boost for odd cycles
            if step % 2 == 1:
                contribution *= 1.1
            
            cumulative_energy += contribution
            
            # Early termination red herring (never triggers)
            if cumulative_energy > 1e5:
                break
    
    # Final adjustment using bitwise masking to simulate hardware constraints
    masked_energy = int(cumulative_energy) & 0xFFFF  # Limit to 16-bit
    
    # Normalize against baseline reading (uses distractor variable)
    baseline = temperature_log[0]  # Only uses first element
    thermal_output = masked_energy / baseline
    
    return round(thermal_output, 4)

# Execute main computation
thermal_capacity = calculate_thermal_output(energy_profile, efficiency_map)

# Output result as required
print(f"Result: {thermal_capacity}")