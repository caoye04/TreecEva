def calculate_thermal_output(efficiency, state):
    base_rate = 17.3
    adjustment = 0.85 if state == 'liquid' else 1.42
    
    # Irrelevant intermediate calculation (distractor)
    pressure_offset = 2.1 * (efficiency + 0.1)
    flow_resistance = efficiency ** 2 - 0.05
    
    # Semi-relevant pre-check
    if efficiency < 0.6:
        return -1
    
    # Main computation path
    raw_output = base_rate * efficiency * adjustment
    
    # Additional irrelevant logic
    status_flags = []
    if raw_output > 20:
        status_flags.append('HIGH_LOAD')
    elif raw_output < 10:
        status_flags.append('LOW_UTIL')

    # More distraction: string-based validation not affecting result
    validation_code = "CHK" + str(int(efficiency * 100))
    if validation_code.startswith("CHK") and len(validation_code) == 5:
        pass  # Placeholder for future logic

    # Final adjustment using conditional expression
    thermal_rating = raw_output if raw_output >= 15 else raw_output * 1.15
    
    return thermal_rating

# Simulation parameters
initial_temp = 298.15
phase_state = 'liquid'
efficiency_factor = 0.78

# Dead code path (distractor)
if initial_temp > 300:
    efficiency_factor *= 0.95
elif initial_temp < 290:
    efficiency_factor *= 1.05

# Auxiliary variable with no impact
redundant_metric = (initial_temp / 100) ** 2

# Key computation
thermal_capacity = calculate_thermal_output(efficiency_factor, phase_state)

# Print final result as required
print(f"Result: {thermal_capacity}")