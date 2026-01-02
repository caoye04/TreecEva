def evaluate_component_health(age, usage_cycles):
    degradation_factor = 0.98 ** age
    cycle_penalty = 1 - (usage_cycles / 10000)
    return degradation_factor * cycle_penalty

def analyze_signal_integrity(signal, noise):
    snr = signal / (noise + 1e-5)
    distortion = abs(signal - noise) * 0.01
    return snr > 15 and distortion < 0.5

def generate_phase_sequence(seed_value):
    sequence = []
    temp = seed_value
    for _ in range(6):
        temp = (temp * 7 + 13) % 19
        sequence.append(temp)
    # Distractor: unused transformation
    reversed_seq = [x * 2 for x in sequence if x % 2 == 0]
    return sequence

def evaluate_system_stability(threshold, phases):
    base_score = 0
    adjustment = 1.0
    
    for i, p in enumerate(phases):
        if i % 2 == 0:
            base_score += p * (i + 1)
        else:
            base_score -= p // 2
    
    # Semi-relevant computation with conditional expression
    health_status = 'stable' if base_score > threshold else 'unstable'
    modifier = 1.25 if health_status == 'stable' else 0.75
    
    # Additional logic with recursion
    def recursive_weight(n):
        return 1 if n <= 1 else n + recursive_weight(n - 2)
    
    weight_factor = recursive_weight(len(phases))
    
    # Irrelevant diagnostic trace
    diagnostics = []
    for idx in range(len(phases)):
        diag_val = (phases[idx] ^ idx) % 5
        diagnostics.append(f'D{idx}:{diag_val}')
    
    # Core calculation
    raw_rating = base_score * modifier * weight_factor
    
    # Dead code path - misleading but syntactically present
    if False:
        raw_rating = sum(diagnostics)  # unreachable
    
    # Final adjustment using conditional expression
    pressure_rating = int(raw_rating) if raw_rating >= 0 else -int(abs(raw_rating))
    
    return pressure_rating

# Main execution flow
sensor_age = 4
operational_cycles = 8700
signal_strength = 23.5
background_noise = 1.2

# Distractor variables
thermal_load = sensor_age * operational_cycles / 100
voltage_spike_risk = (signal_strength > 20) and (background_noise < 2)

# Real data initialization
health_metric = evaluate_component_health(sensor_age, operational_cycles)
logic_threshold = 40 if health_metric > 0.8 else 55

phase_sequence = generate_phase_sequence(3)

# Key statement
pressure_rating = evaluate_system_stability(logic_threshold, phase_sequence)

# Output result
print(f"Result: {pressure_rating}")