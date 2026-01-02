def calculate_thermal_rating(factor, loads):
    base_rating = 42.5
    adjustment = 0.0
    peak_load = max(loads)
    load_average = sum(loads) / len(loads)
    normalized_peak = peak_load / 100.0
    
    # Distractor: voltage stability calculations (not used in final result)
    voltage_stability = 0.98
    for load in loads:
        if load > 80:
            voltage_stability -= 0.002 * (load - 80)
    voltage_stability = max(0.7, voltage_stability)
    
    # Real logic path
    if factor > 0.85:
        adjustment += 15.2
    elif factor > 0.75:
        adjustment += 8.4
    else:
        adjustment += 3.1

    # Secondary adjustment based on load pattern
    high_load_count = sum(1 for x in loads if x > 90)
    adjustment += 2.5 * high_load_count

    # Dummy state tracking (irrelevant)
    system_states = ['idle', 'active', 'peak']
    current_state = 'idle'
    for i, load in enumerate(loads):
        if load > 95 and i % 2 == 0:
            current_state = 'peak'
        elif load > 70:
            current_state = 'active'

    # Conditional expression (required Python feature)
    efficiency_bonus = 7.3 if factor * load_average > 75 else 2.9
    
    # Final calculation
    result = base_rating + adjustment + efficiency_bonus
    return round(result, 4)

# Main execution
phase_current = [88, 92, 95, 76, 81]
efficiency_factor = 0.88
voltage_rms = 230.0  # unused distractor
frequency_hz = 50.0  # unused
phase_loads = [int(curr * 1.15) for curr in phase_current]  # scaled loads

# Extraneous computation: simulate temperature drift (unused)
temp_drift = 0.0
temp_base = 25.0
for i in range(len(phase_loads)):
    temp_drift += (phase_loads[i] - 80) * 0.05
    if temp_drift > 10:
        temp_drift *= 0.95

# Key assignment statement
thermal_capacity = calculate_thermal_rating(efficiency_factor, phase_loads)

# Output result as required
print(f"Result: {thermal_capacity}")