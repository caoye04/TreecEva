from itertools import cycle

def analyze_soil_composition(elements):
    # Irrelevant computation: simulates soil analysis but not used in final result
    trace_metals = sum([e % 7 for e in elements if e > 5])
    base_nutrients = len([e for e in elements if e % 2 == 0])
    return trace_metals * 0.1  # Distractor return

def calculate_growth_potential(temp_seq, moisture_level):
    # Semi-relevant: computes a factor that's logged but not directly used
    trend_score = 0
    for i, t in enumerate(temp_seq):
        if t > 25:
            trend_score += (t - 25) * moisture_level
    normalized = trend_score / (len(temp_seq) + 1)
    return round(normalized, 2)

def calculate_harvest_efficiency(areas, cycles):
    efficiency_log = []
    total_adjusted_area = 0
    
    for i, area in enumerate(areas):
        # Apply cyclic growth factor
        growth_factor = cycles[i % len(cycles)]
        adjusted_area = area * growth_factor
        
        # Conditional adjustment based on size class
        size_class = 'large' if area > 10 else 'small'
        modifier = 1.2 if size_class == 'large' else 0.9
        
        adjusted_area *= modifier
        total_adjusted_area += adjusted_area
        efficiency_log.append(adjusted_area)
    
    # Final aggregation with filtering
    valid_yields = [y for y in efficiency_log if y > 15]
    base_yield = sum(valid_yields)
    
    # Bonus logic: if more than 2 high-yield zones, add bonus
    bonus = 10 if len(valid_yields) > 2 else 0
    
    # Key answer computation
    final_yield = int(base_yield + bonus)
    
    # Dead code path - never executed due to prior filtering
    if False and sum(efficiency_log) < 10:
        final_yield -= 5
        
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Input data
    area_metrics = [8, 12, 15, 9]
    temperature_data = [22, 26, 28, 24, 27]
    moisture_index = 0.8
    element_trace = [3, 6, 8, 10, 14]

    # Distractor function calls
    soil_analysis = analyze_soil_composition(element_trace)
    potential_score = calculate_growth_potential(temperature_data, moisture_index)

    # Actual key computation
    growth_cycles = [1.1, 0.9, 1.3]
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Print result as required
    print(f"Target result: {final_yield}")