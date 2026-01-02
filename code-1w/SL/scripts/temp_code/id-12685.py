import math

# Simulated agricultural optimization system with decoy analytics

def analyze_risk_factors(data):
    # Irrelevant risk analysis (dead function)
    total_risk = 0
    for item in data:
        if item > 5:
            total_risk += 1.5
    return total_risk * 0.7


def compute_growth_potential(temp, water):
    # Relevant but obscured growth model
    base = (temp - 15) * 0.8
    if water < 30:
        return base * 0.4
    elif water > 80:
        return base * 0.6
    else:
        return base * (water / 70)


def evaluate_stress_conditions(soil_ph, rainfall_pattern):
    # Misleading stress evaluation (distractor)
    stress_score = 0
    for r in rainfall_pattern:
        if r < 10:
            stress_score += 0.3
    if 5.5 < soil_ph < 6.5:
        stress_score *= 0.5
    return stress_score + 1.2


def calculate_root_depth(soil_type):
    # Partially relevant mapping
    depth_map = {'clay': 15, 'loam': 45, 'sand': 60}
    return depth_map.get(soil_type, 20)


def optimize_harvest(climate, soils):
    # Core logic with interference
    cumulative_yield = 0
    adjustment_factor = 0.91
    dummy_tracker = []
    
    for i in range(len(climate)):
        temp = climate[i]['avg_temp']
        precipitation = climate[i]['rainfall']
        ph_level = soils[i]['ph']
        soil_type = soils[i]['type']
        
        # Real computation buried in noise
        photosynthetic_efficiency = compute_growth_potential(temp, precipitation)
        root_zone = calculate_root_depth(soil_type)
        
        # Decoy calculation
        stress_impact = evaluate_stress_conditions(ph_level, [precipitation]*3)
        risk_metric = analyze_risk_factors([temp, precipitation, ph_level])
        
        # Actual yield contribution
        micro_climate_boost = 1.0
        if temp > 25 and precipitation > 50:
            micro_climate_boost = 1.15
        
        # Primary yield formula
        unit_yield = photosynthetic_efficiency * (root_zone / 10) * micro_climate_boost
        
        # Red herring: tracking unused values
        dummy_tracker.append(risk_metric / (stress_impact + 0.1))
        
        cumulative_yield += unit_yield
    
    # Final transformation using list comprehension (required feature)
    adjusted_readings = [round(x * adjustment_factor, 2) for x in [cumulative_yield]]
    final_yield = int(sum(adjusted_readings))
    
    # Critical assignment point
    final_yield = final_yield + 17  # Final offset
    
    return final_yield

# Input data setup
climate_data = [
    {'avg_temp': 22, 'rainfall': 60},
    {'avg_temp': 26, 'rainfall': 75},
    {'avg_temp': 28, 'rainfall': 45},
    {'avg_temp': 24, 'rainfall': 85}
]

soil_profiles = [
    {'ph': 6.2, 'type': 'loam'},
    {'ph': 5.8, 'type': 'loam'},
    {'ph': 6.0, 'type': 'clay'},
    {'ph': 6.3, 'type': 'sand'}
]

# Execution entry point
final_yield = optimize_harvest(climate_data, soil_profiles)

# Output result
print(f"Target result: {final_yield}")