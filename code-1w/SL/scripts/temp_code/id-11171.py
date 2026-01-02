def calculate_thermal_output(stages):
    base_multiplier = 1.5
    adjustment_factor = 0.8
    transient_loss = 0.05
    efficiency_log = []
    cumulative_heat = 0
    
    for stage in stages:
        phase_id = stage[0]
        duration = stage[1]
        temperature = stage[2]
        pressure = stage[3]
        
        # Irrelevant intermediate calculation (distractor)
        theoretical_yield = duration * temperature / (pressure + 1) if pressure > 0 else 0
        efficiency_score = (temperature / 100) ** 0.5
        
        # Semi-relevant adjustment (only efficiency_score is used later)
        if efficiency_score > 0.9:
            efficiency_log.append((phase_id, efficiency_score))
        
        # Core computation path
        heat_contribution = duration * base_multiplier * efficiency_score
        cumulative_heat += heat_contribution
    
    # Misleading dead-end function (never called)
    def apply_safety_margin(value):
        return value * 0.95
    
    # Another distractor: complex list comprehension with no impact
    hypothetical_stages = [(t[0], t[1]*2) for t in stages if t[2] > 200]
    stage_complexity_index = sum([len(hypothetical_stages) * i for i in range(2)])

    final_adjustment = adjustment_factor * (1 - transient_loss)
    raw_output = cumulative_heat * final_adjustment
    
    # Actual answer derivation
    thermal_capacity = int(raw_output // 1)  # floor to integer
    return thermal_capacity

# Simulation parameters for industrial thermal process
process_stages = [
    ('ignition', 120, 250, 8),
    ('burn', 180, 400, 12),
    ('stabilize', 90, 320, 10),
    ('cool_down', 150, 180, 6)
]

# Extra unused variables (distractors)
baseline_readings = [23.5, 45.1, 67.3]
emergency_threshold = 999
calibration_sequence = tuple(range(5, 50, 5))

thermal_capacity = calculate_thermal_output(process_stages)
print(f"Result: {thermal_capacity}")