from collections import defaultdict, Counter

# Simulated land block data with soil types and moisture levels
block_data = [
    {'id': 'A1', 'soil': 'clay', 'moisture': 0.6, 'temp': 22, 'yield_potential': 85},
    {'id': 'B2', 'soil': 'loam', 'moisture': 0.7, 'temp': 25, 'yield_potential': 93},
    {'id': 'C3', 'soil': 'sand', 'moisture': 0.4, 'temp': 27, 'yield_potential': 70},
    {'id': 'D4', 'soil': 'loam', 'moisture': 0.8, 'temp': 24, 'yield_potential': 97},
    {'id': 'E5', 'soil': 'clay', 'moisture': 0.5, 'temp': 23, 'yield_potential': 80}
]

# Irrelevant weather log (distractor)
weather_log = {
    'day_1': {'precip': 12, 'wind': 8},
    'day_2': {'precip': 0, 'wind': 15},
    'day_3': {'precip': 22, 'wind': 5}
}

# Mapping soil types to base nutrient score (used later)
soil_nutrient_base = {
    'clay': 7,
    'loam': 9,
    'sand': 5
}

# Spurious transformation: unused in final logic
transformed_blocks = []
for block in block_data:
    transformed = {**block}
    transformed['adjusted_yield'] = block['yield_potential'] * (block['moisture'] + 0.1)
    transformed_blocks.append(transformed)

# Distractor function: looks relevant but not used
def predict_rainfall_impact(blocks):
    total = 0
    for b in blocks:
        if b['soil'] == 'sand':
            total += b['yield_potential'] * 0.3
    return total

# Another red herring: calculates something unrelated
sensor_variance = sum((b['temp'] - 24)**2 for b in block_data) / len(block_data)

# Real processing begins: filter viable blocks based on moisture threshold
viable_blocks = [b for b in block_data if b['moisture'] >= 0.55]

# Compute average temperature of viable blocks (used in optimization)
avg_temp_viable = sum(b['temp'] for b in viable_blocks) / len(viable_blocks)

# Efficiency map: maps block ID to efficiency factor using multiple criteria
efficiency_map = defaultdict(float)
for block in viable_blocks:
    base_eff = soil_nutrient_base[block['soil']]
    temp_factor = 1.0 if 23 <= block['temp'] <= 26 else 0.85
    moisture_factor = 1.0 + (block['moisture'] - 0.6) * 0.5
    efficiency_map[block['id']] = round(base_eff * temp_factor * moisture_factor, 3)

# Unused alternative calculation path (dead code path)
candidate_selections = []
for k, v in efficiency_map.items():
    if v > 8.0:
        candidate_selections.append(k)

# Primary data structure transformation: tuple packing
processed_blocks = []
for block in viable_blocks:
    key_attrs = (
        block['id'],
        block['yield_potential'],
        efficiency_map[block['id']],
        (block['yield_potential'] * efficiency_map[block['id']]) / 10
    )
    processed_blocks.append(key_attrs)

# Decoy aggregation using set operations (irrelevant)
distinct_soils = set()
for b in block_data:
    distinct_soils.add(b['soil'])
distinct_yield_set = {int(b['yield_potential']) for b in block_data}
overlap_check = distinct_soils & {'silt', 'peat'}  # empty, misleading

# Simulated pest resistance scores (unused)
pest_resistance = dict(zip(['A1','B2','C3','D4','E5'], [0.88, 0.91, 0.76, 0.84, 0.90]))

# Core optimization algorithm (depends on processed_blocks and efficiency_map)
def optimize_harvest(blocks, efficiency_lookup):
    total_yield = 0.0
    for block_id, base_yield, eff_score, bonus in blocks:
        # Additional filtering: only high-efficiency blocks contribute fully
        if efficiency_lookup[block_id] >= 8.0:
            contribution = base_yield * (eff_score / 7.5)
        else:
            contribution = base_yield * 0.65  # reduced yield
        # Non-linear adjustment based on bonus component
        adjusted_contribution = contribution * (1 + (bonus / 100))
        total_yield += adjusted_contribution
    # Final environmental tax
    total_yield *= (0.97 + (avg_temp_viable - 23) * 0.01)
    return round(total_yield, 4)

# Execute main computation
final_yield = optimize_harvest(processed_blocks, efficiency_map)

# Print result as required
print(f"Target result: {final_yield}")