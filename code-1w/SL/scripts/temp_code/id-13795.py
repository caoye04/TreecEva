import math

# Simulated quantum register diagnostics with extensive irrelevant processing
def initialize_quantum_stack():
    base_states = [1, 0, 1, 1]
    padding = [0] * 4
    return base_states + padding

def calculate_coherence_score(state):
    # Irrelevant coherence metric (red herring)
    score = 0
    for i in range(len(state)):
        if state[i] == 1:
            score += math.sin(i) ** 2
    return round(score, 6)

def apply_hamiltonian_noise(registers):
    # Distractor function - modifies but not used in final result
    noise_level = 0.05
    perturbed = []
    for r in registers:
        perturbed.append(r + int(noise_level * 100))
    return perturbed

def validate_register_integrity(registers):
    # Dead code path - looks important but unused
    checksum = sum(registers) % 7
    expected = 5
    return checksum == expected

def extract_entanglement_pairs(registers):
    # Complex-looking but irrelevant data transformation
    pairs = {}
    for i in range(len(registers) - 1):
        key = f"q{i}:q{i+1}"
        value = (registers[i] ^ registers[i+1]) & 1
        pairs[key] = value
    return pairs

def compute_decoherence_trace(registers):
    # Another misleading intermediate calculation
    trace = 0
    factor = 1
    for i, val in enumerate(registers):
        if i % 3 == 0:
            trace += val * (factor + i)
            factor *= 2
    return trace * 0.1

def analyze_system_state(registers):
    # Core logic embedded within distractions
    
    # Irrelevant preprocessing
    temp_snapshot = [x * 2 for x in registers]
    temporal_weight = len(temp_snapshot) if temp_snapshot else 1
    
    # Real computation begins
    activation_chain = 0
    for idx, bit in enumerate(registers):
        if bit:  # Only when bit is 1
            contribution = (idx + 1) * ((idx + 1) + 1) // 2  # Triangular number
            activation_chain += contribution
    
    # Conditional expression (required feature)
    scaling_factor = 3 if activation_chain > 10 else 1
    activation_chain *= scaling_factor
    
    # Dictionary operations (required feature)
    metrics = {
        'initial_sum': sum(registers),
        'length': len(registers),
        'activation': activation_chain,
        'derived_key': activation_chain // 4
    }
    
    # More decoy logic
    if metrics['initial_sum'] > 5:
        adjustment = 0
        for k in range(metrics['length']):
            adjustment += (k * metrics['initial_sum']) % 4
        metrics['phantom_adjustment'] = adjustment
    
    # Final relevant transformation
    diagnostic_value = metrics['activation'] - metrics['initial_sum']
    
    # Nested conditional with red herring branches
    if diagnostic_value % 7 == 0:
        diagnostic_value //= 7
    elif diagnostic_value > 50:
        diagnostic_value -= 25
    else:
        diagnostic_value += 10
    
    # Critical assignment point
    final_diagnostic = diagnostic_value
    
    # Unused complex structure (distractor)
    debug_log = {
        'states': registers.copy(),
        'pairs': extract_entanglement_pairs(registers),
        'noise_profile': apply_hamiltonian_noise(registers),
        'coherence': calculate_coherence_score(registers)
    }
    
    return final_diagnostic

# Main execution flow
quantum_registers = initialize_quantum_stack()

# Irrelevant transformations
quantum_registers = [x ^ 1 for x in quantum_registers]  # Flip bits (but then overwritten)
quantum_registers = initialize_quantum_stack()  # Reset to original

# Apply meaningless shift
shifted = [(x + 2) % 3 for x in quantum_registers]

# Reassign back (no change)
quantum_registers = [x for x in quantum_registers]

# Actual key computation
final_diagnostic = analyze_system_state(quantum_registers)

print(f"Result: {final_diagnostic}")