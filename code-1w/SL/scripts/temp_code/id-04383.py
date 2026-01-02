def calculate_harvest_efficiency(plots, cycles):
    # Irrelevant transformation (distractor)
    shadow_factor = sum(p['size'] * 0.07 for p in plots if p['soil_type'] == 'clay')

    # Semi-relevant preprocessing: normalize yield per plot
    normalized_yields = []
    for plot in plots:
        base = plot['size'] * plot['fertility']
        adjusted = base * (1.2 if plot['sun_exposure'] > 6 else 0.9)
        normalized_yields.append(adjusted)

    # Simulate growth decay over cycles using lambda
    decay_fn = lambda x, c: x * (0.95 ** c)
    decayed_yields = [decay_fn(y, len(cycles)) for y in normalized_yields]

    # Track cumulative water impact (not used in final result)
    total_water = 0
    for cycle in cycles:
        total_water += sum(farm['irrigation'] for farm in plots)  # misleading aggregation

    # Core logic: efficiency depends on top 3 yields and cycle stability
    sorted_yields = sorted(decayed_yields, reverse=True)
    top_three_avg = sum(sorted_yields[:3]) / 3

    # Stability metric from cycles (distractor computation)
    variances = []
    for i in range(1, len(cycles)):
        diff = abs(cycles[i] - cycles[i-1])
        variances.append(diff)
    stability_score = 1 / (1 + sum(variances))  # interesting but unused

    # Actual efficiency formula
    baseline_efficiency = top_three_avg * 0.85
    penalty = len([y for y in decayed_yields if y < 50]) * 15  # penalty for low-yield plots
    final_efficiency = baseline_efficiency - penalty

    # Additional red herring: unused conditional adjustment
    if shadow_factor > 10:
        final_efficiency *= 1.1

    return int(final_efficiency)

# Input data setup
area_metrics = [
    {'size': 20, 'fertility': 4.2, 'soil_type': 'loam', 'sun_exposure': 7, 'irrigation': 3},
    {'size': 15, 'fertility': 3.8, 'soil_type': 'sandy', 'sun_exposure': 8, 'irrigation': 2},
    {'size': 25, 'fertility': 4.5, 'soil_type': 'clay', 'sun_exposure': 5, 'irrigation': 4},
    {'size': 18, 'fertility': 3.0, 'soil_type': 'loam', 'sun_exposure': 9, 'irrigation': 3},
    {'size': 30, 'fertility': 5.0, 'soil_type': 'clay', 'sun_exposure': 4, 'irrigation': 5}
]

growth_cycles = [22, 21, 19, 20, 18, 17]  # Environmental stress reducing over time

# Key statement
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

print(f"Result: {final_yield}")