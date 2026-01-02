import math

def analyze_soil_composition(elements):
    # Irrelevant function - dead code path
    toxicity = 0
    for elem in elements:
        if elem['level'] > 50:
            toxicity += elem['weight'] * 0.3
    return toxicity

def shift_matrix(grid):
    # Distractor: complex-looking but unused bit manipulation
    shifted = [[0]*len(grid) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            shifted[(i+1)%len(grid)][(j+2)%len(grid)] = grid[i][j] ^ 7
    return shifted

def evaluate_stability(matrix):
    # Another decoy function with misleading intermediate results
    total = 0
    for row in matrix:
        for val in row:
            total += (val >> 2) & 3
    return total % 100 == 0

def calculate_harvest_efficiency(plots, config):
    base_yield = 0
    adjustment_factor = config['base_factor']
    stress_modifiers = config['stress_factors']
    
    # Real logic begins: process each plot with enumerate and zip
    for idx, plot in enumerate(plots):
        climate = plot['climate']
        soil_nutrients = plot['nutrients']
        crop_data = plot['crops']
        
        # Extract relevant nutrients using zip
        primary, secondary = zip(*[(n['primary'], n['secondary']) for n in soil_nutrients])
        avg_primary = sum(primary) / len(primary)
        avg_secondary = sum(secondary) / len(secondary)
        
        # Compute base productivity
        productivity = (avg_primary * 0.7) + (avg_secondary * 0.3)
        
        # Apply growth cycles
        for cycle in crop_data:
            growth_rate = cycle['rate']
            days = cycle['days']
            productivity *= (1 + growth_rate) ** days
        
        # Apply index-based adjustment
        if idx % 2 == 0:
            productivity *= adjustment_factor
        else:
            productivity *= 0.9
        
        # Simulate pest resistance (bitwise distraction)
        resistance_code = plot.get('resistance', 255)
        penalty_mask = ~(resistance_code | 16) & 7  # Looks important, barely used
        productivity -= penalty_mask * 0.05
        
        base_yield += productivity
    
    # Final efficiency calculation - this is the real answer
    efficiency_score = base_yield * config['efficiency_ratio']
    scaling_offset = sum([config['offsets'][i] for i in range(len(config['offsets'])) if i % 3 == 0])
    final_yield = int(efficiency_score - scaling_offset)
    
    return final_yield

# Unused data structures as distractors
elements = [
    {'name': 'lead', 'level': 67, 'weight': 4.2},
    {'name': 'arsenic', 'level': 55, 'weight': 3.8}
]

decoymatrix = [
    [240, 101, 15],
    [17, 88, 200],
    [63, 192, 44]
]

# Shift matrix (unused call)
shifted = shift_matrix(decoymatrix)

# Main configuration and data
config = {
    'base_factor': 1.1,
    'stress_factors': {'heat': 0.05, 'drought': 0.1, 'frost': 0.08},
    'efficiency_ratio': 0.85,
    'offsets': [12, 7, 3, 9, 15, 6, 18]
}

plots = [
    {
        'climate': 'temperate',
        'nutrients': [
            {'primary': 40, 'secondary': 25},
            {'primary': 45, 'secondary': 30},
            {'primary': 38, 'secondary': 20}
        ],
        'crops': [
            {'rate': 0.02, 'days': 30},
            {'rate': 0.01, 'days': 20}
        ],
        'resistance': 239
    },
    {
        'climate': 'arid',
        'nutrients': [
            {'primary': 30, 'secondary': 15},
            {'primary': 33, 'secondary': 18},
            {'primary': 28, 'secondary': 12}
        ],
        'crops': [
            {'rate': 0.015, 'days': 35},
            {'rate': 0.008, 'days': 25}
        ],
        'resistance': 191
    },
    {
        'climate': 'tropical',
        'nutrients': [
            {'primary': 50, 'secondary': 35},
            {'primary': 55, 'secondary': 40},
            {'primary': 48, 'secondary': 33}
        ],
        'crops': [
            {'rate': 0.03, 'days': 25},
            {'rate': 0.012, 'days': 15}
        ],
        'resistance': 255
    }
]

# Evaluate stability (called but result unused)
stability = evaluate_stability(decoymatrix)

# Key computation
final_yield = calculate_harvest_efficiency(plots, config)

print(f"Result: {final_yield}")