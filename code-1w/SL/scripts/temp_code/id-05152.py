def analyze_growth_potential(plots, climate_index):
    growth_scores = []
    temp_modifier = 0.8 if climate_index < 3 else 1.2
    for i, plot in enumerate(plots):
        base_score = plot['size'] * plot['fertility']
        adjusted_score = base_score * temp_modifier
        growth_scores.append((i, adjusted_score))
    return growth_scores


def calculate_harvest_efficiency(plots, soil_quality):
    efficiency_list = []
    total_plots = len(plots)
    cumulative_yield = 0
    
    # Irrelevant sorting - doesn't affect final result but adds cognitive load
    sorted_plots = sorted(plots, key=lambda x: x['fertility'], reverse=True)
    
    for idx, plot in enumerate(sorted_plots):
        size = plot['size']
        fertility = plot['fertility']
        
        # Misleading intermediate calculation (not used later)
        theoretical_max = size * fertility * 2.5
        
        # Real computation path
        base_yield = size * 10
        quality_bonus = fertility * soil_quality[plot['zone']]
        
        # Conditional expression usage (required feature)
        yield_modifier = 1.4 if fertility > 7 else (1.1 if fertility > 4 else 0.7)
        
        actual_yield = base_yield + quality_bonus
        actual_yield *= yield_modifier
        
        # Only every even-indexed plot contributes to final cumulative yield
        if idx % 2 == 0:
            cumulative_yield += int(actual_yield)

        efficiency_list.append(actual_yield)
    
    # Dead code path - never executed but looks relevant
    if len(efficiency_list) > 100:
        fallback = sum(efficiency_list) / 100
    
    # Final aggregation
    avg_efficiency = sum(efficiency_list) / len(efficiency_list)
    final_yield = cumulative_yield + int(avg_efficiency * 0.3)
    
    return final_yield

# Main execution
plots = [
    {'size': 12, 'fertility': 8, 'zone': 0},
    {'size': 9, 'fertility': 5, 'zone': 1},
    {'size': 15, 'fertility': 9, 'zone': 0},
    {'size': 7, 'fertility': 3, 'zone': 1}
]

soil_quality = [6, 4]

# Distractor function call - does not affect final answer
_ = analyze_growth_potential(plots, climate_index=2)

# Key statement
final_yield = calculate_harvest_efficiency(plots, soil_quality)

print(f"Result: {final_yield}")