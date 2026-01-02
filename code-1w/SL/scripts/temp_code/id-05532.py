import math

# System calibration constants (irrelevant to final result)
calibration_map = {i: (i ** 2 + 3 * i + 7) % 89 for i in range(15)}
offset_table = [sum(calibration_map.values()) // (i + 1) for i in range(10)]

# Irrelevant diagnostic function (dead code path)
def legacy_diagnostic(x):
    return sum([i for i in str(x) if i in '02468'])

# Unused signal processor with misleading intermediate values
def process_signal_stream(stream):
    accumulator = 0
    for val in stream:
        if val > 50:
            accumulator += int(math.log(val, 2))
        else:
            accumulator -= val // 7
    return accumulator

# Primary data structures
logic_core = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]

activation_sequence = [True, False, True, True, False]

# Decoy transformation matrix (never used)
transform_matrix = [[i * j for j in range(4)] for i in range(4)]
for i in range(4):
    transform_matrix[i][i] = pow(i + 2, 3, 10)

# Auxiliary functions with partial relevance
def compute_entropy(vector):
    total = 0
    for x in vector:
        if x > 0:
            total -= x * math.log(x + 1e-9)
    return round(total, 6)

# Red herring: complex bit analysis (not used in final computation)
def analyze_bit_stability(value):
    binary_rep = bin(value)[2:]
    ones_ratio = binary_rep.count('1') / len(binary_rep)
    cyclic_shift = (value << 3) | (value >> 5)
    return ones_ratio > 0.4 and cyclic_shift % 17 != 0

# Key algorithm: pattern analyzer
# Combines combinatorics, boolean logic, dictionary ops, list traversal, and comparisons
def count_symmetric_pairs(matrix):
    count = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == matrix[n - i - 1][n - j - 1] and (i != n - i - 1 or j != n - j - 1):
                count += 1
    return count

def evaluate_activation_chain(seq):
    score = 0
    for i in range(len(seq)):
        if seq[i]:
            # Logical dependency on position and neighbors
            left_ok = (i == 0) or seq[i - 1]
            right_ok = (i == len(seq) - 1) or not seq[i + 1]
            if left_ok != right_ok:  # XOR-like condition
                score += i * 2
            else:
                score += 1
    return score

# Real but obscured core logic
pattern_metrics = {
    'mirror_count': count_symmetric_pairs(logic_core),
    'complexity_factor': len(logic_core) * len(logic_core[0]),
    'sparsity': sum(sum(row) for row in logic_core) / float(pattern_metrics['complexity_factor']) if 'complexity_factor' in locals() else 0.5
}

# Fix missing initialization due to forward reference
pattern_metrics['sparsity'] = sum(sum(row) for row in logic_core) / float(pattern_metrics['complexity_factor'])

# Secondary metric with decoy dependencies
signal_proxy = 0
for row in logic_core:
    for cell in row:
        signal_proxy = (signal_proxy << 1) ^ cell  # Bit manipulation red herring

# Main analysis function
# Uses dictionary operations, list processing, comparison logic, and combinatorial evaluation
def analyze_pattern(core, sequence):
    
    # Step 1: Compute structural symmetry (relevant)
    pairs = count_symmetric_pairs(core)
    
    # Step 2: Evaluate activation logic chain (relevant)
    activation_score = evaluate_activation_chain(sequence)
    
    # Step 3: Build feature dictionary with some irrelevant entries
    features = {
        'base_symmetry': pairs,
        'temporal_weight': activation_score,
        'harmonic_mean': 2 * pairs * activation_score / (pairs + activation_score) if (pairs + activation_score) > 0 else 0,
        'entropy_proxy': compute_entropy([len(row) for row in core]),
        'dummy_flag': any(analyze_bit_stability(x) for x in [128, 256, 512])  # Always false, distractor
    }
    
    # Step 4: Apply conditional adjustment based on combinatorial threshold
    n_rows = len(core)
    n_cols = len(core[0])
    total_elements = n_rows * n_cols
    
    # Critical comparison operation
    if features['harmonic_mean'] >= 4.0 and total_elements == 16:
        adjustment = 3
    elif activation_score > 5:
        adjustment = 2
    else:
        adjustment = 0
    
    # Step 5: Incorporate sparsity from earlier calculation
    normalized_sparsity = int(round(pattern_metrics['sparsity'] * 10))
    
    # Step 6: Final composition using multiple concepts
    intermediate = (features['base_symmetry'] + features['temporal_weight']) * adjustment
    
    # Step 7: Apply sparsity-based modulation
    modulated = intermediate // (normalized_sparsity if normalized_sparsity > 0 else 1)
    
    # Step 8: Final correction based on exact equality
    final_value = modulated + (1 if normalized_sparsity == 6 else -1)
    
    # Dead code block (misleading)
    if False:
        backup_system = [pow(i, 3) for i in offset_table]
        final_value = sum(backup_system) % 100
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_pattern(logic_core, activation_sequence)

# Print result as required
print(f"Target result: {final_diagnostic}")