def simulate_agricultural_cycle():
    # Core variables
    base_rainfall = 850
    temperature_avg = 22.5
    soil_nutrients = 370
    pest_pressure = 65
    
    # Distractor: Weather anomaly calculations (irrelevant)
    wind_speed_avg = 14.2
    humidity_index = 68
    cloud_cover = 73
    solar_radiation = base_rainfall * 1.3 - wind_speed_avg
    frost_days = 0
    for day in range(1, 366):
        if temperature_avg < 0 and humidity_index > 60:
            frost_days += 1
    adjusted_humidity = humidity_index if frost_days < 10 else 45
    
    # Distractor: Pest resistance chain (unused path)
    pesticide_effectiveness = 0.88
    resistant_pests = pest_pressure * (1 - pesticide_effectiveness)
    crop_rotation_bonus = 1.15
    if resistant_pests > 50:
        crop_rotation_bonus *= 0.9
    legacy_yield_estimate = soil_nutrients * 2.1 * crop_rotation_bonus

    # Real computation begins
    rainfall_effectiveness = base_rainfall / 1000.0
    nutrient_efficiency = soil_nutrients / 500.0
    
    # Primary yield components
    yield_component_a = int(rainfall_effectiveness * 400)
    yield_component_b = int(nutrient_efficiency * 350)
    yield_component_c = int((temperature_avg - 15) * 20) if temperature_avg > 15 else 50

    harvest = [yield_component_a, yield_component_b, yield_component_c]
    
    # Irrelevant sorting operation on copy
    sorted_harvest = sorted(harvest)
    median_yield = sorted_harvest[1]
    peak_prediction = max(harvest) * 1.1

    # Slice-based adjustment (relevant only in index access)
    recent_trend = harvest[-2:]  # Last two components
    trend_average = sum(recent_trend) // 2

    # Efficiency factor influenced by non-pest factors
    efficiency_factor = 90
    if trend_average > 120:
        efficiency_factor += 15
    elif median_yield < 80:
        efficiency_factor -= 10
    
    # Decoy transformation (never used)
    normalized_harvest = [round(x / 10.0) * 10 for x in harvest]
    buffer_stock = sum(normalized_harvest) % 100

    # Key statement
    final_yield = harvest[2] * efficiency_factor // 2

    # Unused branching based on red herring
    if buffer_stock > 50 and solar_radiation > 1000:
        final_yield += 5
    elif adjusted_humidity < 50:
        final_yield -= 3

    # Output the target result
    print(f"Result: {final_yield}")

simulate_agricultural_cycle()