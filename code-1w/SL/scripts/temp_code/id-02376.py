def analyze_soil_composition(ph_levels):
    avg_ph = sum(ph_levels) / len(ph_levels)
    deviation = sum(abs(ph - avg_ph) for ph in ph_levels)
    stability_score = 10 - (deviation / len(ph_levels))
    return stability_score

ph_readings = [6.8, 7.2, 6.9, 7.4, 7.0, 6.7, 7.1]

soil_quality = analyze_soil_composition(ph_readings)
baseline_yield_per_acre = 120 if soil_quality > 8 else 90

# Simulate seasonal weather effects
seasonal_rainfall = [80, 105, 95, 110, 75]  # mm per month
avg_rainfall = sum(seasonal_rainfall) / len(seasonal_rainfall)
rainfall_effect = 1.0 + (min(max(avg_rainfall - 90, -15), 15) / 100)

temperature_records = [22, 25, 24, 26, 23, 21, 25]
temp_optimal_range = sum(1 for t in temperature_records if 22 <= t <= 25)
temp_adaptability = temp_optimal_range / len(temperature_records)
temp_bonus = 1.05 if temp_adaptability >= 0.7 else 1.0

# Irrelevant calculation: biodiversity index (not used in final yield)
biodiversity_index = len(set(temperature_records)) * len(set(seasonal_rainfall))
crop_rotation_cycle = 3
rotation_efficiency = {1: 0.9, 2: 1.0, 3: 1.05}

# Field and operational parameters
total_area = 45.5  # hectares
equipment_age = 5
maintenance_factor = 0.95 if equipment_age > 3 else 1.0
labor_efficiency = 0.98

# Efficiency chain with conditional expression
base_efficiency = baseline_yield_per_acre * rainfall_effect * temp_bonus
adjusted_efficiency = base_efficiency * maintenance_factor * labor_efficiency

# Distractor: unused crop variety mapping
varietal_map = {
    'early': {'yield_boost': 1.1, 'risk': 0.05},
    'standard': {'yield_boost': 1.0, 'risk': 0.02},
    'drought_resistant': {'yield_boost': 0.95, 'risk': 0.01}
}

# Simulated pest pressure (semi-relevant but capped)
pest_index = 12
pest_control_efficiency = 0.85
suppressed_pest_level = max(pest_index * (1 - pest_control_efficiency), 0)
pest_penalty = 1 - (suppressed_pest_level / 100)

# Final efficiency factor incorporating multiple factors
if adjusted_efficiency > 100:
    efficiency_factor = adjusted_efficiency * pest_penalty * rotation_efficiency[crop_rotation_cycle]
else:
    efficiency_factor = adjusted_efficiency * rotation_efficiency[1]

# Harvest model with string-based condition (using string method)
harvest_conditions = 'optimal_wind optimal_temp no_storm'.split()
wind_condition = 'optimal_wind'
weather_suitability = any(wind_condition.startswith(cond.split('_')[0]) for cond in harvest_conditions)
weather_modifier = 1.02 if weather_suitability else 0.98

# Secondary distractor: nutrient set analysis
required_nutrients = {'N', 'P', 'K', 'Mg', 'Ca'}
applied_fertilizers = {'NPK_blend', 'lime', 'magnesium_sulfate'}
provided_elements = set(''.join(applied_fertilizers).upper())
nutrient_coverage = required_nutrients & provided_elements
coverage_ratio = len(nutrient_coverage) / len(required_nutrients)

# Final yield calculation depends on area and efficiency
final_yield = 0
def harvest_results(area, efficiency):
    gross_output = area * efficiency
    processing_loss = 0.03
    net_output = gross_output * (1 - processing_loss)
    return round(net_output, 2)

# Critical execution point
final_yield = harvest_results(total_area, efficiency_factor)

# Output result
print(f"Result: {final_yield}")