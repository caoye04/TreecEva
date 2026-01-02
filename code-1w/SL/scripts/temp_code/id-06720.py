def analyze_phase_shift(elements):
    shift_sum = 0
    for i, val in enumerate(elements):
        shift_sum += (val ^ i) & 3
    return shift_sum

# Irrelevant sensor array processing (dead path)
def compute_signal_noise(signal):
    noise_floor = 0
    for s in signal:
        noise_floor += abs(s - 5) * 0.1
    return noise_floor

# Unused transformation function
def transform_coordinate(x, y):
    return (x << 2) | (y >> 1)

# Core physics simulation logic
def evaluate_resonance(seq):
    resonance = 1
    for item in seq:
        resonance *= (item % 7) or 1
        if resonance > 100:
            resonance //= 3
    return resonance

# Main thermal modeling function
def process_thermal_metrics(conductivity, convectivity):
    metrics = zip(conductivity, convectivity)
    base_score = 0
    adjustment = 0
    
    # Complex but relevant computation with distractors
    for idx, (cond, conv) in enumerate(metrics):
        temp_adjust = (cond + conv) // (idx + 1) if idx != 0 else (cond + conv)
        phase_factor = analyze_phase_shift([cond, conv, idx])
        
        # Red herring: irrelevant signal processing
        signal_test = [cond * 2 + i for i in range(3)]
        noise_check = compute_signal_noise(signal_test)  # Computed but unused
        
        # Actual contribution to result
        base_score += temp_adjust * (phase_factor % 4)
        adjustment ^= (cond ^ conv)  # Bitwise red herring
    
    # Secondary evaluation using another decoy function
    dummy_coords = [(i*2, i+1) for i in range(3)]
    coord_results = [transform_coordinate(x, y) for x, y in dummy_coords]  # Dead computation
    
    # Final integration with key dependency on resonance
    conduction = [3, 5, 7, 9]
    resonance_value = evaluate_resonance(conduction)
    thermal_index = base_score // (resonance_value or 1)
    
    # Critical assignment point
    thermal_capacity = thermal_index + (adjustment & 15)  # adjustment lower bits only used
    
    return thermal_capacity

# Irrelevant global constants
electrical_threshold = 23.7
voltage_regulator = [0.1, 0.3, 0.5]

# Input data
conduction_profile = [4, 8, 6, 10]
convection_profile = [5, 7, 9, 11]

# Execution entry point
thermal_capacity = process_thermal_metrics(conduction_profile, convection_profile)

# Output result
print(f"Target result: {thermal_capacity}")