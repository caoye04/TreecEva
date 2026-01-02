import math

def analyze_rainfall(patterns):
    # Irrelevant function: analyzes rainfall but not used in final computation
    total = 0
    for p in patterns:
        if p % 3 == 0:
            total += p * 0.1
    return total

def compute_root_depth(texture_list):
    # Decoy function with misleading relevance
    depth_map = {}
    for i, t in enumerate(texture_list):
        depth_map[i] = math.sqrt(t) * 0.5 if t > 5 else t * 0.2
    return depth_map

def assess_ph_stress(ph_levels):
    # Dead code path — looks important but unused
    stress_score = 0
    for ph in ph_levels:
        if ph < 6.0 or ph > 7.5:
            stress_score += abs(6.75 - ph)
    return stress_score

def filter_productive_zones(yields, threshold=0.65):
    # Actually relevant: filters zones above threshold
    return [y for y in yields if y >= threshold]

def simulate_growth_cycles(base_yield, cycles):
    # Relevant transformation with red herring variables
    history = []
    temp_mod = 1.0
    ph_factor = 0.95  # Misleading: never actually applied
    for cycle in range(cycles):
        if cycle % 4 == 0:
            temp_mod *= 1.05
        elif cycle % 7 == 0:
            temp_mod *= 0.92  # Distractor adjustment
        adjusted = base_yield * temp_mod * (1 + 0.03 * math.sin(cycle))
        history.append(adjusted)
    return history

def optimize_harvest(weather, composition):
    # Core function with embedded logic and distractions
    
    # Irrelevant mappings
    zone_codes = {i: f'Z{i % 10}' for i in range(len(weather))}
    dummy_matrix = [[i * j for j in range(3)] for i in range(len(composition))]
    
    # Real computation begins
    base_moisture = sum([w['precip'] for w in weather]) / len(weather)
    temp_amplitude = max(w['temp'] for w in weather) - min(w['temp'] for w in weather)
    
    # Simulate multiple growth cycles
    projected_yields = simulate_growth_cycles(base_moisture * 0.02, 12)
    
    # Filter only high-yield cycles
    stable_yields = filter_productive_zones(projected_yields, threshold=0.65)
    
    # Soil contribution (only one field matters)
    nutrient_score = sum(comp['nitrogen'] for comp in composition) / len(composition)
    
    # Key distraction: complex but unused bitwise mix
    decoy_key = 0
    for c in composition:
        decoy_key ^= int(c['carbon'] * 10) & 255
    decoy_key = (decoy_key << 3) | (decoy_key >> 5)
    
    # Final calculation
    avg_stable = sum(stable_yields) / len(stable_yields) if stable_yields else 0
    enhancement = nutrient_score * 0.015
    final_yield = round(avg_stable + enhancement, 6)
    
    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Main execution data
climate_data = [
    {'temp': 22.1, 'precip': 85},
    {'temp': 25.3, 'precip': 92},
    {'temp': 19.8, 'precip': 77},
    {'temp': 24.0, 'precip': 88},
    {'temp': 26.5, 'precip': 95},
    {'temp': 20.4, 'precip': 80},
    {'temp': 23.7, 'precip': 90},
    {'temp': 27.1, 'precip': 94}
]

soil_profiles = [
    {'nitrogen': 2.1, 'carbon': 3.4},
    {'nitrogen': 1.9, 'carbon': 3.1},
    {'nitrogen': 2.3, 'carbon': 3.6},
    {'nitrogen': 2.0, 'carbon': 3.3},
    {'nitrogen': 2.2, 'carbon': 3.5}
]

# Triggering call
final_yield = optimize_harvest(climate_data, soil_profiles)