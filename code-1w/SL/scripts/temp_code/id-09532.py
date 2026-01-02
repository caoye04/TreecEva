import math

# System calibration constants (some are decoys)
CALIBRATION_OFFSET = 0.0034
TEMPORAL_DAMPING = 0.987
PHASE_SHIFT_LIMIT = 127
INVALID_THRESHOLD = -400
RED_HERRING_CONSTANT = sum([i for i in range(100) if i % 7 == 0])

# Simulated quantum register states from sensor array
quantum_registers = [
    {'state': 'superposed', 'qubits': [1, 0, 1, 1], 'entropy': 0.642, 'timestamp': 1623456789},
    {'state': 'collapsed', 'qubits': [0, 0, 0, 1], 'entropy': 0.001, 'timestamp': 1623456792},
    {'state': 'superposed', 'qubits': [1, 1, 0, 0], 'entropy': 0.587, 'timestamp': 1623456795},
    {'state': 'entangled', 'qubits': [1, 1, 1, 1], 'entropy': 0.921, 'timestamp': 1623456798},
    {'state': 'collapsed', 'qubits': [0, 1, 0, 0], 'entropy': 0.003, 'timestamp': 1623456801}
]

# Auxiliary data structures with red herrings
sensor_health = {f'sensor_{i}': {'status': 'OK' if i % 3 != 0 else 'FAILED', 'readings': []} for i in range(1, 10)}
duplicate_check_set = set()
processing_log = []

# Decoy function – looks important but unused in critical path
def validate_entanglement_phase(readings):
    return sum(abs(r['entropy'] * 100) for r in readings if r['state'] == 'entangled') < 100

# Another irrelevant utility
misleading_aggregator = lambda data: {
    'max_entropy': max(d['entropy'] for d in data),
    'avg_timestamp': sum(d['timestamp'] for d in data) / len(data),
    'state_distribution': {s: len([d for d in data if d['state'] == s]) for s in set(d['state'] for d in data)}
}

# Core analysis pipeline
conversion_matrix = [8, 4, 2, 1]  # Binary to decimal positional weights

filtered_registers = [r for r in quantum_registers if r['entropy'] > 0.5]

# Extract and convert qubit patterns to diagnostic values
converted_states = []
for reg in filtered_registers:
    if reg['state'] in ['superposed', 'entangled']:
        # Convert qubit array to decimal using matrix multiplication logic
        decimal_value = sum(q * m for q, m in zip(reg['qubits'], conversion_matrix))
        normalized = decimal_value * math.cos(math.pi * reg['entropy'])
        converted_states.append(round(normalized))

# Irrelevant transformation chain
shifted_values = [v << 2 for v in converted_states]  # Bit shift decoy
inverted_map = {i: (~v + 100) for i, v in enumerate(shifted_values)}  # Two's complement red herring

# Real processing begins here — obscure due to prior noise
def calculate_coherence_score(states):
    score = 0
    for val in states:
        if val > 5:
            score += val ** 2
        elif val == 5:
            score += 25
        else:
            score += val * 3
    return score

intermediate_score = calculate_coherence_score(converted_states)

# Conditional expression with string method distraction
status_flag = 'CRITICAL' if intermediate_score > 100 else 'STABLE'
log_entry = f"System {status_flag.lower().replace('i', 'I').title()}: Score={intermediate_score}"
processing_log.append(log_entry)

# Real key computation hidden among distractors
binary_diagnostic = bin(intermediate_score & 255)[2:]  # Mask to 8 bits

# Use of set operation: find duplicate digits in binary form (mostly irrelevant)
digits = set(binary_diagnostic)
duplicate_check_set.update([d for d in digits if binary_diagnostic.count(d) > 1])

# Final transformation using conditional expression and bit manipulation
adjusted_length = len(binary_diagnostic) if len(binary_diagnostic) % 2 == 0 else len(binary_diagnostic) + 1
padded_bin = binary_diagnostic.zfill(adjusted_length)  # String method used

# Key calculation: interpret padded binary as decimal, then apply damping
raw_diagnostic = int(padded_bin, 2)

# Apply temporal damping factor (only relevant constant used)
final_diagnostic = raw_diagnostic * TEMPORAL_DAMPING

# Dead code path — never executed but looks plausible
if final_diagnostic < INVALID_THRESHOLD:
    final_diagnostic = -1  # This will never trigger

# Output the required result
print(f"Result: {final_diagnostic}")