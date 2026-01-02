from collections import defaultdict
import itertools

# Simulate geothermal energy diffusion across layered earth strata
def initialize_strata(layers, base_temp):
    strata = defaultdict(float)
    for i in range(layers):
        strata[f'layer_{i}'] = base_temp + (i * 15) + 7 * (i % 3)
    return strata

# Irrelevant helper - simulates seismic noise (dead code path)
def generate_seismic_noise(duration):
    noise_profile = []
    for t in range(duration):
        noise_profile.append((t * 0.3) % 1.0)
    return noise_profile

# Unused transformation function (decoy)
def transform_coordinates(coord_list):
    transformed = [c * 1.618 % 100 for c in coord_list if c > 10]
    return sorted(transformed, reverse=True)[:5]

# Core heat distribution model
def build_flow_matrix(strata_dict, pressure):
    keys = sorted(strata_dict.keys())
    matrix = []
    for i, k1 in enumerate(keys):
        row = []
        for j, k2 in enumerate(keys):
            if i == j:
                flow = strata_dict[k1] * 0.8
            elif abs(i - j) == 1:
                flow = (strata_dict[k1] + strata_dict[k2]) * 0.1
            else:
                flow = 0.05 * (pressure / (abs(i - j) * 10))
            row.append(flow)
        matrix.append(row)
    return matrix

# Secondary log builder - partially relevant
def compile_conductivity_log(strata_count):
    log = []
    for i in range(strata_count):
        base_cond = 0.5 + (i % 4) * 0.2
        adjusted = base_cond * (1.1 + (i // 4) * 0.05)
        log.append(round(adjusted, 3))
        
        # Distractor computation (no effect on output)
        _ = [x**2 for x in range(i+1)]  # Dead list comprehension
        temp_offset = sum([base_cond / (k+1) for k in range(1, 5)])
    
    # Add decoy entry (never used later)
    log.append(999.999)
    return log[:-1]  # Correct slice ignores decoy

# Main calculation engine
def calculate_diffusion(matrix, cond_log):
    size = len(matrix)
    total_influence = 0.0
    
    # Cross-layer interaction grid
    for i in range(size):
        row_effect = 0
        col_effect = 0
        for j in range(size):
            weight = cond_log[min(i, j, len(cond_log)-1)]
            row_effect += matrix[i][j] * weight
            col_effect += matrix[j][i] * weight * 0.9
            
            # Misleading intermediate with side-effect-free ops
            _ = (i * j) ^ (i + j)  # Bitwise red herring
            
        # Accumulate diagonal dominance
        if i % 2 == 0:
            total_influence += row_effect * 0.7
        else:
            total_influence += col_effect * 0.4
    
    # Final non-linear scaling
    normalized = total_influence * 0.25 / (size * 0.3 + 1e-8)
    return round(normalized, 4)

# Orchestration sequence
if __name__ == "__main__":
    # Initialize geological structure
    strata_conditions = initialize_strata(7, 25)
    
    # Generate irrelevant data streams
    seismic_data = generate_seismic_noise(50)  # Not used later
    coords = [12, 15, 23, 45, 67, 89]
    processed_coords = transform_coordinates(coords)  # Dead assignment
    
    # Build core simulation components
    flow_matrix = build_flow_matrix(strata_conditions, pressure=220)
    conductivity_log = compile_conductivity_log(len(strata_conditions))
    
    # Critical computation step
    thermal_gradient = calculate_diffusion(flow_matrix, conductivity_log)
    
    # Distraction block: fake validation check
    validation_score = 0
    for v in strata_conditions.values():
        if v > 100:
            validation_score += 1
    # This score is never used
    
    # Output only the required result
    print(f"Result: {thermal_gradient}")