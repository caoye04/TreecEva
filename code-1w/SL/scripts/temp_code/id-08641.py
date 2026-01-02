import itertools

# Irrelevant helper function (dead code path)
def unused_energy_calculator(x):
    return sum(i ** 3 for i in x if i % 2 == 0)

# Misleading intermediate computation
temporal_sequence = [i * 2 + 1 for i in range(15) if i % 3 != 0]
decoherence_mask = [t ^ 7 for t in temporal_sequence[:10]]

# Core data structures with distractors
state_registry = {
    'baseline': [1, 0, 1, 1],
    'excited': [0, 1, 1, 0],
    'invalid': [1, 1, 1, 1],  # Unused state
    'null': [0, 0, 0, 0]      # Unused state
}

threshold_map = {
    'phase_x': 0.63,
    'phase_y': 0.21,
    'phase_z': 0.87
}

quantum_state = (1, 0, 1, 1)

# Decoy variables with plausible but irrelevant calculations
entanglement_entropy = 0
for i in range(len(temporal_sequence)):
    if temporal_sequence[i] > 10:
        entanglement_entropy += (i * 0.15) % 0.5

# Fake accumulation using itertools (no effect on result)
fake_pairs = list(itertools.combinations_with_replacement([2, 3], 2))
phantom_sum = sum(a * b for a, b in fake_pairs if (a + b) % 2 == 0)

# Real logic begins — conditional phase analysis
active_bits = sum(bit for bit in quantum_state)

if active_bits >= 3:
    base_threshold = threshold_map['phase_z']
elif active_bits == 2:
    base_threshold = threshold_map['phase_x']
else:
    base_threshold = threshold_map['phase_y']

# Bitwise manipulation disguised as noise filtering
filtered_state = 0
for idx, val in enumerate(quantum_state):
    filtered_state |= (val << idx)

# Secondary check using comparison and modular arithmetic
consistency_check = (filtered_state ^ 6) % 5

# Conditional expression chain with red herring variables
coherence_factor = 3.14159 if consistency_check in (1, 3) else 2.71828
scaling_proxy = coherence_factor * 0.1  # Unused beyond this point

# Actual answer derivation (non-obvious due to distractions)
def analyze_phase_transition(qs, thresholds):
    accumulated = 0
    for i, bit in enumerate(qs):
        if bit:
            accumulated += (i + 1) ** 2
    
    # Real calculation buried in logic
    adjustment = 0
    if accumulated > 10:
        adjustment = thresholds['phase_x'] * 100
    elif accumulated == 5:
        adjustment = thresholds['phase_y'] * 100
    else:
        adjustment = thresholds['phase_z'] * 100
    
    # Final deterministic result
    return int(accumulated * 10 + adjustment)

# Dead code: function defined but not used in critical path
def simulate_tunneling(seq, factor):
    return [x ^ int(factor) for x in seq if x % 4 == 0]

# Critical execution point
final_flux = analyze_phase_transition(quantum_state, threshold_map)

# Output required format
print(f"Result: {final_flux}")