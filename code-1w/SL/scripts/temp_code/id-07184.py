def calculate_harvest(plots):
    base_multiplier = 2
    adjustment_factor = 0.5
    temp_offset = 3  # unused in final logic, red herring
    decay_rate = 0.9

    # Irrelevant helper that's defined but not used
    def climate_score(temp, rain):
        return (temp * 0.3) + (rain * 0.7)

    # Misleading intermediate calculation
    outlier_buffer = [x['yield'] * 0.1 for x in plots if x['soil_quality'] < 3]
    buffer_sum = sum(outlier_buffer)  # Computed but not used

    # Core logic with lambda for transformation
    process_plot = lambda p: (
        p['yield'] 
        * base_multiplier 
        * (1 + p['fertilizer'] * 0.2)
        * (decay_rate if p['pests'] else 1.0)
    )

    # List of adjusted yields
    adjusted_yields = []
    for plot in plots:
        if plot['soil_quality'] >= 2:
            adjusted_yields.append(process_plot(plot))
        else:
            continue  # Skip low-quality soil

    # Secondary filtering distractor
    filtered_caps = [y for y in adjusted_yields if y > 5]  # Used only for len check below
    size_proxy = len(filtered_caps) * 0.01  # Minor influence, mostly noise

    # Final aggregation
    base_total = sum(adjusted_yields)
    final_yield = int(base_total + size_proxy)  # Cast to int as per deterministic requirement

    return final_yield

# Input data setup
plots = [
    {'yield': 4, 'soil_quality': 4, 'fertilizer': 3, 'pests': False},
    {'yield': 5, 'soil_quality': 3, 'fertilizer': 2, 'pests': True},
    {'yield': 3, 'soil_quality': 5, 'fertilizer': 4, 'pests': False},
    {'yield': 2, 'soil_quality': 1, 'fertilizer': 5, 'pests': False},  # skipped due to soil quality
    {'yield': 6, 'soil_quality': 4, 'fertilizer': 1, 'pests': False}
]

# Execution entry point
final_yield = calculate_harvest(plots)
print(f"Target result: {final_yield}")