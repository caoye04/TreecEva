from itertools import combinations

def analyze_soil_quality(plots):
    # Irrelevant helper: computes average pH (not used in final result)
    total_ph = 0
    count = 0
    for plot in plots:
        for sensor_readings in plot['soil_data']:
            total_ph += sum(sensor_readings)
            count += len(sensor_readings)
    return total_ph / count if count else 0

def calculate_max_stress_factor(plots):
    # Distractor function: calculates max drought stress (never called)
    max_stress = 0
    for plot in plots:
        stress = sum(plot['drought_days']) * 0.3
        if stress > max_stress:
            max_stress = stress
    return max_stress

def calculate_optimal_harvest(plots):
    base_yield = 0
    bonus_multiplier = 1.0
    penalty_applied = False
    
    # Real logic begins: only plots with sufficient sunlight qualify
    valid_plots = []
    for plot in plots:
        if plot['sunlight_hours'] >= 6:
            valid_plots.append(plot)
    
    # Use itertools to explore pairs for synergy bonus
    for p1, p2 in combinations(valid_plots, 2):
        if abs(p1['moisture_level'] - p2['moisture_level']) < 5:
            bonus_multiplier += 0.05  # Synergy between similar moisture plots
    
    # Accumulate base yield from valid plots
    for plot in valid_plots:
        base_yield += plot['crop_count'] * 10
        
        # Apply pest penalty if detected (affects only some plots)
        if plot['pest_detected'] and not penalty_applied:
            base_yield -= 15
            penalty_applied = True  # Only apply once
    
    # Dead code block: never reached due to structure, but looks relevant
    if bonus_multiplier > 2.0:
        extra_boost = base_yield * 0.1
        base_yield += int(extra_boost)
    
    # Final calculation
    final_yield = int(base_yield * bonus_multiplier)
    return final_yield

# Main data setup
plots = [
    {
        'crop_count': 8,
        'sunlight_hours': 7,
        'moisture_level': 42,
        'pest_detected': False,
        'drought_days': [3, 1, 4],
        'soil_data': [[6.2, 6.4], [6.3, 6.1]]
    },
    {
        'crop_count': 5,
        'sunlight_hours': 4,  # Below threshold, excluded
        'moisture_level': 40,
        'pest_detected': True,
        'drought_days': [5, 5],
        'soil_data': [[5.9, 6.0]]
    },
    {
        'crop_count': 12,
        'sunlight_hours': 8,
        'moisture_level': 45,
        'pest_detected': True,
        'drought_days': [2],
        'soil_data': [[6.5, 6.7, 6.6]]
    },
    {
        'crop_count': 7,
        'sunlight_hours': 6,
        'moisture_level': 43,
        'pest_detected': False,
        'drought_days': [0],
        'soil_data': [[6.0, 6.1]]
    }
]

# Execute main logic
analyze_soil_quality(plots)  # Called but result ignored
max_stress = calculate_max_stress_factor(plots)  # Computed but unused
final_yield = calculate_optimal_harvest(plots)
print(f"Result: {final_yield}")