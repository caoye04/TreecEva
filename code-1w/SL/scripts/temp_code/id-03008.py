def calculate_harvest(regions, efficiency):
    base_yield = 100
    bonus_multiplier = 1.0
    penalty_factor = 0.9
    debug_logs = []

    # Irrelevant transformation (distractor)
    transformed_regions = {k: v * 1.05 for k, v in regions.items()}

    total_area = sum(regions.values())
    if total_area > 500:
        bonus_multiplier += 0.1

    # Unused helper function (dead code path)
    def get_soil_quality(area):
        return 'rich' if area > 100 else 'normal'

    # Simulate conditional yield adjustments
    adjusted_yields = []
    for name, area in regions.items():
        effect = efficiency.get(name, 1.0)
        raw_yield = base_yield * area * effect
        
        # Apply dynamic adjustment based on size
        if area > 150:
            raw_yield *= bonus_multiplier
        elif area < 50:
            raw_yield *= penalty_factor
        
        adjusted_yields.append(raw_yield)
        
        # Logging irrelevant info
        debug_logs.append(f'{name}: {raw_yield:.2f}')

    # Secondary processing with lambda and dictionary ops
    valid_yields = list(filter(lambda y: y > 5000, adjusted_yields))
    yield_map = {i: val for i, val in enumerate(valid_yields)}

    # Extra computation that doesn't affect result
    average_loss = sum(adjusted_yields) * 0.02 if len(valid_yields) < 3 else 0.0

    # Final aggregation
    base_total = sum(valid_yields)
    fluctuation = len(valid_yields) % 3 * 100
    final_yield = int(base_total + fluctuation - average_loss)

    return final_yield

# Main execution context
regions = {'alpha': 200, 'beta': 80, 'gamma': 160, 'delta': 40}
efficiency_map = {'alpha': 1.2, 'gamma': 0.9, 'epsilon': 1.5}  # epsilon not present

# Key statement
final_yield = calculate_harvest(regions, efficiency_map)
print(f'Result: {final_yield}')