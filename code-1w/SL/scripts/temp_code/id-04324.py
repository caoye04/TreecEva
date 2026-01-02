def analyze_growth_potential(soil_data, temp_readings):
    # Irrelevant preprocessing: normalize temperature (not used in final result)
    normalized_temps = [round((t - 20) * 1.5, 2) for t in temp_readings]
    avg_normalized = sum(normalized_temps) / len(normalized_temps)

    # Distractor: complex soil scoring with unused components
    soil_scores = {}
    for idx, data in enumerate(soil_data):
        ph_factor = abs(data['ph'] - 6.5) * -0.3
        nutrient_score = (data['nitrogen'] + data['phosphorus'] + data['potassium']) / 30
        soil_scores[idx] = round(nutrient_score + ph_factor, 3)

    # Semi-relevant: identify high-nitrogen plots (only nitrogen matters later)
    high_nitrogen = [k for k, v in soil_data.items() if v['nitrogen'] > 80]
    return avg_normalized  # Red herring return


def calculate_harvest_efficiency(plot_config, climate_map):
    # Core logic hidden among distractions
    efficiency_ratings = []
    cumulative_weight = 0.0

    # Key structure: using enumerate and zip together
    for i, (plot_id, config) in enumerate(plot_config.items()):
        climate_key = list(climate_map.keys())[i % len(climate_map)]
        base_yield = config['base_yield']
        
        # Real computation path
        stress_factor = 1.0
        if config['irrigation'] == 'low':
            stress_factor *= 0.6
        if config['shade_coverage'] > 0.4:
            stress_factor *= 0.8

        # Critical use of dictionary and set operations
        nutrient_set_a = {k for k, v in config['nutrients'].items() if v > 50}
        nutrient_set_b = {'nitrogen', 'potassium', 'magnesium'}
        common_nutrients = nutrient_set_a & nutrient_set_b  # intersection
        bonus_multiplier = 1 + (0.1 * len(common_nutrients))

        # Actual yield calculation
        adjusted_yield = base_yield * stress_factor * bonus_multiplier
        efficiency_ratings.append(adjusted_yield)
        cumulative_weight += adjusted_yield * (i + 1)  # Weighted accumulation

    # Final formula uses both sum and weighted average
    total_efficiency = sum(efficiency_ratings) * 0.9
    final_rating = cumulative_weight / len(efficiency_ratings)
    return round(final_rating, 4)

# Main execution
soil_profiles = {
    0: {'ph': 6.8, 'nitrogen': 85, 'phosphorus': 70, 'potassium': 65},
    1: {'ph': 6.2, 'nitrogen': 90, 'phosphorus': 60, 'potassium': 80},
    2: {'ph': 7.0, 'nitrogen': 75, 'phosphorus': 75, 'potassium': 55}
}

temperature_log = [22.5, 23.1, 21.8, 24.0, 22.9]

# Plot configuration (key input)
plots = {
    'A1': {
        'base_yield': 120,
        'irrigation': 'low',
        'shade_coverage': 0.3,
        'nutrients': {'nitrogen': 88, 'potassium': 76, 'magnesium': 52, 'calcium': 45}
    },
    'A2': {
        'base_yield': 135,
        'irrigation': 'high',
        'shade_coverage': 0.5,
        'nutrients': {'nitrogen': 92, 'potassium': 81, 'magnesium': 48, 'sulfur': 60}
    },
    'A3': {
        'base_yield': 110,
        'irrigation': 'medium',
        'shade_coverage': 0.2,
        'nutrients': {'nitrogen': 78, 'potassium': 54, 'magnesium': 56, 'iron': 40}
    }
}

weather_factors = {
    'coastal': {'wind': 15, 'humidity': 0.75},
    'inland': {'wind': 10, 'humidity': 0.55},
    'valley': {'wind': 8, 'humidity': 0.62}
}

# Dead code path: analysis not used
baseline_potential = analyze_growth_potential(soil_profiles, temperature_log)

# Key assignment
final_yield = calculate_harvest_efficiency(plots, weather_factors)

# Print result
print(f"Target result: {final_yield}")