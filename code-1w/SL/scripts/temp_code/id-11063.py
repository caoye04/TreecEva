from itertools import compress, cycle

def calculate_harvest_efficiency(plots):
    # Simulate soil quality filtering (only odd-indexed plots are fertile)
    fertility_mask = [i % 2 == 1 for i in range(len(plots))]
    fertile_plots = list(compress(plots, fertility_mask))

    # Misleading transformation: elevation adjustment (not used in final calculation)
    elevation_bias = [1.05 + 0.01 * i for i in range(len(plots))]
    adjusted_plots = [p * e for p, e in zip(plots, elevation_bias)]

    # Calculate base yield per fertile plot with diminishing returns
    base_yields = []
    for i, plot in enumerate(fertile_plots):
        if plot > 80:
            yield_val = 100 - (plot - 80) * 0.5
        elif plot < 30:
            yield_val = plot * 0.8
        else:
            yield_val = plot
        base_yields.append(yield_val)

    # Apply seasonal multiplier using cycling pattern (dry, normal, wet years)
    season_cycle = cycle([0.9, 1.0, 1.2])
    seasonal_yields = [y * next(season_cycle) for y in base_yields[:3]]  # Only first 3 seasons matter

    # Compute efficiency as average of top 2 seasonal yields
    sorted_yields = sorted(seasonal_yields, reverse=True)
    efficiency_score = sum(sorted_yields[:2]) / 2

    # Final scaling based on infrastructure index (constant factor)
    infrastructure_multiplier = 1.4
    final_yield = int(efficiency_score * infrastructure_multiplier)

    # Dead code: unused diagnostic log
    diagnostics = {"input_count": len(plots), "fertile_count": len(fertile_plots), "max_base": max(base_yields)}

    return final_yield

# Input data: agricultural plot productivity indices
test_plots = [25, 85, 40, 90, 60, 35]

# Key computation step
final_yield = calculate_harvest_efficiency(test_plots)
print(f"Result: {final_yield}")