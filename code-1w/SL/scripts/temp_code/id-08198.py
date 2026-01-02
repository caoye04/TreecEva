import itertools

# Simulated sensor array data (flux readings across time and sectors)
sensor_readings = [
    [14, 17, 23, 15, 19],
    [21, 18, 20, 22, 16],
    [25, 24, 13, 19, 27],
    [18, 20, 23, 21, 14],
    [16, 19, 17, 25, 22]
]

# Irrelevant auxiliary data - red herring (thermal calibration offsets not used in final logic)
thermal_offsets = [[(i + j) * 0.1 for j in range(5)] for i in range(5)]
offset_correction_factor = sum(sum(row) for row in thermal_offsets)  # Dead computation

# Sector classification map (real-world zone types)
sector_types = ['core', 'edge', 'core', 'rim', 'edge']
zone_weights = {'core': 1.2, 'edge': 0.9, 'rim': 0.7}

# Misleading intermediate transformation (never actually used)
decoy_weights = [zone_weights[stype] * 1.1 for stype in sector_types]
decoy_matrix = [[val * 0.95 for val in row] for row in sensor_readings]

# Real processing begins here
scaling_table = {i: (i % 3 + 1) * 0.8 for i in range(5)}  # Time-step dependent scaling

# Apply non-uniform scaling using enumerate
transformed_data = []
for idx, row in enumerate(sensor_readings):
    scaled_row = []
    for val in row:
        scaled_val = val * scaling_table[idx]
        scaled_row.append(scaled_val)
    transformed_data.append(scaled_row)

# Create threshold map based on dynamic criteria
threshold_map = {}
for i, stype in enumerate(sector_types):
    base_threshold = 18.0
    if stype == 'core':
        threshold_map[i] = base_threshold * 1.1
    elif stype == 'edge':
        threshold_map[i] = base_threshold * 0.95
    else:
        threshold_map[i] = base_threshold

# Decoy function - looks important but unused
def compute_bias_factor(data_matrix):
    total = 0
    for row in data_matrix:
        for x in row:
            total += x ** 0.5
    return total / 1000.0

bias_score = compute_bias_factor(sensor_readings)  # Red herring variable

# Real calculation function with nested logic
def calculate_sector_flux(data_block, thresh_map):
    flux_values = []
    for row_idx, row in enumerate(data_block):
        row_flux = 0
        for col_idx, val in enumerate(row):
            base_thresh = thresh_map[col_idx]
            if val > base_thresh:
                deviation = val - base_thresh
                # Nonlinear response curve
                contribution = deviation ** 1.2
                if col_idx % 2 == 0:
                    contribution *= 1.15
                else:
                    contribution *= 0.85
                row_flux += contribution
            else:
                # Below threshold still contributes weakly
                row_flux += (base_thresh - val) * -0.1  # Small negative contribution
        flux_values.append(row_flux)
    return flux_values

# Secondary transformation using zip and itertools
temp_transposed = list(zip(*transformed_data))
smoothed_blocks = []
for block in temp_transposed:
    smoothed = []
    for a, b, c in itertools.zip_longest(block, [x*0.98 for x in block], [x*1.02 for x in block], fillvalue=0):
        smoothed.append((a + b + c) / 3.0 if a != 0 else 0)
    smoothed_blocks.append(smoothed)

refined_data = list(zip(*smoothed_blocks))  # Transpose back

# Final flux calculation function
def calculate_net_flux(processed_data, thresholds):
    sector_fluxes = calculate_sector_flux(processed_data, thresholds)
    composite_score = 0
    
    # Weighting by position importance
    for i, flux in enumerate(sector_fluxes):
        weight = 1.0
        if i == 0:
            weight = 1.3
        elif i == len(sector_fluxes) - 1:
            weight = 0.8
        else:
            weight = 1.0 + (i * 0.1)
        
        # Complex interaction term
        interaction = 0
        for j in range(len(sector_fluxes)):
            if i != j:
                interaction += (sector_fluxes[i] * sector_fluxes[j]) * 0.01
        
        composite_score += (flux * weight) + interaction
    
    # Normalize by number of active sectors
    active_count = sum(1 for f in sector_fluxes if f > 5.0)
    if active_count > 0:
        composite_score /= active_count
    else:
        composite_score = 0
    
    # Final nonlinear compression
    if composite_score > 0:
        composite_score = (composite_score ** 0.95) * 1.05
    else:
        composite_score = composite_score * 0.9
    
    return composite_score

# Execute main computation
final_flux = calculate_net_flux(transformed_data, threshold_map)

# Print result as required
print(f"Target result: {final_flux}")