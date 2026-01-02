def analyze_soil_quality(plots):
    quality_scores = []
    for plot in plots:
        base_score = plot['nutrients'] * 0.4 + plot['moisture'] * 0.6
        adjusted = base_score * (1 + plot.get('sun_exposure', 5) / 10)
        normalized = min(max(adjusted, 0), 10)
        quality_scores.append(normalized)
    return quality_scores


def filter_optimal_plots(plots, threshold=6.5):
    filtered = [p for p in plots if p['nutrients'] > 7 and p['moisture'] > 6]
    return filtered


def simulate_growth_cycles(initial_value, cycles=3):
    growth_trace = [initial_value]
    value = initial_value
    for i in range(cycles):
        if value < 50:
            value *= 1.8
        elif value < 80:
            value *= 1.3
        else:
            value *= 1.1
        growth_trace.append(value)
    
    # Distractor: irrelevant tracking
    peak_deviation = max(growth_trace) - min(growth_trace)
    stability_index = 1 / (peak_deviation + 1) if peak_deviation else 0
    
    return value


def optimize_harvest(plots, factor):
    total_yield = 0
    for plot in plots:
        raw_yield = plot['size'] * plot['efficiency']
        boosted = raw_yield * factor
        capped_yield = min(boosted, 95)
        total_yield += capped_yield
        
        # Distractor: unused intermediate
        penalty = 0
        if plot['size'] > 8:
            penalty = boosted * 0.05
        
    adjustment_rate = 0.9 if len(plots) > 4 else 1.0
    final_yield = int(total_yield * adjustment_rate)
    
    # Irrelevant post-processing
    auxiliary_metric = sum([p['size'] for p in plots]) / (final_yield + 1e-5)
    
    return final_yield

# Main execution
soil_data = [
    {'nutrients': 8.2, 'moisture': 7.1, 'sun_exposure': 6, 'size': 5, 'efficiency': 3.2},
    {'nutrients': 6.5, 'moisture': 8.3, 'sun_exposure': 7, 'size': 7, 'efficiency': 2.8},
    {'nutrients': 9.0, 'moisture': 6.9, 'sun_exposure': 5, 'size': 6, 'efficiency': 3.5},
    {'nutrients': 7.8, 'moisture': 7.5, 'sun_exposure': 8, 'size': 8, 'efficiency': 2.9},
    {'nutrients': 8.5, 'moisture': 6.2, 'sun_exposure': 4, 'size': 4, 'efficiency': 4.0}
]

# Distractor: unused data transformation
transformed = [{k: v*0.95 for k, v in d.items()} for d in soil_data]

# Filter relevant plots based on nutrients and moisture
processed_plots = filter_optimal_plots(soil_data)

# Compute dynamic growth factor using simulation
base_factor = 1.5
growth_factor = simulate_growth_cycles(base_factor)

# Apply optimization function
final_yield = optimize_harvest(processed_plots, growth_factor)

# Output result
print(f"Result: {final_yield}")