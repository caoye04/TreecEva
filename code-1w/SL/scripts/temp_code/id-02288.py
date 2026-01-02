def analyze_production_efficiency():
    base_units = [12, 15, 14, 18, 20, 13]
    adjustment_factors = [0.9, 1.1, 1.0, 0.95, 1.05, 1.0]
    
    # Irrelevant preprocessing: reverse and scale factors (not used in final computation)
    reversed_factors = [f * 0.5 for f in reversed(adjustment_factors)]
    temp_sum = sum(reversed_factors)
    avg_adjustment = temp_sum / len(reversed_factors)  # Distractor variable
    
    # Real computation begins
    total_output = 0
    cycle_time = 0
    
    # Simulate production cycles with side-effect-free enumeration
    for idx, unit in enumerate(base_units):
        cycle_time += 2  # Each unit takes 2 time units
        if unit > 14:
            bonus = 1
        else:
            bonus = 0
        adjusted_unit = unit * adjustment_factors[idx] + bonus
        total_output += int(adjusted_unit)
    
    # Secondary loop to calculate auxiliary metric (unused)
    peak_index = 0
    max_val = base_units[0]
    for i, val in enumerate(base_units):
        if val > max_val:
            max_val = val
            peak_index = i
    
    # Efficiency formula uses only total_output and cycle_time
    efficiency_score = total_output / (cycle_time * 0.75)
    
    # Additional red herring: zipping unrelated sequences
    synthetic_data = list(zip(base_units, [x**2 for x in range(len(base_units))]))
    dummy_accum = 0
    for a, b in synthetic_data:
        dummy_accum += a % (b + 1)  # Dead-end calculation
    
    # Final result output
    print(f"Result: {efficiency_score}")
    return efficiency_score

# Execute function
analyze_production_efficiency()