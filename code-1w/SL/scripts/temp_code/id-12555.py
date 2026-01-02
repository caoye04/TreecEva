from itertools import combinations

def analyze_soil_composition(elements):
    # Irrelevant helper: computes element pairs but only used for distraction
    acid_levels = {e: (e * 1.3 + 2) % 4.1 for e in elements}
    pair_interactions = list(combinations(elements, 2))
    interaction_score = sum(abs(a - b) for a, b in pair_interactions)
    return interaction_score * 0.1

def normalize_readings(readings):
    # Semi-relevant normalization, but output not fully used
    base_offset = min(readings)
    normalized = [(r - base_offset) * 1.1 for r in readings]
    adjusted_total = sum(normalized)
    return adjusted_total

def calculate_harvest_efficiency(data):
    # Core logic begins
    total_rainfall = sum(d['rain'] for d in data)
    avg_temp = sum(d['temp'] for d in data) / len(data)
    
    # Distractor: complex set operations with partial relevance
    crop_set_a = {d['crop'] for d in data if d['rain'] > 80}
    crop_set_b = {d['crop'] for d in data if d['temp'] < 25}
    common_crops = crop_set_a & crop_set_b
    
    # Key accumulation logic
    yield_accum = 0
    for record in data:
        base_yield = record['base']
        temp_factor = 1.0 if 18 <= record['temp'] <= 30 else 0.6
        rain_factor = 0.8 if record['rain'] < 60 or record['rain'] > 120 else 1.0
        
        # Apply modifiers
        effective_yield = base_yield * temp_factor * rain_factor
        yield_accum += effective_yield
    
    # Final adjustment based on diversity bonus
    unique_crops = len({d['crop'] for d in data})
    diversity_bonus = 1.05 if unique_crops >= 3 else 1.0
    final_efficiency = yield_accum * diversity_bonus
    
    # Dead code path - misleading control flow
    if len(common_crops) > 5:
        fallback = normalize_readings([d['rain'] for d in data])
        final_efficiency = fallback  # never executed
    
    return final_efficiency

# Simulated regional agricultural data
region_data = [
    {'crop': 'wheat', 'base': 45, 'temp': 22, 'rain': 75},
    {'crop': 'corn', 'base': 60, 'temp': 26, 'rain': 110},
    {'crop': 'rice', 'base': 50, 'temp': 24, 'rain': 130},
    {'crop': 'barley', 'base': 40, 'temp': 19, 'rain': 85},
    {'crop': 'oats', 'base': 35, 'temp': 17, 'rain': 90}
]

# Irrelevant preprocessing
element_list = [23, 45, 12, 8, 31]
analyze_soil_composition(element_list)

# Normalization call with unused return
unused_total = normalize_readings([d['temp'] for d in region_data])

# Key execution point
final_yield = calculate_harvest_efficiency(region_data)
print(f"Result: {final_yield}")