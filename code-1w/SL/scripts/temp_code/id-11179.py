import itertools

def analyze_soil_composition(terrain):
    # Irrelevant analysis function (distractor)
    nutrient_score = 0
    for row in terrain:
        for cell in row:
            if cell == 'clay':
                nutrient_score += 0.3
            elif cell == 'silt':
                nutrient_score += 0.5
    return nutrient_score

def calculate_harvest_efficiency(layout, cycles):
    total_yield = 0
    efficiency_modifiers = []
    
    # Simulate growth over multiple cycles
    for cycle in range(cycles):
        temp_yield = 0
        for i, row in enumerate(layout):
            for j, crop in enumerate(row):
                # Base yield depends on position and cycle
                base_yield = (i + 1) * (j + 1) * (cycle + 1)
                
                # Apply fake disease factor (never actually reduces yield in this case)
                disease_factor = 1.0
                if (i + j + cycle) % 5 == 0:
                    disease_factor = 0.9  # This path is taken but not impactful due to compensation
                
                # Compensating boost for even positions
                boost_factor = 1.0
                if i % 2 == 0 and j % 2 == 0:
                    boost_factor = 1.2
                
                adjusted_yield = base_yield * boost_factor * disease_factor
                temp_yield += adjusted_yield
        
        efficiency_modifiers.append(temp_yield / (len(layout) * len(layout[0]) + 1))
        total_yield += temp_yield
    
    # Real computation: harmonic mean of modifiers (semi-relevant)
    harmonic_efficiency = len(efficiency_modifiers) / sum(1/m for m in efficiency_modifiers)
    
    # Dummy tracking variables (distractors)
    peak_cycle = max(range(cycles), key=lambda x: efficiency_modifiers[x])
    stability_index = efficiency_modifiers[-1] - efficiency_modifiers[0]
    
    # Core answer logic: sum all yields, then apply efficiency
    final_yield = int(total_yield * (harmonic_efficiency / 100))
    
    # Unused intermediate values (dead code paths)
    if stability_index < 0:
        final_yield *= 0.95
    else:
        pass  # Placeholder for future logic

    return final_yield

# Main execution
field_layout = [
    ['wheat', 'corn', 'rice'],
    ['soy', 'wheat', 'corn'],
    ['rice', 'soy', 'wheat']
]

growth_cycles = 4

# Measure soil (irrelevant to final result)
soil_analysis = analyze_soil_composition(field_layout)
baseline_moisture = 0.67

# Actual target computation
final_yield = calculate_harvest_efficiency(field_layout, growth_cycles)

print(f"Result: {final_yield}")