def analyze_crop_potential(soil_data, climate_data):
    base_yield = 0
    adjustment_factor = 1.0
    
    # Irrelevant processing of soil data (distractor)
    for entry in soil_data:
        ph_level = entry.get('ph', 7.0)
        nutrient_score = sum([entry.get(nut, 0) for nut in ['n', 'p', 'k']])
        if ph_level < 6.0 or ph_level > 7.5:
            adjustment_factor *= 0.95

    # Semi-relevant climate preprocessing (some used later)
    temperature_stress = 0
    total_rainfall = 0
    ideal_days = 0
    for day in climate_data:
        temp = day['temp']
        rain = day['precip']
        total_rainfall += rain
        if temp < 10 or temp > 35:
            temperature_stress += 1
        if 20 <= temp <= 30 and 2 <= rain <= 5:
            ideal_days += 1

    # Dummy metric with no impact (dead code path)
    theoretical_max = len(climate_data) * 45.0
    unused_buffer = theoretical_max * 0.1

    return total_rainfall, ideal_days, adjustment_factor


def calculate_harvest_efficiency(area_metrics, growth_conditions):
    efficiency = 1.0
    size_factor = len(area_metrics) * 0.1
    
    # Real computation begins: aggregate area features
    total_area = sum([plot['size'] for plot in area_metrics])
    avg_elevation = sum([plot['elev'] for plot in area_metrics]) / len(area_metrics)
    
    # Conditional efficiency modifiers
    if total_area > 50:
        efficiency *= 1.1
    if avg_elevation > 200:
        efficiency *= 0.9
    
    # Integration with growth conditions (key dependency)
    stress_levels = [cond['stress'] for cond in growth_conditions]
    avg_stress = sum(stress_levels) / len(stress_levels)
    
    # Efficiency penalty based on stress
    efficiency *= (1 - avg_stress * 0.05)
    
    # Red herring: unused transformation
    normalized_stress = [max(0, 1 - s/10) for s in stress_levels]
    buffer_value = sum(normalized_stress) / len(normalized_stress)

    # Final nonlinear scaling
    final_yield = int((total_area * efficiency) + (avg_elevation / 10))
    
    return final_yield

# Main execution block
soil_profiles = [
    {'ph': 6.8, 'n': 3, 'p': 2, 'k': 4},
    {'ph': 7.2, 'n': 2, 'p': 3, 'k': 3},
    {'ph': 6.5, 'n': 4, 'p': 4, 'k': 5}
]

weather_log = [
    {'temp': 25, 'precip': 3},
    {'temp': 18, 'precip': 6},
    {'temp': 32, 'precip': 1},
    {'temp': 27, 'precip': 4},
    {'temp': 15, 'precip': 2}
]

field_layout = [
    {'size': 20, 'elev': 150},
    {'size': 35, 'elev': 210},
    {'size': 18, 'elev': 190}
]

# Trigger irrelevant analysis (distractor call)
growth_potential = analyze_crop_potential(soil_profiles, weather_log)
baseline_rain, optimal_days, adj_factor = growth_potential

# Simulate stress from suboptimal days
simulated_stress = []
for i, day in enumerate(weather_log):
    temp = day['temp']
    stress_score = 0
    if temp < 15 or temp > 30:
        stress_score += 0.4
    if day['precip'] < 1 or day['precip'] > 5:
        stress_score += 0.3
    simulated_stress.append({'day': i, 'stress': min(1.0, stress_score)})

# Extract only stress values for actual use
stress_index = [entry['stress'] for entry in simulated_stress]

# Key data structures for main calculation
area_summary = field_layout  # reused meaningful data
conditions_snapshot = [{'stress': s} for s in stress_index]

# Critical statement: compute final yield
final_yield = calculate_harvest_efficiency(area_summary, conditions_snapshot)

# Output result as required
print(f"Result: {final_yield}")