def preprocess_signal(data, threshold=0.5):
    filtered = []
    magnitude_sum = 0.0
    for x in data:
        if abs(x) > threshold:
            filtered.append(x ** 2)
            magnitude_sum += abs(x)
    normalization_factor = magnitude_sum or 1
    return [val / normalization_factor for val in filtered]


def evaluate_coherence(sequence):
    score = 0
    for i in range(len(sequence) - 1):
        score += (sequence[i] ^ sequence[i + 1]) & 3
    return score


def transform_register(registers):
    temp_result = 0
    decoy_accumulator = 0
    for reg in registers:
        temp_result ^= (reg << 1) | (reg >> 2)
        decoy_accumulator += reg * reg  # irrelevant to final result
    inverted_map = {i: (temp_result >> i) & 1 for i in range(8)}
    return temp_result


def validate_checksum(structure):
    checksum = 0
    for key, val in structure.items():
        checksum += len(key) * val
    return checksum % 7


def analyze_system_state(registers):
    # Irrelevant preprocessing chain
    raw_data = [r * 1.5 for r in registers]
    processed_data = preprocess_signal(raw_data)
    coherence = evaluate_coherence([int(sum(processed_data)) % 10])

    # Core transformation (this is what actually matters)
    transformed = transform_register(registers)

    # Decoy dictionary structure with misleading calculations
    diagnostics = {
        'baseline': sum(registers) % 100,
        'entropy': len(set(registers)),
        'phase_shift': evaluate_coherence(registers),
        'harmonic': validate_checksum({'a': registers[0], 'b': registers[1], 'c': registers[2]})
    }

    # Actual answer derivation path
    intermediate = (transformed ^ diagnostics['phase_shift']) + 5
    correction_factor = 0
    for i in range(3):
        if (intermediate >> i) & 1:
            correction_factor |= (1 << (i + 2))
    
    # Linear search through dummy list (distractor)
    search_space = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    target_found = False
    for val in search_space:
        if val == intermediate:  # never true for expected inputs
            target_found = True
            break

    final_diagnostic = intermediate + correction_factor - diagnostics['harmonic']
    return final_diagnostic

# Main execution
quantum_registers = [12, 7, 3, 14]

# Dead code paths and red herrings
legacy_mode = False
if legacy_mode:
    fallback_value = 0
    for r in quantum_registers:
        fallback_value += r << 2

auxiliary_buffer = []
for i in range(len(quantum_registers)):
    auxiliary_buffer.append((i + 1) * quantum_registers[i] // 2)

# Key computation
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")