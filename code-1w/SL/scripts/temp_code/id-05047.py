def analyze_health_status(health_data):
    """Irrelevant function analyzing health metrics."""
    total_stress = 0
    for record in health_data:
        if record['heart_rate'] > 100:
            total_stress += record['oxygen_level']
    return total_stress

# Irrelevant global variables (distractors)
current_moon_phase = 'waxing'
population_density_factor = 0.87
baseline_offset = 33
unrelated_threshold = 999

# Real data structures for agricultural modeling
grid = [
    [12, 15, 10],
    [8, 14, 11],
    [13, 9, 16]
]

efficiency_map = [
    [0.9, 1.1, 0.8],
    [1.0, 1.2, 0.9],
    [1.1, 0.85, 1.3]
]

# Decoy function with misleading similarity
def calculate_efficiency_score(data):
    score = 0
    for row in data:
        for val in row:
            score += val ** 0.5
    return score * 0.1  # irrelevant result

# Unused transformation table (dead code path)
transform_table = {
    'A': lambda x: x + 1,
    'B': lambda x: x * 2,
    'C': lambda x: x - 5
}

# Distractor: fake accumulator with plausible name
phantom_accumulator = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        phantom_accumulator += grid[i][j] * (i + j)  # meaningless computation

# Real core logic buried among distractions
def apply_modifiers(value, modifier):
    if modifier > 1.0:
        return int(value * modifier) + 1
    else:
        return int(value * modifier)

def validate_grid_integrity(grid, map_ref):
    """Ensures dimensions match - actually used."""
    rows = len(grid)
    cols = len(grid[0])
    return rows == len(map_ref) and cols == len(map_ref[0])

def aggregate_production(area_grid, efficiency_coefficients):
    if not validate_grid_integrity(area_grid, efficiency_coefficients):
        return -1
    
    temp_results = []
    # Use enumerate and zip as required
    for idx, (row, eff_row) in enumerate(zip(area_grid, efficiency_coefficients)):
        row_total = 0
        for jdx, (cell, eff) in enumerate(zip(row, eff_row)):
            # Core relevant calculation hidden in loop
            adjusted = apply_modifiers(cell, eff)
            # Only every second cell contributes to actual final yield
            if (idx + jdx) % 2 == 0:
                row_total += adjusted
        temp_results.append(row_total)
    
    # Final computation
    base_yield = sum(temp_results)
    
    # Distractor: another unused intermediate
    fake_normalization = base_yield / (len(temp_results) or 1)
    scaling_factor = 1.0
    
    # Additional red herring: conditional that never triggers
    if baseline_offset > 100:
        scaling_factor = 0.5
    
    # Actual answer derivation
    final = int(base_yield * 1.5) - 17
    
    # Dead code: unreachable due to structure
    for _ in range(0):  
        final = calculate_efficiency_score(area_grid)
    
    return final

# Simulated health data (irrelevant input)
health_monitoring = [
    {'heart_rate': 105, 'oxygen_level': 97},
    {'heart_rate': 92, 'oxygen_level': 94}
]

# Irrelevant call
stress_metric = analyze_health_status(health_monitoring)

# Key execution point
final_yield = aggregate_production(grid, efficiency_map)

# Print result as required
print(f"Result: {final_yield}")