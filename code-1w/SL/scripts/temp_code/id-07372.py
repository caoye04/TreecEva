def calculate_harvest_efficiency(plots, quality_map):
    base_yield = 100
    penalty_factor = 0.1
    bonus_factor = 0.2
    total_yield = 0
    temp_results = []
    efficiency_log = []

    for i, (plot, size) in enumerate(plots):
        soil_status = quality_map.get(plot, 'normal')
        base_production = base_yield * size
        
        # Misleading computation - not actually used in final result
        hypothetical_rainfall = (i + 1) * 0.75
        adjusted_for_weather = base_production * (1 + hypothetical_rainfall / 100)
        temp_results.append(adjusted_for_weather)

        if soil_status == 'fertile':
            effective_yield = base_production * (1 + bonus_factor)
        elif soil_status == 'barren':
            effective_yield = base_production * (1 - penalty_factor * 2)
        else:
            effective_yield = base_production * (1 - penalty_factor)

        stagnation_check = effective_yield % 5  # Dead computation
        if stagnation_check > 3:
            pass  # Simulate inspection delay (no effect)

        rolling_modifier = 1 + (i % 3) * 0.05
        final_plot_yield = int(effective_yield * rolling_modifier)
        
        efficiency_log.append(f"Plot-{i}: {final_plot_yield}")
        total_yield += final_plot_yield

    # Distractor: unused aggregation
    avg_temp = sum(temp_results) / len(temp_results) if temp_results else 0
    peak_potential = max(temp_results) if temp_results else 0

    # Actual answer computation
    scaling_multiplier = 0.85
    final_yield = int(total_yield * scaling_multiplier)
    
    # Additional red herring variables
    projected_next_season = final_yield * 1.1
    loss_ratio = (total_yield - final_yield) / total_yield
    
    return final_yield

# Input data
plots_info = [('A1', 5), ('B2', 3), ('C3', 8), ('D4', 4)]
soil_conditions = {'A1': 'fertile', 'C3': 'barren', 'D4': 'fertile'}

# Execution point
final_yield = calculate_harvest_efficiency(plots_info, soil_conditions)
print(f"Result: {final_yield}")