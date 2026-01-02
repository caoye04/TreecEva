import itertools

# Simulated quantum error correction diagnostic system

def generate_synthetic_data(size):
    return [i ^ (i >> 2) & 1 for i in range(size)]

def compute_redundancy_pattern(base, length):
    pattern = []
    for i in range(length):
        pattern.append((base + i * 3) % 7)
    return pattern

# Irrelevant helper - distractor function
def deprecated_checksum(data):
    checksum = 0
    for val in data:
        checksum = (checksum * 31 + val) % 10007
    return checksum

# Unused transformation - dead code path
def transform_legacy_format(registers):
    transformed = {}
    for k, v in registers.items():
        transformed[f'old_{k}'] = [x << 1 for x in v]
    return transformed

# Core analysis function with embedded logic
def analyze_system_state(registers, syndrome):
    active_qubits = 0
    error_mask = 0
    
    # Extract and process register states
    for reg_name, qubit_states in registers.items():
        if 'ancilla' in reg_name:
            continue  # Ancilla registers are excluded from main count
        for bit in qubit_states:
            active_qubits += (bit & 1)
            error_mask ^= bit << 1
    
    # Compute syndrome alignment score (red herring computation)
    alignment_score = 0
    for i, s in enumerate(syndrome):
        alignment_score += abs(s - (i % 5))
    
    # Distractor: unused intermediate structure
    diagnostics_log = {
        'version': '2.1',
        'mode': 'QUANTUM_CORRECTION',
        'redundancy_check': compute_redundancy_pattern(4, 6),
        'timestamp': 1625094889,
        'debug_flag': False
    }
    
    # Real processing begins: filter non-ancilla registers
    filtered_values = []
    for name, values in registers.items():
        if not name.startswith('ancilla'):
            filtered_values.extend(values)
    
    # Apply modular transformation on filtered data
    transformed = [(val * 2 + 1) % 13 for val in filtered_values if val % 2 == 1]
    
    # Accumulate using bitwise interactions
    accumulator = 0
    for val in transformed:
        accumulator = (accumulator << 1) ^ val
    
    # Introduce set-based interference
    unique_remainders = set()
    for val in transformed:
        unique_remainders.add(val % 4)
    
    # Another red herring: complex but unused dictionary aggregation
    metadata_aggregate = {
        f'group_{i}': list(itertools.islice(itertools.cycle([1,2]), i*2)) 
        for i in range(1, 4)
    }
    
    # Critical logic step: combine accumulator with syndrome characteristics
    syndrome_key = sum(s % 3 for s in syndrome) * len([s for s in syndrome if s > 2])
    
    # Final diagnostic depends only on these two values
    final_diagnostic = accumulator + syndrome_key * 17
    
    # Decoy output - looks important but unused
    noise_floor = (len(transformed) + len(unique_remainders)) / 7.0
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Initialize quantum registers (simulated)
    quantum_registers = {
        'data_a': [1, 0, 1, 1],
        'data_b': [0, 1, 1, 0],
        'ancilla_x': [1, 1, 0, 0],
        'ancilla_y': [0, 0, 1, 1],
        'syndrome_reg': [1, 0, 1, 0]
    }
    
    # Generate error syndrome
    error_syndrome = generate_synthetic_data(8)
    
    # Perform diagnostic analysis
    final_diagnostic = analyze_system_state(quantum_registers, error_syndrome)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")