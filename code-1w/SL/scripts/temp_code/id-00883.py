import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading intermediate computation
turbine_efficiency = [0.85, 0.91, 0.77, 0.88]
baseline_offset = sum(turbine_efficiency) * 1000  # Decoy value

# Core logic setup
logic_matrix = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]

phase_shifters = [math.pi / 4, math.pi / 6, math.pi / 3, math.pi / 2]
diagnostic_codes = {1: 'OK', 0: 'FAULT'}

# Irrelevant sorting operation (distractor)
sorted_phases = sorted(phase_shifters, reverse=True)

# Bit manipulation red herring
def mask_phases(phases):
    result = []
    for p in phases:
        bits = int(p * 100)
        masked = bits & 0b11111100  # Mask lower 2 bits
        result.append(masked if masked > 0 else 1)
    return result

masked_ints = mask_phases(phase_shifters)  # Unused result

# Conditional expression with distractor logic
mode_flag = 'advanced' if len(logic_matrix) >= 4 else 'basic'
override_enabled = True if mode_flag == 'debug' else False  # Never true

# Set operations - relevant to final calculation
def generate_symmetry_pairs(n):
    indices = set(range(n))
    pairs = set()
    for i in indices:
        for j in indices:
            if i != j and (j, i) not in pairs:
                pairs.add((i, j))
    return pairs

pair_set = generate_symmetry_pairs(4)
pruned_pairs = {(i, j) for i, j in pair_set if i < j}  # Use subset

# Core calculation function with nesting and logic chain
def calculate_thermal_response(matrix, phases):
    n = len(matrix)
    total_flux = 0.0
    
    # Nested loops with conditional expressions
    for i in range(n):
        row_contribution = 0
        for j in range(n):
            if matrix[i][j] == 1:
                # Complex trigonometric accumulation
                angle = phases[j] if i % 2 == 0 else (phases[(j + 1) % n])
                base_weight = math.sin(angle) * (i + 1)
                
                # Additional condition using set lookup
                if (i, j) in pruned_pairs:
                    base_weight *= 1.5
                
                # Bitwise influence on weight
                control_flag = (i ^ j) & 0x1
                adjusted_weight = base_weight * (1.1 if control_flag else 0.9)
                
                row_contribution += adjusted_weight
            else:
                # Dead branch with misleading comment
                # This would apply damping if active, but rarely triggers
                row_contribution -= 0.05  # Minimal effect
        
        # Accumulate with exponential scaling
        total_flux += row_contribution * math.exp(-0.1 * i)
    
    # Final transformation using conditional expression
    normalized = total_flux / n if n > 0 else 0
    return normalized * 10000  # Scale to integer-friendly range

# Execution point of interest
thermal_capacity = calculate_thermal_response(logic_matrix, phase_shifters)

# Print required output
print(f"Target result: {thermal_capacity}")