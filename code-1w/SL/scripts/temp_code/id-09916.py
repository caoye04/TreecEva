def analyze_phase_transition(energy_levels):
    phase_shift = 0
    for i, level in enumerate(energy_levels):
        if i % 2 == 0:
            phase_shift += level * (i + 1)
        else:
            phase_shift -= level // (i + 1) if i != 0 else 0
    return phase_shift

# Irrelevant function - decoy for thermodynamic analysis
def compute_enthalpy(states):
    total = 0
    for s in states:
        total += s ** 2 - s
    return total + 117  # misleading constant

# Core transformation pipeline
def transform_sensor_data(raw_readings):
    processed = []
    offset = len(raw_readings) // 2
    for idx, val in enumerate(raw_readings):
        if idx < offset:
            processed.append(val * 3 + 5)
        else:
            processed.append(val * 2 - 3)
    return processed

# Misleading data structure manipulation
def shuffle_segments(data_blocks):
    temp_store = [0] * len(data_blocks)
    for i in range(len(data_blocks)):
        temp_store[(i * 3) % len(data_blocks)] = data_blocks[i]
    return temp_store  # never actually used in final computation

# Central calculation with key logic
def calculate_thermal_flux(layers):
    base_flux = 0
    adjustment_factor = 1.0
    
    # Real logic begins here
    for index, (inner, outer) in enumerate(zip(layers[:-1], layers[1:])):
        delta = outer - inner
        if delta > 0 and index % 2 == 0:
            base_flux += delta * (index + 1)
        elif delta < 0:
            base_flux -= abs(delta) // (index + 1) if index > 0 else 0
    
    # Apply non-linear correction using bit manipulation
    binary_mask = 0b1010
    masked_flux = base_flux & binary_mask
    
    # Final adjustment through conditional logic chain
    if base_flux > 50:
        adjustment_factor = 0.85
    elif base_flux < 20:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 1.0
    
    refined_flux = base_flux * adjustment_factor
    
    # Dead code path - looks important but unused
    secondary_correction = 0
    for bit in range(4):
        secondary_correction += (refined_flux >> bit) & 1
    
    return int(refined_flux)

# Unused auxiliary function - red herring
def validate_calibration(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= val + i * 7
    return bin(checksum).count('1') % 3 == 0

# Main execution flow
if __name__ == '__main__':
    # Simulated raw sensor inputs (real data source)
    temperature_profile = [12, 15, 14, 18, 22, 25, 24, 20]
    pressure_zones = [101, 105, 103, 110, 115, 112, 108, 106]
    
    # Irrelevant preprocessing steps
    enthalpy_states = [t + p//10 for t, p in zip(temperature_profile, pressure_zones)]
    computed_enthalpy = compute_enthalpy(enthalpy_states)  # distractor
    
    # Real data processing
    conduction_layers = transform_sensor_data(temperature_profile)
    
    # Another decoy operation
    scrambled_data = shuffle_segments(pressure_zones)
    is_valid = validate_calibration(scrambled_data)  # irrelevant boolean
    
    # Key physics-based analysis
    phase_energy = analyze_phase_transition(conduction_layers)
    
    # Critical assignment point - this is where the answer is determined
    thermal_gradient = calculate_thermal_flux(conduction_layers)
    
    # Output required result
    print(f"Result: {thermal_gradient}")