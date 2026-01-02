def analyze_growth_potential(temperature, rainfall):
    # Irrelevant agricultural metrics (distraction)
    ph_level = 6.5
    nutrient_index = sum([0.3, 0.7, 0.2]) * 1.5
    growth_score = 0
    for i, temp in enumerate(temperature):
        if temp > 20 and rainfall[i] > 100:
            growth_score += 1.5
        elif temp > 15 and rainfall[i] > 50:
            growth_score += 0.8
    return growth_score

# Unused decoy function (dead code path)
def calculate_erosion_risk(terrain, water_flow):
    risk_factor = 0
    for t, flow in zip(terrain, water_flow):
        risk_factor += (flow / (t + 1)) ** 0.5
    return risk_factor

# Misleading preprocessing with red herring variables
soil_composition = [0.2, 0.4, 0.6, 0.8]
elevation_zones = [100, 150, 200, 250]
unused_gradient = [e / 50 for e in elevation_zones]

# Relevant data structures
climate_data = [22, 25, 19, 17]
rainfall_data = [120, 95, 130, 60]

# Complex nested data structure with cross-references (distractor)
soil_profiles = [
    {'type': 'clay', 'depth': 30, 'ph': 6.2, 'organic': 0.03},
    {'type': 'loam', 'depth': 45, 'ph': 6.8, 'organic': 0.06},
    {'type': 'sand', 'depth': 40, 'ph': 5.9, 'organic': 0.02},
    {'type': 'silt', 'depth': 50, 'ph': 6.7, 'organic': 0.05}
]

# Decoy transformation chain
processed_ph = []
for profile in soil_profiles:
    adjusted = profile['ph'] + 0.1 * profile['depth'] / 10
    processed_ph.append(round(adjusted, 2))

# Linear search for optimal zone (partially relevant but over-complicated)
best_zone = -1
max_rainfall = 0
for idx, rain in enumerate(rainfall_data):
    if rain > max_rainfall and climate_data[idx] > 18:
        max_rainfall = rain
        best_zone = idx

# Red herring: unused yield estimation
theoretical_yield = 0
if best_zone != -1:
    base_yield = 3.5
    organic_boost = soil_profiles[best_zone]['organic'] * 100
    theoretical_yield = base_yield * (1 + organic_boost / 100)

# Core logic obscured by context
legacy_yield_map = {0: 2.1, 1: 3.4, 2: 2.8, 3: 1.9}
current_estimates = []
for day_temp, day_rain in zip(climate_data, rainfall_data):
    if day_temp >= 20 and day_rain >= 100:
        current_estimates.append(4.0)
    elif day_temp >= 15 and day_rain >= 50:
        current_estimates.append(2.5)
    else:
        current_estimates.append(1.0)

# Bit manipulation distraction (irrelevant)
diagnostic_flag = 0
for val in current_estimates:
    diagnostic_flag ^= int(val * 10) & 0xFF

def optimize_harvest(weather, soils):
    # Actual key computation buried in noise
    total_yield = 0.0
    adjustment_factor = 0.9
    
    # Real logic with multiple steps
    for i, temp in enumerate(weather):
        # Primary yield model
        if temp > 21:
            base = 4.2
        elif temp > 16:
            base = 2.7
        else:
            base = 1.3
        
        # Rainfall modulation
        rain_mod = 1.0
        if rainfall_data[i] > 110:
            rain_mod = 1.2
        elif rainfall_data[i] < 70:
            rain_mod = 0.8
        
        # Soil quality bonus (only depth matters in final calc)
        depth_bonus = soils[i]['depth'] / 100  # Max 0.5
        
        # Composite calculation
        daily_yield = base * rain_mod + depth_bonus
        total_yield += daily_yield
    
    # Final adjustment using conditional expression
    total_yield *= adjustment_factor if diagnostic_flag > 0 else 1.1
    
    # Critical assignment
    final_yield = round(total_yield, 4)
    
    # Distractor: unused transformation
    binary_pattern = ''.join(['1' if y > 3 else '0' for y in current_estimates])
    salvage_value = int(binary_pattern, 2) if len(binary_pattern) == 4 else 0
    
    return final_yield

# Execution point
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Target result: {final_yield}")