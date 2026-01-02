from collections import defaultdict, Counter
import math

# Simulate material deformation analysis under variable stress

def apply_noise_filter(signal):
    # Irrelevant preprocessing - red herring
    return [x * 0.99 for x in signal]

def compute_entropy(seq):
    # Distractor function - not used in main logic
    freqs = Counter(seq)
    total = len(seq)
    return -sum((count/total) * math.log2(count/total) for count in freqs.values())

def integrate_displacement(velocity_series):
    # Dead code path - looks relevant but unused
    displacement = 0
    for v in velocity_series:
        displacement += v * 0.1
    return displacement

def evaluate_stiffness_coefficient(config):
    # Misleading intermediate calculation
    base_modulus = config.get('elastic_modulus', 200) * 1.5
    adjustment = len(config.get('phases', [])) * 0.05
    return base_modulus * (1 + adjustment)

def calculate_strain_response(stress_levels, properties):
    # Core logic embedded within distractions
    
    # Initialize with default structural response
    strain_accumulator = defaultdict(float)
    thermal_offset = properties.get('thermal_expansion', 0.000012) * 25
    
    # Irrelevant phase tracker
    phase_counter = {phase: idx for idx, phase in enumerate(properties.get('phases', []))}
    
    # Real logic begins: nonlinear strain accumulation
    peak_stress = max(stress_levels)
    yield_threshold = properties['yield_strength']
    hardening_factor = properties['hardening_coeff']
    
    effective_strain = 0.0
    plastic_component = 0.0
    
    for i, stress in enumerate(stress_levels):
        elastic_strain = stress / properties['elastic_modulus']
        
        if stress > yield_threshold:
            excess_stress = stress - yield_threshold
            plastic_increment = excess_stress * hardening_factor / 1000
            plastic_component += plastic_increment
            
        # Accumulate total strain
        total_strain_at_step = elastic_strain + plastic_component
        strain_accumulator[f'step_{i}'] = round(total_strain_at_step, 6)
        
        # Update running effective strain
        effective_strain = total_strain_at_step
    
    # Final transformation using accumulated data
    nonlinearity_score = len([v for v in strain_accumulator.values() if v > 0.001])
    degradation_penalty = 1 - (nonlinearity_score * 0.02)
    
    # Key result computation
    final_output = effective_strain * (1 + thermal_offset) * degradation_penalty
    
    # Decoy normalization
    normalized_output = final_output / (1 + properties.get('damping_ratio', 0.07))
    
    return round(normalized_output * 1000000)  # Scale to integer for precision

# Experimental setup (simulated sensor inputs)
stress_profile = [50, 120, 180, 210, 230, 245, 260, 270, 265, 250]

material_config = {
    'elastic_modulus': 200,                # GPa
    'yield_strength': 220,                  # MPa
    'hardening_coeff': 0.8,                # Work hardening rate
    'thermal_expansion': 12e-6,            # Per °C
    'damping_ratio': 0.07,                 # Structural damping
    'phases': ['austenite', 'martensite', 'tempered'],
    'treatment': 'quench'
}

# Apply irrelevant preprocessing chain
filtered_signal = apply_noise_filter(stress_profile)
entropy_value = compute_entropy([int(x) for x in stress_profile])
displacement_mock = integrate_displacement([1.2, 2.3, 1.8, 3.1])
stiffness_metric = evaluate_stiffness_coefficient(material_config)

# Main computation
final_yield = calculate_strain_response(stress_profile, material_config)

print(f"Result: {final_yield}")