from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def compute_gravitational_pull(mass, distance):
    G = 6.67430e-11
    return G * mass / (distance ** 2)

# Distractor data structure
cosmic_constants = {
    'alpha': 0.007297,
    'beta': 3.141592,
    'gamma_shift': 2.718281
}

# Real computational components
flow_matrix = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

activation_threshold = 0.75

# Misleading intermediate calculation (unused later)
signal_interference = sum(sum(row) for row in flow_matrix) * 0.33

# Complex distractor: nested lambda with unused transformation
tensor_transform = lambda x: [
    [math.sin(cell * math.pi / 4) for cell in row]
    for row in x
]

transformed_flow = tensor_transform(flow_matrix)  # Dead end

# Another red herring: frequency analysis with no impact
event_sequence = 'AABBCADAEEDBC'
frequency_map = Counter(event_sequence)
amplitude_modulation = max(frequency_map.values()) - min(frequency_map.values())

# Real logic begins here — recursive bit weight counter
def count_active_bits(n):
    if n <= 0:
        return 0
    return (n & 1) + count_active_bits(n >> 1)

# Bitwise reduction across rows
def reduce_row_to_int(row):
    acc = 0
    for idx, val in enumerate(row):
        acc |= (val << idx)
    return acc

# Critical function: uses multiple concepts
def calculate_entropy(matrix, threshold):
    entropy = 0.0
    bit_weights = []

    # Step 1: Convert each row to integer via bit shifting
    for row in matrix:
        packed = reduce_row_to_int(row)
        bit_weights.append(count_active_bits(packed))
    
    # Step 2: Frequency distribution of bit counts
    weight_counter = defaultdict(int)
    for w in bit_weights:
        weight_counter[w] += 1
    
    # Step 3: Shannon entropy computation
    total = len(bit_weights)
    for count in weight_counter.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    
    # Step 4: Apply threshold filter on derived metric
    adjustment_factor = 1.0
    if entropy < threshold:
        adjustment_factor = 2.0
    
    # Step 5: Incorporate positional influence using enumerate and zip
    positional_sum = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            positional_sum += val * (i + 1) * (j + 1)
    
    # Step 6: Combine entropy with spatial moment
    final_entropy = entropy * adjustment_factor + math.sqrt(positional_sum) * 0.1
    
    # Irrelevant smoothing (does not affect output)
    smoothed = (final_entropy + math.cos(math.pi / 5)) / 1.05
    
    return final_entropy  # Actual return used

# Secondary decoy function
def analyze_quantum_coherence(data):
    coherence_score = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            coherence_score ^= (i * j + data[i][j]) % 7
    return coherence_score

# Unused but plausible-looking call
quantum_diagnostic = analyze_quantum_coherence(flow_matrix)

# Key statement that produces the answer
thermodynamic_potential = calculate_entropy(flow_matrix, activation_threshold)

# Print result as required
print(f"Result: {thermodynamic_potential}")