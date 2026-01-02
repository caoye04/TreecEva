from collections import defaultdict
import math

# Simulated sensor array data (irrelevant but plausible)
sensor_readings = [0.88, 0.76, 0.91, 0.65, 0.83]
adjusted_weights = [math.sin(x * 2) for x in sensor_readings]

# Legacy calibration constants (unused red herring)
CALIBRATION_MAP = {
    'alpha': 0.12,
    'beta': 0.093,
    'gamma': 0.117
}

# System state vectors
def generate_phase_vector(n):
    return [i ^ (i >> 1) for i in range(n)]  # Gray code sequence

def build_baseline_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1
            elif i < j:
                matrix[i][j] = (i + j) % 7
    return matrix

def apply_mask(layer, mask):
    return [layer[i] ^ mask[i % len(mask)] for i in range(len(layer))]

# Irrelevant transformation chain (dead path)
raw_sequence = list(range(17))
masked_sequence = apply_mask(raw_sequence, [3, 7, 2])
decoded_chain = [x & 0xF for x in masked_sequence if x % 3 != 0]

# Core diagnostic logic
def compute_entropy(vector):
    count_map = defaultdict(int)
    for v in vector:
        count_map[v] += 1
    entropy = 0.0
    total = len(vector)
    for count in count_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_quantum_signature(state_vector, threshold=4):
    sig = 0
    for i, val in enumerate(state_vector):
        if val > threshold:
            sig ^= (val << 1) | (i & 1)
    return sig

def analyze_system_state(signature, baseline):
    # Extract key dimensions
    size = len(baseline)
    edge_sum = sum(baseline[i][size-1] for i in range(size))
    
    # Diagnostic core
    diag = signature
    diag ^= int(compute_entropy([signature & 0xFF, signature >> 8, size]))
    diag += edge_sum
    
    # Decoy operations with plausible names
    temp_buffer = [diag ^ i for i in range(5)]  # unused
    checksum = sum(temp_buffer) % 256               # computed but irrelevant
    
    # Actual contributing factor: diagonal XOR
    diagonal_xor = 0
    for i in range(size):
        diagonal_xor ^= baseline[i][i]
    
    diag ^= diagonal_xor
    diag -= size  # final adjustment
    
    return diag

# Orchestration block
if __name__ == "__main__":
    # Initialize relevant components
    phase_vector = generate_phase_vector(16)
    baseline_matrix = build_baseline_matrix(7)
    
    # Compute critical signature
    quantum_signature = extract_quantum_signature(phase_vector, threshold=5)
    
    # UNUSED: alternate analysis path (misleading)
    def legacy_diagnostic(seq):
        acc = 0
        for x in seq[:10]:
            acc += (x * 3) % 5
        return acc * 2
    
    # This call is never made - dead function
    # legacy_score = legacy_diagnostic(phase_vector)
    
    # Key execution point
    final_diagnostic = analyze_system_state(quantum_signature, baseline_matrix)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")