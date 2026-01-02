def analyze_growth_patterns(data, threshold=0.75):
    high_yield_regions = []
    temp_accumulator = 0
    
    for zone in data:
        if zone['avg_rainfall'] > 800 and zone['sunlight_hours'] > 6:
            growth_score = (zone['avg_rainfall'] * 0.003) + (zone['sunlight_hours'] * 0.2)
            adjusted_score = growth_score * (1 - zone.get('pest_pressure', 0.1))
            if adjusted_score > threshold:
                high_yield_regions.append(adjusted_score)
                temp_accumulator += adjusted_score  # distractor: used only for logging
    
    return high_yield_regions


def calculate_soil_stability(indices):
    stability = 0
    for i in indices:
        stability += (i ** 2) * 0.05  # irrelevant computation
    return stability  # never actually used


def calculate_harvest_potential(zones):
    climate_filtered = [z for z in zones if z['temperature_range'][0] >= 18]
    
    # Distractor: soil health preprocessing (semi-relevant but not used in final calc)
    soil_health_scores = []
    for z in zones:
        base_score = z['soil_ph'] * 10
        if 6.0 <= z['soil_ph'] <= 7.5:
            base_score += 15
        soil_health_scores.append(base_score)
    
    # Real logic begins
    valid_zones = []
    for z in climate_filtered:
        growing_period = z['temperature_range'][1] - z['temperature_range'][0]
        if growing_period >= 4:
            potential = (z['nutrient_level'] * 2.5) + (growing_period * 3.1)
            if z['elevation'] < 800:
                potential *= 1.2
            valid_zones.append(potential)
    
    # Use slicing to consider only top-performing half
    sorted_zones = sorted(valid_zones, reverse=True)
    top_half = sorted_zones[:len(sorted_zones)//2] if len(sorted_zones) > 1 else sorted_zones
    
    # Final calculation
    final_yield = sum(top_half) / len(top_half) if top_half else 0
    
    # Distractor: unused aggregation
    avg_soil = sum(soil_health_scores) / len(soil_health_scores) if soil_health_scores else 0
    max_rainfall = max([z['avg_rainfall'] for z in zones])
    
    return final_yield

# Input data
climate_zones = [
    {
        'name': 'Zone_A',
        'avg_rainfall': 1200,
        'sunlight_hours': 7.2,
        'temperature_range': (20, 28),
        'elevation': 650,
        'soil_ph': 6.8,
        'nutrient_level': 42
    },
    {
        'name': 'Zone_B',
        'avg_rainfall': 950,
        'sunlight_hours': 5.8,
        'temperature_range': (16, 22),
        'elevation': 720,
        'soil_ph': 5.9,
        'nutrient_level': 38
    },
    {
        'name': 'Zone_C',
        'avg_rainfall': 1400,
        'sunlight_hours': 6.5,
        'temperature_range': (19, 26),
        'elevation': 850,
        'soil_ph': 7.1,
        'nutrient_level': 45
    },
    {
        'name': 'Zone_D',
        'avg_rainfall': 1100,
        'sunlight_hours': 7.0,
        'temperature_range': (21, 30),
        'elevation': 580,
        'soil_ph': 6.5,
        'nutrient_level': 40
    }
]

# Trigger analysis (distractor call)
analyze_growth_patterns(climate_zones)

# Unused helper result
calculate_soil_stability([2, 3, 4])

# Critical execution point
final_yield = calculate_harvest_potential(climate_zones)
print(f"Target result: {final_yield}")