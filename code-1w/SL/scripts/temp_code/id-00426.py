def analyze_growth_potential(temperature, moisture):
    # Auxiliary calculation with partial relevance
    base_index = (temperature - 15) * 0.8
    if moisture > 60:
        base_index += 12
    elif moisture > 40:
        base_index += 7
    else:
        base_index += 3
    return base_index

# Simulate seasonal climate fluctuations
temperature_profile = [22, 25, 28, 30, 27, 24]
moisture_levels = [55, 65, 70, 60, 50, 45]

# Irrelevant historical data (distractor)
historical_rainfall = [120, 110, 95, 130, 140, 125]
legacy_yield_data = [x * 0.7 for x in historical_rainfall]  # Dead computation path

# Soil nutrient mapping (mixed relevance)
soil_nutrients = {'nitrogen': 0.23, 'phosphorus': 0.18, 'potassium': 0.31}
nutrient_factor = sum(soil_nutrients.values()) * 10

# Generate growth index per week using list comprehension
growth_indices = [
    analyze_growth_potential(temp, moist) 
    for temp, moist in zip(temperature_profile, moisture_levels)
]

# Secondary distraction: simulate pest pressure (unused in final logic)
pest_pressure = 0
for i, moisture in enumerate(moisture_levels):
    if moisture > 65 and temperature_profile[i] > 26:
        pest_pressure += 5

# Normalize growth indices with dampening effect
dampened_indices = [
    idx * (0.95 ** i) for i, idx in enumerate(growth_indices)
]

# Calculate cumulative viability score
cumulative_viability = 0
for idx in dampened_indices:
    if idx >= 18:
        cumulative_viability += idx * 1.1
    elif idx >= 14:
        cumulative_viability += idx * 1.0
    else:
        cumulative_viability += idx * 0.8

# Soil condition weighting
soil_score = 0
if soil_nutrients['nitrogen'] > 0.2:
    soil_score += 5
if soil_nutrients['phosphorus'] > 0.15:
    soil_score += 4
if soil_nutrients['potassium'] > 0.3:
    soil_score += 6

# Mock calibration process (irrelevant)
calibration_offset = 0
for _ in range(3):
    calibration_offset += nutrient_factor % 7
    nutrient_factor /= 2  # Distractor update

# Final optimization function
def optimize_harvest(climate_data, soil_conditions):
    base_yield = sum(climate_data) * 2.5
    bonus_factor = 1 + (soil_score / 100)
    adjusted_yield = base_yield * bonus_factor
    
    # Apply random-seed deterministic modifier (fixed seed for determinism)
    import random
    random.seed(42)
    fluctuation = random.uniform(-0.05, 0.08)  # Small controlled variation
    adjusted_yield *= (1 + fluctuation)
    
    # Final threshold adjustment
    if adjusted_yield > 220:
        adjusted_yield *= 0.95
    
    return round(adjusted_yield, 4)

# Execute main logic
final_yield = optimize_harvest(dampened_indices, soil_nutrients)
print(f"Target result: {final_yield}")