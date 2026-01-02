import itertools

# Simulated agricultural yield optimization system
soil_samples = [0.45, 0.62, 0.58, 0.39, 0.71, 0.53]
precipitation_data = [120, 89, 145, 167, 95, 134]
temperature_readings = [22.1, 25.6, 23.8, 21.9, 26.3, 24.7]

def calculate_moisture_index(precip, temp):
    # Irrelevant helper with misleading intermediate
    base = precip / 100.0
    adjustment = max(0, 25 - temp) * 0.05
    return round(base + adjustment, 3)

def generate_grid_coordinates(rows, cols):
    # Distractor: unused coordinate generator
    return [(r, c) for r in range(rows) for c in range(cols)]

def analyze_soil_stability(samples):
    # Red herring function - not used in final logic
    avg = sum(samples) / len(samples)
    variance = sum((x - avg) ** 2 for x in samples) / len(samples)
    return variance < 0.02

def compute_growth_potential(soil, precip, temp):
    # Composite metric with partial relevance
    normalized_soil = sum(soil) / len(soil)
    moisture = calculate_moisture_index(sum(precip) / len(precip), sum(temp) / len(temp))
    thermal_factor = max(0.5, min(1.0, temp[0] / 25.0))
    return (normalized_soil * 0.4) + (moisture * 0.3) + (thermal_factor * 0.3)

# Unused data structures as distractors
equipment_status = {'tractor': 'active', 'drone': 'maintenance', 'sprayer': 'idle'}
maintenance_log = [
    {'date': '2023-06-01', 'action': 'calibration', 'cost': 120},
    {'date': '2023-06-08', 'action': 'repair', 'cost': 340}
]

# Core data structure - agricultural map with nested dictionaries
agricultural_map = {
    'zone_A': {'soil_quality': 0.61, 'crop_type': 'wheat', 'area_hectares': 12},
    'zone_B': {'soil_quality': 0.48, 'crop_type': 'barley', 'area_hectares': 8},
    'zone_C': {'soil_quality': 0.72, 'crop_type': 'oats', 'area_hectares': 15},
    'zone_D': {'soil_quality': 0.54, 'crop_type': 'wheat', 'area_hectares': 10}
}

# Thresholds dictionary - key input to actual computation
thresholds = {
    'minimum_soil': 0.55,
    'bonus_threshold': 0.70,
    'penalty_threshold': 0.50
}

# Decoy statistical analysis
historical_yields = [4.2, 4.5, 4.1, 4.8, 4.6, 4.3, 4.7]
projected_trend = sum(historical_yields[-3:]) / 3 * 1.02

# Complex multi-step evaluation with list comprehension and dict ops
def evaluate_harvest_quality(farm_map, limits):
    base_multiplier = 1.0
    bonus_applied = 0
    penalty_count = 0
    total_area = 0
    qualified_zones = []

    # Nested logic with filtering and transformation
    for zone_id, attributes in farm_map.items():
        soil_score = attributes['soil_quality']
        area = attributes['area_hectares']
        total_area += area
        
        # Relevant conditional branch
        if soil_score >= limits['minimum_soil']:
            if soil_score >= limits['bonus_threshold']:
                bonus_applied += 1
            qualified_zones.append(zone_id)
        elif soil_score < limits['penalty_threshold']:
            penalty_count += 1

    # Actual answer depends on this complex derived value
    base_yield = len(qualified_zones) * 1000
    area_adjusted_yield = base_yield * (total_area / 20)
    
    # Multiple modifiers with one actually affecting result
    modifier_chain = [
        1.1 if bonus_applied > 0 else 1.0,
        0.9 if penalty_count > 0 else 1.0,
        1.05 if len(qualified_zones) >= 3 else 1.0
    ]
    
    cumulative_modifier = 1.0
    for mod in modifier_chain:
        cumulative_modifier *= mod  # Only 1.05 matters due to conditions
    
    # Final calculation - only this line determines answer
    final_output = area_adjusted_yield * cumulative_modifier
    
    # Dead code path - never executed but looks important
    if False:
        fallback = sum(itertools.chain.from_iterable(
            [[v['soil_quality'] * v['area_hectares']] for k, v in farm_map.items()]
        ))
        final_output = fallback
    
    return int(final_output)

# Execution point of interest
final_yield = evaluate_harvest_quality(agricultural_map, thresholds)

# Print result as required
print(f"Result: {final_yield}")