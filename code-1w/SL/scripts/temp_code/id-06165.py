def analyze_growth_potential(conditions):
    # Irrelevant analysis function (dead code path)
    score = 0
    for factor in conditions:
        if factor == 'light':
            score += conditions[factor] * 0.3
        elif factor == 'water':
            score += conditions[factor] * 0.5
    return score

# Simulate crop yield based on soil composition and cycles
def calculate_harvest_yield(soil_data, cycles):
    base_yield = 0
    nutrient_boost = 1.0
    
    # Distractor: unused variable tracking
    peak_nutrient_cycle = -1
    total_acidity = 0.0
    
    for i in range(len(cycles)):
        phase = cycles[i]
        
        # Real logic: accumulate yield from growth phases
        if phase == 'germination':
            base_yield += soil_data['nitrogen'] * 0.4
        elif phase == 'growth':
            base_yield += soil_data['phosphorus'] * 0.7
            nutrient_boost *= 1.1
        elif phase == 'flowering':
            base_yield += soil_data['potassium'] * 0.9
            nutrient_boost *= 1.2
        
        # Distractor computation: acidity accumulates but isn't used
        total_acidity += (i + 1) * 0.05
        
        # Misleading conditional (never reached due to data)
        if i > 100:
            base_yield *= 0.1  # dead code

    # Real final calculation
    final_output = base_yield * nutrient_boost
    
    # Extra dictionary operation (semi-relevant)
    adjustments = {'temp': 1.05, 'humidity': 0.95}
    for key in adjustments:
        final_output *= adjustments[key]
        
    return int(final_output)

# Main execution
soil_quality = {
    'nitrogen': 12,
    'phosphorus': 8,
    'potassium': 10,
    'ph': 6.5
}

growth_cycles = ['germination', 'growth', 'growth', 'flowering', 'growth']

# Unused variables (distractors)
current_phase_index = 0
max_daily_light = 14.5
water_schedule = [3, 5, 4, 6, 3]

# Key statement
final_yield = calculate_harvest_yield(soil_quality, growth_cycles)

print(f"Result: {final_yield}")