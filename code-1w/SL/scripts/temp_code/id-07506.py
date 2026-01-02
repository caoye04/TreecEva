def calculate_harvest_efficiency(plots, quality, cycles):
    base_yield = 0
    bonus_multiplier = 1.0
    temp_adjustment = 0
    decay_factor = 0.95
    
    # Irrelevant temperature adjustment (distractor)
    for i in range(len(cycles)):
        cycle_data = cycles[i]
        if cycle_data['season'] == 'summer':
            temp_adjustment += 0.05
        elif cycle_data['season'] == 'winter':
            temp_adjustment -= 0.1
    
    # Real computation begins: track cumulative yield and apply soil modifiers
    total_rainfall = sum([c['rain'] for c in cycles])
    avg_rain = total_rainfall / len(cycles) if cycles else 0
    
    for idx, plot in enumerate(plots):
        plot_id = f'P{idx+1000}'
        status_flag = plot['status']
        
        # String manipulation to determine plot class (relevant)
        plot_class = plot_id[1:].strip('0')
        class_modifier = 1.2 if int(plot_class) % 2 == 0 else 0.9
n        
        # Harvest base from size and fertility
        base_from_size = plot['size'] * 10
        fertility_score = quality[idx] * 0.3
        
        # Conditional expression based on rainfall adequacy
        water_bonus = 1.15 if avg_rain > 80 else (0.9 if avg_rain < 50 else 1.0)
        
        # Accumulate base yield with modifiers
        plot_yield = base_from_size + fertility_score * 25
        plot_yield *= class_modifier * water_bonus
        
        # Simulate decay over cycles using nested loop (semi-relevant)
        for _ in range(cycle_data.get('count', 1)):
            plot_yield *= decay_factor
        
        base_yield += plot_yield
    
    # Bonus logic that never triggers (dead code - distractor)
    if bonus_multiplier > 2:
        extra_boost = sum([q**2 for q in quality if q > 8])
        base_yield += extra_boost * 10
    
    # Final efficiency calculation (key statement)
    final_yield = int(base_yield / len(plots)) if plots else 0
    return final_yield

# Input data setup
plots = [
    {'size': 5, 'status': 'active'},
    {'size': 7, 'status': 'active'},
    {'size': 6, 'status': 'standby'}
]

soil_quality = [6, 8, 5]

growth_cycles = [
    {'season': 'spring', 'rain': 75, 'count': 2},
    {'season': 'summer', 'rain': 95, 'count': 3},
    {'season': 'autumn', 'rain': 45, 'count': 2}
]

cycle_data = growth_cycles[-1]  # snapshot used in loop

# Execute main function
final_yield = calculate_harvest_efficiency(plots, soil_quality, growth_cycles)
print(f"Result: {final_yield}")