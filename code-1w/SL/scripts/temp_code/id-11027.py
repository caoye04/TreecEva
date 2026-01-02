def calculate_agricultural_yield():
    # Environmental data
    rainfall_mm = [80, 120, 95, 140, 70]
    temperature_c = [22, 25, 24, 27, 21]
    soil_quality_index = {'clay': 68, 'loam': 88, 'sand': 55}
    
    # Crop parameters
    base_yield_per_hectare = 3.2
    ideal_rainfall = 100
    tolerance_band = 25
    baseline_offset = 5
    
    # Distractor: unused crop type list
    crop_varieties = ['drought_resistant', 'high_yield', 'hybrid']
    growth_cycles = []
    for temp in temperature_c:
        if temp > 23:
            growth_cycles.append(2)
        else:
            growth_cycles.append(3)
    
    # Calculate adaptive yield factors
    adjusted_yields = []
    for i, rain in enumerate(rainfall_mm):
        deviation = abs(rain - ideal_rainfall)
        penalty = deviation * 0.01 if deviation > tolerance_band else 0
        adjusted_yield = base_yield_per_hectare - penalty
        adjusted_yields.append(round(adjusted_yield, 2))
    
    # Simulate field trial results across soil types
    trial_results = []    
    for idx, adj_yield in enumerate(adjusted_yields):
        for soil_type, quality in soil_quality_index.items():
            efficiency_factor = quality / 100.0
            # Irrelevant intermediate calculation (distractor)
            hypothetical_loss = (idx + 1) * 0.05  
            actual_field_yield = adj_yield * efficiency_factor
            trial_results.append(actual_field_yield)
    
    # Aggregate results by averaging trials
    average_trial_yield = sum(trial_results) / len(trial_results)
    
    # Determine potential yields with artificial inflation factor (unused)
    inflated_potentials = [y * 1.1 for y in trial_results if y > 2.0]  
    
    # Core logic: extract unique high-performing yields above threshold
    high_performance_set = {round(y, 2) for y in trial_results if y > 2.5}
    sorted_high = sorted(high_performance_set, reverse=True)
    
    # Introduce irrelevant set operation
    dummy_set = {1, 2, 3} | {3, 4, 5}
    dummy_intersection = dummy_set & {2, 3, 4}
    
    # Compute final candidate yields
    potential_yields = []
    for val in sorted_high:
        normalized = val - 0.1  # minor adjustment
        if normalized > 2.0:
            potential_yields.append(normalized)
    
    # Key statement
    final_yield = max(potential_yields) - baseline_offset
    
    # Print result for verification
    print(f"Result: {final_yield}")
    
    # Return distractor to increase cognitive load
    return average_trial_yield

# Execute function
result = calculate_agricultural_yield()