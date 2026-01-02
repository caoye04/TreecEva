def preprocess_signal(data):
    return [x ^ 3 for x in data if x % 2 == 1]


def generate_hamming_weights(n):
    weights = {}
    for i in range(n):
        weights[i] = bin(i).count('1')
    return weights

# Irrelevant helper function (dead code path)
def deprecated_checksum(seq):
    return sum(seq) % 256

# System state simulation with red herrings
def evaluate_coherence(state_vector):
    magnitude = sum([x**2 for x in state_vector])
    normalized = [x / magnitude**0.5 for x in state_vector]
    return sum(normalized[i] * i for i in range(len(normalized)))

# Core logic disguised among distractors
def extract_phase_shifts(signal, threshold=5):
    shifts = []
    for i, val in enumerate(signal):
        if val > threshold:
            shifts.append((i * val) % 7)
    return shifts

# Misleading transformation chain (partially unused)
def transform_coordinates(x, y):
    temp = (x + y) * 3
    return (temp & 0xFF), ((temp >> 4) ^ 0xAA)

# Key analysis function — only this contributes to final answer
def analyze_system_state(sequence, flags):
    base_offset = sum(flags) * 2
    
    # Distractor: unused computation
    entropy_estimate = len(sequence) * 1.58496  # log2(3) approx
    
    # Real work begins: process sequence using bit manipulation and filtering
    filtered = [x for x in sequence if x & 1 == 0]  # even numbers only
    shifted = [x >> 1 for x in filtered]
    
    # Use enumerate and conditional expression (required Python features)
    indexed_sum = sum(index + (value if value > 3 else 0) 
                      for index, value in enumerate(shifted))
    
    # Introduce zip with unrelated list (distractor)
    aux_data = [10, 20, 30, 40]
    zipped_results = [a ^ b for a, b in zip(filtered, aux_data)]  # not used
    
    # Final computation involving modular arithmetic and offset
    aggregate = sum(shifted) + base_offset
    adjustment = len(filtered) % 4
    
    # Critical result
    return aggregate * 3 - adjustment

# --- Simulation Setup ---

# Primary input data
quantum_sequence = [5, 8, 12, 3, 16, 7, 10, 14]

# System flags (used in key calculation)
system_flags = [1, 0, 1, 1]

# Dead variables and irrelevant computations
signal_snapshot = preprocess_signal(quantum_sequence)
coherence_score = evaluate_coherence(quantum_sequence)
phase_info = extract_phase_shifts(quantum_sequence, threshold=6)

# Unused coordinate transforms
coords = []
for i in range(3):
    coords.append(transform_coordinates(i, i*2))

# Hamming weights generated but not fully used
hamming_map = generate_hamming_weights(10)

# Decoy checksum
checksum = deprecated_checksum(quantum_sequence)

# Main execution point
final_diagnostic = analyze_system_state(quantum_sequence, system_flags)

# Output result as required
print(f"Result: {final_diagnostic}")