import math

# Simulated industrial thermal processing sequence
def generate_phase_data():
    raw_phases = ['alpha', 'beta', 'gamma']
    phase_map = {p: idx + 1 for idx, p in enumerate(raw_phases)}
    phase_weights = [0.85, 1.15, 0.92]
    return phase_map, phase_weights

# Irrelevant signal processing decoy function
def analyze_signal(noise_level=0.05):
    samples = [math.sin(x * 0.1) + noise_level * x for x in range(100)]
    filtered = [s for s in samples if abs(s) > 0.1]
    avg_noise = sum(filtered) / len(filtered) if filtered else 0
    return avg_noise  # Dead-end, never used

# Misleading energy accumulator with red herring logic
def accumulate_energy(nodes):
    total = 0
    for node in nodes:
        if node % 3 == 0:
            total += node ** 2
        elif node % 5 == 0:
            total -= node * 1.5
    return total * 0.1  # Computationally isolated

# Core calculation with nested dependencies
def transform_sequence(seq, key_offset):
    shifted = [(x + key_offset) * 0.75 for x in seq]
    processed = []
    for val in shifted:
        if val > 2.0:
            processed.append(math.log(val) * 1.5)
        elif val > 1.0:
            processed.append(val ** 1.2)
        else:
            processed.append(val + math.sqrt(abs(val)))
    return processed

def evaluate_stability(risk_profile):
    baseline = 100.0
    adjustments = []
    for level in risk_profile:
        if level < 2:
            adjustments.append(baseline * 0.05)
        elif level < 4:
            adjustments.append(baseline * 0.15)
        else:
            adjustments.append(baseline * 0.35)
    net_risk = sum(adjustments) / len(adjustments) if adjustments else 0
    return net_risk  # Distractor: looks important but unused later

def calculate_thermal_output(process_sequence):
    base_modifier = 1.618
    temp_grid = [[i * j for j in range(1, 5)] for i in range(1, 6)]
    flat_grid = [item for row in temp_grid for item in row]
    grid_correction = sum(flat_grid) / 100.0

    # Real computation path starts here
    phase_lookup, weights = generate_phase_data()
    indices = [phase_lookup[p] for p in process_sequence if p in phase_lookup]
    
    # Apply transformation with offset
    transformed = transform_sequence(indices, key_offset=2)
    
    # Weighted aggregation
    weighted_sum = 0
    for i, t_val in enumerate(transformed):
        weight = weights[i % len(weights)]
        weighted_sum += t_val * weight * base_modifier
    
    # Final adjustment using grid correction (only relevant use)
    result = weighted_sum - grid_correction
    
    # Decoy variables and operations below
    dummy_nodes = [7, 9, 15, 18, 21]
    decoy_energy = accumulate_energy(dummy_nodes)
    signal_trace = analyze_signal(0.08)
    stability_metric = evaluate_stability([3, 1, 4, 1, 5])
    
    # Critical assignment
    thermal_capacity = result  # This is the target variable
    return thermal_capacity

# Execution block
if __name__ == "__main__":
    sequence_log = ['beta', 'gamma', 'alpha', 'beta']
    diagnostic_mode = True
    
    # Simulated calibration (irrelevant)
    if diagnostic_mode:
        calib_values = [x * 0.1 for x in range(10)]
        norm_factor = sum([math.exp(-v) for v in calib_values])
    
    # Key execution point
    thermal_capacity = calculate_thermal_output(sequence_log)
    
    # Output result as required
    print(f"Result: {thermal_capacity}")