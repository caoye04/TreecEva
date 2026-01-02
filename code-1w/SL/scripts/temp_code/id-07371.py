def analyze_growth_rate(temp, rainfall):
    # Irrelevant helper function that isn't used in final calculation
    return (temp * 0.3) + (rainfall * 0.7)

# Simulate agricultural yield prediction across multiple regions
regions = ['north', 'south', 'east', 'west']
soil_quality = {'north': 0.8, 'south': 0.5, 'east': 0.9, 'west': 0.6}
temp_data = {'north': 22, 'south': 28, 'east': 24, 'west': 26}
rainfall_data = {'north': 120, 'south': 80, 'east': 140, 'west': 100}

# Distractor variables - not used in final result
unused_baseline_yield = 350
phantom_region_factor = 0.05
adjustment_log = []

# Lambda for irrelevant transformation
moisture_index = lambda rain: round(rain / 10.0, 2)
moisture_values = {r: moisture_index(rainfall_data[r]) for r in regions}

# Tracking growth stages (some values are unused)
growth_stage_multiplier = {
    'early': 0.3,
    'mid': 0.6,
    'mature': 1.0
}

# Real computation begins here
base_yield_per_region = {}
for region in regions:
    base_yield = 0
    if soil_quality[region] >= 0.7:
        base_yield += 200
    elif soil_quality[region] >= 0.5:
        base_yield += 150
    else:
        base_yield += 100
    
    # Add climate adjustment (only temperature matters in this logic)
    if temp_data[region] > 25:
        base_yield *= 0.9  # Slight heat stress
    elif temp_data[region] < 23:
        base_yield *= 0.95  # Suboptimal cold
    else:
        base_yield *= 1.05  # Ideal range
        
    base_yield_per_region[region] = int(base_yield)

# Unused aggregation - red herring
average_moisture = sum(moisture_values.values()) / len(moisture_values)

# Actual yield calculation using only soil quality and base yields
weighted_sum = 0
total_weight = 0
for reg in regions:
    weight = soil_quality[reg]
    weighted_sum += base_yield_per_region[reg] * weight
    total_weight += weight

def calculate_harvest(reg_list, sq_dict):
    # Final calculation depends only on weighted average by soil quality
    yield_sum = 0
    count = 0
    for r in reg_list:
        adj_yield = base_yield_per_region[r] * (sq_dict[r] / 0.5)  # Normalize by 0.5
        yield_sum += adj_yield
        count += 1
    return int(yield_sum / count)  # Average adjusted yield

# Key execution point
final_yield = calculate_harvest(regions, soil_quality)

# Log some irrelevant info
adjustment_log.append(f'Processed {len(regions)} regions')

# Print result as required
print(f"Result: {final_yield}")