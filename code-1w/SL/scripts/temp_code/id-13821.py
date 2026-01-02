def analyze_growth_factors(temperature, humidity):
    # Irrelevant helper function dealing with microclimate
    if temperature < 20:
        return 'suboptimal'
    elif humidity > 80:
        return 'risky'
    return 'stable'

# Simulate agricultural yield prediction with distractors
def calculate_harvest_potential(climate_data, soil_profile):
    base_yield = 50
    modifier = 1.0
    stress_count = 0

    # Distractor: unused variable tracking phantom pests
    pest_incidents = []
    for day in range(1, 8):
        risk = (day * 2) % 13
        if risk > 10:
            pest_incidents.append(day)

    # Real logic begins: using set operations on climate zones
    tropical = {25, 26, 27, 28, 29, 30}
    arid = {30, 31, 32, 33, 34, 35}
    climate_set = set(climate_data)

    overlap = tropical & climate_set  # shared favorable temps
    extreme_heat = climate_set & arid

    if len(extreme_heat) > 2:
        modifier *= 0.85
        stress_count += 1

    if len(overlap) >= 3:
        modifier += 0.1

    # Soil analysis with dictionary lookups and slicing
    nutrient_levels = {
        'nitrogen': soil_profile[0],
        'phosphorus': soil_profile[1],
        'potassium': soil_profile[2]
    }

    # Distractor: dead code path never executed due to fixed condition
    backup_yield = 0
    if False:  # Simulates deprecated fallback model
        backup_yield = base_yield * 1.2
        if nutrient_levels['phosphorus'] > 40:
            backup_yield *= 1.1

    primary_nutrients = list(nutrient_levels.values())[:3]  # slicing first three

    rich_soil = sum(1 for v in primary_nutrients if v > 50)

    if rich_soil == 3:
        modifier *= 1.25
    elif rich_soil == 2:
        modifier *= 1.1

    # Climate-soil interaction effect
    if len(extreme_heat) > 1 and nutrient_levels['nitrogen'] < 45:
        stress_count += 1

    # Final adjustment based on stress but not directly used
    stress_penalty = 0.9 - (stress_count * 0.05)  # max penalty 0.8

    # Key assignment - this is where final_yield gets its value
    final_yield = base_yield * modifier

    # Additional misleading computation
    projected_loss = 0
    for i in range(3):
        projected_loss += (final_yield * 0.02) * (i + 1)

    # Output the correct result as required
    print(f"Result: {final_yield}")
    return final_yield

# Input data
climate_history = [26, 27, 28, 31, 32, 29]
soil_composition = [52, 55, 48]

# Execute main logic
final_yield = calculate_harvest_potential(climate_history, soil_composition)