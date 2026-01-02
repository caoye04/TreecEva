import math

# System calibration constants (irrelevant to final result)
CALIBRATION_FACTOR = 0.987
REFERENCE_VOLTAGE = 3.3
BASELINE_NOISE = 42

# Quantum register simulation with decoherence modeling
quantum_registers = [
    {'state': 1, 'coherence': 0.88, 'error_flag': False},
    {'state': 0, 'coherence': 0.91, 'error_flag': True},
    {'state': 1, 'coherence': 0.76, 'error_flag': False},
    {'state': 1, 'coherence': 0.94, 'error_flag': False}
]

# Ancillary diagnostic tables (partially used)
diagnostic_weights = {"A": 2, "B": 3, "C": 5, "D": 7, "E": 11}
phase_shifts = {0: 1.0, 1: -1.0, 2: 0.5, 3: -0.5}

# Historical performance log (dead data - irrelevant)
historical_metrics = {
    'cycles': [992, 1001, 987, 1012],
    'errors': [3, 5, 2, 4],
    'throughput': [88.2, 89.1, 87.5, 90.3]
}

# Auxiliary functions (some unused)
def apply_hamiltonian(registers):
    total_energy = 0.0
    for r in registers:
        total_energy += r['coherence'] * (r['state'] + 1)
    return total_energy  # Not used in main path

def compute_redundancy_score(logs):
    return sum(logs['errors']) * 10  # Dead function

def evaluate_stability(register_list):
    # Irrelevant stability metric
    avg_coherence = sum(r['coherence'] for r in register_list) / len(register_list)
    unstable_count = sum(1 for r in register_list if r['coherence'] < 0.8)
    return avg_coherence > 0.85 and unstable_count == 0

def extract_active_states(registers):
    # Extract binary state vector
    return tuple(r['state'] for r in registers)

def calculate_entropy(registers):
    # Unused physics-inspired metric
    entropy = 0.0
    for r in registers:
        p = r['coherence']
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def filter_faulty_registers(registers):
    # Returns only non-error flagged registers
    return [r for r in registers if not r['error_flag']]

def map_to_syndrome(state_tuple):
    # Maps qubit state to error syndrome code
    syndrome_key = 0
    for i, bit in enumerate(state_tuple):
        syndrome_key += bit * (2 ** i)
    return diagnostic_weights.get(chr(syndrome_key % 5 + ord('A')), 1)

def adjust_for_interference(coherence_val, factor=1.02):
    # Distractor adjustment (not ultimately used)
    adjusted = coherence_val * factor
    return min(adjusted, 1.0)

def analyze_system_state(registers):
    # Core analysis with multiple steps and red herrings
    
    # Step 1: Filter out erroneous registers
    valid_registers = filter_faulty_registers(registers)
    
    # Step 2: Extract active quantum states
    active_states = extract_active_states(valid_registers)
    
    # Step 3: Compute raw operational sum (distraction)
    temp_sum = 0
    for reg in registers:
        temp_sum += reg['state'] * 10
    temp_sum = int(temp_sum * CALIBRATION_FACTOR)  # Misleading intermediate
    
    # Step 4: Calculate coherence-weighted activation
    weighted_activation = 0.0
    for vr in valid_registers:
        weighted_activation += vr['state'] * vr['coherence']
    
    # Step 5: Apply artificial normalization (red herring)
    normalized_weight = weighted_activation / (len(valid_registers) + 1e-8)
    scaled_norm = int(normalized_weight * 100)
    
    # Step 6: Generate syndrome mapping
    syndrome_code = map_to_syndrome(active_states)
    
    # Step 7: Compute bitmask from state
    state_vector = list(active_states)
    bitmask = 0
    for idx, val in enumerate(state_vector):
        if val:
            bitmask |= (1 << idx)
    
    # Step 8: Final diagnostic computation (ACTUAL ANSWER PATH)
    # Uses: bitmask, syndrome_code, and one decoy constant
    # Note: BASELINE_NOISE is a red herring; only bitmask and syndrome_code matter
    final_value = (bitmask * syndrome_code) - 17
    
    # DEAD PATH: The following would modify it but is never reached
    # if evaluate_stability(quantum_registers):
    #    final_value = int(final_value * REFERENCE_VOLTAGE)
    
    return final_value

# Execution flow
initial_check = apply_hamiltonian(quantum_registers)  # Irrelevant call
redundancy_metric = compute_redundancy_score(historical_metrics)  # Dead call

# Key execution point
final_diagnostic = analyze_system_state(quantum_registers)

# Output result
print(f"Result: {final_diagnostic}")