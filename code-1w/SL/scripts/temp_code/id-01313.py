import math

# System diagnostics simulation with redacted data paths and interference

def generate_entropy_sequence(length):
    # Irrelevant entropy generation (dead-end function)
    return [math.sin(i * 0.7) * 100 for i in range(length)]


def validate_checksum(data):
    # Unused validation routine (distractor)
    checksum = 0
    for d in data:
        checksum = (checksum + d) % 257
    return checksum

# Global decoy variables (misleading state)
current_phase = 3
system_lock = True
baseline_offset = -999
reference_ticks = [1, 1, 2, 3, 5, 8, 13]

# Real operational data
quantum_buffer = [
    {'qubit': 0, 'state': 1, 'decay': 0.05},
    {'qubit': 1, 'state': 0, 'decay': 0.02},
    {'qubit': 2, 'state': 1, 'decay': 0.08},
    {'qubit': 3, 'state': 1, 'decay': 0.01}
]

fault_map = {
    'threshold': 0.05,
    'mode': 'strict',
    'exclusions': {1, 4}  # qubit indices to ignore
}

# Distractor: complex-looking but unused transformation
transform_matrix = [[1 if i == j else 0.1 for j in range(4)] for i in range(4)]
projected_state = []
for row in transform_matrix:
    projected_state.append(sum([r * q['decay'] for r, q in zip(row, quantum_buffer)]))

# Secondary irrelevant computation chain
event_log = []
for tick in reference_ticks:
    if tick % 2 == 1:
        event_log.append(tick ** 2)

# Key analysis function with embedded logic and distractions
def analyze_system_state(buffer, config):
    active_count = 0
    total_decay = 0.0
    flagged_qubits = set()
    
    # Real logic begins: count active qubits above threshold
    for entry in buffer:
        qid = entry['qubit']
        if entry['state'] == 1:
            active_count += 1
            # Check decay only if not excluded
            if qid not in config['exclusions']:
                if entry['decay'] > config['threshold']:
                    flagged_qubits.add(qid)
            total_decay += entry['decay']
    
    # Distractor: unused nested dictionary construction
    shadow_analysis = {
        'metrics': {
            'peak': max([b['decay'] for b in buffer]),
            'floor': min([b['decay'] for b in buffer]),
            'range': len(buffer)
        },
        'flags': {k: False for k in ['stale', 'sync_loss', 'noise_spike']}
    }
    
    # Another red herring: recursive sum that's never used
    def recursive_sum(lst, idx=0):
        if idx >= len(lst):
            return 0
        return lst[idx]['decay'] + recursive_sum(lst, idx + 1)
    
    unused_total = recursive_sum(buffer)
    
    # Real computation: diagnostic score
    base_score = active_count * 100
    penalty = len(flagged_qubits) * 50
    adjustment = int(total_decay * 100)
    
    # Misleading intermediate (looks important)
    diagnostic_vector = [base_score, penalty, adjustment, unused_total]
    
    # Final result built from key components
    final_diagnostic = base_score - penalty + adjustment
    
    # Dead code branch (never reached due to config['mode'] == 'strict')
    if config['mode'] == 'relaxed':
        final_diagnostic = int(final_diagnostic * 1.1)
    
    # Irrelevant sorting of keys (distractor)
    sorted_excl = sorted(config['exclusions'])
    
    # Unused character counting on stringified data (red herring)
    raw_text = str(buffer)
    char_count = sum(1 for c in raw_text if c.isalpha())
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_buffer, fault_map)
print(f"Result: {final_diagnostic}")