def analyze_soil_composition(elements):
    # Irrelevant computation: calculates trace minerals but not used in final result
    trace_minerals = sum([v * 0.05 for v in elements.values() if v > 10])
    ph_balance = (elements.get('calcium', 0) + elements.get('magnesium', 0)) / 2
    return ph_balance

region_data = [
    {'area': 'north', 'crop': 'wheat', 'soil': {'nitrogen': 80, 'phosphorus': 45, 'potassium': 30, 'calcium': 60, 'magnesium': 50}},
    {'area': 'south', 'crop': 'barley', 'soil': {'nitrogen': 70, 'phosphorus': 55, 'potassium': 35, 'calcium': 75, 'magnesium': 40}},
    {'area': 'east', 'crop': 'oats', 'soil': {'nitrogen': 90, 'phosphorus': 40, 'potassium': 25, 'calcium': 65, 'magnesium': 55}},
    {'area': 'west', 'crop': 'rye', 'soil': {'nitrogen': 85, 'phosphorus': 50, 'potassium': 40, 'calcium': 70, 'magnesium': 45}}
]

# Misleading global variable (not directly used)
total_farms = len(region_data)
decay_factor = 0.92

# Helper function that appears important but only partially contributes
def compute_risk_assessment(data_list):
    risk_scores = []
    for entry in data_list:
        base_risk = 100
        if entry['soil']['phosphorus'] < 50:
            base_risk -= 15
        if entry['soil']['potassium'] < 30:
            base_risk -= 10
        # Dead code path - never executed due to logic
        if False and entry['crop'] == 'maize':
            base_risk += 20
        risk_scores.append(base_risk)
    return risk_scores  # Not used in final calculation

# Main computation with distractors
baseline_multiplier = 2.5
adjustment_map = {entry['area']: entry['soil']['nitrogen'] * 0.1 for entry in region_data}

# List comprehension combining multiple soil metrics (some irrelevant)
nutrient_index = [
    (item['soil']['nitrogen'] * 0.4 + 
     item['soil']['phosphorus'] * 0.3 + 
     item['soil']['potassium'] * 0.2 + 
     sum(item['soil'].get(oligo, 0) for oligo in ['iron', 'zinc', 'copper']) * 0.01)  # Always zero
    for item in region_data
]

# Simulated growth cycle stages (only last stage matters)
current_stage = 1
max_stages = 3
stage_multiplier = 1.0
while current_stage <= max_stages:
    if current_stage == 2:
        stage_multiplier *= 1.1
    elif current_stage == 3:
        stage_multiplier *= 1.15
    current_stage += 1

# Core yield calculation
yield_per_region = []
for region in region_data:
    soil = region['soil']
    # Real contribution: balanced fertility index
    fertility = (soil['nitrogen'] * 0.4 + soil['phosphorus'] * 0.4 + soil['potassium'] * 0.2)
    # Adjusted by area-specific factor
    adjustment = adjustment_map[region['area']]
    # Final regional yield before stage scaling
    yield_per_region.append(fertility * baseline_multiplier * (1 + adjustment / 100))

# Aggregate total potential
aggregate_yield = sum(yield_per_region)

# Secondary processing chain (distractor)
soil_ph_levels = [analyze_soil_composition(r['soil']) for r in region_data]
avg_ph = sum(soil_ph_levels) / len(soil_ph_levels)

# Final harvest potential incorporates stage multiplier only
final_yield = aggregate_yield * stage_multiplier

# Print result for verification
print(f"Result: {final_yield}")