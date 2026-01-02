from itertools import compress, count

def analyze_growth_cycle(data, threshold=75):
    # Simulate analysis of plant growth cycles with sensor data
    indices = range(len(data))
    valid_cycles = list(compress(indices, (x > threshold for x in data)))
    return valid_cycles if valid_cycles else [0]

def calculate_harvest_efficiency(plots, sensors):
    total_yield = 0
    adjustment_factor = 0.85
    base_multiplier = 1.2
    
    # Irrelevant pre-calculation (distractor)
    hypothetical_max = sum(sensors) * base_multiplier - len(plots)
    
    cycle_data = [sum(p) for p in plots]
    filtered_indices = analyze_growth_cycle(cycle_data)
    
    # Use enumerate and zip together (required python feature)
    for i, (plot, sensor) in enumerate(zip(plots, sensors)):
        if i not in filtered_indices:
            continue
        
        # Real computation path
        raw_yield = sum(plot) * sensor
        penalty = 0
        
        # Nested conditional with misleading internal logic
        if raw_yield > 400:
            temp_adjust = lambda x: x * 0.9 if x > 100 else x * 1.1
            penalty = temp_adjust(sensor) // 10
            
            # Dead code branch (distractor)
            if penalty < 0:
                hypothetical_min = 999  # unused
        
        net_yield = raw_yield - penalty
        total_yield += int(net_yield * adjustment_factor)

    # Secondary distractor: complex but unused calculation
    idle_count = sum(1 for s in sensors if s < 30)
    idle_compensation = idle_count * 15 if idle_count > 2 else 0  # not added to result

    final_yield = total_yield + 10  # Final adjustment
    return final_yield

# Main execution
plots = [
    [12, 15, 10, 20],
    [25, 30, 28, 32],
    [45, 50, 48, 52],
    [18, 20, 17, 19]
]

sensors = [68, 82, 95, 73]

final_yield = calculate_harvest_efficiency(plots, sensors)
print(f"Result: {final_yield}")