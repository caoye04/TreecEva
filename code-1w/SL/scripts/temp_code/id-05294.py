from itertools import combinations

# Agricultural yield optimization with environmental factors
soil_types = ['clay', 'loam', 'sand', 'silt']
decay_rates = {'clay': 0.02, 'loam': 0.01, 'sand': 0.03, 'silt': 0.015}
base_productivity = {'clay': 70, 'loam': 100, 'sand': 60, 'silt': 80}
temperature_zones = [22, 25, 20, 24, 26, 19]

# Irrelevant sensor calibration data (distractor)
sensor_offsets = [0.12, 0.15, 0.08, 0.21, 0.11, 0.09]
calibration_matrix = [[0.98 + i*0.01 for i in range(6)] for _ in range(4)]

# Rainfall data over 12 months (some irrelevant)
rainfall_mm = [80, 120, 140, 100, 60, 40, 30, 50, 90, 110, 130, 95]
seasonal_multiplier = {'dry': 0.7, 'wet': 1.3, 'normal': 1.0}
monthly_weights = [seasonal_multiplier['wet']] * 3 + [seasonal_multiplier['normal']] * 6 + [seasonal_multiplier['dry']] * 3

# Simulated region configurations (only first 3 used)
regions = [
    {'id': 'R1', 'soil': 'loam', 'area': 500, 'microclimate': 22},
    {'id': 'R2', 'soil': 'clay', 'area': 300, 'microclimate': 25},
    {'id': 'R3', 'soil': 'silt', 'area': 400, 'microclimate': 20},
    {'id': 'R4_unused', 'soil': 'sand', 'area': 600, 'microclimate': 28},  # Dead region
    {'id': 'R5_unused', 'soil': 'loam', 'area': 200, 'microclimate': 18}   # Dead region
]

# Efficiency map with decoy entries
efficiency_map = {
    'loam': lambda x: x * 1.2,
    'clay': lambda x: x * 0.9,
    'silt': lambda x: x * 1.1,
    'sand': lambda x: x * 0.7,
    'pebbles': lambda x: x * 0.1  # Decoy soil type never used
}

# Historical yield trends (irrelevant data)
historical_yields = [
    [95, 98, 102, 97, 105, 101],
    [72, 70, 68, 73, 75, 71],
    [83, 85, 80, 88, 82, 86]
]

# Unused helper function (red herring)
def calculate_irrigation_cost(area, rainfall):
    total_water_needed = area * 1000  # liters per hectare
    supplied = sum(rainfall) * 0.6
    deficit = max(0, total_water_needed - supplied)
    return deficit * 0.002  # cost per liter

# Complex preprocessing with slicing and filtering (partially relevant)
trimmed_rainfall = rainfall_mm[1:-1]  # Remove first and last month
weighted_rainfall = [r * w for r, w in zip(trimmed_rainfall, monthly_weights[1:-1])]
avg_effective_rainfall = sum(weighted_rainfall) / len(weighted_rainfall)

# Environmental adjustment factor computed but only partially used
env_factor = 1.0
if avg_effective_rainfall > 90:
    env_factor *= 1.05
elif avg_effective_rainfall < 60:
    env_factor *= 0.95

for zone_temp in temperature_zones[:4]:  # Only first 4 zones affect result
    if zone_temp > 24:
        env_factor *= 0.98
    elif zone_temp < 21:
        env_factor *= 0.97

# Core computation disguised among distractions
def compute_base_yield(region):
    soil = region['soil']
    area = region['area']
    base = base_productivity[soil]
    decay = decay_rates[soil]
    # Simulate 3-year decay effect
    yield_after_decay = base * ((1 - decay) ** 3)
    return yield_after_decay * area

def optimize_harvest(regions, efficiency_map):
    total = 0.0
    count = 0
    for region in regions:
        # Skip unused regions based on id (control flow distraction)
        if 'unused' in region['id']:
            continue
        
        raw_yield = compute_base_yield(region)
        soil_type = region['soil']
        
        # Apply efficiency function from map
        if soil_type in efficiency_map:
            optimized = efficiency_map[soil_type](raw_yield)
        else:
            optimized = raw_yield
        
        # Microclimate adjustment (only for active regions)
        temp_adj = 1.0
        if region['microclimate'] > 23:
            temp_adj = 0.96
        elif region['microclimate'] < 21:
            temp_adj = 0.94
        
        final_region_yield = optimized * temp_adj
        total += final_region_yield
        count += 1
    
    # Spurious combination logic (distractor - not used)
    if count > 2:
        possible_combinations = list(combinations(range(count), 2))
        diversity_bonus = len(possible_combinations) * 0.01
        total *= (1 + diversity_bonus * 0.0)  # Neutralized bonus (decoy)
    
    return total

# Execute main logic
intermediate_debug = [compute_base_yield(r) for r in regions[:3]]
baseline_total = sum(intermediate_debug)
optimized_total = optimize_harvest(regions, efficiency_map)

# Final adjustment using environmental factor (only partial relevance)
final_yield = optimized_total * env_factor

# Print result as required
print(f"Target result: {final_yield}")