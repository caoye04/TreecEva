def calculate_thermal_output(sequence):
    base_factor = 1.75
    adjustment = 0.93
    temp_result = 0
    accumulator = 0
    
    for step in sequence:
        phase_id, intensity, duration = step
        
        # Irrelevant signal processing simulation (distractor)
        signal_noise = (intensity * 0.07) % 0.5
        filtered_signal = intensity - signal_noise
        
        if phase_id == 'A':
            temp_result += intensity ** 1.2 * duration
        elif phase_id == 'B':
            temp_result += intensity * (duration ** 0.8) * 1.1
        else:
            temp_result += intensity * duration * 0.75

    # Secondary loop with semi-relevant computation (adds cognitive load)
    scaling_factor = 1.0
    for _ in range(3):
        scaling_factor *= 0.98 + (scaling_factor * 0.02)
    
    # Dummy state tracking variables (dead code path)
    last_state = None
    transition_log = []
    for s in sequence:
        if s[0] != last_state:
            transition_log.append(f"Switch to {s[0]}")
        last_state = s[0]
    
    # Actual core computation wrapped in conditional expression
    efficiency_mode = len(sequence) > 4
    final_multiplier = 1.25 if efficiency_mode else 0.88
    
    accumulator = temp_result * base_factor * final_multiplier * adjustment
    
    # Additional red herring: unused heat dissipation calculation
    surface_area = 2.4
    dissipation_rate = surface_area * 0.11
    theoretical_loss = accumulator * 0.03  # Not subtracted
    
    return int(accumulator)

# Simulated industrial thermal process steps
process_sequence = [
    ('A', 12, 5),
    ('B', 8, 7),
    ('A', 15, 3),
    ('C', 10, 6),
    ('B', 9, 8),
    ('A', 11, 4)
]

# Key execution point
thermal_capacity = calculate_thermal_output(process_sequence)
print(f"Result: {thermal_capacity}")