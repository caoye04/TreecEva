def analyze_reactor_metrics(energy_log, threshold=0.75):
    cumulative_stress = 0
    peak_margins = []
    for idx, (power_level, temp) in enumerate(energy_log):
        stress_ratio = power_level / (temp + 1e-5)
        if stress_ratio > threshold:
            cumulative_stress += stress_ratio
            peak_margins.append((idx, stress_ratio))
    return cumulative_stress, peak_margins


def calculate_dynamic_offset(sequence):
    offset = 0
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            offset += val ** 0.5
        elif i % 3 == 1:
            offset -= val // 2
        else:
            offset ^= int(val)
    return offset

# Irrelevant data transformation (dead path)
def compute_buffer_score(data):
    score = 0
    for x in data:
        score += x * 2 if x > 5 else -x
    return score

# Decoy function with misleading name
def adjust_thermal_rating(flux, eff):
    # This function looks complex but only uses basic arithmetic
    base_rating = flux * eff
    penalty = 0
    if eff < 0.8:
        penalty = base_rating * 0.15
    adjusted = base_rating - penalty
    
    # Red herring: unused intermediate values
    dummy_factor = adjusted ** 2 + 17
    shadow_buffer = [adjusted * i for i in range(3)]
    debug_trace = {"level": 9, "mode": "simulated", "value": dummy_factor}
    
    return adjusted

# Unused helper that mimics relevant logic
def evaluate_core_stability(readings):
    total = 0
    for r in readings:
        total += r[0] * r[1]
    return total / len(readings) if readings else 0

# Main simulation block
if __name__ == "__main__":
    # Real input data
    reactor_trace = [(1.2, 300), (0.8, 280), (1.5, 310), (0.9, 290)]
    signal_sequence = [4, 9, 2, 7, 1]
    
    # Distractor variables
    calibration_data = [6, 3, 8, 1, 4, 7]
    buffer_metrics = compute_buffer_score(calibration_data)  # Dead call
    
    # Relevant computation chain
    base_flux = 420
    efficiency_factor = 0.85
    
    # Simulated diagnostic (irrelevant)
    stress_total, alerts = analyze_reactor_metrics(reactor_trace)
    
    # Another red herring
    dynamic_shift = calculate_dynamic_offset(signal_sequence)
    
    # Key assignment - target of the question
    thermal_capacity = adjust_thermal_rating(base_flux, efficiency_factor)
    
    # Final output (must print result in required format)
    print(f"Result: {thermal_capacity}")