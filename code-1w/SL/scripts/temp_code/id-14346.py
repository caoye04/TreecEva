import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([len(row) for row in data]) % 2 == 0

# Misleading intermediate computation
temp_snapshot = [[i * j + 2 for j in range(3)] for i in range(3)]
baseline_offset = sum(temp_snapshot[0]) * 0.1

# Real input data
energy_levels = [8, 12, 16, 24]
efficiency_curve = lambda x: round(math.log(x) * 0.75, 4)

def generate_energy_matrix(levels):
    matrix = []
    for i in levels:
        row = []
        for j in levels:
            if i == j:
                row.append(i ** 0.5)
            elif i < j:
                row.append((i + j) // 4)
            else:
                row.append(abs(i - j) % 7)
        matrix.append(row)
    return matrix

# Distractor: complex-looking but unused transformation
decoy_transformation = lambda mat: [
    [math.sin(cell) * math.cos(i + j) for j, cell in enumerate(row)]
    for i, row in enumerate(mat)
]

# Actual efficiency map builder
def build_efficiency_map(levels, curve):
    return {lvl: curve(lvl) for lvl in levels}

# Core calculation function
def calculate_thermal_output(matrix, efficiency):
    total = 0.0
    adjustment_factor = 1.35
    
    # Nested logic with mixed paradigms
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        level = energy_levels[i]
        efficiency_value = efficiency[level]
        
        # Conditional expression with distractors
        contribution = row_sum * efficiency_value if row_sum > 10 else row_sum * 0.5
        
        # Bit manipulation red herring (appears relevant but isn't used in final logic)
        masked_contribution = contribution ^ int(baseline_offset) & 0xFF
        
        # Only this line matters
        total += contribution * adjustment_factor
    
    # Final transformation using tuple unpacking and summation
    base, modifier = divmod(total, 100)
    return round(base * modifier + len(matrix), 4)

# Build real components
energy_matrix = generate_energy_matrix(energy_levels)
efficiency_map = build_efficiency_map(energy_levels, efficiency_curve)

# Unused but plausible-looking diagnostic
snapshot_hash = sum(sum(row) for row in energy_matrix) % 17

# Key execution point
thermal_capacity = calculate_thermal_output(energy_matrix, efficiency_map)

# Irrelevant set operation (distractor)
redundant_set = {x % 5 for x in energy_levels}
redundant_set.add(int(efficiency_map[8] * 10))

# Output result as required
print(f"Result: {thermal_capacity}")