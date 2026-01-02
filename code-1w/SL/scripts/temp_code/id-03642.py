def calculate_efficiency(sequence):
    base_level = 7
    adjustment_factor = 1.25
    spike_detected = any(x > 8 for x in sequence)
    
    # Apply conditional scaling based on spike presence
    scale = 1.5 if spike_detected else 1.0
    
    # Compute weighted contributions using slicing and lambda
    recent_data = sequence[-3:]
    weight_func = lambda i, val: (i + 1) * val
    weighted_sum = sum(weight_func(i, v) for i, v in enumerate(recent_data))
    
    # Final efficiency calculation
    efficiency_score = base_level * scale + (weighted_sum / len(recent_data)) * adjustment_factor
    return round(efficiency_score, 3)

# Sensor activation sequence over time
activation_sequence = [5, 6, 8, 9, 7]

# Irrelevant auxiliary variable (minor distraction)
status_flag = True

energy_threshold = calculate_efficiency(activation_sequence)
print(f"Result: {energy_threshold}")