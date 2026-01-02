import math

# Simulate agricultural yield prediction with noise and irrelevant transformations
def generate_noise_factor(size):
    return [math.sin(i * 0.1) + abs(math.cos(i * 0.05)) for i in range(size)]

def deprecated_scaling(values):
    # Dead function - never used but looks relevant
    return [v * 1.75 for v in values]

def compute_thermal_index(temps):
    # Irrelevant computation path
    base = sum(t ** 0.8 for t in temps)
    return base / len(temps)

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

def accumulate_growth_phases(cycles):
    # Accumulates growth phase weights using list comprehension and transformation
    weights = [0.3, 0.5, 0.7, 1.0, 0.8, 0.4]
    total_per_cycle = []
    for cycle in cycles:
        weighted_sum = sum(w * g for w, g in zip(weights, cycle[:6]))
        total_per_cycle.append(weighted_sum)
    return total_per_cycle

def calculate_harvest_efficiency(metrics, cycles):
    # Core logic hidden among distractions
    filtered_areas = filter_outliers(metrics['areas'])
    avg_area = sum(filtered_areas) / len(filtered_areas)
    
    # Distractor: thermal processing (not actually related)
    dummy_temp_impact = compute_thermal_index(metrics['temperatures'])
    adjusted_by_heat = [a * (1 + dummy_temp_impact * 0.01) for a in filtered_areas]
    
    # Real logic begins here
    raw_yields = metrics['yields']
    normalized_yields = [y / a for y, a in zip(raw_yields, metrics['areas'])]  # yield per unit area
    
    # Apply growth cycle accumulation
    cycle_contributions = accumulate_growth_phases(cycles)
    composite_multiplier = sum(cycle_contributions) / len(cycle_contributions)
    
    # Final efficiency calculation
    base_efficiency = sum(normalized_yields) / len(normalized_yields)
    final_efficiency = base_efficiency * composite_multiplier
    
    # Red herring variables
    phantom_correction = sum(generate_noise_factor(10)) * 0.05
    final_efficiency += phantom_correction  # misleading adjustment
    
    # Key result
    final_yield = final_efficiency * avg_area
    
    # Unused complex expression to mislead
    _ = [math.log(1 + x) for x in adjusted_by_heat if x > 0]
    
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Input data setup
    area_metrics = {
        'areas': [120, 135, 110, 150, 140, 130, 160, 115],
        'yields': [480, 520, 400, 600, 560, 500, 620, 450],
        'temperatures': [28, 31, 26, 33, 30, 29, 32, 27]
    }
    
    growth_cycles = [
        [2.1, 3.0, 4.2, 5.1, 4.8, 3.9],
        [2.3, 3.1, 4.0, 5.3, 4.9, 4.0],
        [2.0, 2.9, 4.3, 5.0, 4.7, 3.8],
        [2.2, 3.2, 4.1, 5.2, 4.8, 3.9],
        [2.1, 3.0, 4.2, 5.1, 4.8, 3.9],
        [2.0, 2.9, 4.1, 5.0, 4.6, 3.7],
        [2.3, 3.1, 4.0, 5.3, 4.9, 4.0],
        [2.1, 3.0, 4.2, 5.1, 4.8, 3.9]
    ]
    
    # These variables look important but are unused in final path
    soil_ph_levels = [6.2, 6.5, 5.9, 6.8, 6.4, 6.3, 6.6, 6.1]
    rainfall_data = [110, 130, 95, 140, 125, 115, 135, 100]
    
    # Execution point of interest
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Output result
    print(f"Result: {final_yield}")