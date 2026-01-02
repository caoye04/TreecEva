import itertools

# Irrelevant helper function (decoy)
def calculate_noise_level(signal):
    return sum([(s ** 2) % 7 for s in signal])

# Misleading data structure with red herring values
noise_profile = {
    'level_a': [1, 3, 6, 10],
    'level_b': [2, 5, 9, 13],
    'unused_metric': 999
}

# Simulate sensor array input (partially relevant)
sensor_grid = [
    [4, 7, 2],
    [1, 8, 3],
    [6, 5, 9]
]

# Dead code path — never called
def deprecated_analysis(data):
    return [d * 0.5 for d in data if d > 4]

# Auxiliary transformation (mostly irrelevant)
transformed_mask = set()
for i in range(len(sensor_grid)):
    for j in range(len(sensor_grid[i])):
        if (i + j) % 2 == 0:
            transformed_mask.add((i * 2, j * 2))

# Unused intermediate calculation (misleading)
aggregate_score = 0
for row in sensor_grid:
    for val in row:
        aggregate_score += val ** 2 % 5

# Real processing begins here
grid_state = list(itertools.chain.from_iterable(sensor_grid))
efficiency_factor = len([x for x in grid_state if x > 5])

# Secondary distraction: complex but unused filter operation
filtered_pairs = list(itertools.combinations(grid_state, 2))
valid_transitions = set()
for a, b in filtered_pairs:
    if (a + b) % 3 == 0 and abs(a - b) < 7:
        valid_transitions.add((a, b))

# Core logic hidden among distractions
def evaluate_thermal_response(sequence, factor):
    base_energy = 0
    peak_count = 0
    
    # Nested logic with early termination red herring
    for idx, val in enumerate(sequence):
        if val == 0:
            break  # Dead condition — never triggered
        if val > 7:
            peak_count += 1
        base_energy += (val * (idx + 1))
    
    # Bit manipulation decoy (looks important, used minimally)
    shifted = (base_energy >> 2) ^ 0x1F
    
    # Actual key computation buried here
    adjustment = 1 if len(valid_transitions) > 10 else -1
    thermal_index = shifted + (factor * peak_count * adjustment)
    
    # More noise: unused conditional branch
    if thermal_index < 0:
        return -thermal_index * 2
    
    # Real return value
    return thermal_index + 42

# Critical statement containing the target variable assignment
temperature_flags = [t for t in grid_state if t >= 8]
thermal_capacity = evaluate_thermal_response(grid_state, efficiency_factor)

# Output must follow required format
print(f"Target result: {thermal_capacity}")