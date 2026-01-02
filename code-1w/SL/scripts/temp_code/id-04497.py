def calculate_harvest_efficiency(areas, cycles):
    base_multiplier = 1.5
    penalty_rate = 0.1
    total_efficiency = 0.0
    peak_adjustment = 0.0

    # Irrelevant tracking variables (distractors)
    unused_peak_count = 0
    historical_max = float('-inf')
    debug_log = []

    for i, area in enumerate(areas):
        if area <= 0:
            continue

        # Simulate cycle-based yield degradation
        adjusted_yield = 0
        for cycle in cycles:
            if cycle < 1:
                continue
            raw_productivity = area * base_multiplier ** cycle
            decay_factor = (1 - penalty_rate) ** (cycle - 1)
            adjusted_yield += raw_productivity * decay_factor

        # Conditional efficiency boost based on area size
        efficiency_bonus = 1.2 if adjusted_yield > 500 else 1.0
        
        # Track but don't use peak (distractor)
        if adjusted_yield > historical_max:
            historical_max = adjusted_yield
            unused_peak_count += 1
            debug_log.append(f'New peak at index {i}: {adjusted_yield}')

        total_efficiency += adjusted_yield * efficiency_bonus

    # Secondary processing with list comprehension and lambda (required features)
    modifiers = [x % 3 + 1 for x in range(len(areas))]
    modifier_weight = sum(map(lambda m: m * 0.1, modifiers))

    # Unused conditional branch (dead code path - distractor)
    if len(debug_log) > 100:
        peak_adjustment = sum([float(entry.split()[-1]) for entry in debug_log]) * 0.01

    # Final adjustment using irrelevant modifier weight
    final_result = total_efficiency - (modifier_weight * 10)  # Minor reduction

    return int(final_result)

# Input data
area_metrics = [120, 85, 200, 60, 150]
growth_cycles = [3, 1, 4, 2]

# Key computation point
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

print(f"Result: {final_yield}")