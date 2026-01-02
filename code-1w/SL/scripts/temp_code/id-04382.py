def analyze_growth_factors(temperature, rainfall):
    # Irrelevant helper: simulates microclimate effect (not used in final result)
    if temperature > 25:
        return min(rainfall * 0.3, 120)
    else:
        return max(rainfall * 0.1, 60)


def calculate_stress_index(age, pests_present):
    # Distractor function: models plant stress but unused in core logic
    base_stress = age * 0.05
    if pests_present:
        base_stress += 0.25
    return round(base_stress, 3)

# Main agricultural yield model
temperature_data = [22, 28, 19, 31, 25]
rainfall_data = [80, 105, 95, 50, 73]
pest_infestation = True
plant_age_days = 160

# Simulated climate zones and soil quality (core data)
climate_zones = set(['temperate', 'arid', 'tropical', 'mediterranean'])
soil_quality = {
    'temperate': {'ph': 6.5, 'nutrients': 85, 'moisture_retention': 0.7},
    'arid': {'ph': 7.8, 'nutrients': 40, 'moisture_retention': 0.2},
    'tropical': {'ph': 5.2, 'nutrients': 60, 'moisture_retention': 0.5},
    'mediterranean': {'ph': 7.0, 'nutrients': 70, 'moisture_retention': 0.4}
}

# Dead code path - never executed, adds interference
if False:
    legacy_system_override = True
    buffer_zone = [0] * 10

# Auxiliary variables with misleading relevance
theoretical_capacity = 0.0
for temp in temperature_data:
    if temp > 20:
        theoretical_capacity += 5.5

# Core calculation function
def calculate_harvest_potential(zones, soil):
    base_yield = 0
    efficiency_modifiers = []
    
    for zone in zones:
        nutrients = soil[zone]['nutrients']
        moisture = soil[zone]['moisture_retention']
        
        # Primary yield contribution
        zone_yield = nutrients * moisture
        base_yield += zone_yield
        
        # Efficiency factor collection (some never used)
        ph_level = soil[zone]['ph']
        if ph_level > 7.0:
            efficiency_modifiers.append(0.85)
        elif ph_level < 6.0:
            efficiency_modifiers.append(0.78)
        else:
            efficiency_modifiers.append(0.92)
    
    # Aggregate modifier (only length matters, content distracts)
    avg_modifier = len(efficiency_modifiers) * 0.1
    
    # Final adjustment using fixed logic
    final_potential = base_yield * (1 + avg_modifier)
    
    # Secondary adjustment based on temperature threshold count
    high_temp_days = sum(1 for t in temperature_data if t > 25)
    final_potential += high_temp_days * 3.5
    
    return int(final_potential)

# Extraneous state tracking
monitoring_logs = []
for i, (t, r) in enumerate(zip(temperature_data, rainfall_data)):
    microclimate_effect = analyze_growth_factors(t, r)
    monitoring_logs.append(f'Day{i*10}: {microclimate_effect}mm effective rain')

# Key execution point
final_yield = calculate_harvest_potential(climate_zones, soil_quality)

# Print result as required
print(f"Target result: {final_yield}")