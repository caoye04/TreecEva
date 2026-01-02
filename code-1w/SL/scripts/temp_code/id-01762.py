def calculate_efficiency(chain):
    base_efficiency = 85.0
    adjustment_factor = 0.9
    
    # Lambda to compute stage contribution
    contribution = lambda x: x['weight'] * (x['intensity'] / 10)
    
    total_contribution = sum(contribution(stage) for stage in chain)
    
    # Set operations to identify redundant phases
    primary_phases = {1, 2, 3, 4}
    optional_phases = {3, 4, 5, 6}
    overlapping = primary_phases & optional_phases  # intersection
    
    redundancy_penalty = len(overlapping) * 1.5
    
    final_score = base_efficiency * adjustment_factor - redundancy_penalty + (total_contribution / 10)
    return round(final_score, 3)

# Process definition with realistic parameters
process_chain = [
    {'weight': 2.1, 'intensity': 8},
    {'weight': 3.5, 'intensity': 6},
    {'weight': 1.8, 'intensity': 9}
]

# Irrelevant utility variable (minor distraction)
status_flag = True

# Key computation
filtration_score = calculate_efficiency(process_chain)

# Output result
print(f"Result: {filtration_score}")