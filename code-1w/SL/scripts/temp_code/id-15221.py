import itertools

# Simulate agricultural yield optimization under varying conditions
def calculate_base_yield(area, fertility_index):
    return area * (fertility_index ** 1.5)

def adjust_for_rainfall(base_yield, rainfall_mm):
    if rainfall_mm < 300:
        return base_yield * 0.6
    elif rainfall_mm > 800:
        return base_yield * 0.75
    else:
        return base_yield * (1 + (rainfall_mm - 500) / 1000)

def assess_pest_pressure(temperature_avg):
    # Irrelevant function - simulated pest modeling
    pressure = 0
    for t in range(int(temperature_avg)):
        pressure += (t % 7) * 0.3
    return min(pressure, 10)

def generate_soil_compatibility_map(soil_types):
    # Distractor: creates a red herring dictionary
    compatibility = {}
    for s in soil_types:
        compatibility[s] = hash(s) % 100
    temp_score = sum(compatibility.values())
    normalized = {k: v / (temp_score + 1e-8) for k, v in compatibility.items()}
    return normalized  # Never used in final calculation

def filter_reliable_regions(yields, threshold=200):
    # Another distractor - region filtering not affecting main result
    valid = []
    for i, y in enumerate(yields):
        if y > threshold and i % 2 == 0:
            valid.append(i)
    return valid

def simulate_crop_rotation(crops):
    rotations = list(itertools.permutations(crops, 3))
    scores = []
    for rot in rotations:
        score = 0
        for i, crop in enumerate(rot):
            score += len(crop) * (i + 1)
        scores.append(score)
    avg_rotation_score = sum(scores) / len(scores) if scores else 0
    return avg_rotation_score  # Unused but looks important

def optimize_harvest(climate_data, soil_profiles):
    total_yield = 0
    peak_multiplier = 1.0
    
    # Real logic starts here
    for region, data in climate_data.items():
        area = data['area']
        fertility = soil_profiles.get(region, {}).get('fertility', 1.0)
        rainfall = data['rainfall']
        temperature = data['temp_avg']
        
        base = calculate_base_yield(area, fertility)
        adjusted = adjust_for_rainfall(base, rainfall)
        
        # Hidden critical adjustment: only certain regions get boost
        if temperature > 22 and rainfall > 500:
            adjusted *= 1.3
        
        total_yield += adjusted
    
    # Decoy section: looks like it modifies total_yield but doesn't
    dummy_yield = total_yield
    for _ in range(3):
        dummy_yield = (dummy_yield * 0.95 + 50) // 1
    
    # Critical red herring: complex transformation that appears relevant
    all_crops = ['wheat', 'corn', 'rice', 'barley']
    rotation_value = simulate_crop_rotation(all_crops)
    
    # Fake normalization using unused components
    compatibility_map = generate_soil_compatibility_map(['clay', 'loam', 'sand'])
    reliability_zones = filter_reliable_regions([total_yield])
    
    # Actual answer derivation buried in noise
    scaling_factor = 0.88
    if len(reliability_zones) > 0:
        scaling_factor += 0.05
    
    # Final computation — only this matters
    final_yield = int(total_yield * scaling_factor)
    
    # Multiple print statements to distract
    # print(f'Debug: rotation={rotation_value}')
    # print(f'Soil map: {compatibility_map}')
    
    return final_yield

# Input data
climate_data = {
    'region_A': {'area': 200, 'rainfall': 600, 'temp_avg': 24},
    'region_B': {'area': 150, 'rainfall': 700, 'temp_avg': 19},
    'region_C': {'area': 180, 'rainfall': 550, 'temp_avg': 26}
}

soil_profiles = {
    'region_A': {'fertility': 1.2, 'ph': 6.5},
    'region_B': {'fertility': 1.4, 'ph': 7.0},
    'region_C': {'fertility': 1.1, 'ph': 6.0}
}

# Execution point
final_yield = optimize_harvest(climate_data, soil_profiles)
Result: {final_yield}