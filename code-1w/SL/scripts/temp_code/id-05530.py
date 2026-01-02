import math

# System calibration constants (some are decoys)
CALIBRATION_FACTOR = 1.037
NOISE_THRESHOLD = 0.882
DECOY_CONSTANT_A = 2.718
DECOY_CONSTANT_B = 3.14159

# Initialize quantum register states (simulated qubit arrays)
quantum_registers = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# Irrelevant diagnostic logs (dead code path)
def log_register_trace(registers):
    trace_log = []
    for i, reg in enumerate(registers):
        parity = sum(reg) % 2
        trace_log.append(f'Register-{i}: Parity={parity}')
    return trace_log

# Unused transformation matrix (red herring)
transformation_matrix = [
    [0.707, 0.707],
    [-0.707, 0.707]
]

# Misleading entropy calculation (not actually used in final result)
def calculate_entropy(vector):
    total = 0
    for x in vector:
        if x > 0:
            total -= x * math.log2(x)
    return round(total, 6)

# Auxiliary function: Compute Hamming weight of a binary list
def hamming_weight(bits):
    return sum(bits)

# Auxiliary: Apply XOR folding across bits
def fold_bits(bits):
    result = 0
    for b in bits:
        result ^= b
    return result

# Core analysis pipeline
processed_states = []
symbolic_hashes = set()

for reg in quantum_registers:
    # Step 1: Fold bits to get signature
    folded = fold_bits(reg)
    
    # Step 2: Compute extended features
    hw = hamming_weight(reg)
    is_balanced = hw == len(reg) / 2
    
    # Step 3: Transform using fake calibration (partially relevant)
    calibrated_value = hw * CALIBRATION_FACTOR
    
    # Step 4: Generate symbolic tag (used later in filtering)
    tag = f'{folded}-{int(is_balanced)}'
    symbolic_hashes.add(tag)
    
    # Step 5: Append processed state (only calibrated_value and hw matter)
    processed_states.append({
        'raw': reg.copy(),
        'folded': folded,
        'weight': hw,
        'calibrated': calibrated_value,
        'tag': tag
    })

# Dead branch: never executed due to constant condition (distractor)
if len(symbolic_hashes) > 10:
    print("High entropy detected")
    exit(1)

# Decoy list comprehension: computes but doesn't affect main logic
ghost_weights = [p['weight'] ** 2 for p in processed_states if p['weight'] > 3]

# Real computation begins: aggregate calibrated values above threshold
filtered_calibrated = [
    p['calibrated'] for p in processed_states if p['weight'] >= 2
]

# Combine using lambda-based reduction
combiner = lambda x, y: round(x + y + 0.01, 4)
total_signal = round(sum(filtered_calibrated), 4)

# Secondary processing: count balanced forms
balanced_count = sum(1 for p in processed_states if p['weight'] == 2)

# Tertiary: compute diagnostic checksum using set operations
expected_tags = {"1-1", "0-0", "1-0", "0-1"}
found_in_expected = symbolic_hashes & expected_tags  # intersection
checksum = len(found_in_expected) * 100

# Fake signal injection (misleading intermediate)
pseudo_entropy = calculate_entropy([0.25, 0.25, 0.25, 0.25])

# Final aggregation with distraction variables
auxiliary_offset = len(ghost_weights) * 10  # always 0, ghost_weights empty
perturbation = DECOY_CONSTANT_A * 0  # red herring

# Critical statement: this determines the actual answer
final_diagnostic = int(total_signal + checksum + auxiliary_offset - perturbation)

# Print result for execution visibility
print(f"Result: {final_diagnostic}")