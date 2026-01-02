def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [x / sum(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]


def transform_coordinates(coords):
    # Irrelevant transformation (dead path)
    return [(c[0] * 2 + 1, c[1] * 3 - 1) for c in coords]


def simulate_decay(values, factor=0.92):
    # Misleading physics-inspired decay (not used in final result)
    return [v * (factor ** i) for i, v in enumerate(values)]

# Unused but plausible decoy function
def calculate_entropy(seq):
    from math import log
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Main system simulation
initial_pulse = [12, -5, 8, 0, -3, 19, 4]
baseline_shift = 7
adjusted_signal = [x + baseline_shift for x in initial_pulse]

# Signal processing chain
clipped_signal = [x for x in adjusted_signal if x >= 5]
squared_components = [x**2 for x in clipped_signal]
root_mean_square = (sum(squared_components) / len(squared_components)) ** 0.5

# Quantum register simulation (core logic disguised among distractions)
quantum_registers = [
    {'state': 'superposed', 'qubits': [1, 0, 1], 'energy': 3},
    {'state': 'entangled', 'qubits': [1, 1, 0], 'energy': 2},
    {'state': 'superposed', 'qubits': [0, 1, 1], 'energy': 3}
]

# Decoy data structure (looks important but unused)
legacy_cache = {
    'version': '2.1.0',
    'checksum': 'a1b2c3d4',
    'timestamp': 1678886400,
    'data': [hex(i)[2:] for i in range(10)]
}

# Real-time monitoring system (mix of relevant and irrelevant)
status_log = []
diagnostic_flags = set()

for reg in quantum_registers:
    qb = reg['qubits']
    pop_count = sum(qb)
    
    # Bitwise analysis (actually used)
    bit_pattern_score = 0
    for i, bit in enumerate(qb):
        bit_pattern_score += bit << (2 - i)  # Convert to decimal
    
    parity = pop_count % 2
    if parity:
        diagnostic_flags.add('odd_parity')
    
    # Store intermediate (misleading name)
    reg['diagnostic_hint'] = bit_pattern_score * reg['energy']

# Auxiliary computation (red herring)
coordinate_grid = [(i, i+1) for i in range(5)]
transformed_grid = transform_coordinates(coordinate_grid)

# Core diagnostic logic
lookup_table = {3: 7, 5: 2, 6: 9, 1: 4}

def analyze_system_state(registers):
    total = 0
    state_map = {}
    
    for r in registers:
        key = r['state']
        if key not in state_map:
            state_map[key] = 0
        state_map[key] += 1
    
    # Critical calculation
    for r in registers:
        qubits = r['qubits']
        active = sum(qubits)
        pattern = qubits[0] * 4 + qubits[1] * 2 + qubits[2]
        base_score = lookup_table.get(pattern, 1) * r['energy']
        adjustment = 2 if active >= 2 else -1
        total += base_score + adjustment
    
    # Final adjustment based on system diversity
    diversity_bonus = len(state_map) * 3
    total += diversity_bonus
    
    # Additional distractor: string processing that looks significant
    tag_sequence = "QUBIT-ENTANGLED-SUPERPOSED"
    tokens = tag_sequence.lower().split('-')
    token_lengths = [len(t) for t in tokens]
    avg_length = sum(token_lengths) / len(token_lengths)
    
    # This print is just noise
    # print(f'Avg token length: {avg_length}')
    
    return int(total)

# Execute main analysis
final_diagnostic = analyze_system_state(quantum_registers)

# Print result as required
print(f"Result: {final_diagnostic}")