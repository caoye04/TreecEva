from itertools import cycle

# Simulate agricultural yield optimization with environmental constraints
def calculate_harvest_efficiency(plot_layout, cycles):
    base_yield = 15
    stress_factor = 0.92
    recovery_boost = 1.08
    cumulative_output = 0
    temp_buffer = []

    # Environmental fluctuation model
    weather_patterns = cycle([1.0, 0.88, 1.15, 0.94])
    
    # Irrelevant tracking variables (distractors)
    unused_diagnostic = [0] * len(plot_layout)  # Dead computation
    debug_snapshot = None

    for cycle_count in range(cycles):
        pattern = next(weather_patterns)
        adjusted_yield = base_yield
        
        # Apply layout-specific density factor
        total_plots = sum(1 for row in plot_layout if row[0].isdigit())
        density_modifier = 1 + (total_plots * 0.03) if total_plots < 10 else 0.95
        
        for plot in plot_layout:
            # Parse plot characteristics
            if plot[0].isdigit():
                plot_id = int(plot[0])
                soil_type = plot[1]
                irrigation = plot[2]
                
                # Core yield calculation
                if soil_type == 'loam':
                    adjusted_yield += 3
                elif soil_type == 'clay':
                    adjusted_yield -= 1

                if irrigation == 'drip':
                    adjusted_yield *= 1.1
                elif irrigation == 'sprinkler':
                    adjusted_yield *= 1.05

                # Non-impacting diagnostic logic (distractor)
                if plot_id % 2 == 0:
                    unused_diagnostic[plot_id - 1] += 2

        # Weather and stress modulation
        if pattern < 0.9:
            adjusted_yield *= stress_factor
        elif pattern > 1.1:
            adjusted_yield *= recovery_boost
        
        adjusted_yield *= pattern * density_modifier
        
        # Conditional expression for yield capping
        capped_yield = adjusted_yield if adjusted_yield <= 22 else 22
        
        temp_buffer.append(capped_yield)
        
        # State update that doesn't affect final outcome
        debug_snapshot = f"Cycle-{cycle_count}:Y{capped_yield:.2f}"

    # Final efficiency metric
    total_harvest = sum(temp_buffer)
    avg_yield = total_harvest / cycles
    penalty = 0.5 if any(x < 14 for x in temp_buffer) else 0
    final_yield = avg_yield - penalty
    
    # Additional red herring computation
    theoretical_max = cycles * 22 * density_modifier
    utilization_rate = (total_harvest / theoretical_max) * 100  # Not used
    
    return round(final_yield, 4)

# Define test scenario
area_config = [
    ('1', 'loam', 'drip'),
    ('2', 'clay', 'sprinkler'),
    ('3', 'loam', 'none'),
    ('4', 'sand', 'drip')
]
growth_cycles = 6

# Execute main computation
final_yield = calculate_harvest_efficiency(area_config, growth_cycles)
print(f"Result: {final_yield}")