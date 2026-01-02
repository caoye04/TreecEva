def analyze_soil_composition(elements):
    ratios = []
    for i, elem in enumerate(elements):
        if elem['atomic_number'] % 2 == 0:
            ratios.append(elem['mass'] / (elem['atomic_number'] + 1))
        else:
            ratios.append(elem['mass'] * 0.95)
    return sum(ratios)


def calculate_nutrient_balance(nutrients, soil_pH):
    balance_score = 0
    ph_factor = 1.0
    if 6.0 <= soil_pH <= 7.0:
        ph_factor = 1.2
    elif soil_pH < 6.0:
        ph_factor = 0.8
    else:
        ph_factor = 0.9
    
    temp_tracker = []
    for nutrient in nutrients:
        adjusted_level = nutrient['level'] * ph_factor
        if nutrient['type'] == 'macro':
            balance_score += adjusted_level * 0.7
        else:
            balance_score += adjusted_level * 0.3
        temp_tracker.append(adjusted_level)
    
    avg_temp = sum(temp_tracker) / len(temp_tracker) if temp_tracker else 0
    return balance_score


def calculate_harvest_efficiency(plot_list, limits):
    efficiency = 0
    waste_counter = 0
    total_area = 0
    
    for idx, plot in enumerate(plot_list):
        area = plot['dimensions']['length'] * plot['dimensions']['width']
        total_area += area
        
        # Track subplot yields using zip
        subplot_yields = [plot['crop_yield']] * plot['subplots']
        adjustment_factors = [0.8, 1.0, 1.2][:plot['subplots']]
        
        for yield_val, factor in zip(subplot_yields, adjustment_factors):
            efficiency += yield_val * factor * (area / 100)
        
        # Misleading computation: tracks unused metric
        max_possible = plot['max_capacity']
        if area > limits['max_plot_size']:
            waste_counter += 1

        # Distractor loop with no effect on final result
        temp_vals = []
        for _ in range(3):
            temp_vals.append(area ** 0.5)
        
    # Secondary logic path: average subplot processing
    total_subplots = sum(p['subplots'] for p in plot_list)
    if total_subplots > 0:
        avg_yield_per_subplot = efficiency / total_subplots
        efficiency += avg_yield_per_subplot * 0.5  # minor refinement
    
    # Final threshold adjustment
    soil_elements = [
        {'atomic_number': 6, 'mass': 12.01, 'name': 'Carbon'},
        {'atomic_number': 7, 'mass': 14.01, 'name': 'Nitrogen'},
        {'atomic_number': 8, 'mass': 16.00, 'name': 'Oxygen'}
    ]
    
    # Unused call - red herring
    base_composition = analyze_soil_composition(soil_elements)
    
    nutrient_data = [
        {'type': 'macro', 'level': 40},
        {'type': 'micro', 'level': 8},
        {'type': 'macro', 'level': 35}
    ]
    
    # Another unused but plausible call
    score = calculate_nutrient_balance(nutrient_data, soil_pH=6.5)
    
    return int(efficiency)

# Main execution block
plots = [
    {
        'dimensions': {'length': 10, 'width': 8},
        'crop_yield': 15,
        'subplots': 3,
        'max_capacity': 90
    },
    {
        'dimensions': {'length': 12, 'width': 5},
        'crop_yield': 18,
        'subplots': 2,
        'max_capacity': 70
    },
    {
        'dimensions': {'length': 6, 'width': 6},
        'crop_yield': 12,
        'subplots': 1,
        'max_capacity': 50
    }
]

thresholds = {
    'max_plot_size': 60
}

final_yield = calculate_harvest_efficiency(plots, thresholds)
print(f"Result: {final_yield}")