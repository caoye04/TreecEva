def calculate_farm_yield():
    # Simulate a multi-field crop yield analysis with filtering and transformation
    base_yields = [3200, 4500, 2800, 5100, 3900]
    rainfall_levels = [120, 160, 90, 180, 140]  # in mm
    soil_quality = [7, 9, 5, 8, 6]

    # Irrelevant scaling factor (distractor)
    dummy_scale = 1.05
    adjusted_rainfall = [r * dummy_scale for r in rainfall_levels]

    # Determine viable fields based on combined conditions
    viable_mask = [
        (yield_val >= 3000) and (rain >= 100) and (soil >= 6)
        for yield_val, rain, soil in zip(base_yields, rainfall_levels, soil_quality)
    ]

    # Compute auxiliary statistics (semi-relevant, not used later)
    avg_soil = sum(soil_quality) / len(soil_quality)
    high_yield_count = sum(1 for y in base_yields if y > 4000)

    # Filter relevant fields using enumerate and conditionals
    selected_indices = [
        i for i, viable in enumerate(viable_mask) if viable
    ]

    # Extract yields from viable fields
    filtered_yields = [base_yields[i] for i in selected_indices]

    # Simulate pest impact on each viable field (loop with state tracking)
    pest_impact = 0
    for idx, yield_val in enumerate(filtered_yields):
        if idx % 2 == 0:
            pest_impact += yield_val * 0.05
        else:
            pest_impact += yield_val * 0.03

    total_potential = sum(filtered_yields)
    net_output = total_potential - pest_impact

    # Efficiency factor based on conditional logic
    if len(filtered_yields) > 2:
        efficiency_factor = 0.92
    else:
        efficiency_factor = 0.85

    # Critical assignment point
    final_yield = net_output * efficiency_factor

    # Dead code path (distractor)
    if False:
        final_yield *= 1.1

    print(f"Result: {final_yield}")
    return final_yield

# Execute function
calculate_farm_yield()