def analyze_soil(ph, moisture, nutrients):
    # Irrelevant soil analysis with misleading outputs
    texture = 'loam' if 6.0 < ph < 7.5 else 'clay'
    conductivity = moisture * 1.7
    organic_matter = nutrients * 0.3 + 2.1
    quality_score = (ph - 5.5) * 2 + moisture  # Distractor metric
    return texture == 'loam'


def assess_rainfall_pattern(rainfall_data):
    total = sum(rainfall_data)
    avg = total / len(rainfall_data)
    trend = 'stable' if abs(rainfall_data[-1] - avg) < 5 else 'volatile'
    threshold_breached = any(x > 50 for x in rainfall_data)  # Unused path
    return avg > 8 and trend == 'stable'


def compute_growth_potential(temp_min, temp_max, daylight_hours):
    peak_temp = (temp_min + temp_max) / 2
    efficiency = 0.8 if 20 <= peak_temp <= 30 else 0.4
    base_growth = daylight_hours * efficiency
    stress_factor = 1.0
    if temp_max > 35:
        stress_factor = 0.6
    elif temp_min < 10:
        stress_factor = 0.5
    adjusted_growth = base_growth * stress_factor
    return adjusted_growth > 12


def validate_pest_pressure(index_values):
    # Complex but irrelevant pest logic
    severity = max(index_values) - min(index_values)
    risk_level = 'high' if severity > 20 else 'low'
    normalized_threat = sum(x ** 0.5 for x in index_values) / len(index_values)
    return False  # Hardcoded decoy result


def calculate_harvest(climate_conditions):
    ph = climate_conditions['soil_ph']
    moisture = climate_conditions['soil_moisture']
    nutrients = climate_conditions['nutrient_level']
    temps = climate_conditions['temperature_range']
    daylight = climate_conditions['daylight_hours']
    rainfall = climate_conditions['weekly_rainfall']
    pests = climate_conditions['pest_index']

    # Step 1: Soil suitability
    soil_ok = analyze_soil(ph, moisture, nutrients)
    
    # Step 2: Rainfall stability
    rain_ok = assess_rainfall_pattern(rainfall)
    
    # Step 3: Thermal and light adequacy
    growth_ok = compute_growth_potential(temps[0], temps[1], daylight)
    
    # Step 4: Pest resistance check (always fails - red herring)
    pest_ok = validate_pest_pressure(pests)
    
    # Step 5: Secondary nutrient calculation (distractor)
    synthetic_nutrient_boost = nutrients * 0.2 + 5 if ph > 6.0 else 0
    
    # Step 6: Temperature deviation penalty (unused)
    deviation = abs(temps[0] - 15) + abs(temps[1] - 30)
    penalty_applied = deviation > 10
    
    # Step 7: Conditional override based on historical data (fake)
    use_historical_baseline = False
    fallback_yield = 4200 if use_historical_baseline else None
    
    # Step 8: Main yield formula - only this matters
    base_yield = 1000 + (moisture * 20) + (daylight * 150)
    if soil_ok and rain_ok and growth_ok:  # pest_ok intentionally excluded
        bonus = 1800 if daylight > 14 else 900
        base_yield += bonus
    
    # Step 9: Final adjustment using conditional expression
    final_yield = base_yield * (1.1 if climate_conditions['fertilizer_used'] else 0.9)
    
    # Step 10: Debug logging (no effect)
    status_log = f"Yield calculated: {final_yield}, Pest status: {pest_ok}"
    
    # Step 11: Redundant bounds clamping (not actually used)
    clamped = max(500, min(final_yield, 9500))
    
    # Step 12: Return final value
    return final_yield

# Main execution
conditions = {
    'soil_ph': 6.8,
    'soil_moisture': 32,
    'nutrient_level': 78,
    'temperature_range': [16, 31],
    'daylight_hours': 15,
    'weekly_rainfall': [12, 8, 14, 10, 9, 13, 11],
    'pest_index': [5, 7, 6, 20, 8],
    'fertilizer_used': True
}

final_yield = calculate_harvest(conditions)
print(f"Result: {final_yield}")