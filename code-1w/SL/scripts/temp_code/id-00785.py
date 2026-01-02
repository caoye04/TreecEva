def analyze_growth_potential(species_list, climate_zone):
    # Irrelevant analysis of species adaptability (distractor)
    adaptability_score = 0
    for species in species_list:
        if 'tropical' in species['habitat'] and climate_zone == 'equatorial':
            adaptability_score += len(species['name']) % 7
    return adaptability_score * 0.3

# Simulate agricultural yield prediction with multiple factors
def calculate_harvest_efficiency(area, soil_quality, rainfall):
    base_yield = area * 2.5
    quality_factor = 1.0
    
    # Determine quality multiplier using conditional expressions
    quality_factor = 0.7 if soil_quality < 4 else (1.2 if soil_quality < 7 else 1.8)
    
    # Rainfall adjustment with nested logic
    if rainfall < 300:
        deficit = 300 - rainfall
        reduction = min(deficit / 100, 0.4)
        base_yield *= (1 - reduction)
    elif rainfall > 800:
        excess = rainfall - 800
        waterlogging_loss = excess / 1000
        base_yield *= (1 - waterlogging_loss)
    else:
        base_yield *= 1.05  # Optimal range bonus

    # Dummy computation: evaporation rate (semi-relevant but not used directly)
    evaporation = rainfall * 0.6 if climate_temperature > 25 else rainfall * 0.3
    net_water = rainfall - evaporation

    # Final efficiency calculation
    efficiency_modifier = (soil_quality / 10) * (min(rainfall, 800) / 400)
    final_yield = base_yield * efficiency_modifier

    # Additional irrelevant tracking variables
    compliance_status = "PASS" if final_yield > 500 else "REVIEW"
    audit_log = f"Yield assessment completed for zone-{climate_temperature}: {compliance_status}"
    
    return final_yield

# Main simulation setup
climate_temperature = 28  # Ambient condition
plot_area = 120
soil_health_index = 6.8
precipitation_level = 650

crop_varieties = [
    {'name': 'maize', 'habitat': 'temperate', 'yield_potential': 7},
    {'name': 'sorghum', 'habitat': 'arid', 'yield_potential': 5},
    {'name': 'rice', 'habitat': 'tropical', 'yield_potential': 9}
]

# Run irrelevant ecological analysis (distractor branch)
adaptability_index = analyze_growth_potential(crop_varieties, 'equatorial')

# Key execution point
final_yield = calculate_harvest_efficiency(plot_area, soil_health_index, precipitation_level)

# Print result as required
print(f"Result: {final_yield}")