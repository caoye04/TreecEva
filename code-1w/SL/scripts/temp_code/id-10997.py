def calculate_workload(phases):
    base_capacity = 0
    temp_buffer = []
    total_phases = len(phases)
    phase_weights = [0] * total_phases
    
    for i, phase in enumerate(phases):
        weight = len(phase.strip())
        if weight % 2 == 0:
            weight += 3
        else:
            weight -= 1
        phase_weights[i] = weight
        base_capacity += weight

    # Irrelevant normalization (distractor)
    max_weight = max(phase_weights) if phase_weights else 1
    normalized = [w / max_weight for w in phase_weights]
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0

    # Simulate data reshaping (semi-relevant)
    reshaped = []
    for idx, val in enumerate(phase_weights):
        reshaped.append((idx + 1) * (val % 4))
    
    # Dead code: unused helper logic
    def smooth_data(arr):
        return [sum(arr[i:i+3]) / 3 for i in range(len(arr) - 2)]
    
    # Efficiency determined by string pattern analysis
    control_flag = "ENABLED"
    flag_lower = control_flag.lower()
    flag_chars = list(flag_lower)
    flag_sum = sum(ord(c) for c in flag_chars)
    efficiency_modifier = flag_sum % 17

    # Key computation chain
    scaling_factor = 1.0
    if efficiency_modifier > 10:
        scaling_factor = 1.2
    elif efficiency_modifier > 5:
        scaling_factor = 1.1
    else:
        scaling_factor = 0.95

    # Auxiliary tracking (irrelevant)
    status_log = []
    for i in range(total_phases):
        status_log.append(f"Phase {i+1}: Processed")

    # String-based switch simulation
    mode_str = "performance_mode"
    segments = mode_str.split("_")
    mode_key = ''.join([s[0].upper() for s in segments])

    adjustment = 0
    if mode_key == "PM":
        adjustment = 5
    else:
        adjustment = -3

    # Core state variables
    raw_total = base_capacity + efficiency_modifier
    adjusted_total = raw_total + adjustment
    efficiency_factor = (adjusted_total / (total_phases or 1)) * scaling_factor

    # Final load calculation — critical execution point
    final_load = base_capacity * efficiency_factor // 2

    print(f"Result: {final_load}")
    return final_load

# Inputs
work_phases = ['  initialize ', 'run_diagnostic', ' calibrate  ', 'execute_cycle']
calculate_workload(work_phases)