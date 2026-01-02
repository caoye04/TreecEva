import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([x ** 2 for x in data if x > 0])

# Decoy system parameters
baseline_offset = 17.3
redundant_buffer = [0] * 15
sync_threshold = 42

# Core system configuration
phase_shifters = [0.8, 1.2, 0.9, 1.5]
efficiency_nodes = {1, 2, 4, 8, 16}
logic_matrix = [
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]

# Misleading intermediate calculation (distractor)
current_draw = 0
for i in range(len(logic_matrix)):
    for j in range(len(logic_matrix[i])):
        current_draw += logic_matrix[i][j] * (i + j)

# Unused transformation map
transform_map = {}
for idx in range(4):
    transform_map[idx] = math.sin(phase_shifters[idx]) + math.cos(phase_shifters[(idx+1)%4])

# Simulated signal noise (irrelevant)
signal_noise = []
for _ in range(6):
    val = (baseline_offset * _) % 7
    signal_noise.append(int(val))

# Real computation begins: analyze node coverage
def compute_node_weight(nodes, shifters):
    total = 0
    for i, row in enumerate(shifters):
        if i in nodes:
            total += row * (i + 1)
    return total

# Evaluate logical coherence using set operations
def assess_coherence(matrix):
    row_patterns = set()
    for row in matrix:
        pattern = tuple(row)
        row_patterns.add(pattern)
    
    # Use set difference to filter redundant patterns (real usage)
    base_pattern = {(1,0,1,0), (0,1,1,1)}
    unique_patterns = row_patterns - base_pattern
    
    score = len(row_patterns) * 1.5 - len(unique_patterns) * 0.5
    return score

# Conditional expression with nested logic
def calculate_phase_load(phases):
    load = 0
    for p in phases:
        if p < 1.0:
            load += math.log(p + 1.1)
        elif p >= 1.0 and p < 1.4:
            load += math.sqrt(p)
        else:
            load += p * 0.8
    return load

# Main evaluation function with multiple concepts
def evaluate_system_response(mat, phs):
    # Step 1: Compute structural weight
    weights = compute_node_weight(efficiency_nodes, mat)
    
    # Step 2: Assess logical coherence via set operations
    coherence = assess_coherence(mat)
    
    # Step 3: Calculate dynamic phase load
    phase_load = calculate_phase_load(phs)
    
    # Step 4: Combine with conditional scaling
    if coherence > 3.0:
        adjusted_weights = weights * 1.2
    else:
        adjusted_weights = weights * 0.85
    
    # Step 5: Apply nonlinear transformation
    nonlin_factor = math.exp(coherence / 5.0)
    
    # Step 6: Incorporate phase dynamics
    dynamic_component = phase_load * len(phs)
    
    # Step 7: Final integration
    result = (adjusted_weights + dynamic_component) * nonlin_factor
    
    # Step 8: Correction based on matrix diagonal
    diag_sum = sum(mat[i][i] for i in range(min(len(mat), len(mat[0]))))
    result -= diag_sum * 0.6
    
    return result

# Execution point of interest
thermal_capacity = evaluate_system_response(logic_matrix, phase_shifters)

# Print final result as required
print(f"Target result: {thermal_capacity}")