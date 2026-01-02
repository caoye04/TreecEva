def optimize_harvest(crop_set, params):
    base_yield = 0
    modifier = 1.0
    
    # Environmental factors (distractor: some values not fully used)
    temp_factor = params.get('temperature', 0.95)
    humidity = params.get('humidity_level', 70)
    soil_quality = params.get('soil_grade', 'medium')
    legacy_mode = params.get('legacy', False)  # unused dead flag

    # Irrelevant intermediate calculation (distractor)
    phantom_score = 0
    for item in crop_set:
        if isinstance(item, str) and len(item) > 3:
            phantom_score += hash(item) % 7
    
    # Real computation begins
    valid_crops = {c for c in crop_set if isinstance(c, int) and c > 0}  # set comprehension
    
    if soil_quality == 'high':
        modifier *= 1.25
    elif soil_quality == 'low':
        modifier *= 0.75
    else:
        modifier *= 0.9
        
    # Accumulation with filtering
    total_rainfall = 0
    rainfall_log = params.get('rainfall', [])
    for day_rain in rainfall_log:
        if day_rain < 0:
            continue
        total_rainfall += day_rain
    
    avg_rain = total_rainfall / len(rainfall_log) if rainfall_log else 0
    
    if avg_rain > 5.0:
        modifier *= 1.1
    elif avg_rain < 2.0:
        modifier *= 0.9

    # Core yield calculation
    for crop_id in valid_crops:
        if crop_id % 3 == 0:
            base_yield += crop_id * 2
        elif crop_id % 5 == 0:
            base_yield += crop_id * 1.5
        else:
            base_yield += crop_id

    # Final adjustment
    final_yield = int(base_yield * modifier)
    
    # Dead code path (distractor)
    if temp_factor < 0.8:
        final_yield = -1  # never reached due to default 0.95
        
    return final_yield

# Main execution
projection_set = {15, 9, 25, 4, 'wheat', 'corn', 30}
adjustment_map = {
    'temperature': 0.97,
    'humidity_level': 65,
    'soil_grade': 'high',
    'rainfall': [3.2, 6.1, 4.8, 7.0, 2.5],
    'legacy': True
}

interim_check = sum(projection_set.intersection({9, 15, 20}))  # semi-relevant distractor

final_yield = optimize_harvest(projection_set, adjustment_map)
print(f"Target result: {final_yield}")