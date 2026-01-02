def analyze_terrain(terrain_data):
    elevation = terrain_data.get('elevation', 0)
    slope = terrain_data.get('slope', 0)
    aspect_ratio = terrain_data.get('aspect', 1)
    
    # Irrelevant calculation (distractor)
    shadow_coverage = (elevation * 0.3) + (slope * 0.1)
    
    if slope > 15:
        return False, shadow_coverage
    
    return True, shadow_coverage


def preprocess_sample(sample_str):
    # Use string method for cleaning input (required feature)
    cleaned = sample_str.strip().lower().replace('contaminated', '')
    parts = cleaned.split(':')
    ph_level = float(parts[1]) if len(parts) > 1 else 7.0
    
    # Misleading intermediate
    stability_index = (ph_level * 2) % 5
    
    return ph_level > 6.5 and ph_level < 7.5


def modular_decay(value, iterations):
    # Modular arithmetic (suggested paradigm)
    for i in range(iterations):
        value = (value * 7 + 3) % 101
    return value

# Simulate soil analysis across multiple plots
def calculate_harvest_potential(samples):
    base_yield = 0
    adjustment_factor = 1.0
    
    terrain = {'elevation': 820, 'slope': 12, 'aspect': 1.4}
    valid_terrain, coverage = analyze_terrain(terrain)
    
    if not valid_terrain:
        return 0
    
    total_compatibility = 0
    sample_count = 0
    
    for raw_sample in samples:
        # Preprocess each soil string
        compatible = preprocess_sample(raw_sample)
        
        # Simulated compatibility score
        temp_score = len(raw_sample) % 9
        
        # Only certain samples contribute (logic dependency)
        if compatible:
            total_compatibility += temp_score
            sample_count += 1
        
        # Dead code path (distractor)
        if 'toxic' in raw_sample:
            adjustment_factor *= 0.9

    if sample_count == 0:
        avg_compatibility = 0
    else:
        avg_compatibility = total_compatibility / sample_count
    
    # Core calculation with modular decay
    base_yield = int(modular_decay(avg_compatibility * 12, 4))
    
    # Secondary irrelevant transformation
    predicted_rainfall = (sum([len(s) for s in samples]) * 0.25) % 30
    
    # Final yield depends only on base_yield and terrain-adjusted factor
    terrain_bonus = 1 + (terrain['elevation'] / 10000)
    final_yield = base_yield * terrain_bonus
    
    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Input data
soil_samples = [
    "plot:A:ph:7.2:status:normal",
    "plot:B:ph:6.8:status:stable",
    "plot:C:ph:5.4:status:acidic",
    "plot:D:ph:7.1:status:normal"
]

# Execute
final_yield = calculate_harvest_potential(soil_samples)