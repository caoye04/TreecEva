from itertools import compress, cycle

def analyze_growth_potential(size, base_rate):
    return size * base_rate * 0.85

def calculate_harvest_efficiency(plots, quality_map):
    adjusted_yields = []
    efficiency_flags = []
    
    # Simulate seasonal adjustments (irrelevant to final logic but adds distraction)
    season_modifiers = [1.1, 0.95, 1.0, 0.85]
    current_season = cycle(season_modifiers)
    
    temp_accumulator = 0
    for i, plot in enumerate(plots):
        base_yield = plot['size'] * plot['fertility']
        
        # Irrelevant intermediate calculation
        theoretical_max = analyze_growth_potential(plot['size'], plot['fertility'])
        temp_accumulator += theoretical_max
        
        # Actual relevant logic with conditional filtering
        if quality_map[i] > 2:
            adjusted_yield = base_yield * 1.2
        else:
            adjusted_yield = base_yield * 0.7
        
        # Distraction: unused flag tracking
        efficiency_flags.append(adjusted_yield > 150)
        
        adjusted_yields.append(adjusted_yield)
    
    # Real computation path
    valid_indices = [q > 2 for q in quality_map]
    filtered_yields = list(compress(adjusted_yields, valid_indices))
    
    # Secondary irrelevant sum
    total_temp = sum(temp_accumulator / len(plots) for _ in range(len(plots)))  # dead computation
    
    # Final result depends only on filtered, high-quality plots
    final_yield = int(sum(filtered_yields) * 0.9)  # 10% loss during harvest
    
    return final_yield

# Main execution context
plots = [
    {'size': 10, 'fertility': 12},
    {'size': 15, 'fertility': 8},
    {'size': 20, 'fertility': 10},
    {'size': 12, 'fertility': 14}
]

soil_quality = [1, 3, 4, 2]

# Unused variables - red herrings
baseline_projection = 180.5
projection_buffer = [baseline_projection * (1 + 0.05 * i) for i in range(4)]

final_yield = calculate_harvest_efficiency(plots, soil_quality)
print(f"Result: {final_yield}")