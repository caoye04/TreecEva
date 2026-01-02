def initialize_subsystem():
    base_offset = 37
    calibration_sequence = [i ** 2 % 19 for i in range(12) if i % 3 != 0]
    temp_buffer = {x: x * base_offset for x in range(5)}
    return base_offset

initial_threshold = 0.67
safety_margin = 0.12
legacy_modes = ['A', 'B', 'C']
deprecated_flag = False

# Irrelevant legacy configuration block (distractor)
def legacy_redundancy_check(mode):
    if mode in legacy_modes:
        return sum(ord(c) for c in mode) % 7
    return -1

# Unused intermediate diagnostic function (dead code path)
def compute_health_score(values):
    mean_val = sum(values) / len(values)
    variance = sum((v - mean_val) ** 2 for v in values) / len(values)
    return mean_val - variance ** 0.5

# Core system state analyzer
quantum_registers = [
    {'state': 1, 'phase': 0.25, 'entangled': True},
    {'state': 0, 'phase': 0.75, 'entangled': False},
    {'state': 1, 'phase': 0.50, 'entangled': True},
    {'state': 1, 'phase': 0.10, 'entangled': True}
]

fault_mask = 0b1010  # Simulated error detection pattern
auxiliary_flags = [False, True, False]

# Misleading precomputation with decoy result (irrelevant)
decoy_aggregate = 0
for i in range(8):
    if i % 3 == 0:
        decoy_aggregate += i * i
    elif i == 5:
        decoy_aggregate -= 17

# Real processing begins here
phase_sum = 0.0
active_states = 0
entanglement_chain = []

for reg in quantum_registers:
    phase_sum += reg['phase']
    if reg['state'] == 1:
        active_states += 1
    if reg['entangled']:
        entanglement_chain.append(reg['phase'])

# Conditional expression usage (required feature)
average_phase = phase_sum / len(quantum_registers) if quantum_registers else 0.0

# Set operations to determine coherence groups (required feature)
coherence_set_a = {0.25, 0.50, 0.75}
coherence_set_b = {0.10, 0.25, 0.50}
common_coherence = coherence_set_a & coherence_set_b  # {0.25, 0.5}

overlap_count = len(common_coherence)

# Simulated bit manipulation for fault analysis
fault_diagnosis = 0
for i in range(len(quantum_registers)):
    if fault_mask & (1 << i):
        fault_diagnosis += 1

# Secondary validation using dictionary aggregation
validation_map = {
    'active': active_states,
    'average_phase': round(average_phase, 3),
    'chain_length': len(entanglement_chain),
    'overlap': overlap_count
}

# Unused derived metric (distractor)
synthetic_index = (validation_map['active'] + validation_map['overlap']) * 117 % 1000

# Main analysis logic
threshold_crossed = average_phase > initial_threshold + safety_margin
redundant_check = active_states >= 2 and fault_diagnosis <= 2

# Complex conditional with short-circuit logic and distractors
if threshold_crossed and (redundant_check or not deprecated_flag):
    adjustment_factor = 3 if len(entanglement_chain) > 2 else 2
    # Key arithmetic and integer division
    raw_diagnostic = (active_states * 1000 + int(phase_sum * 100)) // adjustment_factor
    secondary_weight = validation_map['overlap'] * 42
    final_diagnostic = raw_diagnostic - secondary_weight
else:
    final_diagnostic = -999  # unreachable under current config

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers, fault_mask)

# Wrapper function to obscure logic (abstraction layer)
def analyze_system_state(registers, mask):
    phase_total = sum(r['phase'] for r in registers)
    active_cnt = sum(1 for r in registers if r['state'] == 1)
    entangled_cnt = sum(1 for r in registers if r['entangled'])
    mask_effect = bin(mask).count('1')
    
    # Integer division and rounding used meaningfully
    score_component = int(phase_total * 100) // 3
    adjustment = max(1, entangled_cnt - mask_effect)
    
    # Final deterministic computation (answer = 235)
    return (active_cnt * 500 + score_component) // adjustment

print(f"Target result: {final_diagnostic}")