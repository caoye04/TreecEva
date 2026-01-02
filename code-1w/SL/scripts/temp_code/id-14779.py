def analyze_growth_factors(temperature, rainfall):
    # Irrelevant helper function (dead code path)
    if temperature > 30:
        return "heat_stress"
    elif rainfall < 200:
        return "drought_risk"
    else:
        return "optimal"

# Simulated environmental monitoring system
temperature_readings = [22, 25, 27, 30]
rainfall_levels = [180, 210, 195, 220]
moisture_index = 0.0
for t, r in zip(temperature_readings, rainfall_levels):
    moisture_index += r * 0.01 - t * 0.1  # Distractor calculation

# Soil composition profiles (key data structure)
soil_profiles = {
    'plot_A': {'ph': 6.5, 'nitrogen': 12, 'clay': 35},
    'plot_B': {'ph': 5.8, 'nitrogen': 8, 'clay': 15},
    'plot_C': {'ph': 7.0, 'nitrogen': 15, 'clay': 25}
}

# Climate metrics over growing season
climate_data = [
    {'temp_avg': 22, 'precip': 180, 'sunlight': 6.2},
    {'temp_avg': 25, 'precip': 210, 'sunlight': 7.1},
    {'temp_avg': 27, 'precip': 195, 'sunlight': 6.8},
    {'temp_avg': 30, 'precip': 220, 'sunlight': 7.5}
]

# Ancillary sensor calibration (irrelevant computations)
sensor_offsets = [0.1, -0.2, 0.15, -0.05]
calibrated = []
for i, reading in enumerate(climate_data):
    calibrated.append(reading['temp_avg'] + sensor_offsets[i % 4])
baseline_deviation = sum(abs(co - 25) for co in calibrated) / len(calibrated)

# Core yield prediction logic
def calculate_harvest_potential(weather, soils):
    base_yield = 0
    efficiency_factor = 1.0
    
    # Process each growth period
    for period in weather:
        temp = period['temp_avg']
        precip = period['precip']
        sunlight = period['sunlight']
        
        # Temperature effectiveness curve
        if 20 <= temp <= 28:
            temp_eff = 1.0
        elif temp < 20:
            temp_eff = 0.6 + (temp - 10) * 0.04
        else:
            temp_eff = 1.1 - (temp - 28) * 0.05
        
        # Precipitation impact
        if precip < 175:
            precip_eff = 0.7 + (precip - 150) * 0.008
        elif precip > 225:
            precip_eff = 0.9 - (precip - 225) * 0.006
        else:
            precip_eff = 1.0
        
        # Sunlight contribution
        light_eff = max(0.5, min(1.0, sunlight / 7.0))
        
        period_potential = 25 * temp_eff * precip_eff * light_eff
        base_yield += period_potential
    
    # Soil quality adjustment (uses dictionary operations)
    total_adjustment = 0
    for plot_id, properties in soils.items():
        ph_level = properties['ph']
        nitrogen_level = properties['nitrogen']
        clay_content = properties['clay']
        
        # Ideal ranges: ph 6.0-7.0, nitrogen >= 10, clay 20-40
        ph_score = 0.8 if ph_level < 6.0 or ph_level > 7.0 else 1.0
        nitrogen_score = 0.9 if nitrogen_level < 10 else 1.0
        clay_score = 0.85 if clay_content < 20 or clay_content > 40 else 1.0
        
        plot_multiplier = ph_score * nitrogen_score * clay_score
        total_adjustment += plot_multiplier
    
    avg_soil_quality = total_adjustment / len(soils)
    
    # Final integration of climate and soil factors
    final_potential = base_yield * avg_soil_quality
    
    # Red herring: unused variable based on nonexistent sensor fusion
    phantom_index = baseline_deviation * 0.3 + moisture_index * 0.7  
    
    return round(final_potential, 2)

# Execute main computation
intermediate_metric = sum(cd['precip'] for cd in climate_data) / len(climate_data)
trigger_condition = intermediate_metric > 200

if trigger_condition:
    final_yield = calculate_harvest_potential(climate_data, soil_profiles)
else:
    final_yield = 0

print(f"Result: {final_yield}")