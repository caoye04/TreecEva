import math

# Simulated environmental data (real inputs)
climate_data = {
    'temp_avg': [22.1, 23.5, 25.0, 26.8, 24.7],
    'precip': [80, 110, 140, 95, 70],
    'humidity': [65, 70, 75, 68, 60]
}

soil_profiles = [
    {'ph': 6.2, 'nitrogen': 18, 'organic_matter': 3.1},
    {'ph': 5.9, 'nitrogen': 22, 'organic_matter': 2.8},
    {'ph': 6.5, 'nitrogen': 15, 'organic_matter': 3.5}
]

# Irrelevant auxiliary data (distractor)
disease_risk = {
    'fungus_x': 0.3,
    'blight_y': 0.15,
    'mold_z': 0.05
}

# Decoy function - looks important but unused in final calculation
def calculate_pest_pressure(weather):
    risk_score = 0
    for day_temp in weather['temp_avg']:
        if day_temp > 25:
            risk_score += 0.02 * day_temp
    return risk_score

# Unused transformation (dead code path)
processed_precip = []
for p in climate_data['precip']:
    normalized = (p - min(climate_data['precip'])) / (max(climate_data['precip']) - min(climate_data['precip']))
    processed_precip.append(round(normalized * 100))

# Misleading intermediate metric (red herring)
average_stress_index = 0
for i in range(len(climate_data['temp_avg'])):
    stress = 0
    if climate_data['temp_avg'][i] > 25:
        stress += 0.8
    if climate_data['humidity'][i] < 65:
        stress += 0.3
    average_stress_index += stress
average_stress_index /= len(climate_data['temp_avg'])

# Auxiliary computation with bit manipulation (distractor)
temp_flags = 0
for t in climate_data['temp_avg']:
    temp_flags |= int(t) << 1

# Real processing begins here — key logic buried among noise
def assess_soil_fertility(soils):
    scores = []
    for s in soils:
        # Core formula: weighted fertility index
        score = (s['ph'] * 10) + s['nitrogen'] + (s['organic_matter'] * 15)
        scores.append(score)
    return sum(scores) / len(scores)  # Average fertility

# Climate suitability with logarithmic scaling (relevant)
def compute_climate_fitness(data):
    base = 0
    for i in range(len(data['temp_avg'])):
        temp_factor = math.log(1 + abs(data['temp_avg'][i] - 24))
        precip_factor = math.sqrt(data['precip'][i]) / 10
        base += (precip_factor - temp_factor)
    return base  # Higher = better alignment with ideal

# Hidden control flow with tuple unpacking and conditional override
override_mode = False
default_offsets = (0.5, -0.3, 0.7)
alpha, beta, gamma = default_offsets

if sum(climate_data['temp_avg']) / len(climate_data['temp_avg']) > 24.5:
    alpha += 0.2
    gamma -= 0.1
else:
    beta += 0.4  # This branch is taken

# Main optimization function — only this affects final answer
def optimize_harvest(climate, soils):
    # Step 1: Base yield from soil
    soil_base = assess_soil_fertility(soils)
    
    # Step 2: Modulate by climate fitness
    climate_boost = compute_climate_fitness(climate)
    
    # Step 3: Apply hidden offset (beta adjusted above)
    adjustment = beta * 100
    
    # Step 4: Count favorable days (basic counting)
    favorable_days = 0
    for i in range(len(climate['temp_avg'])):
        if 22 <= climate['temp_avg'][i'] <= 26 and climate['precip'][i] >= 85:
            favorable_days += 1
    
    # Step 5: Grouping logic - how many soils have high nitrogen?
    high_n_count = 0
    for s in soils:
        if s['nitrogen'] > 20:
            high_n_count += 1
    
    # Final composite formula (8-12 logic steps)
    yield_potential = (
        soil_base * 2.1 + 
        climate_boost * 15 + 
        favorable_days * 3.5 + 
        high_n_count * 7.2 + 
        adjustment
    )
    
    # Red herring: this dictionary looks important but isn't used further
    diagnostics = {
        'soil_base': soil_base,
        'climate_score': climate_boost,
        'flag_checksum': temp_flags & 0xFF,
        'stability_ratio': average_stress_index
    }
    
    return int(yield_potential)  # Deterministic integer output

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)

# Output required format
print(f"Result: {final_yield}")