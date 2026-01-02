from itertools import compress, cycle

def analyze_efficiency(rates):
    avg = sum(rates) / len(rates)
    return [r > avg for r in rates]

def calculate_thermal_output(stages):
    base_multiplier = 1.75
    adjustment_factor = 0.89
    temp_result = 0
    
    # Simulate stage processing with conditional logic and accumulation
    for i, (temp, pressure, phase) in enumerate(stages):
        if phase == 'liquid':
            contribution = temp * (pressure ** 0.5) * base_multiplier
        elif phase == 'gas':
            contribution = temp * (1 + pressure / 100) * adjustment_factor
        else:
            contribution = temp * 0.5
            
        # Irrelevant filtering (distractor)
        status_flags = [True, False, True, True, False]
        valid_contributions = list(compress([contribution] * 5, status_flags))
        
        temp_result += contribution if i % 2 == 0 else contribution * 0.95
    
    # Dead code path (distractor)
    final_cycle = cycle([1, 2])
    for _ in range(3):
        next(final_cycle)
    
    # Real computation continues
    scaling_sequence = [1.1, 0.9, 1.05, 0.95]
    applied_scale = sum(scaling_sequence) / len(scaling_sequence)
    
    return temp_result * applied_scale

# Main data setup
process_stages = [
    (300, 10, 'liquid'),
    (420, 25, 'gas'),
    (380, 18, 'liquid'),
    (510, 40, 'gas'),
    (290, 5, 'solid')
]

# Auxiliary variables (some irrelevant)
baseline_energy = 1250
reference_points = {300, 420, 380, 510, 290}
outlier_check = max(reference_points) - min(reference_points) > 200  # distractor

# Secondary calculation not affecting main result
stability_index = sum(pressure for _, pressure, _ in process_stages) / len(process_stages)
efficiency_mask = analyze_efficiency([88, 92, 85, 94, 83])  # unused later

# Key execution point
thermal_capacity = calculate_thermal_output(process_stages)

# Print result as required
print(f"Result: {thermal_capacity}")