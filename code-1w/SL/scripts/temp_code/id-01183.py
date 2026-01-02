import itertools

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.0034
TEMPORAL_DAMPING = 0.987
REFERENCE_PHASE = 1.224

# Irrelevant diagnostic counters
diag_counter_a = 0
diag_counter_b = 0
diag_counter_c = 0

# Simulated quantum register states (key data structure)
quantum_registers = [
    {'state': 5, 'coherence': 0.77, 'flagged': False},
    {'state': 3, 'coherence': 0.62, 'flagged': True},
    {'state': 8, 'coherence': 0.81, 'flagged': False},
    {'state': 2, 'coherence': 0.59, 'flagged': True}
]

# Auxiliary decoy function (never called)
def compute_entanglement_entropy(registers):
    total = 0
    for r in registers:
        total += r['coherence'] ** 2
    return total / len(registers)

# Unused transformation matrix
TRANSFORMATION_MATRIX = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# Decoy statistical accumulator (dead code path)
stats_buffer = []
for i in range(4):
    stats_buffer.append({
        'index': i,
        'value': quantum_registers[i]['state'] * CALIBRATION_OFFSET,
        'adjusted': False
    })

# Real processing begins: filter unflagged registers
active_registers = [r for r in quantum_registers if not r['flagged']]

# Compute base energy from state values
base_energy = sum(r['state'] for r in active_registers)

# Apply coherence-weighted adjustment using dictionary lookup
weight_map = {5: 1.1, 8: 1.3, 2: 0.9, 3: 0.8}
weighted_adjustment = 0
for reg in active_registers:
    if reg['state'] in weight_map:
        weighted_adjustment += weight_map[reg['state']] * reg['coherence']

# Simulate phase interference using itertools combinations (red herring)
phase_interference = 0
for pair in itertools.combinations(active_registers, 2):
    delta = abs(pair[0]['state'] - pair[1]['state'])
    phase_interference += delta * REFERENCE_PHASE  # Not used in final calculation

# Hidden accumulator: count valid transitions
transition_log = {}
for i in range(len(quantum_registers) - 1):
    if quantum_registers[i]['coherence'] > 0.6 and quantum_registers[i+1]['coherence'] <= 0.6:
        transition_log[f'forward_{i}'] = True
    elif quantum_registers[i]['coherence'] <= 0.6 and quantum_registers[i+1]['coherence'] > 0.6:
        transition_log[f'reverse_{i}'] = True

# Critical computation: analyze system state
# This function uses only base_energy and weighted_adjustment
def analyze_system_state(registers):
    global diag_counter_a, diag_counter_b
    diag_counter_a += 1  # Misleading side effect

    # Recompute active registers (duplicate logic)
    actives = [r for r in registers if not r['flagged']]
    energy = sum(r['state'] for r in actives)

    # Weighted adjustment based on state and coherence
    w_map = {5: 1.1, 8: 1.3}
    adj = 0
    for r in actives:
        if r['state'] in w_map:
            adj += w_map[r['state']] * r['coherence']

    # Final diagnostic formula: energy + floor(adj * 10)
    diagnostic_value = energy + int(adj * 10)
    diag_counter_b += 1
    return diagnostic_value

# Execute critical statement
final_diagnostic = analyze_system_state(quantum_registers)

# Print result as required
print(f"Target result: {final_diagnostic}")