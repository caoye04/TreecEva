def analyze_growth_potential(temperature, rainfall):
    # Irrelevant auxiliary function (dead code path)
    return (temperature + rainfall) * 0.5

# Misleading intermediate constants
critical_threshold = 75
baseline_productivity = 42

# Distractor data structures
soil_pH_levels = [6.2, 5.8, 7.1, 6.9, 5.5, 8.0, 6.3]
unused_nutrient_matrix = [[3, 7, 2], [1, 8, 4], [9, 0, 5]]

# Real input data
climate_data = {
    'temp_avg': [22, 25, 27, 24, 20],
    'rainfall_mm': [80, 120, 60, 100, 140]
}

soil_profiles = [
    {'type': 'clay', 'moisture': 0.35, 'nitrogen': 18},
    {'type': 'loam', 'moisture': 0.42, 'nitrogen': 23},
    {'type': 'sand', 'moisture': 0.25, 'nitrogen': 15},
    {'type': 'loam', 'moisture': 0.39, 'nitrogen': 20}
]

# Decoy transformation (never used)
transformed_rainfall = [r * 1.1 for r in climate_data['rainfall_mm'] if r > 90]

# Bitwise red herring calculation
mask = 0b101010
encoded_value = mask ^ len(soil_profiles) << 2

# Set operations with irrelevant outcome
unique_soil_types = {s['type'] for s in soil_profiles}
desired_types = {'loam', 'silt'}
available_for_rotation = unique_soil_types & desired_types

# Conditional expression with misleading branch
legacy_mode = True
scaling_factor = 1.8 if legacy_mode else 2.1

# Core logic disguised among distractions
def compute_stress_index(t_list, r_list):
    stress = 0
    for t, r in zip(t_list, r_list):
        if t > 26 or r < 70:
            stress += 1
    return stress

# Unused recursive distraction
def forecast_degradation(depth):
    if depth <= 1:
        return 1
    return forecast_degradation(depth - 1) + forecast_degradation(depth - 2)

# Real processing function
def evaluate_agronomic_score(temp_seq, rain_seq, soils):
    base_score = 0
    for i in range(len(temp_seq)):
        # Relevant arithmetic and comparison
        heat_factor = 1 if temp_seq[i] >= 24 else 0.8
        water_factor = 1.1 if 90 <= rain_seq[i] <= 130 else 0.7
        base_score += heat_factor * water_factor
    
    # Slicing operation on relevant subset
    recent_conditions = rain_seq[-3:]
    bonus = 2 if sum(recent_conditions) > 300 else 0
    
    return base_score + bonus

# Secondary transformation with conditional expression
def adjust_for_soil_quality(profiles):
    total_N = sum(p['nitrogen'] for p in profiles)
    avg_moisture = sum(p['moisture'] for p in profiles) / len(profiles)
    # Use of slicing and conditional expression
    rich_soils = [p for p in profiles if p['nitrogen'] > 18][:2]
    premium_count = len(rich_soils) if avg_moisture > 0.35 else 0
    return total_N + premium_count * 5

# Main optimization with multiple concepts
def optimize_harvest(climate, soils):
    temps = climate['temp_avg']
    rains = climate['rainfall_mm']
    
    # Step 1: Environmental score
    env_score = evaluate_agronomic_score(temps, rains, soils)
    
    # Step 2: Soil adjustment
    soil_bonus = adjust_for_soil_quality(soils)
    
    # Step 3: Stress penalty
    stress = compute_stress_index(temps, rains)
    penalty = stress * 1.5
    
    # Step 4: Combine with bitwise distraction (irrelevant bit op)
    dummy_flag = 0b1100 & len(temps)
    dummy_shift = dummy_flag << 1
    
    # Step 5: Final composition
    preliminary = env_score + (soil_bonus / 10.0) - penalty
    
    # Step 6: Conditional scaling (legacy_mode is True)
    adjusted = preliminary * scaling_factor
    
    # Step 7: Offset with constant (distractor-based but fixed)
    final_yield = int(adjusted - baseline_productivity // 3)
    
    # Step 8: Return key result
    return final_yield

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Target result: {final_yield}")