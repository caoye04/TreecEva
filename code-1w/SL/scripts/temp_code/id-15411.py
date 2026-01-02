def calculate_thermal_capacity(efficiency, state):
    base_capacity = 120.5
    modifier = 1.0
    
    # Conditional expression for phase-based adjustment
    modifier = 0.8 if state == 'solid' else (1.1 if state == 'liquid' else 1.3)
    
    # Irrelevant computation - red herring
    theoretical_max = base_capacity * 2.718
    temp_adjustment = (theoretical_max / 10) * 0.91
    
    # Relevant capacity calculation
    adjusted_capacity = base_capacity * modifier
    
    # State-dependent efficiency tuning (only some branches matter)
    if efficiency > 0.85:
        adjusted_capacity *= 1.05
    elif efficiency > 0.75:
        adjusted_capacity *= 1.02
    else:
        adjusted_capacity *= 0.97  # Dead code path (efficiency will be high)

    # Extra distraction: unused function call simulation
    diagnostic_trace = [base_capacity, modifier, efficiency]
    trace_mean = sum(diagnostic_trace) / len(diagnostic_trace)

    # Final nonlinear correction based on operational load
    load_factor = 0.9 + (efficiency * 0.1)
    return round(adjusted_capacity * load_factor, 4)

# Simulation parameters
initial_temperature = 293.15
pressure_kpa = 101.3
phase_state = 'liquid'
efficiency = 0.88

# Unused sensor readings - distractor variables
sensor_array = [0.12, 0.09, 0.11, 0.13]
sensor_bias = sum(sensor_array) / 4

calibration_offset = 0.0034
reference_voltage = 3.3

# Key computational chain
if phase_state in ['liquid', 'gas']:
    stability_index = efficiency * 1.07
    if stability_index > 0.9:
        # Nested condition with side computation
        safety_margin = 1.02
        contingency_buffer = stability_index * 0.05
    else:
        safety_margin = 1.0

    # Critical statement
    thermal_capacity = calculate_thermal_capacity(efficiency, phase_state)

    # Post-processing with irrelevant transformations
    normalized_output = thermal_capacity / reference_voltage
    scaled_display = int(normalized_output * 100)

print(f"Result: {thermal_capacity}")