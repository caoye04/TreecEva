from itertools import combinations

def analyze_soil_composition(ph_levels, nutrient_data):
    # Irrelevant helper function - not used in final result
    composite_scores = []
    for i, ph in enumerate(ph_levels):
        score = ph * 0.7 + nutrient_data[i] * 0.3
        composite_scores.append(round(score, 2))
    return composite_scores


def calculate_harvest_efficiency(plots, thresholds):
    efficiency_list = []
    total_area = sum(plot['area'] for plot in plots)
    baseline_yield = 100
    adjustment_factor = 0.0

    # Misleading computation: calculates unused average slope
    total_slope = 0
    for plot in plots:
        total_slope += plot.get('slope', 0)
    avg_slope = total_slope / len(plots) if plots else 0

    # Real logic begins: apply threshold-based filtering
    valid_plots = []
    for plot in plots:
        meets_conditions = True
        for key, threshold in thresholds.items():
            if plot.get(key, 0) < threshold:
                meets_conditions = False
                break
        if meets_conditions:
            valid_plots.append(plot)

    # Use enumerate and zip together (required feature)
    cumulative_yield = 0
    for idx, plot in enumerate(valid_plots):
        moisture = plot['moisture']
        fertility = plot['fertility']
        area = plot['area']
        
        # Efficiency formula with conditional boost
        base_efficiency = (moisture * 0.4 + fertility * 0.6)
        if base_efficiency >= 75:
            base_efficiency *= 1.1  # Bonus for high efficiency
        
        # Track per-plot yield
        plot_yield = base_efficiency * area / 100
        cumulative_yield += plot_yield

    # Distractor: unused combination analysis using itertools
    if len(valid_plots) >= 2:
        pair_impact = 0
        for pair in combinations(valid_plots, 2):
            diff = abs(pair[0]['fertility'] - pair[1]['fertility'])
            pair_impact += diff * 0.1

    # Final adjustment based on number of valid plots
    plot_count_bonus = len(valid_plots) * 5
    
    final_efficiency = cumulative_yield + plot_count_bonus
    
    # Key variable assignment
    final_yield = int(round(final_efficiency))
    
    return final_yield

# Main data setup
ph_values = [6.2, 5.8, 6.5, 7.1, 6.0]
nutrients = [88, 75, 92, 80, 70]

# Real input data
plots = [
    {'area': 20, 'moisture': 85, 'fertility': 90, 'slope': 3},
    {'area': 15, 'moisture': 70, 'fertility': 60, 'slope': 8},
    {'area': 25, 'moisture': 90, 'fertility': 85, 'slope': 2},
    {'area': 10, 'moisture': 60, 'fertility': 50, 'slope': 12},
    {'area': 30, 'moisture': 78, 'fertility': 80, 'slope': 5}
]

thresholds = {
    'moisture': 75,
    'fertility': 80
}

# Unused dictionary operation - red herring
soil_names = ['clay', 'loam', 'sand']
soil_map = {i: name for i, name in enumerate(soil_names)}
zipped_data = list(zip(ph_values, nutrients))

# Call the main function
final_yield = calculate_harvest_efficiency(plots, thresholds)
print(f"Target result: {final_yield}")