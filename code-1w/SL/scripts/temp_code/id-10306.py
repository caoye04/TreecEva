import itertools

# Simulated agricultural block data with moisture, nutrient, and sunlight levels
block_data = [
    {'moisture': 78, 'nutrients': 65, 'sunlight': 88, 'elevation': 120},
    {'moisture': 85, 'nutrients': 70, 'sunlight': 75, 'elevation': 135},
    {'moisture': 90, 'nutrients': 60, 'sunlight': 92, 'elevation': 110},
    {'moisture': 65, 'nutrients': 80, 'sunlight': 80, 'elevation': 140},
    {'moisture': 72, 'nutrients': 75, 'sunlight': 85, 'elevation': 128}
]

# Irrelevant transformation: elevation to letter grade (not used in final logic)
def elevation_to_grade(elev):
    if elev > 130:
        return 'B'
    elif elev > 120:
        return 'C'
    else:
        return 'A'

# Distractor function: calculates unused 'soil_score'
def compute_soil_score(block):
    base = block['nutrients'] * 0.7 + block['moisture'] * 0.3
    adjustment = 10 if block['elevation'] < 125 else -5
    return round(base + adjustment, 2)

# Misleading intermediate: normalizes sunlight but isn't ultimately decisive
def normalize_sunlight(value):
    return (value - 70) / 30

# Real processing: filter blocks by optimal growing conditions
def is_optimal(block):
    return (block['moisture'] >= 75 and 
            block['sunlight'] >= 85 and 
            block['nutrients'] >= 60)

# Auxiliary function: computes composite health index (used only for sorting)
def block_health(block):
    return (block['moisture'] * 0.3 + 
            block['nutrients'] * 0.3 + 
            block['sunlight'] * 0.4)

# Main processing pipeline
def preprocess_blocks(data):
    # Apply irrelevant grading (dead assignment)
    for b in data:
        grade = elevation_to_grade(b['elevation'])  # Dead variable
        score = compute_soil_score(b)                # Unused result

    # Sort by health but keep all blocks
    sorted_blocks = sorted(data, key=block_health, reverse=True)
    
    # Select only optimal blocks based on threshold criteria
    filtered = [b for b in sorted_blocks if is_optimal(b)]
    
    # Compute normalized sunlight for distraction
    for b in filtered:
        norm_light = normalize_sunlight(b['sunlight'])  # Computed but not used
    
    return filtered

# Complex yield calculation with bit manipulation red herring
def calculate_yield(block):
    base_yield = (block['moisture'] + block['sunlight']) / 2
    
    # Bit manipulation decoy: adjusts using unused flag
    quality_flag = 0b101
    if block['nutrients'] > 65:
        quality_flag |= 0b010  # This flag is never used
    adjusted = base_yield * (quality_flag & 0b111) / 5  # Deliberately misleading
    
    # Actual yield formula (overrides previous)
    actual_yield = base_yield * 1.2 + (block['nutrients'] - 60) * 0.8
    return actual_yield

# Optimization using itertools grouping (actual relevant usage)
def optimize_harvest(blocks):
    if not blocks:
        return 0.0
    
    # Group blocks by moisture tier (tens digit) - real logic step
    sorted_by_moisture = sorted(blocks, key=lambda b: b['moisture'] // 10)
    grouped = {k: list(g) for k, g in itertools.groupby(sorted_by_moisture, key=lambda b: b['moisture'] // 10)}
    
    max_group_yield = 0
    for tier, group in grouped.items():
        group_total = sum(calculate_yield(b) for b in group)
        if group_total > max_group_yield:
            max_group_yield = group_total
    
    # Final adjustment: apply efficiency multiplier based on group count
    efficiency_factor = len(grouped) * 0.9
    final_output = max_group_yield * efficiency_factor
    
    # Dead code path: this condition never triggers due to data constraints
    if efficiency_factor > 10:
        backup = sum(block_health(b) for b in blocks)
        final_output = backup  # Never reached
    
    return final_output

# Execution flow
processed_blocks = preprocess_blocks(block_data)
# Key statement: final_yield = optimize_harvest(processed_blocks)
final_yield = optimize_harvest(processed_blocks)

# Print result as required
print(f"Result: {final_yield}")