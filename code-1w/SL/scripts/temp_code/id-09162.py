def analyze_system_state(readings, calib):
    # Preprocess: filter valid quantum states
    valid_states = {x for x in readings if x % 3 == 0}
    adjusted = [x ^ calib['offset'] for x in readings]

    # Irrelevant transformation (distractor)
    transformed = [abs(x - calib['baseline']) ** 2 for x in adjusted]
    avg_transformed = sum(transformed) / len(transformed)  # Not used later

    # State aggregation with modular arithmetic
    state_sum = 0
    for i, val in enumerate(adjusted):
        if i % 2 == 0:
            state_sum += val % calib['modulus']
        else:
            state_sum -= val % calib['modulus']

    # Conditional logic with bitwise masking
    mask = calib['safety_mask']
    masked_sum = state_sum & mask

    # Secondary check: unused health score (distractor)
    health_score = 0
    for v in valid_states:
        if v > 50:
            health_score += 1
        elif v < 10:
            health_score -= 1  # Dead code path due to data

    # Final diagnostic computation
    critical_flag = len(valid_states) > 0 and masked_sum > 0
    scaling_factor = 1.5 if critical_flag else 0.5
    
    final_diagnostic = int((masked_sum + len(valid_states)) * scaling_factor)
    
    # Output required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
quantum_readings = [12, 15, 18, 21, 44, 73]
calibration_data = {
    'offset': 7,
    'baseline': 5,
    'modulus': 10,
    'safety_mask': 15
}

# Execute
analyze_system_state(quantum_readings, calibration_data)