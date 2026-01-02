import math

def analyze_risk(factors):
    # Irrelevant risk analysis function (dead code path)
    score = 0
    for f in factors:
        score += f * 0.3
    return round(score, 2)

risk_factors = [0.4, 0.7, 0.9, 1.2]
baseline = sum(risk_factors) / len(risk_factors)
adjusted_risk = baseline * 0.85

# Distractor: Unused but plausible agricultural indices
crop_index_map = {
    'wheat': 0.67,
    'barley': 0.52,
    'maize': 0.83,
    'rye': 0.45
}

soil_nutrients = {'nitrogen': 58, 'phosphorus': 32, 'potassium': 41}
texture_score = 76
organic_content = 3.8

# Real processing begins here — subtle signal in noise
climate_data = [22.4, 18.9, 25.1, 20.3, 23.0, 19.7, 24.2]
soil_conditions = [texture_score, organic_content, soil_nutrients['phosphorus']]

lambda_transform = lambda x, a: x ** 0.5 * (1 + a / 100)

processed_climate = []
for temp in climate_data:
    adjusted_temp = lambda_transform(temp, 8.5) if temp < 22 else lambda_transform(temp, -2.3)
    processed_climate.append(round(adjusted_temp, 3))

# Hidden core logic: yield estimation via multi-step filtering and transformation
mask = [1 if 20 <= t <= 24 else 0 for t in climate_data]
masked_temps = [t for t, m in zip(processed_climate, mask) if m == 1]

avg_masked = sum(masked_temps) / len(masked_temps) if masked_temps else 0

# Secondary distractor: unused crop rotation simulator
rotation_cycle = ['corn', 'beans', 'oats']
field_history = {year: crop for year, crop in enumerate(rotation_cycle * 3)}

# Core algorithm disguised among red herrings
buffer_zone = []
for i in range(len(soil_conditions)):
    val = soil_conditions[i]
    if i == 0:
        buffer_zone.append(val * 0.7)
    elif i == 1:
        buffer_zone.append(val * 1.2)
    else:
        buffer_zone.append(val * 0.9)

soil_potency = sum(buffer_zone) / 3

# Decoy intermediate result (misleading)
temp_potency_ratio = avg_masked / soil_potency if soil_potency != 0 else 0
flag_check = temp_potency_ratio > 0.65

# Conditional expression with actual relevance
modifier = 1.15 if flag_check and len(masked_temps) > 3 else 0.88

# Critical calculation buried in abstraction
def optimize_harvest(temps, soil):
    base_yield = 0
    for t in temps:
        if t > 21.5:
            base_yield += t * 1.05
        else:
            base_yield += t * 0.95
    
    # Integration with soil component
    s1, s2, s3 = soil
    soil_factor = (s1 * 0.2) + (s2 * 0.5) + (s3 * 0.3)
    
    # Final composition
    preliminary = (base_yield / len(temps)) * (soil_factor / 100)
    
    # Early return red herring (never taken due to data)
    if preliminary < 10:
        return -1  # Dead path
    
    return preliminary * modifier

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_conditions)

# Print required output
print(f"Target result: {final_yield}")