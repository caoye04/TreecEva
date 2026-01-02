def analyze_growth_potential(temp, moisture):
    # Irrelevant helper with misleading name
    if temp < 20 or moisture < 30:
        return 0
    return (temp - 15) * (moisture / 10)

# Distractor function - looks important but unused in final calculation
def calculate_irrigation_need(rainfall, evaporation):
    base_need = 50 - rainfall + evaporation
    return max(0, base_need)

# Another decoy: complex but unused
soil_quality_map = {
    'clay': lambda x: x * 0.7,
    'loam': lambda x: x * 1.2,
    'sand': lambda x: x * 0.5
}

# Real data structures used
climate_data = [
    {'temp': 25, 'rain': 40, 'wind': 12},
    {'temp': 28, 'rain': 35, 'wind': 8},
    {'temp': 23, 'rain': 50, 'wind': 15},
    {'temp': 30, 'rain': 20, 'wind': 10}
]

soil_profiles = [
    {'type': 'loam', 'ph': 6.5, 'nutrients': 80},
    {'type': 'clay', 'ph': 7.0, 'nutrients': 60},
    {'type': 'loam', 'ph': 6.8, 'nutrients': 85},
    {'type': 'sand', 'ph': 5.5, 'nutrients': 40}
]

# Unused intermediate arrays
microbe_activity = [0.88, 0.76, 0.91, 0.67]
decomp_rates = [x * 0.3 for x in microbe_activity]

# Key transformation: filters high-wind days and computes yield factors
yield_factors = []
for i in range(len(climate_data)):
    temp = climate_data[i]['temp']
    rain = climate_data[i]['rain']
    wind = climate_data[i]['wind']
    nutrients = soil_profiles[i]['nutrients']
    
    # Distractor: calculating irrelevant index
    drought_index = temp - rain
    flood_risk = 1 if rain > 45 else 0
    
    # Real logic: only consider low-wind conditions
    if wind <= 12:
        base_yield = analyze_growth_potential(temp, rain)
        nutrient_boost = nutrients * 0.01
        adjusted_yield = base_yield + nutrient_boost
        yield_factors.append(adjusted_yield)

# Dead code path - never executed due to prior filtering
if len(yield_factors) == 0:
    yield_factors = [5.0] * len(climate_data)

# Red herring computation
theoretical_max = sum([max(profile['nutrients'], 70) for profile in soil_profiles]) / 4

# Actual optimization logic
aggregated_score = 0
for factor in yield_factors:
    if factor > 12.0:  # threshold filter
        aggregated_score += factor * 1.5
    else:
        aggregated_score += factor

# Final adjustment using unused ph data (misleading)
pH_correction = sum([abs(p['ph'] - 6.5) for p in soil_profiles])
final_yield = int(aggregated_score - pH_correction)

# Decoy print statements (commented out)
# print(f"Microbial decomposition: {sum(decomp_rates)}")
# print(f"Irrigation baseline: {calculate_irrigation_need(20, 10)}")

print(f"Result: {final_yield}")