def analyze_soil_composition(elements):
    # Irrelevant analysis with dead-end computation
    trace_metals = {e for e in elements if e in ['Zn', 'Cu', 'Mn']}
    toxicity_score = len(trace_metals) * 1.5
    ph_level = 6.8 if 'Ca' in elements else 5.5
    return ph_level > 6 and len(trace_metals) < 4


def validate_irrigation(flow_rates):
    # Distractor function: computes statistics but not used in final result
    total_flow = sum(flow_rates)
    avg_flow = total_flow / len(flow_rates)
    fluctuations = [abs(flow_rates[i] - flow_rates[i-1]) for i in range(1, len(flow_rates))]
    stability_index = 1 / (1 + sum(fluctuations))  # Never actually used
    return avg_flow > 2.0


def calculate_optimal_harvest(plots, constraints):
    eligible_plots = []
    penalty_adjustment = 0.0
    
    for plot_id, data in plots.items():
        # Primary logic: check crop density and sunlight
        base_yield = data['density'] * data['sunlight']
        
        # Simulate microclimate adjustment (some distractor logic)
        micro_factors = data.get('microclimate', {})
        temp_bonus = 1.1 if micro_factors.get('temp') in ['optimal', 'warm'] else 0.9
        humidity_penalty = 0.95 if micro_factors.get('humidity') == 'high' else 1.0
        
        adjusted_yield = base_yield * temp_bonus * humidity_penalty
        
        # Check eligibility using constraint rules
        meets_constraints = True
        for constraint in constraints:
            if constraint == 'organic' and not data['organic']:
                meets_constraints = False
            elif constraint == 'no_shade' and data['sunlight'] < 5:
                meets_constraints = False
        
        if meets_constraints:
            eligible_plots.append(adjusted_yield)
        else:
            # Accumulate penalty even though it's unused later
            penalty_adjustment += adjusted_yield * 0.1
    
    # Real key computation: average of eligible plots
    if not eligible_plots:
        return 0.0
    
    raw_total = sum(eligible_plots)
    count = len(eligible_plots)
    average_yield = raw_total / count
    
    # Final transformation: apply diminishing returns
    final_yield = average_yield * (0.95 ** penalty_adjustment)  # penalty_adjustment mostly irrelevant
    
    # Dead code: this block is unreachable due to logic above
    if len(eligible_plots) > 100:
        fallback = max(eligible_plots) - min(eligible_plots)
        return round(fallback, 4)
    
    return round(final_yield, 4)

# Main execution
soil_elements = ['N', 'P', 'K', 'Ca', 'Mg', 'Zn']
flow_data = [2.1, 2.3, 1.9, 2.0, 2.2]

# Validate irrelevant systems
analyze_soil_composition(soil_elements)
validate_irrigation(flow_data)

# Define actual input data
plots = {
    'p1': {'density': 85, 'sunlight': 7, 'organic': True, 'microclimate': {'temp': 'optimal', 'humidity': 'normal'}},
    'p2': {'density': 90, 'sunlight': 4, 'organic': True, 'microclimate': {'temp': 'cool', 'humidity': 'high'}},
    'p3': {'density': 95, 'sunlight': 8, 'organic': False, 'microclimate': {'temp': 'warm', 'humidity': 'high'}},
    'p4': {'density': 80, 'sunlight': 9, 'organic': True, 'microclimate': {'temp': 'optimal', 'humidity': 'normal'}}
}

constraints = ['organic', 'no_shade']

final_yield = calculate_optimal_harvest(plots, constraints)
print(f"Result: {final_yield}")