import math

# System calibration constants (some are decoys)
CALIBRATION_OFFSET = 0.0034
TEMPORAL_DAMPING = 0.987
PHASE_SHIFT_TABLE = [0.1 * i ** 0.5 for i in range(10)]
IRRELEVANT_THRESHOLD = 42.8

# Quantum register simulation with bit-level encoding
quantum_registers = [
    {'state': 0b1101, 'flag': True, 'energy': 3.2},
    {'state': 0b1010, 'flag': False, 'energy': 4.1},
    {'state': 0b1111, 'flag': True, 'energy': 3.9}
]

# Irrelevant signal processing chain
raw_signals = [math.sin(i * 0.5) + CALIBRATION_OFFSET for i in range(5)]
filtered_signals = [s * TEMPORAL_DAMPING for s in raw_signals if s > 0.1]
peak_magnitude = max(filtered_signals) if filtered_signals else 0.0

# Unused transformation matrix (dead code path)
transformation_matrix = [
    [1, 0, 0],
    [0, math.cos(PHASE_SHIFT_TABLE[2]), -math.sin(PHASE_SHIFT_TABLE[2])],
    [0, math.sin(PHASE_SHIFT_TABLE[2]), math.cos(PHASE_SHIFT_TABLE[2])]
]

# Auxiliary function that appears relevant but is not used in critical path
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Bit manipulation and set operations for fault detection
def detect_fault_patterns(registers):
    active_bits = set()
    for reg in registers:
        bits = {i for i in range(8) if (reg['state'] >> i) & 1}
        active_bits.update(bits)
    
    # Simulate fault mask using XOR of high-order bits
    fault_mask = 0
    for reg in registers:
        fault_mask ^= (reg['state'] >> 4) & 0b11
    
    # Red herring computation
    dummy_entropy = len(active_bits) * 0.33
    
    return active_bits, fault_mask

# Core diagnostic analyzer
def analyze_system_state(registers):
    # Extract bit patterns and fault info
    bits, mask = detect_fault_patterns(registers)
    
    # Energy aggregation with conditional filtering
    flagged_energies = [r['energy'] for r in registers if r['flag']]
    avg_energy = sum(flagged_energies) / len(flagged_energies) if flagged_energies else 0
    
    # Bitwise analysis
    combined_state = 0
    for r in registers:
        combined_state |= r['state']
    
    # Critical intermediate: count of unique high-energy lit bits
    high_bit_count = sum(1 for b in range(8) if (combined_state >> b) & 1 and b >= 3)
    
    # Decoy logic branch (never executed under current inputs)
    if len(registers) > 5:
        fallback_score = math.log2(len(registers))
    else:
        fallback_score = 0  # dead assignment
    
    # Accumulation with distractor variables
    base_score = 0
    for r in registers:
        if r['flag']:
            base_score += bin(r['state']).count('1') * r['energy']
    
    # Set-based anomaly detection
    expected_bits = {0, 1, 2, 3, 4, 5}
    unexpected_bits = bits - expected_bits  # should be {6,7} if present
    anomaly_penalty = 5 * len(unexpected_bits)
    
    # Final diagnostic calculation
    final_diagnostic = int(
        base_score * avg_energy - anomaly_penalty + mask * 100
    )
    
    # Print trace for debugging (not affecting result)
    debug_info = {
        'bits_found': sorted(bits),
        'unexpected': sorted(unexpected_bits),
        'mask_value': mask
    }
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")