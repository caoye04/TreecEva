def process_quantum_readings(readings):
    # Irrelevant transformation: applies noise filter (not used in final path)
    filtered = [r ^ 0b101 for r in readings]
    enhanced = [r << 2 for r in readings]
    return enhanced

# System constants (some are decoys)
default_threshold = 42
error_margin = 0.05
MAX_ENTANGLEMENT = 17

# Simulated quantum register states (input data)
quantum_registers = [12, 8, 15, 3, 9]

# Historical log with red herring entries
timeline_events = [
    {'type': 'decay', 'value': 1},
    {'type': 'spike', 'value': 999},  # distraction
    {'type': 'sync', 'value': 0}
]

# Auxiliary function that looks important but is never called
def compute_coherence_factor(seq):
    total = 0
    for i in range(len(seq)):
        total += seq[i] * (i + 1)
    return total % 13

# Unused recursive decoy function
def trace_back(id, depth):
    if depth == 0:
        return id
    return trace_back(id ^ depth, depth - 1)

# Core diagnostic map (used later)
diagnostic_map = {
    12: 'stable',
    8: 'metastable',
    15: 'critical',
    3: 'neutral',
    9: 'transition'
}

# System log with multiple irrelevant fields
system_log = {
    'version': 'QX-9',
    'uptime': 1203,
    'last_reset': 'manual',
    'readings_processed': 0,  # updated nowhere
    'flags': { 'debug': False, 'safe_mode': True },
    'history': timeline_events
}

# Set operations simulating qubit group analysis (one is relevant)
active_qubits = {1, 2, 3, 4, 5}
failed_qubits = {6, 7}
potential_neighbors = {3, 4, 5, 8, 9}
entangled_pairs = active_qubits & potential_neighbors  # {3,4,5} - subtle distractor

# Secondary processing chain with dead-end logic
aggregated = 0
for reg in quantum_registers:
    if reg > 10:
        aggregated += reg // 3
    else:
        aggregated -= reg % 4

# This function appears complex but only one branch matters
def analyze_register_state(val, index):
    if val in [12, 8, 3]:
        return val * 2
    elif val == 15:
        return val + 7
    elif val == 9:
        return val * 3
    else:
        return val

# Another distraction: builds unused structure
shadow_copy = []
for idx, v in enumerate(quantum_registers):
    shadow_copy.append({
        'idx': idx,
        'raw': v,
        'processed': analyze_register_state(v, idx),
        'status': diagnostic_map.get(v, 'unknown')
    })

# Critical intermediate transformation
transformed_registers = []
for r in quantum_registers:
    result = analyze_register_state(r, 0)
    transformed_registers.append(result)

# Decoy statistical summary
mean_val = sum(transformed_registers) / len(transformed_registers)
variance_proxy = sum((x - mean_val) ** 2 for x in transformed_registers) / len(transformed_registers)

# Real work happens here: modular reduction chain
def reduce_chain(values):
    acc = 0
    for v in values:
        acc = (acc + v) % 19
    return acc * 2

# Apply reduction to original registers (not transformed! subtle)
reduced = reduce_chain(quantum_registers)

# Now map reduced value through logical conditions
primary_diagnostic = 0
if reduced < 20:
    primary_diagnostic = reduced * 3
elif reduced < 35:
    primary_diagnostic = reduced * 2 + 5
else:
    primary_diagnostic = reduced + 12

# Final analysis uses set intersection to adjust outcome
sideband_interference = entangled_pairs & {1, 2, 3}
adjustment_factor = len(sideband_interference)  # yields 1

# Main analysis function
def analyze_system_state(registers, log_entry):
    base = primary_diagnostic
    # Use diagnostic map counts as modifier
    state_counter = 0
    for val in registers:
        if diagnostic_map[val] in ['critical', 'transition']:
            state_counter += 1
    # Actual formula
    result = base + state_counter * 4 - adjustment_factor
    return int(result)

# Execute key statement
final_diagnostic = analyze_system_state(quantum_registers, system_log)

# Print result as required
print(f"Result: {final_diagnostic}")