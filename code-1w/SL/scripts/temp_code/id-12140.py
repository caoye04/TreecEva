def analyze_growth_potential(temperature, rainfall):
    # Irrelevant ecological model (dead code path)
    base_index = temperature * 0.8 + rainfall * 0.2
    if base_index > 30:
        return base_index * 1.2
    return base_index

def calculate_root_depth(layers):
    # Distractor function: computes something unused later
    total = 0
    for layer in layers:
        if layer['type'] == 'clay':
            total += layer['depth'] * 0.7
        elif layer['type'] == 'loam':
            total += layer['depth'] * 1.3
        else:
            total += layer['depth'] * 0.9
    return round(total / len(layers), 2)

def filter_optimal_conditions(data):
    # Processes climate data but introduces red herring variables
    filtered = []
    threshold = 18.5
    fluctuation_buffer = 0
    for entry in data:
        temp = entry['temp']
        rain = entry['precip']
        humidity = entry['humidity']  # Unused parameter
        # Misleading intermediate calculation
        adjusted_rain = rain * (1 + (humidity - 60) / 100) if humidity > 50 else rain
        if temp > threshold and rain > 50:
            score = temp * 0.3 + rain * 0.7
            filtered.append({'day': entry['day'], 'score': score})
    # Sort by irrelevant metric
    sorted_filtered = sorted(filtered, key=lambda x: x['day'])
    return [x['score'] for x in sorted_filtered]

def compute_nutrient_score(profiles):
    # Complex but mostly irrelevant nutrient logic
    scores = []
    for profile in profiles:
        ph_factor = abs(profile['ph'] - 6.5) * -2
        nitrogen = profile['nitrogen']
        phosphorus = profile['phosphorus']
        potassium = profile['potassium']
        primary_sum = nitrogen + phosphorus + potassium
        # Decoy transformation
        transformed = (primary_sum ** 0.5) * (1 + ph_factor / 10)
        if profile['organic_matter'] > 3.0:
            transformed *= 1.15
        scores.append(round(transformed, 3))
    avg_score = sum(scores) / len(scores) if scores else 0
    return round(avg_score * 0.6, 2)

def optimize_harvest(climate, soil):
    # Core relevant logic hidden among distractions
    
    # Red herring initialization
    max_biomass = 0
    growth_cycles = []
    for i in range(3):
        growth_cycles.append({'cycle': i, 'yield': 0})
    
    # Irrelevant normalization
    normalized_rainfall = [c['precip'] / 100 for c in climate if c['precip'] > 0]
    cumulative_stress = 0
    for nr in normalized_rainfall:
        if nr < 0.4:
            cumulative_stress += (0.4 - nr) * 2
    
    # Key preprocessing (relevant)
    valid_scores = filter_optimal_conditions(climate)
    base_yield = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    
    # Distracting secondary input processing
    dummy_depth = calculate_root_depth([{'depth': s['thickness'], 'type': s['texture']} for s in soil])
    fake_nutrient = compute_nutrient_score(soil)
    
    # Hidden core logic using list comprehensions (required feature)
    stress_factors = [abs(c['temp'] - 22) + max(0, 60 - c['precip']) / 10 for c in climate]
    avg_stress = sum(stress_factors) / len(stress_factors)
    
    # Critical adjustment based on soil clay content (subtle but deterministic)
    clay_layers = len([s for s in soil if s['texture'] == 'clay'])
    thickness_list = [s['thickness'] for s in soil]
    total_thickness = sum(thickness_list)
    weighted_clay_ratio = sum(s['thickness'] for s in soil if s['texture'] == 'clay') / total_thickness if total_thickness > 0 else 0
    
    # Real yield computation buried in noise
    modifier = 1.0
    if weighted_clay_ratio > 0.4:
        modifier *= 0.85
    elif weighted_clay_ratio < 0.1:
        modifier *= 1.1
    
    # Final formula combining multiple concepts
    potential = base_yield * (1 - avg_stress * 0.02) * modifier
    
    # Dead code: simulation loop never used
    simulations = []
    for seed in [1, 2, 3]:
        simulations.append({'seed': seed, 'result': potential * (0.9 + seed/100)})
    
    # Answer is here
    final_yield = int(round(potential * 100))
    return final_yield

# Main execution block
climate_data = [
    {'day': 1, 'temp': 25, 'precip': 60, 'humidity': 65},
    {'day': 2, 'temp': 23, 'precip': 45, 'humidity': 70},
    {'day': 3, 'temp': 20, 'precip': 80, 'humidity': 80},
    {'day': 4, 'temp': 26, 'precip': 30, 'humidity': 55},
    {'day': 5, 'temp': 28, 'precip': 70, 'humidity': 60},
    {'day': 6, 'temp': 24, 'precip': 90, 'humidity': 75},
    {'day': 7, 'temp': 22, 'precip': 55, 'humidity': 50}
]

soil_profiles = [
    {'layer': 1, 'thickness': 20, 'texture': 'loam', 'ph': 6.8, 'nitrogen': 2.3, 'phosphorus': 1.8, 'potassium': 2.0, 'organic_matter': 3.2},
    {'layer': 2, 'thickness': 30, 'texture': 'clay', 'ph': 6.2, 'nitrogen': 1.9, 'phosphorus': 1.5, 'potassium': 1.7, 'organic_matter': 2.1},
    {'layer': 3, 'thickness': 15, 'texture': 'sand', 'ph': 7.0, 'nitrogen': 1.2, 'phosphorus': 0.8, 'potassium': 1.3, 'organic_matter': 1.5},
    {'layer': 4, 'thickness': 35, 'texture': 'clay', 'ph': 6.4, 'nitrogen': 2.0, 'phosphorus': 1.6, 'potassium': 1.9, 'organic_matter': 2.8}
]

# Execute main logic
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Target result: {final_yield}")