def calculate_agricultural_yield():
    # Simulate multi-stage crop yield calculation with environmental factors
    base_productivity = 87
    rainfall_mm = 420
    temperature_avg = 23.5
    pest_index = 12

    # Irrelevant meteorological computations (distractors)
    wind_speed_kph = 14
    humidity_pct = 68
    dew_point = humidity_pct * 0.7 + 5  # Not used in final calculation

    # Effective growth window based on temperature
    if 18 <= temperature_avg <= 25:
        growth_multiplier = 1.4
    else:
        growth_multiplier = 0.9

    # Rainfall effectiveness with diminishing returns
    if rainfall_mm < 300:
        water_stress = 0.7
    elif rainfall_mm > 500:
        water_stress = 0.85
    else:
        water_stress = 1.0

    # Simulated field zones with varying soil quality
    soil_quality = [0.92, 1.05, 0.88, 1.10, 0.95]
    zone_adjustments = []
    for i, sq in enumerate(soil_quality):
        adjusted = sq * (1 + 0.02 * (temperature_avg - 20))
        zone_adjustments.append(round(adjusted, 2))

    # Pest impact model
    max_damage = pest_index * 0.015
    pest_resistance_treatment = 0.4
    effective_pest_loss = max(0, max_damage - pest_resistance_treatment)
    pest_multiplier = 1 - effective_pest_loss

    # Distractor: unused disease model
    disease_risk = 0.05 * (100 - humidity_pct / 2) / 100
    treatment_efficacy = 0.6
    net_disease_risk = disease_risk * (1 - treatment_efficacy)  # Dead code path

    # Primary yield components
    gross_yield_per_hectare = base_productivity * growth_multiplier * water_stress
    
    # Apply zone adjustments using average
    avg_zone_factor = sum(zone_adjustments) / len(zone_adjustments)
    
    # Incorporate pest and zone factors
    net_output = gross_yield_per_hectare * avg_zone_factor * pest_multiplier
    
    # Efficiency factor from equipment (fixed for this season)
    equipment_units = 7
    maintenance_downtime = 0.12
    efficiency_factor = equipment_units * (1 - maintenance_downtime)

    # Final processing step
    final_yield = net_output // efficiency_factor

    # Diagnostic logging (irrelevant to result)
    total_monitoring_points = len(soil_quality) * 3
    calibration_offset = 0.033
    baseline_deviation = calibration_offset * 100

    return final_yield

result = calculate_agricultural_yield()
print(f"Result: {result}")