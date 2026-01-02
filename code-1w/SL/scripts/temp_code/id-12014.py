def analyze_crop_performance(areas, cycles):
    total_yield = 0
    peak_growth = []
    baseline_adjustment = 0.95
    
    for i, (area, cycle) in enumerate(zip(areas, cycles)):
        if area <= 0:
            continue
        
        # Simulate environmental interference
        temp_modifier = (i + 1) * 0.1
        humidity_factor = 1.0 + (temp_modifier % 0.3)
        
        # Core yield calculation
        base_yield = area * 100
        adjusted_yield = base_yield * (cycle / 10) * humidity_factor
        
        # Distractor: irrelevant nutrient tracking
        nitrogen_used = adjusted_yield * 0.02
        phosphorus_ratio = nitrogen_used / (area + 1) if area > 5 else 0
        
        # Only accumulate yield for viable cycles
        if cycle >= 3:
            total_yield += adjusted_yield
            peak_growth.append((i, adjusted_yield))
        
    return total_yield, peak_growth


def calculate_harvest_efficiency(area_data, growth_cycles):
    efficiency_log = []
    cumulative_area = sum(area_data)
    total_waste = 0
    
    # Irrelevant irrigation simulation
    for idx, a in enumerate(area_data):
        irrigation_needed = a * 2.5
        evaporation_loss = irrigation_needed * 0.15
        total_waste += evaporation_loss
    
    raw_yield, peaks = analyze_crop_performance(area_data, growth_cycles)
    
    # Efficiency damping due to distribution loss
    distribution_loss = raw_yield * 0.08
    net_output = raw_yield - distribution_loss
    
    # Early exit condition (not triggered in this case)
    if cumulative_area < 10:
        return 0
    
    # Final efficiency scaling
    efficiency_score = net_output / cumulative_area if cumulative_area > 0 else 0
    efficiency_log.append(efficiency_score)
    
    # Key result computation
    final_yield = int(efficiency_score * 1.1)  # Boost from optimized storage
    
    # Red herring: unused optimization trace
    optimization_trace = [e * 0.99 for _, e in peaks]
    
    return final_yield

# Input data
area_data = [12, 8, 15, 6, 20]
growth_cycles = [4, 2, 5, 1, 4]

# Execution point of interest
final_yield = calculate_harvest_efficiency(area_data, growth_cycles)

print(f"Result: {final_yield}")