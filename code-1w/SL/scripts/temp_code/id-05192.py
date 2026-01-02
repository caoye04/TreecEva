def calculate_plot_score(area, fertility, water):
    base_score = area * fertility
    adjustment = 0
    if water > 0:
        adjustment = (water * 0.3) if water < 50 else (50 * 0.3)
    distraction_score = (area + fertility) / (water + 1)
    return base_score + adjustment


def filter_viable_plots(plots):
    viable = []
    threshold = 80
    for plot in plots:
        score = plot['area'] * plot['fertility']
        if score >= threshold:
            viable.append(plot)
    sorted_viable = sorted(viable, key=lambda x: x['area'])
    normalized_scores = [p['area'] * 0.1 for p in sorted_viable]
    return viable


def calculate_optimal_yield(plots, available_water):
    total_yield = 0
    used_water = 0
    water_limit = available_water
    efficiency_log = []

    for i in range(len(plots)):
        plots[i]['index'] = i

    # Misleading pre-processing
    dummy_set = {p['area'] for p in plots}
    derived_values = [x * 0.5 for x in dummy_set if x > 10]
    cumulative_shift = sum(derived_values) * 0.01

    viable_plots = filter_viable_plots(plots)

    water_per_plot = water_limit // len(viable_plots) if viable_plots else 0
    extra_water = water_limit % len(viable_plots) if viable_plots else 0

    secondary_boost = 0
    for idx, plot in enumerate(viable_plots):
        local_water = water_per_plot + (1 if idx < extra_water else 0)
        plot_yield = calculate_plot_score(plot['area'], plot['fertility'], local_water)
        
        if plot['fertility'] > 6 and local_water > 40:
            secondary_boost += 5.5
        
        efficiency_entry = {
            'plot_id': idx,
            'yield': plot_yield,
            'water_used': local_water
        }
        efficiency_log.append(efficiency_entry)
        total_yield += plot_yield

    final_adjustment = 0
    if len(efficiency_log) > 3:
        high_yield_entries = [e for e in efficiency_log if e['yield'] > 120]
        final_adjustment = len(high_yield_entries) * 3.2
    
    unused_water_penalty = (water_limit - used_water) * 0.05
    debug_value = unused_water_penalty * 2  # Unused in logic
    
    total_yield += final_adjustment + secondary_boost + cumulative_shift
    return int(total_yield)

# Main execution
land_plots = [
    {'area': 20, 'fertility': 4},
    {'area': 30, 'fertility': 3},
    {'area': 25, 'fertility': 5},
    {'area': 40, 'fertility': 6},
    {'area': 35, 'fertility': 7},
    {'area': 15, 'fertility': 8}
]

water_availability = 200

initial_projection = sum(p['area'] * p['fertility'] for p in land_plots)
dummy_dict = {i: initial_projection // (i+1) for i in range(1, 5)}

final_yield = calculate_optimal_yield(land_plots, water_availability)
print(f"Result: {final_yield}")