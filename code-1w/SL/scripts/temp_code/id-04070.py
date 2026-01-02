def analyze_soil(reading):
    return (reading * 0.85) + 3.2

def assess_rainfall(amount):
    if amount < 20:
        return 0.5
    elif amount < 50:
        return 0.7
    else:
        return 1.0

def compute_growth(days, temp):
    base = 1.0
    for i in range(days):
        if temp > 30:
            base *= 1.02
        elif temp > 20:
            base *= 1.05
        else:
            base *= 0.98
    return base

def calculate_harvest(regions):
    total_yield = 0
    adjustment_factor = 0.9
    dummy_counter = 0
    unused_list = [0] * 100
    
    # Irrelevant pre-processing
    for i in range(len(unused_list)):
        unused_list[i] = (i * 1.5) % 7
        
    # Decoy dictionary with misleading metrics
    decoy_metrics = {
        'stress_index': 0,
        'fake_yield': 0,
        'phantom_rain': 0
    }
    
    for region in regions:
        soil_score = analyze_soil(region['soil'])
        rain_effect = assess_rainfall(region['rainfall'])
        growth_cycle = compute_growth(region['days'], region['temp'])
        
        # Real yield calculation
        raw_yield = soil_score * rain_effect * growth_cycle * region['area']
        
        # Distractor: updating decoy values
        decoy_metrics['stress_index'] += region['temp'] // 10
        decoy_metrics['fake_yield'] += raw_yield * 0.1
        decoy_metrics['phantom_rain'] += region['rainfall'] / 10
        
        # Only certain regions contribute significantly
        if region['zone'] in ['alpha', 'gamma']:
            total_yield += raw_yield * adjustment_factor
        else:
            total_yield += raw_yield * 0.3  # Reduced contribution
        
        # Dead code path: never executed due to logic
        dummy_counter += 1
        if dummy_counter < 0:
            total_yield -= 100

    # Additional red herring: complex but unused transformation
    inverted_map = {v: k for k, v in decoy_metrics.items()}
    secondary_adjustment = sum(inverted_map.keys()) if inverted_map else 0

    final_yield = int(total_yield - 50)
    return final_yield

# Setup data
regions_data = [
    {'soil': 60, 'rainfall': 65, 'days': 90, 'temp': 25, 'area': 120, 'zone': 'alpha'},
    {'soil': 45, 'rainfall': 15, 'days': 100, 'temp': 32, 'area': 80, 'zone': 'beta'},
    {'soil': 70, 'rainfall': 80, 'days': 85, 'temp': 22, 'area': 150, 'zone': 'gamma'},
    {'soil': 50, 'rainfall': 10, 'days': 110, 'temp': 18, 'area': 200, 'zone': 'delta'}
]

# Misleading preliminary analysis
preliminary = 0
for r in regions_data:
    preliminary += r['soil'] // r['temp'] if r['temp'] != 0 else 0

# Critical execution point
final_yield = calculate_harvest(regions_data)
print(f"Target result: {final_yield}")