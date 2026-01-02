def analyze_growth_cycle(data, config):
    # Irrelevant helper: computes average temperature (not used in final result)
    avg_temp = sum(temp['value'] for temp in data['temperatures']) / len(data['temperatures'])
    growth_factor = config.get('factor', 1.0)
    peak_days = [day for day in data['growth_days'] if day > 15]
    return {'factor': growth_factor, 'peaks': len(peak_days)}

# Misleading intermediate calculation with dead code path
def compute_soil_health(indices):
    ph_levels = [i['ph'] for i in indices]
    base_score = sum(ph_levels) / len(ph_levels)
    if base_score > 7:
        return base_score * 1.2
    else:
        # Dead code due to fixed conditions not met
        return base_score * 0.8  

# Real logic buried among distractions
def calculate_harvest_efficiency(plots, thresholds):
    # Extract relevant slice: only consider mature plots (index 2 onwards)
    active_plots = plots[2:]
    
    # Track cumulative yield and apply threshold filtering
    filtered_yields = []
    for p in active_plots:
        base_yield = p['yield']
        age = p['age']
        status = p['status']
        
        # Only include healthy, mature plots
        if status == 'healthy' and age >= 3:
            adjusted_yield = base_yield * (0.9 if age == 4 else 1.0)
            filtered_yields.append(adjusted_yield)
    
    # Compute efficiency using modular constraint: every 3rd plot gets bonus
    total_bonus = 0
    for i, y in enumerate(filtered_yields):
        if (i + 1) % 3 == 0:  # Bonus on 3rd, 6th, etc.
            total_bonus += int(y * 0.15)
    
    base_total = sum(filtered_yields)
    efficiency_score = (base_total + total_bonus) // len(filtered_yields) if filtered_yields else 0
    
    # Distractor: unused min/max calculations
    max_yield = max(filtered_yields) if filtered_yields else 0
    min_yield = min(filtered_yields) if filtered_yields else 0
    range_penalty = (max_yield - min_yield) * 0.05  # Not applied but looks important
    
    return int(efficiency_score - range_penalty)  # Final adjustment ignored due to int truncation

# Main execution
if __name__ == '__main__':
    # Input data with red herrings
    climate_data = {
        'temperatures': [{'value': 22}, {'value': 25}, {'value': 20}, {'value': 24}],
        'growth_days': [12, 16, 18, 14, 20]
    }
    
    config_params = {'factor': 1.1, 'cycles': 4}
    soil_indices = [
        {'ph': 6.8, 'moisture': 40},
        {'ph': 7.2, 'moisture': 55},
        {'ph': 6.5, 'moisture': 38}
    ]
    
    # Critical dataset
    plots_info = [
        {'yield': 120, 'age': 2, 'status': 'immature'},
        {'yield': 90,  'age': 2, 'status': 'stressed'},
        {'yield': 200, 'age': 3, 'status': 'healthy'},
        {'yield': 180, 'age': 4, 'status': 'healthy'},
        {'yield': 210, 'age': 5, 'status': 'healthy'},
        {'yield': 160, 'age': 3, 'status': 'healthy'}
    ]
    
    thresholds_info = {'min_yield': 100, 'tolerance': 0.1}
    
    # Irrelevant function calls (distractors)
    _ = analyze_growth_cycle(climate_data, config_params)
    _ = compute_soil_health(soil_indices)
    
    # Key statement
    final_yield = calculate_harvest_efficiency(plots_info, thresholds_info)
    
    # Print result as required
    print(f"Target result: {final_yield}")