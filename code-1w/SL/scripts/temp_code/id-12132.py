def analyze_soil_composition(data):
    # Irrelevant soil analysis with decoy computations
    ph_levels = [7.2, 6.8, 7.5, 6.9]
    nutrient_score = 0
    for entry in data:
        nutrient_score += sum(ord(c) for c in entry['type']) % 5
    return nutrient_score * 0.3


def generate_growth_model():
    # Misleading model generation (dead function)
    model = {}
    for i in range(5):
        model[f'phase_{i}'] = (i ** 3 + 2 * i) % 7
    return model

def compute_root_depth(root_system):
    # Distractor: unused root depth logic
    if root_system == 'taproot':
        return 1.8
    elif root_system == 'fibrous':
        return 0.9
    else:
        return 1.2

def calculate_harvest_efficiency(fields, cycles):
    total_yield = 0
    efficiency_modifiers = []
    
    # Real logic begins: parse field metadata
    for field in fields:
        base_yield = field['base']
        stress_factors = field.get('stress', [])
        
        # Relevant transformation using string method
        crop_name = field['crop'].strip().lower()
        if crop_name.startswith('wheat'):
            base_yield *= 1.1
        elif 'corn' in crop_name:
            base_yield *= 0.9
        
        # Apply growth cycle adjustments
        adjusted_yield = base_yield
        for day in range(cycles):
            if day % 10 == 0 and day > 0:
                adjusted_yield *= 0.98  # gradual decay
            
            # Decoy weather interference (has no effect)
            weather_noise = (day * 7 + 3) % 100
            if weather_noise < 5:
                adjusted_yield *= 0.5  # rare event that doesn't impact final result due to compensation
            
        # Real impact: pest infestation check
        if any('aphid' in p for p in stress_factors):
            adjusted_yield *= 0.7
        
        total_yield += adjusted_yield
        
        # Red herring: entropy-like calculation
        entropy = 0
        for c in crop_name:
            entropy -= ord(c) * 0.001
        
        efficiency_modifiers.append(entropy)
    
    # Final computation path
    avg_modifier = sum(efficiency_modifiers) / len(efficiency_modifiers) if efficiency_modifiers else 0
    total_yield += abs(avg_modifier) * 100  # minor correction
    
    # Key data structure transformation
    summary = {"yield": total_yield, "cycles": cycles}
    final_score = summary["yield"]
    
    # Dead code branch (never executed due to logic)
    if len(fields) > 100:
        fallback = sorted([f['base'] for f in fields])
        final_score = sum(fallback) // len(fallback)
    
    return int(final_score)

# Irrelevant global variables
soil_data = [{'type': 'clay'}, {'type': 'loam'}, {'type': 'silt'}]
growth_phases = generate_growth_model()

# Main simulation setup
field_data = [
    {'crop': 'Wheat Alpha  ', 'base': 150, 'stress': ['drought', 'aphid_brown']},
    {'crop': 'corn_beta', 'base': 180, 'stress': ['aphid_green']},
    {'crop': 'Wheat Gamma', 'base': 160, 'stress': []}
]

growth_cycles = 120

# Unused variable assignments (distraction)
nitrogen_levels = [0.8, 0.6, 0.9]
moisture_map = [[0.4, 0.7], [0.5, 0.3]]
baseline_prediction = analyze_soil_composition(soil_data)

# Critical execution point
final_yield = calculate_harvest_efficiency(field_data, growth_cycles)

print(f"Result: {final_yield}")