def analyze_growth_potential(soil_nutrients, water_levels):
    nutrient_score = sum([min(n, 10) for n in soil_nutrients]) / len(soil_nutrients)
    water_stress = abs(sum(water_levels) / len(water_levels) - 7.5)
    growth_potential = nutrient_score * (10 - water_stress)
    return max(growth_potential, 0)


def calculate_pest_impact(pest_data, resistance_factors):
    raw_impact = 0
    for pest in pest_data:
        if pest['severity'] > 5:
            raw_impact += pest['spread_rate'] * pest['damage_coefficient']
    adjusted_impact = raw_impact
    for factor in resistance_factors:
        adjusted_impact *= (1 - min(factor, 0.8))
    return min(adjusted_impact, 10)


def calculate_harvest_efficiency(plots, pest_index):
    efficiency_map = {}
    total_area = 0
    valid_plots = 0
    
    for i, plot in enumerate(plots):
        base_yield = plot['size'] * plot['fertility']
        micro_climate_factor = 1 + (plot['sunlight'] - 5) * 0.1
        temperature_modifier = max(0.5, min(1.2, (plot['temp'] - 20) * 0.05 + 1))
        
        # Irrelevant intermediate calculation (distractor)
        theoretical_max = base_yield * micro_climate_factor * 1.5
        decay_loss = theoretical_max * 0.02
        
        adjusted_yield = base_yield * temperature_modifier * micro_climate_factor
        
        if plot['irrigated']:
            adjusted_yield *= 1.15
        
        efficiency_map[i] = adjusted_yield
        total_area += plot['size']
        if adjusted_yield > 0:
            valid_plots += 1

    avg_efficiency = sum(efficiency_map.values()) / len(efficiency_map) if efficiency_map else 0
    
    # Use set operations to filter high-efficiency plots (relevant)
    high_yield_ids = {k for k, v in efficiency_map.items() if v > avg_efficiency}
    low_yield_ids = {k for k, v in efficiency_map.items() if v <= avg_efficiency}
    balanced_ratio = len(high_yield_ids) / len(low_yield_ids) if low_yield_ids else 0
    
    # Dictionary-based modifier lookup (relevant)
    modifier_table = {0: 0.8, 1: 0.9, 2: 1.0, 3: 1.1, 4: 1.2}
    plot_count_modifier = modifier_table.get(valid_plots, 1.0)
    
    # Final efficiency with pest pressure
    pest_penalty = calculate_pest_impact(pest_index, [0.1, 0.3, 0.05])
    final_efficiency = avg_efficiency * plot_count_modifier * (1 - pest_penalty * 0.05)
    
    # Dead code path (distractor)
    if False:
        dummy = 0
        for _ in range(100):
            dummy += 1
        final_efficiency += dummy * 0.001
    
    return round(final_efficiency, 4)

# Main execution
soil_nutrients = [6.2, 8.1, 7.3, 5.9, 9.0, 6.7]
water_levels = [6.1, 7.8, 8.0, 7.2, 6.5, 7.0]
growth_potential = analyze_growth_potential(soil_nutrients, water_levels)

land_plots = [
    {'size': 10, 'fertility': 7.2, 'sunlight': 6, 'temp': 22, 'irrigated': True},
    {'size': 8, 'fertility': 6.5, 'sunlight': 5, 'temp': 18, 'irrigated': False},
    {'size': 12, 'fertility': 8.0, 'sunlight': 7, 'temp': 25, 'irrigated': True},
    {'size': 5, 'fertility': 5.0, 'sunlight': 4, 'temp': 19, 'irrigated': False},
    {'size': 15, 'fertility': 9.1, 'sunlight': 8, 'temp': 24, 'irrigated': True}
]

pest_pressure = [
    {'severity': 6, 'spread_rate': 2.1, 'damage_coefficient': 0.4},
    {'severity': 4, 'spread_rate': 1.8, 'damage_coefficient': 0.3},
    {'severity': 7, 'spread_rate': 3.0, 'damage_coefficient': 0.5}
]

intermediate_metric = growth_potential * 0.75  # Not used in final result
normalization_factor = sum([p['size'] for p in land_plots])  # Semi-relevant but unused

final_yield = calculate_harvest_efficiency(land_plots, pest_pressure)
print(f"Target result: {final_yield}")