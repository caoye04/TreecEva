import math

# Material science simulation: stress-strain analysis with red herrings

def preprocess_signals(raw_data):
    # Irrelevant signal processing (distraction)
    filtered = [x * 0.9 for x in raw_data if x > 0]
    normalized = [y / max(filtered) for y in filtered]
    return [round(z, 3) for z in normalized]


def compute_entropy(sequence):
    # Misleading complexity: information theory decoy
    prob_dist = {x: sequence.count(x)/len(sequence) for x in set(sequence)}
    entropy = -sum(p * math.log2(p) for p in prob_dist.values())
    return round(entropy, 4)


def evaluate_stability(risk_matrix):
    # Dead code path - never called
    total_risk = sum(sum(row) for row in risk_matrix)
    return total_risk < 50

# Unused but plausible-looking helper
lambda_transform = lambda a, b: (a ** 0.5 + b ** 0.5) ** 2

# Real computation starts here
material_config = {
    'elastic_modulus': 210e3,
    'yield_threshold': 450,
    'hardening_factor': 0.18,
    'grain_orientation': [0.7, 0.3, 0.5],
    'thermal_coeff': -0.0025  # Distractor: not used in main calc
}

stress_sequence = [120, 240, 380, 460, 520, 310, 180]
temp_readings = [25, 26, 28, 35, 45, 52, 48]  # Red herring data

# Simulated sensor preprocessing (distractor chain)
calibrated_stress = []
for i, reading in enumerate(stress_sequence):
    adjusted = reading * (1 + 0.05 * math.sin(i))  # Minor adjustment
    calibrated_stress.append(int(adjusted))

# Decoy list comprehension with slicing
analysis_buffer = [calibrated_stress[i:i+3] for i in range(0, len(calibrated_stress), 2)][::2]
buffer_summaries = [sum(segment) for segment in analysis_buffer]

# Core algorithm disguised among distractions
def calculate_strain_response(stress_levels, config):
    modulus = config['elastic_modulus']
    threshold = config['yield_threshold']
    factor = config['hardening_factor']
    
    # Real logic embedded in complex structure
    strain_components = []
    accumulated_plastic = 0
    
    for idx, stress in enumerate(stress_levels):
        if stress <= threshold:
            # Elastic region
            elastic_strain = stress / modulus
            strain_components.append(elastic_strain)
        else:
            # Plastic deformation with hardening
            base_plastic = (stress - threshold) * factor / modulus
            cycle_adjustment = math.cos(idx * math.pi / 4)  # Pattern-based mod
            accumulated_plastic += base_plastic * abs(cycle_adjustment)
            total_strain = stress / modulus + accumulated_plastic
            strain_components.append(total_strain)
    
    # Final transformation using multiple concepts
    valid_indices = [i for i, val in enumerate(strain_components) if val > 0.002]
    relevant_strains = [strain_components[i] for i in valid_indices]
    
    # Critical calculation using enumerate and zip
    growth_pairs = list(zip(relevant_strains, relevant_strains[1:]))
    enhancement = 0
    for i, (prev, curr) in enumerate(growth_pairs):
        diff = curr - prev
        enhancement += diff * (i + 1) * 0.1
    
    # Final result built from composite reasoning
    base_yield = sum(strain_components) * 1000
    final_output = int(base_yield + enhancement * 100)
    
    # Decoy operations below (no effect on output)
    dummy_zip = list(zip(valid_indices, [x*2 for x in valid_indices]))
    sliced_dummy = dummy_zip[1:-1:2]
    
    return final_output

# Secondary irrelevant transformation
frequency_domain = [math.tan(x/1000) for x in stress_sequence if x > 300]

# Key execution point
final_yield = calculate_strain_response(stress_sequence, material_config)

# Additional distraction: unused matrix operation
risk_grid = [[12, 8, 15], [23, 5, 11], [18, 14, 9]]
stability_score = sum(sum(row[i] for i in range(len(row))) for row in risk_grid)

# Print required result
print(f"Result: {final_yield}")