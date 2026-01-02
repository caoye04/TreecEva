import itertools

def analyze_phase_shift(frequencies, phase_angles):
    # Irrelevant complex frequency analysis (dead code path)
    shifted = []
    for f, p in zip(frequencies, phase_angles):
        shifted.append(f * (p + 45) % 360)
    return shifted

def validate_checksum(data_sequence):
    # Distractor: checksum validation that isn't actually used
    checksum = 0
    for i, val in enumerate(data_sequence):
        checksum ^= (val + i) & 0xFF
    return checksum == 0x7D

def compute_harmonic_decay(signal, iterations=8):
    # Misleading intermediate computation with no impact on final result
    decay_factor = 1.0
    for _ in range(iterations):
        decay_factor *= 0.92
        signal = [s * decay_factor for s in signal]
    return [round(s, 3) for s in signal]

def transform_coordinate_grid(x_coords, y_coords):
    # Unused geometric transformation (red herring)
    grid = set()
    for x, y in itertools.product(x_coords, y_coords):
        rotated_x = x * 0.707 - y * 0.707
        rotated_y = x * 0.707 + y * 0.707
        grid.add((round(rotated_x, 2), round(rotated_y, 2)))
    return grid

def calculate_strain_response(loads, mat_cfg):
    # Core logic embedded within distractions
    base_modulus = mat_cfg['elastic_modulus']
    temperature_factor = mat_cfg['temp_coeff'] * (mat_cfg['operating_temp'] - 25)
    adjusted_modulus = base_modulus * (1 + temperature_factor)

    peak_load = max(loads)
    min_load = min(loads)
    load_ratio = (peak_load - min_load) / peak_load

    # Real calculation path
    stress = peak_load * 1.45  
    strain = stress / adjusted_modulus

    # Distractor: unused damage accumulation model
    damage_accumulated = 0
    for load in loads:
        if load > 0.8 * peak_load:
            damage_accumulated += (load / peak_load) ** 3.2

    # More real logic
    cyclic_factor = 1.0
    for i in range(2, len(loads)):
        diff = abs(loads[i] - loads[i-1])
        if diff > 0.1 * peak_load:
            cyclic_factor *= 1.08

    # Final yield depends only on strain and cyclic_factor
    final_yield = strain * cyclic_factor * 1000000  # Scale to microstrain
    return round(final_yield, 4)

# Simulated sensor load profile (real input data)
load_profile = [120, 180, 95, 210, 165, 140, 195, 105]

# Material configuration (only some fields are actually used)
material_config = {
    'elastic_modulus': 210000,  # MPa - used
    'yield_strength': 355,         # MPa - irrelevant
    'ultimate_strength': 470,      # MPa - irrelevant
    'temp_coeff': -0.00025,       # per °C - used
    'density': 7.85,              # g/cm³ - irrelevant
    'operating_temp': 65,         # °C - used
    'corrosion_rate': 0.02,       # mm/year - irrelevant
    'surface_finish': 'polished'  # string - irrelevant
}

# Irrelevant pre-processing steps
frequency_data = [50, 60, 120, 400]
phase_info = [30, 90, 180, 270]
shifted_phases = analyze_phase_shift(frequency_data, phase_info)
clean_signal = compute_harmonic_decay([1.0, 0.8, 0.6, 0.4])
x_axis = [0, 1, 2]
y_axis = [0, 1]
grid_points = transform_coordinate_grid(x_axis, y_axis)
data_stream = [170, 88, 201, 144, 93]
valid_checksum = validate_checksum(data_stream)

# Key execution point - this is where the actual answer is computed
final_yield = calculate_strain_response(load_profile, material_config)

# Output result as required
print(f"Result: {final_yield}")