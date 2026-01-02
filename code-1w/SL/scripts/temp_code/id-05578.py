def analyze_soil_composition(terrain_data):
    base_nutrients = [d['nitrogen'] * 0.3 + d['phosphorus'] * 0.5 for d in terrain_data]
    adjusted_ph = [max(6.0, min(7.5, d['ph'])) for d in terrain_data]
    stability_score = sum([1 for ph in adjusted_ph if 6.5 <= ph <= 7.0])
    return base_nutrients, adjusted_ph, stability_score


def simulate_rainfall_impact(rain_mm):
    absorption_rate = 0.0
    runoff = 0.0
    for rain in rain_mm:
        if rain < 20:
            absorption_rate += rain * 0.9
        elif rain < 100:
            absorption_rate += rain * 0.6
        else:
            runoff += rain - 60
    efficiency_penalty = 1.0 - (runoff / max(sum(rain_mm), 1))
    return absorption_rate, efficiency_penalty


def calculate_growth_potential(nutrients, moisture_factor, penalty):
    potential = 0.0
    for i, nut in enumerate(nutrients):
        temp_boost = 1.0 + (0.1 * (i % 3))
        base_growth = nut * moisture_factor * temp_boost
        potential += base_growth if base_growth > 2.5 else 2.5
    return round(potential, 4)


def calculate_harvest_efficiency(conditions, cycles):
    # Key distractor: irrelevant processing
    dummy_stats = {f'cycle_{i}': {'peak': 0, 'decline': 0} for i in range(cycles)}
    cumulative_loss = 0.0
    for c in range(cycles):
        if c % 4 == 0:
            cumulative_loss += 0.05
        dummy_stats[f'cycle_{c}']['peak'] = (c + 1) * 1.5 - cumulative_loss

    # Actual relevant logic
    nutrients, ph_levels, stability = analyze_soil_composition(conditions)
    rainfall_data = [c['rainfall'] for c in conditions]
    absorbed, penalty = simulate_rainfall_impact(rainfall_data)
    avg_nutrient = sum(nutrients) / len(nutrients) if nutrients else 0
    moisture_factor = absorbed / max(sum(rainfall_data), 1)

    growth_potential = calculate_growth_potential(nutrients, moisture_factor, penalty)
    
    # Misleading intermediate calculation
    theoretical_max = avg_nutrient * moisture_factor * 12.5
    efficiency_ratio = growth_potential / theoretical_max if theoretical_max > 0 else 0

    # Final yield based on real factors
    adjustment_factor = 0.8 if stability < 3 else 1.0
    final_yield = int(growth_potential * adjustment_factor * (1 - penalty))

    # Dead code branch (never executed due to fixed cycle count)
    if cycles > 100:
        final_yield = int(final_yield * 0.75)

    return final_yield

# Input data
plot_conditions = [
    {'nitrogen': 8,  'phosphorus': 12, 'ph': 6.8, 'rainfall': 25},
    {'nitrogen': 10, 'phosphorus': 14, 'ph': 7.1, 'rainfall': 18},
    {'nitrogen': 7,  'phosphorus': 10, 'ph': 6.3, 'rainfall': 95},
    {'nitrogen': 9,  'phosphorus': 13, 'ph': 7.3, 'rainfall': 5},
    {'nitrogen': 11, 'phosphorus': 15, 'ph': 6.9, 'rainfall': 40}
]
growth_cycles = 8

# Execution point
final_yield = calculate_harvest_efficiency(plot_conditions, growth_cycles)
print(f"Target result: {final_yield}")