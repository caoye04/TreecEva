import itertools

# Simulated agricultural block data with moisture, nutrient, and pH levels
block_data = [
    {'moisture': 72, 'nutrients': 45, 'ph': 6.3, 'elevation': 105},
    {'moisture': 68, 'nutrients': 52, 'ph': 5.9, 'elevation': 112},
    {'moisture': 74, 'nutrients': 38, 'ph': 6.5, 'elevation': 108},
    {'moisture': 65, 'nutrients': 58, 'ph': 6.1, 'elevation': 115},
    {'moisture': 70, 'nutrients': 41, 'ph': 6.7, 'elevation': 103}
]

# Irrelevant auxiliary mapping (distractor)
elevation_zone_map = {100: 'low', 105: 'mid', 110: 'high', 115: 'peak'}
zone_multiplier = {'low': 0.9, 'mid': 1.0, 'high': 1.1, 'peak': 1.05}

# Preprocessing: filter blocks by acceptable pH range (6.0-6.6) and sort by nutrients
filtered_blocks = [b for b in block_data if 6.0 <= b['ph'] <= 6.6]
sorted_blocks = sorted(filtered_blocks, key=lambda x: x['nutrients'])

# Extract nutrient levels for combinatorial analysis (only relevant subset)
nutrient_levels = [b['nutrients'] for b in sorted_blocks]

# Generate all pairs of nutrient values to compute interaction deltas (red herring)
nutrient_pairs = list(itertools.combinations(nutrient_levels, 2))
interaction_deltas = [abs(p[0] - p[1]) for p in nutrient_pairs]
mean_delta = sum(interaction_deltas) / len(interaction_deltas) if interaction_deltas else 0

# Misleading transformation: elevation-based weighting (unused in final logic)
elevation_weights = {}
for block in block_data:
    zone = elevation_zone_map.get(block['elevation'] // 5 * 5, 'mid')
    elevation_weights[block['elevation']] = zone_multiplier[zone] * 1.1  # dead computation

# Real processing path begins here
moisture_sum = sum(b['moisture'] for b in sorted_blocks)
avg_moisture = moisture_sum / len(sorted_blocks) if sorted_blocks else 0

# Apply non-linear yield response to moisture (logarithmic scaling)
moisture_yield_factor = 10 * (1 + (avg_moisture - 60) / 100) ** 2

# Compute base productivity from nutrients using harmonic mean (resistant to outliers)
total_inv = sum(1 / max(n, 1) for n in nutrient_levels)
harmonic_nutrients = len(nutrient_levels) / total_inv if total_inv > 0 else 0
nutrient_yield_factor = harmonic_nutrients * 0.7

# Combine factors with diminishing returns
combined_score = (moisture_yield_factor ** 0.5) * (nutrient_yield_factor ** 0.5)

# Simulate experimental treatment groups (distractor - unused)
treatment_groups = list(itertools.product(['A', 'B'], [1, 2]))
sham_result = []
for t in treatment_groups:
    sham_value = (t[1] * 17) % 9
    sham_result.append(sham_value)  # dead end

# Actual yield optimization function
def optimize_harvest(blocks):
    if not blocks:
        return 0
    
    # Extract elevations for variance calculation (irrelevant to output)
    elevations = [b['elevation'] for b in blocks]
    elev_mean = sum(elevations) / len(elevations)
    elev_variance = sum((e - elev_mean) ** 2 for e in elevations) / len(elevations)  # unused
    
    # Core logic: weighted sum of moisture and nutrients with fixed coefficients
    total_yield = 0
    for idx, b in enumerate(blocks):
        moisture_contrib = b['moisture'] * 0.6
        nutrient_contrib = b['nutrients'] * 0.9
        # pH correction factor: peak at 6.3, falls off quadratically
        ph_deviation = (b['ph'] - 6.3) ** 2
        ph_factor = max(0, 1 - ph_deviation * 2)
        block_yield = (moisture_contrib + nutrient_contrib) * ph_factor
        total_yield += block_yield
        
        # Early termination red herring (never triggers due to data)
        if b['nutrients'] > 60 and b['moisture'] < 50:
            return -1  # unreachable
            
    # Final adjustment based on block count (scaling effect)
    scale_bonus = len(blocks) * 3.5
    return int(total_yield + scale_bonus)

# Additional decoy function
def calculate_erosion_risk(data):
    risk_score = 0
    for d in data:
        risk_score += d['elevation'] % 7
    return risk_score * 0.3  # never called

# Process only high-nutrient blocks above median (actual input to optimizer)
median_nutrients = sorted(nutrient_levels)[len(nutrient_levels)//2]
processed_blocks = [b for b in sorted_blocks if b['nutrients'] >= median_nutrients]

# Critical statement
final_yield = optimize_harvest(processed_blocks)

print(f"Result: {final_yield}")