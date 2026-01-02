import math

# Irrelevant helper function (dead code path)
def unused_signal_transform(data):
    return [math.sin(x) * 0.5 for x in data if x > 0]

# Misleading intermediate calculation with decoy result
decoherence_value = sum([i * i for i in range(7)]) // 3  # Looks important, never used

# Calibration reference table (partially relevant, partially distracting)
calibration_map = {
    'alpha': 0.23, 'beta': 0.45, 'gamma': 0.67,
    'delta': 0.89, 'epsilon': 1.01, 'zeta': 1.23
}

# Unused signal weights
echo_weights = [0.1, 0.3, 0.5, 0.7, 0.9]

# Primary grid state input (relevant)
grid_state = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Auxiliary noise mask (distractor)
noise_mask = [[(i + j) % 2 for j in range(4)] for i in range(4)]

# Bitwise interference pattern (red herring)
interference_flag = (len(grid_state) << 2) ^ 0xF

# Conditional calibration factor assignment (relevant branch)
size_factor = len(grid_state)
calibration_factor = calibration_map['gamma'] if size_factor == 4 else calibration_map['delta']

# Spurious list comprehension with side-effect-free mutation
cleansed_grid = [
    [cell | (cell & 1) for cell in row] 
    for row in grid_state
]

# Dummy accumulator for distraction
temporal_accumulator = 0
for cycle in range(3):
    temporal_accumulator += sum(noise_mask[cycle]) * (cycle + 1)

# Core calculation function with nested logic
def calculate_thermal_response(state, calib):
    total_energy = 0
    response_curve = []
    
    for i, row in enumerate(state):
        row_sum = 0
        for j, cell in enumerate(row):
            # Physics-inspired weight: distance from center
            dist_sq = (i - 1.5)**2 + (j - 1.5)**2
            weight = math.exp(-dist_sq / 2.0)
            
            # Conditional excitation logic
            excitation = cell * (calib * weight) if cell else 0.0
            row_sum += excitation
            
            # Append to curve (used later)
            response_curve.append(excitation if excitation > 0.1 else 0)
        
        total_energy += row_sum * (i + 1)
    
    # Secondary transformation on curve
    filtered = [x for x in response_curve if x > 0]
    
    # Final aggregation using harmonic mean concept
    if filtered:
        harmonic_input = [1.0 / x for x in filtered]
        harmonic_mean = len(filtered) / sum(harmonic_input)
        peak_response = max(filtered)
        
        # Final composite formula
        result = int(total_energy * harmonic_mean + peak_response * 10)
    else:
        result = 0
        
    return result

# Critical execution point
thermal_capacity = calculate_thermal_response(grid_state, calibration_factor)

# Irrelevant post-processing block (dead path)
if thermal_capacity < 0:
    correction = math.log(abs(thermal_capacity) + 1)
    thermal_capacity += int(correction)

# Output the target result
print(f"Result: {thermal_capacity}")