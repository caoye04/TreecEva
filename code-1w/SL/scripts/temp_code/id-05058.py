def analyze_agricultural_output(plots):
    # Simulate soil quality adjustments (irrelevant for final result)
    adjusted_plots = [p * 1.05 for p in plots]
    avg_quality = sum(adjusted_plots) / len(adjusted_plots)

    # Track historical yields (distractor data structure)
    historical_yields = [98, 102, 95, 110, 97]
    baseline = historical_yields[len(historical_yields)//2]

    # Current season data
    crop_production = [p * 12 for p in plots]  # Main transformation
    growth_factor = 0
    if len(crop_production) > 4:
        growth_factor += 2
    else:
        growth_factor += 1

    # Apply growth factor to irrelevant variable
    boosted_yield = [y * growth_factor for y in crop_production]

    # Determine harvest index using slicing and linear search
    temp_slice = crop_production[2:5]
    harvest_index = 0
    for i in range(len(temp_slice)):
        if temp_slice[i] >= 300:
            harvest_index = i + 2  # offset due to slice
            break

    # Introduce rounding and integer division
    preliminary_yield = crop_production[harvest_index] // 10
    normalized = round(preliminary_yield * 0.987)

    # Final computation step
    final_yield = crop_production[harvest_index] // 100

    # Print result as required
    print(f"Result: {final_yield}")

# Input data
plot_sizes = [20, 25, 30, 35, 40]
analyze_agricultural_output(plot_sizes)