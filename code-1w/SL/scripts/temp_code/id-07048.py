def analyze_growth_potential(temp, rainfall):
    # Irrelevant computation: calculate comfort index (not used in final result)
    comfort_index = (temp * 0.7) + (rainfall * 0.3)
    growth_score = 0
    if temp > 25:
        growth_score += 10
    elif temp > 20:
        growth_score += 15
    else:
        growth_score += 8

    if rainfall > 100:
        growth_score += 12
    elif rainfall > 60:
        growth_score += 20  # Optimal range
    else:
        growth_score += 5

    # Distractor: unused variable
    theoretical_max = temp * rainfall / 2.5

    return growth_score


def assess_soil_quality(nutrients, ph_level):
    base_nutrient_score = sum([1 for n in nutrients if n > 0.5])
    ph_factor = 1 if 6.0 <= ph_level <= 7.0 else 0.6
    adjusted_score = base_nutrient_score * ph_factor

    # Dead code path (never executed due to logic above)
    if ph_level < 0:
        adjusted_score = 0  # Impossible condition, distractor

    return adjusted_score

# Simulate multi-season yield estimation (not directly used but looks important)
decoy_seasonal_cycle = []
for month in range(1, 13):
    season_weight = 1.0
    if month in [6, 7, 8]:
        season_weight = 1.2
    elif month in [12, 1, 2]:
        season_weight = 0.5
    decoy_seasonal_cycle.append(season_weight)

# Real data inputs
climate_data = {'avg_temp': 22, 'monthly_rainfall': 75}
rainfall_total = climate_data['monthly_rainfall']
temperature = climate_data['avg_temp']

# Soil conditions
soil_conditions = {
    'nutrients': [0.8, 0.9, 0.4, 0.7],  # N, P, K, Mg
    'ph': 6.8,
    'texture_code': 3  # 1=sand, 2=loam, 3=clay-loam (unused)
}

# Intermediate assessments
growth_metric = analyze_growth_potential(temperature, rainfall_total)
soil_health = assess_soil_quality(soil_conditions['nutrients'], soil_conditions['ph'])

# Complex conditional expression combining multiple factors
efficiency_factor = 1.1 if growth_metric >= 30 and soil_health >= 3 else 0.85

# Bitwise operation as part of yield calculation (adds reasoning complexity)
base_unit = int(growth_metric) & 15  # Use lower 4 bits of growth score
modifier = int(soil_health) | 3  # Ensure at least two bits are set

# Dictionary operations for scenario weighting
scenario_weights = {'optimal': 1.0, 'suboptimal': 0.7, 'critical': 0.3}
status_key = 'optimal' if efficiency_factor > 1 else 'suboptimal'
weight_applied = scenario_weights[status_key]

# Set operation: determine missing nutrients (distractor - not used in final yield)
required_elements = {'N', 'P', 'K', 'Ca', 'Mg'}
measured_names = {'N', 'P', 'K', 'Mg'}
missing = required_elements - measured_names  # {'Ca'} - irrelevant to math

# Core calculation chain
projected_output = (base_unit * modifier) * 10
adjustment = (efficiency_factor * weight_applied)

# Final optimization function
def optimize_harvest(climate, soil):
    local_temp = climate['avg_temp']
    local_rain = climate['monthly_rainfall']
    
    # Red herring: complex polynomial fit (unused)
    curve_fit_estimate = 0.02 * local_temp**2 - 0.5 * local_rain + 100
    
    # Actual signal path
    primary_yield = projected_output * adjustment
    
    # Conditional override based on logical combinations
    if local_temp < 18 or local_rain < 40:
        primary_yield *= 0.4
    elif local_temp > 30 or local_rain > 120:
        primary_yield *= 0.6
    else:
        primary_yield *= 1.0  # Stable condition
    
    # Final clamp using dictionary lookup
    bounds = {True: (50, 200), False: (30, 180)}[local_rain > 50]
    clamped = max(bounds[0], min(primary_yield, bounds[1]))
    
    return round(clamped, 2)

# Execute main logic
final_yield = optimize_harvest(climate_data, soil_conditions)
print(f"Target result: {final_yield}")