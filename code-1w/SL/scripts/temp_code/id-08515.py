def preprocess_signal(data, threshold=0.75):
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [round(x * 0.9 + 0.1, 4) for x in filtered]
    return normalized

# Irrelevant signal processing chain
temp_readings = [-0.3, 0.8, -1.2, 0.5, 1.6, -0.9]
processed_noise = preprocess_signal(temp_readings)

# Decoy diagnostic function
def evaluate_health_status(metrics):
    if sum(metrics) > 1.0:
        return "STABLE"
    else:
        return "CAUTION"

# Unused health check
dummy_metrics = [0.3, 0.4, 0.6]
health_status = evaluate_health_status(dummy_metrics)

# Core quantum register simulation
quantum_registers = [
    {'state': 'superposed', 'coherence': 0.88, 'qubits': [1, 0, 1]},
    {'state': 'entangled', 'coherence': 0.94, 'qubits': [1, 1, 0]},
    {'state': 'collapsed', 'coherence': 0.32, 'qubits': [0, 0, 0]},
    {'state': 'superposed', 'coherence': 0.77, 'qubits': [0, 1, 1]}
]

# Auxiliary mapping table (partially relevant)
state_weights = {
    'superposed': 1.2,
    'entangled': 1.8,
    'collapsed': 0.3
}

# Distractor: unused transformation matrix
transform_matrix = [[1.1, -0.2], [0.5, 1.3]]
matrix_trace = sum(transform_matrix[i][i] for i in range(2))

# Complex state analyzer with red herrings
def analyze_register(register, index):
    base_weight = state_weights.get(register['state'], 0.1)
    coherence_factor = register['coherence']
    
    # Bit manipulation on qubit array
    qubit_value = 0
    for bit in register['qubits']:
        qubit_value = (qubit_value << 1) | bit
    
    # Dummy entropy calculation (not used in final result but looks important)
    entropy = 0.0
    for bit in register['qubits']:
        if bit == 1:
            entropy += 0.693  # Approx -ln(0.5)
    
    # Actual contribution metric
    significance = base_weight * coherence_factor * (qubit_value + 1)
    
    # Red herring: phase shift calculation (unused)
    phase_shift = (index * 3.14159 / 4) % (2 * 3.14159)
    corrected_phase = phase_shift if coherence_factor > 0.5 else 0
    
    return significance, qubit_value, entropy, corrected_phase

# Secondary accumulator with misleading intermediate
consistency_score = 0
for reg in quantum_registers:
    if reg['state'] == 'superposed':
        consistency_score += reg['coherence'] * 100

# Main analysis with multiple distractions
def analyze_system_state(registers):
    total_significance = 0.0
    state_counter = {'superposed': 0, 'entangled': 0, 'collapsed': 0}
    debug_codes = []
    
    # Accumulate across registers with complex logic
    for idx, reg in enumerate(registers):
        state = reg['state']
        
        # Update counter (only partially relevant)
        if state in state_counter:
            state_counter[state] += 1
        
        # Trigger decoy function call (no side effects)
        _ = evaluate_health_status([reg['coherence']])
        
        # Real computation path
        significance, q_val, ent, phase = analyze_register(reg, idx)
        
        # Conditional accumulation (some states contribute more)
        if state == 'entangled' and q_val > 2:
            total_significance += significance * 1.5
        elif state == 'superposed':
            total_significance += significance * 1.1
        else:
            total_significance += significance * 0.4
        
        # Generate fake debug code (irrelevant)
        debug_code = f"D{idx}{q_val}{int(ent):02d}"
        debug_codes.append(debug_code)
    
    # Apply artificial penalty for collapsed states (red herring adjustment)
    collapsed_count = state_counter['collapsed']
    penalty_factor = max(0.5, 1.0 - (collapsed_count * 0.2))
    
    # Final computation - only this matters
    raw_result = total_significance * penalty_factor
    
    # Additional distraction: sort debug codes (no impact)
    sorted_debug = sorted(debug_codes, reverse=True)
    
    # Key transformation: apply logarithmic scaling
    import math
    if raw_result > 0:
        final_output = math.log(raw_result) * 100
    else:
        final_output = -50
    
    return final_output

# Execute main analysis
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Target result: {final_diagnostic}")