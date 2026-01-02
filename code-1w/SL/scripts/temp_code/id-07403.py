def analyze_growth_potential(temp, moisture):
    return lambda nutrient: (temp * 0.6) + (moisture * 0.3) + (nutrient * 0.1)

# Irrelevant weather simulation (distraction)
def simulate_wind_pattern(elevation):
    result = 0
    for i in range(5):
        result += (elevation + i) % 7
    return result * 0.2

def calculate_root_depth(texture, organic_content):
    if texture == 'clay':
        base = 30
    elif texture == 'loam':
        base = 50
    else:
        base = 40
    return base + (organic_content * 2)

# Unused decoy function
def deprecated_yield_model(x, y):
    return x ** 0.5 + y ** 0.7

# Core logic disguised among distractors
def assess_drought_risk(precip_annual, evap_rate):
    risk_score = 0
    if precip_annual < 500:
        risk_score += 3
    elif precip_annual < 800:
        risk_score += 2
    else:
        risk_score += 1
    
    if evap_rate > 1200:
        risk_score += 2
    
    # Red herring calculation
    fake_adjustment = (evap_rate // 100) % 5
    
    return risk_score

soil_profiles = [
    {'ph': 6.2, 'texture': 'loam', 'organic': 3.1, 'depth_cm': 120},
    {'ph': 5.8, 'texture': 'clay', 'organic': 2.3, 'depth_cm': 90},
    {'ph': 7.0, 'texture': 'sand', 'organic': 1.8, 'depth_cm': 75}
]

climate_data = {
    'avg_temp_c': 22.5,
    'precip_mm': 650,
    'evap_mm': 1100,
    'sunlight_hours': 6.8,
    'frost_days': 15
}

# Distractor: unused data structure
topography_map = {
    'slope_pct': 8,
    'aspect': 'south',
    'elevation_m': 234,
    'shade_factor': 0.3
}

# Misleading intermediate calculations
baseline_productivity = 0
for soil in soil_profiles:
    ph_effect = abs(soil['ph'] - 6.5) * -0.4
    depth_bonus = soil['depth_cm'] / 100
    baseline_productivity += ph_effect + depth_bonus  # Not actually used later

# Fake aggregation (dead path)
dummy_scores = [assess_drought_risk(climate_data['precip_mm'], climate_data['evap_mm'])] * 3

# Real processing chain hidden among noise
growth_evaluator = analyze_growth_potential(climate_data['avg_temp_c'], climate_data['precip_mm'] / 1000)

root_metrics = []
for s in soil_profiles:
    depth = calculate_root_depth(s['texture'], s['organic'])
    root_metrics.append(depth)

# Key computation buried in list comprehension with filtering
effective_yields = [
    growth_evaluator(s['organic']) * r * 0.4
    for s, r in zip(soil_profiles, root_metrics)
    if r > 40  # Only deep-rooting soils contribute
]

# Secondary filter based on drought risk (real dependency)
drought_level = assess_drought_risk(climate_data['precip_mm'], climate_data['evap_mm'])
adjustment_factor = 1.0
if drought_level >= 4:
    adjustment_factor = 0.6
elif drought_level >= 3:
    adjustment_factor = 0.8

# Final integration with red herring variable
fake_normalization = sum([simulate_wind_pattern(topography_map['elevation_m']) for _ in range(2)])
final_yield = sum(effective_yields) * adjustment_factor  # This is the target

# Output required format
print(f"Result: {final_yield}")