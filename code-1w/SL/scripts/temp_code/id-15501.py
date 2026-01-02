def analyze_system_load(inputs):
    peak_load = 0
    transient_buffer = []
    for val in inputs:
        if val > peak_load:
            peak_load = val
        transient_buffer.append(val * 0.85)
    return peak_load

# Irrelevant signal processing function (decoy)
def process_signal(data):
    filtered = [x * 0.9 + 1.1 for x in data if x > 0]
    smoothed = []
    for i in range(1, len(filtered)):
        smoothed.append((filtered[i] + filtered[i-1]) / 2)
    return smoothed if len(smoothed) > 0 else [0]

# Unused matrix utility (dead code path)
def generate_jacobian(dim):
    matrix = [[0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = (i + 1) * (j + 1) * 0.01
    return matrix

# Core calculation with embedded distractors
def calculate_thermal_response(sequence, factor):
    base_accum = 0
    temp_offset = 0
    history_log = []
    
    # Real logic begins: simulate thermal integration over time steps
    for t in range(len(sequence)):
        raw_input = sequence[t]
        adjusted_input = raw_input * factor if factor > 0 else raw_input
        
        # Conditional expression (required language feature)
        decay_rate = 0.95 if adjusted_input > 100 else 0.98
        
        # Simulate thermal inertia
        temp_offset = (temp_offset * decay_rate) + (adjusted_input * 0.05)
        
        # Red herring: irrelevant harmonic tracking
        harmonic_tracker = (t % 7 == 0) and (adjusted_input > 50)
        if harmonic_tracker:
            temp_offset -= 2  # Minor perturbation, offset later
        
        base_accum += temp_offset
        
        # Logging irrelevant state
        if t % 10 == 0:
            history_log.append({'step': t, 'value': temp_offset})
    
    # Secondary transformation: apply non-linear correction
    non_linear_coeff = 1.0
    if base_accum > 5000:
        non_linear_coeff = 0.92
    elif base_accum < 1000:
        non_linear_coeff = 1.15
    
    final_accum = base_accum * non_linear_coeff
    
    # Distractor: unused combinatorics calculation
    combo_sum = 0
    for i in range(1, min(len(sequence), 8)):
        product = 1
        for j in range(i):
            product *= (len(sequence) - j)
        combo_sum += product // max(i, 1)
    
    # Final adjustment based on conditional logic
    calibration_shift = 3 if len(history_log) > 2 else -1
    return final_accum + calibration_shift

# Misleading initialization block
system_state = {'status': 'active', 'version': 2.1}
signal_data = [x * 1.2 + 0.5 for x in range(150) if x % 2 != 0]
processed_signal = process_signal(signal_data)

# Unused recursive function (distractor)
def count_nodes(n):
    if n <= 1:
        return 1
    return count_nodes(n-1) + count_nodes(n-2)

# Main simulation parameters
time_series = [t * 2 + (t % 5) * 3 for t in range(120)]
calibration_factor = 1.05

# Key computation step
thermal_capacity = calculate_thermal_response(time_series, calibration_factor)

# Print result as required
print(f"Result: {thermal_capacity}")