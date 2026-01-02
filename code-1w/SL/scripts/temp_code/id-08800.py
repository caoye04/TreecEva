def analyze_soil_composition(samples):
    # Irrelevant analysis with misleading calculations
    avg_pH = sum(sample['pH'] for sample in samples) / len(samples)
    outlier_count = 0
    for sample in samples:
        if sample['pH'] > 7.5 or sample['pH'] < 5.5:
            outlier_count += 1
    normalized_score = (avg_pH - 5.0) * 10
    return avg_pH, normalized_score, outlier_count


def assess_rainfall_pattern(precipitation):
    # Distractor function: computes rainfall stats but not used in final yield
    total_rain = sum(precipitation)
    wet_days = sum(1 for p in precipitation if p > 5)
    dry_streak = 0
    max_dry = 0
    for p in precipitation:
        if p < 2:
            dry_streak += 1
        else:
            max_dry = max(max_dry, dry_streak)
            dry_streak = 0
    max_dry = max(max_dry, dry_streak)
    return total_rain, wet_days, max_dry


def calculate_harvest_potential(data):
    base_yield = data['base_productivity']
    elevation_factor = 1.0 - (data['elevation'] / 1000) * 0.1
    
    # Soil treatment (only pH average matters)
    soil_samples = data['soil_samples']
    _, norm_score, _ = analyze_soil_composition(soil_samples)
    ph_influence = (norm_score - 20) / 10
    
    # Climate factor using temperature extremes
    temps = data['daily_temps']
    heat_stress = 0
    cold_snaps = 0
    for t in temps:
        if t > 35:
            heat_stress += 1
        if t < 5:
            cold_snaps += 1
    temp_penalty = (heat_stress * 0.02) + (cold_snaps * 0.03)
    
    # Misleading use of slicing and tuple unpacking
    recent_temps = temps[-7:]  # Last week
    weekly_avg = sum(recent_temps) / len(recent_temps)
    temp_trend = 'stable'
    if weekly_avg > sum(temps[:7]) / 7:
        temp_trend = 'rising'
    elif weekly_avg < sum(temps[:7]) / 7:
        temp_trend = 'falling'
    
    # Crop resistance modifiers (semi-relevant)
    resistance_level = data['crop_traits']['heat_resistance']
    adjusted_penalty = temp_penalty * (1.0 - resistance_level * 0.05)
    
    # Primary yield formula
    raw_potential = base_yield * elevation_factor * (1 + ph_influence)
    
    # Apply adjusted penalty
    final_potential = raw_potential * (1 - adjusted_penalty)
    
    # Additional distractor: unused irrigation logic
    irrigation_schedule = []
    for i, precip in enumerate(data['precipitation']):
        if precip < 3:
            irrigation_schedule.append((i, 10))  # mm to add
    # This schedule is computed but never applied
    
    # Final adjustment based on sunlight hours (simple arithmetic)
    sun_hours = data['sunlight_hours']
    light_efficiency = min(sun_hours / 8, 1.0)
    final_potential *= light_efficiency
    
    # Round to nearest integer
    return int(round(final_potential))

# Main execution
region_data = {
    'base_productivity': 85,
    'elevation': 420,
    'soil_samples': [
        {'pH': 6.2, 'nitrogen': 18},
        {'pH': 5.9, 'nitrogen': 20},
        {'pH': 6.4, 'nitrogen': 17},
        {'pH': 6.1, 'nitrogen': 19}
    ],
    'daily_temps': [18, 22, 19, 25, 28, 36, 34, 37, 35, 33, 29, 24, 21, 19, 17],
    'precipitation': [2, 0, 5, 12, 8, 1, 0, 3, 7, 9, 4, 2, 1, 0, 6],
    'sunlight_hours': 6.8,
    'crop_traits': {
        'heat_resistance': 6,
        'drought_tolerance': 4
    }
}

# Execute main logic
final_yield = calculate_harvest_potential(region_data)
Result: {final_yield}