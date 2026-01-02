import math

# Simulated quantum register state analyzer with decoy operations
def initialize_quantum_sequence(seed_value):
    base_sequence = [seed_value]
    for i in range(1, 8):
        if i % 3 == 0:
            base_sequence.append(int(base_sequence[-1] * 1.5) ^ (i << 2))
        elif i % 2 == 0:
            base_sequence.append(base_sequence[-1] + (i ** 2))
        else:
            base_sequence.append(base_sequence[-1] + (i * 5) | 7)
    # Irrelevant transformation (red herring)
    normalized = [x / max(base_sequence) for x in base_sequence]
    scaled = [int(x * 100) for x in normalized]
    return base_sequence  # Only base_sequence is used

# Decoy function - looks important but unused in critical path
def legacy_diagnostic_check(seq):
    checksum = 0
    for idx, val in enumerate(seq):
        checksum += val * (idx + 1) % 97
    return checksum % 1000

# Core analysis with multiple distractions
def analyze_system_state(sequence, log_map):
    # Distractor variables (unused in final result)
    temporal_weight = 0
    coherence_factor = 1.0
    entropy_buffer = []
    debug_snapshot = {}
    
    # Real computation begins
    accumulated = 0
    for i, val in enumerate(sequence):
        if val % 2 == 0:
            accumulated += val >> 1
        else:
            accumulated -= val & 7
        
        # Dead code branch - never executed due to loop logic
        if i > len(sequence):
            temporal_weight += math.log(val + 1)
            break
    
    # Dictionary-based state mapping (core component)
    state_registry = {
        'level_0': sequence[0] * 2,
        'level_1': sequence[3] + 100,
        'level_2': sequence[5] - 50,
        'level_3': sequence[7] ^ 15
    }
    
    # Red herring: complex-looking but unused dictionary ops
    derived_metrics = {}
    for k, v in state_registry.items():
        derived_metrics[f'processed_{k}'] = (v * 1.07) // 1
        if '1' in k:
            derived_metrics[f'inverted_{k}'] = 1000 - v

    # Critical intermediate calculation
    raw_diagnostic = accumulated + state_registry['level_0']
    
    # Conditional override based on log map (simulated)
    status_flag = log_map.get('system_stable', True)
    override_code = log_map.get('override_code', None)
    
    # Another decoy block
    if override_code == 999:
        raw_diagnostic = int(math.sqrt(raw_diagnostic))
    
    # Actual decision logic (non-obvious)
    if status_flag and len(log_map.get('history', [])) < 5:
        final_adjustment = state_registry['level_3'] // 4
    else:
        final_adjustment = -25
    
    # Final result
    final_diagnostic = raw_diagnostic + final_adjustment
    
    # Unused cleanup (distraction)
    debug_snapshot['final'] = final_diagnostic
    entropy_buffer.append(final_diagnostic % 10)
    
    return final_diagnostic

# Irrelevant global constants (distractors)
MAX_ITERATIONS = 10000
CONVERGENCE_TOLERANCE = 1e-6
CALIBRATION_MATRIX = [[1, 0], [0, 1]]

# Setup inputs
seed_input = 13
quantum_sequence = initialize_quantum_sequence(seed_input)

# Log structure with meaningful and irrelevant fields
system_log = {
    'timestamp': '2023-11-05T10:30:00Z',
    'system_stable': True,
    'version': '2.1.5',
    'history': [1, 2, 3],  # triggers short history path
    'metrics': {
        'latency': 45.6,
        'throughput': 987,
        'errors': 0
    },
    'debug_mode': False,
    'cache_status': 'cold'
}

# Dead function call (no side effects)
legacy_diagnostic_check(quantum_sequence)

# Key execution point
final_diagnostic = analyze_system_state(quantum_sequence, system_log)

# Output result as required
print(f"Result: {final_diagnostic}")