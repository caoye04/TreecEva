from itertools import combinations, chain

# Simulation of agricultural land blocks with various soil metrics
soil_quality = [0.78, 0.91, 0.63, 0.85, 0.72, 0.55, 0.49, 0.67]
moisture_levels = [0.62, 0.77, 0.51, 0.88, 0.69, 0.53, 0.44, 0.61]
elevation_data = [121, 142, 118, 135, 129, 112, 105, 119]
temperature_zones = [22.3, 23.1, 21.8, 24.0, 22.7, 21.2, 20.9, 22.0]

# Irrelevant preprocessing: dummy transformation on unused data
shifted_temps = [t - 20 for t in temperature_zones if t > 21]
dummy_pairs = list(combinations(shifted_temps, 2))

# Distractor function: looks useful but not used in main logic
def calculate_irrigation_cost(moisture_list):
    base = sum(m * 1.5 for m in moisture_list)
    return base * 0.8 if base > 3 else base * 1.1

# Another red herring: complex elevation normalization (unused)
normalized_elev = [(e - min(elevation_data)) / (max(elevation_data) - min(elevation_data)) for e in elevation_data]
slope_adjustment = [abs(e - 120) / 20 for e in elevation_data]

# Core processing begins here
fertility_index = [
    (soil_quality[i] * 0.6 + moisture_levels[i] * 0.4) * (1 + 0.001 * abs(125 - elevation_data[i]))
    for i in range(len(soil_quality))
]

# Simulate seasonal decay factors (distraction with partial usage)
seasonal_decay = [0.95, 0.92, 0.97, 0.94]
current_decay = seasonal_decay[1]  # Only one used

adjusted_fertility = [f * current_decay for f in fertility_index]

# Generate all possible 3-block farming patterns (combinatorics)
block_indices = list(range(len(adjusted_fertility)))
valid_triplets = list(combinations(block_indices, 3))

# Filter triplets based on spatial continuity heuristic (non-adjacent filtered)
spatial_threshold = 2
continuous_triplets = [
    t for t in valid_triplets 
    if max(t) - min(t) <= spatial_threshold and len(set([abs(t[i]-t[i+1]) for i in range(2)])) == 1
]

# Compute yield estimates for each valid triplet
triplet_yields = []
for triplet in continuous_triplets:
    base_yield = sum(adjusted_fertility[i] for i in triplet)
    diversity_bonus = 0.05 if len(set(round(adjusted_fertility[i], 1) for i in triplet)) == 3 else 0
    penalty = 0.08 if any(adjusted_fertility[i] < 0.55 for i in triplet) else 0
    triplet_yields.append(base_yield + diversity_bonus - penalty)

# Processed blocks: only specific configuration survives
if triplet_yields:
    avg_yield = sum(triplet_yields) / len(triplet_yields)
    max_possible = max(triplet_yields)
    efficiency_ratio = avg_yield / max_possible

    # Key transformation step
    processed_blocks = [
        y for y in triplet_yields 
        if y >= avg_yield and (y * efficiency_ratio) > 0.4
    ]
else:
    processed_blocks = [0.5]

# Decoy statistical analysis (dead code path)
if len(processed_blocks) > 10:
    mean_block = sum(processed_blocks) / len(processed_blocks)
    variance = sum((x - mean_block) ** 2 for x in processed_blocks)
    std_dev = variance ** 0.5

# Real computation path
scaling_factor = 1.75 if len(processed_blocks) % 2 == 1 else 1.6

# Optimization function with conditional expression
def optimize_harvest(blocks):
    total = sum(b ** 1.1 for b in blocks)
    adjustment = 1.2 if total > 5 else 0.95
    # Use itertools.chain to flatten hypothetical nested results (overkill, but plausible)
    chained = list(chain.from_iterable([(b * adjustment,) for b in blocks]))
    return sum(chained) * scaling_factor

# Final computation
final_yield = optimize_harvest(processed_blocks)

# Distraction: unused alternative model
theoretical_model = [
    (fertility_index[i] * 1.1 + moisture_levels[i] * 0.3) * scaling_factor 
    for i in range(len(fertility_index))
    if elevation_data[i] > 115
]

# Print result as required
print(f"Result: {final_yield}")