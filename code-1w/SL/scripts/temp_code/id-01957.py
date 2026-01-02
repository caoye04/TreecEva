import math

def preprocess_stress_data(raw_readings):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in raw_readings if x > 0]

def validate_calibration(sequence):
    # Misleading validation logic (not used in final computation)
    return all(seq % 4 != 0 for seq in sequence)

def shift_encoding(value, direction='left'):
    # Distractor bit manipulation function
    if direction == 'left':
        return (value << 3) & 0xFF
    return (value >> 2) & 0xFF

def recursive_dampener(x, depth=0):
    # Decoy recursive function with no impact
    if depth >= 3:
        return x
    return recursive_dampener((x + 10) // 2, depth + 1)

def transform_key(k):
    # Unused transformation
    return ''.join(chr(ord(c) + 1) for c in k)

def calculate_strain_response(loads, config):
    base_modulus = config['modulus']
    non_critical_factor = config.get('safety_net', 1.1)
    temperature_offset = config.get('temp_comp', 0)
    
    # Real calculation begins
    adjusted_load = sum(loads) * 0.85
    
    # Conditional expression (required language feature)
    strain_rate = 0.02 if adjusted_load < 5000 else (0.05 if adjusted_load < 12000 else 0.09)
    
    # Simulated hysteresis loop with damping
    peak_strain = 0
    current_strain = 0
    for load_step in loads:
        delta = load_step * strain_rate / base_modulus
        current_strain += delta
        if abs(current_strain) > abs(peak_strain):
            peak_strain = current_strain
        elif abs(current_strain) > 0.5 * abs(peak_strain):
            current_strain *= 0.92  # Energy loss simulation
    
    # Core formula: uses peak hysteresis and modulus
    energy_density = (0.5 * base_modulus * (peak_strain ** 2)) * 1000  # in J/m³
    
    # Red herring variables
    dummy_shift = shift_encoding(int(energy_density))
    calibration_check = validate_calibration([12, 17, 24])
    
    # Final yield computed from energy density and configuration
    aging_factor = config.get('aging', 0.93)
    final_yield = int(energy_density * aging_factor)
    
    # More irrelevant operations
    decoy_result = recursive_dampener(dummy_shift)
    readings = [12.1, 13.6, 9.8, 14.2]
    processed = preprocess_stress_data(readings)
    
    return final_yield

# Main execution block
material_config = {
    'modulus': 210000,           # Young's modulus in MPa
    'temp_comp': 25,
    'safety_net': 1.15,
    'aging': 0.93
}

load_profile = [800, -300, 1200, -600, 950, -400, 1400, -700]

# Trigger the actual computation
final_yield = calculate_strain_response(load_profile, material_config)

# Print result as required
print(f"Result: {final_yield}")