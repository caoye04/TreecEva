from itertools import compress, cycle

# Simulated agricultural zone data
zones = [f'Z{i}' for i in range(1, 21)]
base_productivity = [32, 45, 29, 67, 55, 38, 41, 50, 60, 48, 35, 44, 53, 62, 39, 47, 56, 65, 43, 51]
rainfall_score = [0.95, 1.02, 0.88, 1.15, 1.08, 0.93, 0.99, 1.05, 1.12, 1.00, 0.90, 0.97, 1.07, 1.18, 0.91, 1.01, 1.09, 1.16, 0.96, 1.04]
temperature_stress = [0.98, 1.01, 0.94, 1.03, 0.99, 0.96, 0.97, 1.00, 1.02, 0.98, 0.93, 0.95, 1.01, 1.04, 0.92, 0.99, 1.03, 1.06, 0.97, 1.00]

# Irrelevant sensor calibration data (distractor)
sensor_offsets = [0.02, -0.01, 0.03, 0.00, 0.05, -0.02, 0.04, 0.01, -0.03, 0.00]
active_sensors = list(compress(zones, [i % 2 == 0 for i in range(20)]))

# Decoy function: looks relevant but unused
def calculate_soil_health(zone_data):
    return sum(x * 0.7 for x in zone_data if x > 40)

# Efficiency modifiers from external model (simulated)
efficiency_factors = {
    z: round((rainfall_score[i] + temperature_stress[i]) / 2, 3)
    for i, z in enumerate(zones)
}

# Grid representation of land parcels (5x4)
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

# Phantom transformation chain (dead code path)
shifted_grid = [[(cell * 2) % 19 + 1 for cell in row] for row in grid]
doubled_coords = [(i*2, j*2) for i in range(len(grid)) for j in range(len(grid[0]))]

# Real efficiency map aligned with base productivity
efficiency_map = {f'Z{i+1}': efficiency_factors[f'Z{i+1}'] * base_productivity[i] for i in range(20)}

# Auxiliary masking function (partially used)
mask_low_yield = lambda val: val if val >= 45 else 0

# Complex accumulator with filtering and transformation
filtered_zones = []
accumulated_baseline = 0
for i, val in enumerate(base_productivity):
    adjusted = val * rainfall_score[i]
    if temperature_stress[i] < 0.98:
        adjusted *= 0.85
    accumulated_baseline += adjusted
    if adjusted >= 50:
        filtered_zones.append(f'Z{i+1}')

# Unused intermediate model state (red herring)
current_model_epoch = 17
learning_rate_decay = 0.96
epoch_snapshots = [round(accumulated_baseline * (learning_rate_decay ** e), 2) for e in range(current_model_epoch)]

# Core production aggregation logic
zone_lookup = {i+1: f'Z{i+1}' for i in range(20)}

def aggregate_production(parcel_grid, efficiency_lookup):
    total = 0
    for row_idx, row in enumerate(parcel_grid):
        # Row-specific multiplier based on depth
        depth_factor = 1 + (row_idx * 0.05)
        for parcel_id in row:
            zone_name = zone_lookup[parcel_id]
            raw_efficiency = efficiency_lookup[zone_name]
            # Apply dynamic field conditions
            stress_modifier = temperature_stress[parcel_id - 1]
            water_modifier = rainfall_score[parcel_id - 1]
            composite_modifier = (stress_modifier + water_modifier) / 2
            yield_contribution = raw_efficiency * composite_modifier * depth_factor
            # Only include if above threshold
            if yield_contribution >= 40:
                total += round(yield_contribution, 3)
    return int(total)

# Misleading diagnostic trace (looks important)
diagnostic_trace = []
for z in zones:
    fid = int(z[1:])
    temp = efficiency_map[z] * temperature_stress[fid-1]
    diag_entry = f'{z}:{round(temp, 2)}'
    diagnostic_trace.append(diag_entry)

# Key computation
final_yield = aggregate_production(grid, efficiency_map)
print(f'Target result: {final_yield}')