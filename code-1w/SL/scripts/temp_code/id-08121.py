def analyze_system_performance(input_loads, threshold=0.75):
    adjusted_loads = [load * 1.08 for load in input_loads if load > 50]
    
    # Irrelevant tracking variables (distractors)
    stability_log = []
    fluctuation_count = 0
    baseline_reference = sum(input_loads) / len(input_loads)

    for i, load in enumerate(adjusted_loads):
        if load > baseline_reference * 1.2:
            fluctuation_count += 1
        stability_log.append(fluctuation_count)

    # Semi-relevant transformation
    normalized = [max(0, min(1, (x - 50) / 100)) for x in adjusted_loads]
    
    # Efficiency calculation with red herring operations
    total_efficiency = 0.0
    penalty_factor = 0.92
    for norm in normalized:
        if norm > 0.5:
            total_efficiency += norm * 0.85
        else:
            total_efficiency += norm * 0.65
    
    # Dummy loop - misleading but harmless
    convergence_step = 1.0
    for _ in range(3):
        convergence_step *= 0.98

    efficiency_ratio = total_efficiency / len(normalized) if normalized else 0
    return efficiency_ratio if efficiency_ratio >= threshold else 0.5 * efficiency_ratio


def calculate_thermal_output(loss_profile):
    base_scalar = 29.0
    modifier = 1.75
    
    # Complex but partially irrelevant unpacking and assignment
    readings = [12, 18, 24, 36]
    a, b, c, d = readings
    offset_correction = (a + b) * 0.05 - (c - d) * 0.02
    
    # List comprehension with side-effect-free complexity
    derived_factors = [x ** 0.5 for x in readings if x % 6 == 0]
    factor_sum = sum(derived_factors) + offset_correction
    
    # Core computation mixed with noise
    temp_buffer = []
    for val in derived_factors:
        temp_buffer.append(val * 1.1)
    
    # Dead code path (never used)
    final_verification = False
    if len(temp_buffer) > 10:
        final_verification = True

    # Actual answer-determining line
    thermal_output = base_scalar * loss_profile * modifier * factor_sum
    return int(thermal_output)

# Main execution sequence
initial_loads = [45, 60, 70, 80, 55]
efficiency_losses = analyze_system_performance(initial_loads)
thermal_capacity = calculate_thermal_output(efficiency_losses)
print(f"Target result: {thermal_capacity}")