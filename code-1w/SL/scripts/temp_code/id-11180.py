from itertools import combinations

def analyze_soil_variability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return variance

def filter_productive_plots(plots, min_threshold=4.0):
    filtered = []
    temp_stats = []
    for plot_id, data in plots.items():
        base_yield = data['yield']
        soil_q = data['soil_quality']
        if base_yield >= min_threshold and 'A' in soil_q:
            filtered.append(plot_id)
            temp_stats.append(base_yield * 0.8 + 0.2 * ('A+' in soil_q))
    excess_computation = [x ** 0.5 for x in temp_stats if x > 3]  # unused
    return filtered

def calculate_harvest_efficiency(plots, thresholds):
    selected_ids = filter_productive_plots(plots, thresholds['yield'])
    total_efficiency = 0.0
    penalty_factor = 0.95
    boost_count = 0
    
    all_combinations = list(combinations(selected_ids, 2))
    pair_interactions = []
    
    for pid in selected_ids:
        plot_data = plots[pid]
        raw_yield = plot_data['yield']
        age_penalty = max(0, (plot_data['years_farmed'] - 5) * 0.05)
        adjusted_yield = raw_yield * (1 - age_penalty) * (1.1 if 'irrigated' in plot_data and plot_data['irrigated'] else 1.0)
        
        # String processing to simulate metadata analysis
        notes = plot_data.get('notes', '')
        if notes.count('fertilizer') > 0:
            adjusted_yield *= 1.08
        if 'pest' in notes:
            adjusted_yield *= 0.92
        
        total_efficiency += adjusted_yield
        
        # Dummy tracking
        status_log = f"Plot {pid}: Yield={adjusted_yield:.3f}"
        if adjusted_yield > 5.0:
            boost_count += 1
    
    interaction_bonus = len(all_combinations) * 0.02 if len(selected_ids) > 1 else 0
    final_efficiency = total_efficiency * penalty_factor + interaction_bonus
    
    # Irrelevant post-processing
    outlier_check = [x for x in plots.values() if x['yield'] < 2.0]
    shadow_var = sum(1 for x in outlier_check)  # dead code
    
    return round(final_efficiency, 4)

# Main execution block
plots = {
    'P01': {'yield': 6.2, 'soil_quality': 'A+', 'years_farmed': 3, 'irrigated': True, 'notes': 'fertilizer applied'},
    'P02': {'yield': 5.8, 'soil_quality': 'B', 'years_farmed': 6, 'irrigated': False, 'notes': 'pest detected, fertilizer applied'},
    'P03': {'yield': 6.5, 'soil_quality': 'A', 'years_farmed': 4, 'irrigated': True, 'notes': 'fertilizer applied'},
    'P04': {'yield': 3.0, 'soil_quality': 'C', 'years_farmed': 2, 'irrigated': False, 'notes': ''},
    'P05': {'yield': 5.1, 'soil_quality': 'A', 'years_farmed': 7, 'irrigated': True, 'notes': 'fertilizer applied'}
}

thresholds = {'yield': 4.0, 'quality': 'A'}

# Misleading preliminary calculations
baseline_avg = sum(p['yield'] for p in plots.values()) / len(plots)
high_yielders = [k for k, v in plots.items() if v['yield'] > 5.0]
dummy_pairs = list(combinations(high_yielders, 2))

# Key computation
final_yield = calculate_harvest_efficiency(plots, thresholds)

print(f"Result: {final_yield}")