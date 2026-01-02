def analyze_growth_factor(temperature, rainfall):
    # Irrelevant intermediate calculation (distractor)
    stress_index = max(0, 35 - temperature) + max(0, rainfall - 200)
    
    # Semi-relevant scaling factor
    temp_effect = 1.0 if 20 <= temperature <= 30 else 0.7
    rain_effect = 0.8 if rainfall < 100 or rainfall > 250 else 1.0
    
    return temp_effect * rain_effect


def calculate_nutrient_score(soil_ph, nitrogen_level):
    # Dead code path based on unreachable condition (mild red herring)
    if nitrogen_level < 0:
        return 0  # Invalid state, should not occur
    ph_suitability = 0.9 if 6.0 <= soil_ph <= 7.0 else 0.6
    nutrient_balance = min(1.0, nitrogen_level / 150)
    return ph_suitability * nutrient_balance

# Simulate seasonal climate fluctuations (complex but partially irrelevant)
def generate_extended_climate_trend(base_temp, base_rain, weeks):
    trend = []
    for w in range(weeks):
        delta_temp = (w % 4) * 0.5
        delta_rain = (w % 5) * 10
        trend.append((base_temp + delta_temp, base_rain + delta_rain))
    return trend  # Used only for distraction

climate_data = {
    'avg_temperature': 25,
    'avg_rainfall': 180,
    'soil_ph': 6.5,
    'nitrogen_level': 120,
    'growth_weeks': 8
}

# Secondary helper with conditional expression (required language feature)
def assess_light_exposure(daylight_hours):
    return 1.0 if daylight_hours >= 12 else 0.8 if daylight_hours >= 8 else 0.5

# Main computation with multiple concepts and distractors
def calculate_harvest_potential(data):
    # Intermediate variables (some used, some not)
    weeks = data['growth_weeks']
    temp = data['avg_temperature']
    rain = data['avg_rainfall']
    ph = data['soil_ph']
    nitrogen = data['nitrogen_level']
    
    # Generate unused trend (distractor)
    unused_trend = generate_extended_climate_trend(temp, rain, weeks)
    
    # Key growth factors
    base_yield_per_week = 15
    growth_factor = analyze_growth_factor(temp, rain)
    nutrient_factor = calculate_nutrient_score(ph, nitrogen)
    light_factor = assess_light_exposure(14)  # Constant input
    
    # Accumulation over time (relevant logic)
    total_accumulated_yield = 0
    for week in range(weeks):
        weekly_boost = 1.0 + (week * 0.05)  # Increasing efficiency
        if week == 5:
            weekly_boost *= 0.9  # Minor stress event
        total_accumulated_yield += base_yield_per_week * growth_factor * nutrient_factor * light_factor * weekly_boost
        
        # Redundant check with no effect (misleading)
        if total_accumulated_yield > 1000:
            break  # Unreachable due to parameter values
    
    # Final adjustment using conditional expression (required feature)
    final_yield = total_accumulated_yield if total_accumulated_yield > 0 else 0.0
    
    # Unused diagnostic metric (distractor)
    avg_daily_yield = final_yield / (weeks * 7) if weeks > 0 else 0
    
    return final_yield

# Execute main logic
target_result = calculate_harvest_potential(climate_data)
print(f"Result: {target_result}")