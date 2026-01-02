def analyze_growth_potential(temperature, rainfall):
    # Irrelevant analysis with misleading intermediate
    baseline = 2 * temperature + 0.5 * rainfall
    volatility = abs(temperature - 25) if temperature > 20 else 0
    return baseline - volatility if volatility > 5 else baseline + 10

# Unused decoy function (dead code path)
def calculate_fertilizer_need(nitrogen, phosphorus):
    return (nitrogen + phosphorus) * 1.5

# Distractor variables
tank_capacity = 5000
irrigation_cycles = [3, 1, 4, 1, 5]
efficiency_factor = 0.87
phantom_score = sum([x % 2 for x in irrigation_cycles])  # Red herring

soil_quality = [85, 90, 78, 92, 88]
climate_data = {'temp': [22, 26, 24, 28, 23], 'rain': [80, 60, 70, 50, 75]}
pest_index = [0.1, 0.3, 0.6, 0.2, 0.4]

# Complex data transformation with conditional expressions
normalized_rainfall = [(r / 100) if r < 75 else 1.0 for r in climate_data['rain']]
adjusted_temp = [t if 20 <= t <= 30 else (30 if t > 30 else 20) for t in climate_data['temp']]

# Misleading intermediate calculation
dummy_yield = 0
for i in range(len(climate_data['temp'])):
    dummy_yield += analyze_growth_potential(climate_data['temp'][i], climate_data['rain'][i])

dummy_yield = dummy_yield / len(climate_data['temp'])

# Unused list comprehension distraction
synthetic_indices = [abs(soil_quality[i] - climate_data['temp'][i]) for i in range(5) if pest_index[i] < 0.35]

# Core logic embedded within noise
def compute_viability(index):
    return 1 if index < 0.3 else (0.5 if index < 0.5 else 0.2)

def optimize_harvest(climate, soils, pests):
    total = 0.0
    for i in range(len(soils)):
        # Nested conditionals with conditional expressions
        growth_base = analyze_growth_potential(climate['temp'][i], climate['rain'][i])
        adjustment = (0.9 if soils[i] > 85 else 0.7) if pests[i] < 0.3 else (0.4 if soils[i] > 80 else 0.3)
        viability = compute_viability(pests[i])
        
        # Key calculation step
        yield_contribution = growth_base * adjustment * viability * normalized_rainfall[i]
        total += yield_contribution
    
    # Final aggregation with distractor logic
    avg_soil = sum(soils) / len(soils)
    bonus = 10 if avg_soil > 85 else 0  # Small deterministic bonus
    penalty = phantom_score * 2  # Use of misleading variable (but has fixed value)
    
    return total + bonus - penalty

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_quality, pest_index)

print(f"Result: {final_yield}")