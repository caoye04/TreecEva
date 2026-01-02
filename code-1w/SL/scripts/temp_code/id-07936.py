import itertools

# System diagnostic module for quantum coherence array (simulated)

def analyze_phase_shift(seq):
    """Irrelevant helper: analyzes phase coherence in sequence (not used in final result)"""
    return sum((a + b) * i for i, (a, b) in enumerate(itertools.pairwise(seq))) if len(seq) > 1 else 0

def validate_checksum(data):
    """Misleading validation: looks important but unused in critical path"""
    return sum(data) % 17 == 0

def transform_sequence(seq, key):
    """Applies XOR transformation with cyclic key (used in decoy path)"""
    return [seq[i] ^ key[i % len(key)] for i in range(len(seq))]

def generate_reference_map(bounds):
    """Creates red herring dictionary mapping (distractor)"""
    ref_map = {}
    for x in range(bounds[0], bounds[1]):
        ref_map[x] = (x ** 2 + 3*x + 7) % 13
    return ref_map

def filter_candidates(items, threshold=5):
    """Dead code path: never called in execution"""
    return [x for x in items if x > threshold]

def compute_integrity_score(matrix, key):
    """Core function: computes final result through bit manipulation and combinatorics"""
    # Step 1: extract diagonal elements
    diagonal = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
    
    # Step 2: apply bitwise rotation based on key
    rotated = [(val >> 2) | (val << 6) & 0xFF for val in diagonal]
    
    # Step 3: compute pairwise XOR combinations
    xor_combinations = [a ^ b for a, b in itertools.combinations(rotated, 2)]
    
    # Step 4: count how many have even set bits (popcount even)
    even_parity_count = sum(bin(x).count('1') % 2 == 0 for x in xor_combinations)
    
    # Step 5: multiply by sum of key's ASCII values
    key_sum = sum(ord(c) for c in key)
    
    # Step 6: add product of first and last matrix element
    edge_product = matrix[0][0] * matrix[-1][-1]
    
    # Step 7: subtract length of unused reference map (misleading use)
    fake_ref_map = generate_reference_map((10, 25))
    score = even_parity_count * key_sum + edge_product - len(fake_ref_map)
    
    # Step 8: final adjustment using string method on key (irrelevant transformation)
    adjusted_key = ''.join(sorted(set(key), key=key.index))
    adjustment = len(adjusted_key) * 3
    
    return score - adjustment

# --- Simulated system data ---

# Operational matrix from quantum register readout
operational_matrix = [
    [23, 15, 131, 42],
    [87, 194, 56, 111],
    [34, 92, 201, 77],
    [65, 103, 144, 22]
]

# System authentication key (hex-encoded)
system_key = "a3f9c2b"

# Irrelevant pre-processing steps (distractors)
phase_data = [row[0] for row in operational_matrix]
coherence_score = analyze_phase_shift(phase_data)
transformed_data = transform_sequence([23, 87, 34, 65], [1, 0, 1])
checksum_valid = validate_checksum([194, 56, 92, 201])

# Unused collections and variables (red herrings)
status_flags = {"active": True, "locked": False, "priority": 3}
error_log = []
for i in range(4):
    error_log.append(f"Error_{i}: Code {i*17 % 113}")

# Key computation point
diag_elements = [operational_matrix[i][i] for i in range(4)]  # Used internally in function

# Final diagnostic calculation (critical path)
final_diagnostic = compute_integrity_score(operational_matrix, system_key)

# Output result
print(f"Result: {final_diagnostic}")