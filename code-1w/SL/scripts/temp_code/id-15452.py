from collections import defaultdict, Counter

# Simulated agricultural zone data with multiple metrics
zone_data = [
    {'zone': 'A1', 'soil_q': 0.8, 'rainfall': 120, 'temp': 25, 'pests': True, 'crop': 'wheat'},
    {'zone': 'A2', 'soil_q': 0.9, 'rainfall': 140, 'temp': 27, 'pests': False, 'crop': 'corn'},
    {'zone': 'A3', 'soil_q': 0.6, 'rainfall': 100, 'temp': 24, 'pests': True, 'crop': 'wheat'},
    {'zone': 'B1', 'soil_q': 0.7, 'rainfall': 130, 'temp': 26, 'pests': False, 'crop': 'rice'},
    {'zone': 'B2', 'soil_q': 0.5, 'rainfall': 90, 'temp': 28, 'pests': True, 'crop': 'corn'}
]

# Irrelevant baseline constants (distractors)
BASE_YIELD_RICE = 5.0
MAX_PESTICIDE_EFFICIENCY = 0.95
TAX_RATE_AGRICULTURE = 0.07
DEPRECIATION_FACTOR = 0.88

# Misleading accumulator (dead-end computation)
total_depreciated_value = 0.0
for zone in zone_data:
    base = zone['soil_q'] * 100
    total_depreciated_value += base * DEPRECIATION_FACTOR

# Unused function - red herring
def compute_tax_liability(revenue):
    return revenue * TAX_RATE_AGRICULTURE

# Another decoy: pest resistance lookup (not actually used in final logic)
pest_resistance = {
    'wheat': 0.6,
    'corn': 0.4,
    'rice': 0.7
}

# Data transformation pipeline with relevant and irrelevant steps
processed_zones = []
crop_counter = Counter()
soil_quality_map = defaultdict(float)

for i, z in enumerate(zone_data):
    # Extract relevant features
    efficiency_score = (z['soil_q'] + min(z['rainfall'] / 150, 1.0)) / 2
    if z['temp'] < 25 or z['temp'] > 27:
        efficiency_score *= 0.8  # temperature penalty
    
    # Record crop frequency (used later)
    crop_counter[z['crop']] += 1
    
    # Store soil quality by index (partially used)
    soil_quality_map[f'{z["zone"]}-{i}'] = z['soil_q']
    
    # Flag pest-affected zones (used later)
    status = 'infested' if z['pests'] else 'clean'
    
    processed_zones.append({
        'id': z['zone'],
        'eff': efficiency_score,
        'status': status,
        'crop': z['crop']
    })

# Decoy statistical summary (never used)
avg_soil = sum(soil_quality_map.values()) / len(soil_quality_map)
median_rainfall = sorted([z['rainfall'] for z in zone_data])[len(zone_data)//2]

# Key intermediate structure: area_metrics
area_metrics = {
    'zones': processed_zones,
    'crop_dist': dict(crop_counter),
    'total_areas': len(zone_data),
    'region': 'north-east'
}

# Core calculation function with nested logic
def calculate_harvest_efficiency(metrics):
    zones = metrics['zones']
    crop_dist = metrics['crop_dist']
    
    # Irrelevant normalization (distraction)
    total_crops = sum(crop_dist.values())
    normalized_crops = {k: v/total_crops for k, v in crop_dist.items()}
    
    # Main accumulation
    base_yield = 0
    penalty_count = 0
    bonus_applied = False
    
    for z in zones:
        # Base contribution from efficiency
        base_yield += int(z['eff'] * 100)
        
        # Conditional penalty for infestation
        if z['status'] == 'infested':
            penalty_count += 1
        
        # Hidden bonus logic: only one bonus allowed
        if z['crop'] == 'corn' and not bonus_applied and z['status'] == 'clean':
            base_yield += 15
            bonus_applied = True
    
    # Apply penalty: 10 points per infested zone
    final_yield = base_yield - (penalty_count * 10)
    
    # Secret adjustment: if wheat appears exactly twice, add 5
    if crop_dist.get('wheat', 0) == 2:
        final_yield += 5
    
    # Dead code branch - never reached due to logic above
    if bonus_applied and penalty_count == 0 and crop_dist.get('rice') > 1:
        final_yield = int(final_yield * 1.1)
    
    return final_yield

# Execute main logic
final_yield = calculate_harvest_efficiency(area_metrics)

# Print result as required
print(f"Result: {final_yield}")