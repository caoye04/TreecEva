import itertools

def analyze_soil_composition(terrain):
    # Irrelevant analysis with no impact on final result
    ph_levels = [7.2, 6.8, 7.5, 6.9]
    nutrient_score = 0
    for val in ph_levels:
        nutrient_score += (val * 1.5) % 4
    return nutrient_score  # Not used in main logic

def validate_irrigation(system_status):
    # Distractor function: looks important but unused
    if all(system_status) and len(system_status) > 3:
        return sum([i * 0.7 for i in range(len(system_status))])
    return 0

def calculate_harvest_efficiency(layout, cycles):
    total_yield = 0
    bonus_multiplier = 1.0
    decay_factor = 0.95
    
    # Simulate multiple growth cycles across field zones
    for cycle in range(cycles):
        temp_yield = 0
        for i, row in enumerate(layout):
            for j, crop_density in enumerate(row):
                # Core calculation logic
                base_productivity = (i + 1) * (j + 1) * crop_density
                if (i + j) % 2 == 0:
                    base_productivity *= 1.2  # Sunlight advantage
                temp_yield += base_productivity
        
        # Apply decay over time and accumulate
        temp_yield *= (decay_factor ** cycle)
        total_yield += int(temp_yield)
        
        # Conditional bonus logic (only triggers once)
        if cycle == 2 and total_yield > 300:
            bonus_multiplier = 1.3
    
    # Final adjustment using itertools.chain to flatten layout (real use)
    flat_layout = list(itertools.chain.from_iterable(layout))
    max_density = max(flat_layout)
    min_density = min(flat_layout)
    spread_penalty = (max_density - min_density) * 5
    
    # Introduce irrelevant intermediate calculations
    avg_temp = 22.5
    humidity_factor = (avg_temp / 100) * 1.8  # Unused in result
    dew_points = [avg_temp - 2 for _ in range(5)]  # Dead code data
    
    final_yield = int((total_yield * bonus_multiplier) - spread_penalty)
    return final_yield

# Main execution
field_layout = [
    [3, 5, 2],
    [4, 6, 3],
    [2, 4, 5]
]
growth_cycles = 4

# Call irrelevant functions (distractor calls)
soil_analysis = analyze_soil_composition(field_layout)
irrigation_check = validate_irrigation([True, True, False, True])

# Key statement
final_yield = calculate_harvest_efficiency(field_layout, growth_cycles)

print(f"Result: {final_yield}")