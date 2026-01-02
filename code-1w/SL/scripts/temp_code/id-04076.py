import itertools

# Simulated quantum register diagnostics (irrelevant base constants)
BASE_PHASE = 0.618034
CALIBRATION_OFFSET = 2.718281
REFERENCE_CYCLE = 55

# Irrelevant sensor emulation (distractor)
def fetch_sensor_array():
    return [i ** 2 % 7 for i in range(10)]

# Decoy function – looks important but unused in critical path
def deprecated_transform(seq, factor=2):
    return [x * factor + 1 for x in seq if x % 2 == 0]

# Core bit manipulation engine (relevant)
def shift_sequence(data, direction, steps):
    if direction == 'left':
        return (data << steps) & 0xFFFF
    else:
        return data >> steps

# Conditional entropy calculator (mixed relevance)
def compute_conditional_entropy(values):
    total = 0
    for v in values[:8]:  # only first 8 matter
        if v > 5:
            total += v ^ 3
    return total - len(values)  # minor adjustment

# Main analysis with red herrings and multiple concepts
quantum_registers = [
    {'state': 0b1101, 'flag': True, 'history': [1, 0, 1]},
    {'state': 0b1010, 'flag': False, 'history': [0, 1, 1]},
    {'state': 0b1111, 'flag': True, 'history': [1, 1, 0]},
    {'state': 0b0001, 'flag': True, 'history': [0, 0, 1]}
]

# Distractor: unused register group
auxiliary_registers = [
    {'state': 0b1010, 'flag': False, 'temp': 99},
    {'state': 0b1110, 'flag': True, 'temp': 103}
]

# Complex transformation pipeline (some stages are distractions)
def analyze_system_state(registers):
    cumulative = 0
    
    # Step 1: Extract active states (only flag=True)
    active_states = [r['state'] for r in registers if r['flag']]
    
    # Step 2: Apply bit shifts based on index (relevant)
    shifted = []
    for idx, state in enumerate(active_states):
        new_state = shift_sequence(state, 'left', idx + 1)
        shifted.append(new_state)
    
    # Step 3: Compute XOR folding (key operation)
    folded = 0
    for s in shifted:
        folded ^= s
    
    # Step 4: Use lambda to filter out low values (itertools abuse as distractor)
    pair_combinations = list(itertools.combinations(shifted, 2))
    valid_pairs = list(filter(lambda p: (p[0] ^ p[1]) > 50, pair_combinations))
    
    # Step 5: Add count of valid pairs (minor contribution)
    pair_count_bonus = len(valid_pairs) * 3
    
    # Step 6: Apply conditional entropy from history lengths (misleading intermediate)
    histories = [len(r['history']) for r in registers]
    entropy_score = compute_conditional_entropy(histories)
    
    # Step 7: Real computation path begins here — ignore entropy, use folded and pair bonus
    cumulative += folded
    cumulative += pair_count_bonus
    
    # Step 8: Apply BASE_PHASE? No — it's a red herring. But CALIBRATION_OFFSET is used in disguise.
    # Actually using its integer part: int(CALIBRATION_OFFSET) = 2
    cumulative *= 2  # not related to constant directly
    
    # Step 9: Final toggle based on number of active registers
    if len(active_states) % 2 == 0:
        cumulative -= 10
    else:
        cumulative += 5
    
    return cumulative

# Dead code path — never called, adds confusion
def log_diagnostics(data):
    timestamp = sum([ord(c) for c in 'LOG'])
    return f"[{timestamp}] Diagnostic: {data}"

# Trigger the real computation
final_diagnostic = analyze_system_state(quantum_registers)

# Print result as required
print(f"Result: {final_diagnostic}")