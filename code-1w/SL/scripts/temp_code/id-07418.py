def analyze_crop_health(data):
    healthy_count = 0
    stress_threshold = 0.6
    temp_score = 0
    for reading in data:
        moisture = reading['moisture']
        nutrient = reading['nutrients']
        ph_level = reading['ph']
        
        # Irrelevant environmental noise
        uv_index = reading.get('uv', 0)
        wind_speed = reading.get('wind', 0)
        noise_factor = (uv_index * 0.1) - (wind_speed * 0.05)
        
        health_score = (moisture * 0.4) + (nutrient * 0.5) - abs(ph_level - 6.5) * 0.2
        if health_score > stress_threshold:
            healthy_count += 1
        temp_score += health_score  # unused accumulator (distractor)
    
    return healthy_count


def normalize_readings(raw_list):
    cleaned = []
    for item in raw_list:
        item['moisture'] = round(item['moisture'], 2)
        item['nutrients'] = max(0, min(1, item['nutrients']))  # clamp to [0,1]
        cleaned.append(item)
    sorted_cleaned = sorted(cleaned, key=lambda x: x['moisture'], reverse=True)
    return sorted_cleaned


def calculate_harvest_potential(regions):
    total_yield = 0
    penalty_factor = 0.0
    boost_tracker = []
    
    for region in regions:
        zone_id = region['zone']
        crop_type = region['crop']
        base_productivity = region['base_yield']
        
        # Normalize sensor inputs
        processed_data = normalize_readings(region['readings'])
        
        # Analyze health - only this matters
        robust_patches = analyze_crop_health(processed_data)
        
        # Real yield logic
        patch_ratio = robust_patches / len(processed_data) if processed_data else 0
        yield_contribution = base_productivity * (0.3 + 0.7 * patch_ratio)
        
        # Fake complex adjustment (distraction)
        zone_code = ''.join([c for c in zone_id if c.isalpha()]).upper()
        code_value = sum(ord(c) for c in zone_code) % 11
        fake_adjustment = (code_value * 0.01) * base_productivity
        
        # Conditional expression with string method (required feature)
        season_modifier = 1.2 if crop_type.lower().strip().endswith('wheat') else 0.9
        
        adjusted_yield = yield_contribution * season_modifier
        
        # Dead code path (distractor)
        if len(boost_tracker) > 100:  # never true
            adjusted_yield *= 1.1
        
        total_yield += adjusted_yield
        boost_tracker.append(f"Yield_{zone_id}_{round(adjusted_yield, 1)}")

    # Final computation
    disruption_events = ['storm', 'drought', 'pests']
    event_risk = len(disruption_events) * 0.05  # distraction
    final_yield = int(total_yield - (total_yield * event_risk * 0))  # neutralized
    
    # This is the actual answer output
    print(f"Result: {final_yield}")
    return final_yield

# Input data
region_data = [
    {
        'zone': 'Z7N',
        'crop': 'winter_wheat',
        'base_yield': 80,
        'readings': [
            {'moisture': 0.65, 'nutrients': 0.72, 'ph': 6.4},
            {'moisture': 0.54, 'nutrients': 0.61, 'ph': 6.8},
            {'moisture': 0.82, 'nutrients': 0.81, 'ph': 6.3},
            {'moisture': 0.45, 'nutrients': 0.50, 'ph': 7.1},
            {'moisture': 0.73, 'nutrients': 0.77, 'ph': 6.5}
        ]
    },
    {
        'zone': 'E3M',
        'crop': 'barley',
        'base_yield': 60,
        'readings': [
            {'moisture': 0.51, 'nutrients': 0.65, 'ph': 6.6},
            {'moisture': 0.47, 'nutrients': 0.58, 'ph': 6.9},
            {'moisture': 0.59, 'nutrients': 0.70, 'ph': 6.2}
        ]
    }
]

# Execute
final_yield = calculate_harvest_potential(region_data)