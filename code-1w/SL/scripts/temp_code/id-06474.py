from collections import defaultdict, Counter

# Simulated quantum register analysis with decoy computations
def initialize_quantum_sequence(n):
    seq = [1]
    for i in range(1, n):
        if i % 5 == 0:
            seq.append(seq[-1] + 2)
        elif i % 3 == 0:
            seq.append(seq[-1] * 2)
        else:
            seq.append(seq[-1] + i % 7)
    return seq

def compute_entropy(signal):
    count = Counter(signal)
    total = len(signal)
    entropy = 0
    for freq in count.values():
        p = freq / total
        entropy -= p * (p ** 0.5)  # Non-standard pseudo-entropy
    return round(entropy, 6)

def transform_register(reg):
    # Real transformation: sum of squares mod 1000
    transformed = sum(x ** 2 for x in reg) % 1000
    
    # Distractor: irrelevant bit manipulation
    decoy = 0
    for x in reg:
        decoy ^= (x << 2) & 0xFF
        decoy += (x >> 1) | 0x0A
    
    # Distractor: unused recursive path
    def unused_dfs(val, depth):
        if depth == 0 or val < 5:
            return val
        return unused_dfs(val // 2, depth - 1) + unused_dfs(val - 3, depth - 1)
    
    return transformed  # Only this matters

def validate_coherence(chain):
    # Irrelevant validation function (never alters critical state)
    window_size = 3
    coherence_score = 0
    for i in range(len(chain) - window_size + 1):
        window = chain[i:i+window_size]
        if all(w % 2 == i % 2 for i, w in enumerate(window)):
            coherence_score += 1
    return coherence_score

def analyze_subband(frequencies):
    # Real logic: weighted sum
    weights = [0.1, 0.2, 0.3, 0.4, 0.5]
    weighted = sum(f * w for f, w in zip(frequencies[:5], weights))
    
    # Distractor: string manipulation red herring
    status_flag = "OK"
    if weighted > 100:
        status_flag = "OVERLOAD"
    binary_tag = ''.join([status_flag[0] for _ in range(8)])
    case_swapped = binary_tag.lower() if weighted % 2 else binary_tag.upper()
    
    return int(weighted)

def analyze_system_state(registers):
    # Critical data aggregation
    diagnostic_map = defaultdict(int)
    
    # Step 1: Transform each register
    for idx, reg in enumerate(registers):
        trans_val = transform_register(reg)
        diagnostic_map[f'trans_{idx}'] = trans_val
    
    # Step 2: Extract frequency subband from first register
    frequencies = registers[0]
    subband_result = analyze_subband(frequencies)
    diagnostic_map['subband'] = subband_result
    
    # Step 3: Compute system entropy (distractor but looks important)
    flat_regs = [item for sublist in registers for item in sublist]
    entropy_metric = compute_entropy(flat_regs)
    diagnostic_map['entropy'] = int(entropy_metric * 1000)  # Looks important
    
    # Step 4: Validate coherence (completely irrelevant)
    decoy_chain = [len(reg) for reg in registers]
    coherence_index = validate_coherence(decoy_chain)
    diagnostic_map['coherence'] = coherence_index
    
    # Step 5: Use only specific components for final result
    base = diagnostic_map['trans_0']
    modifier = diagnostic_map['subband']
    scaling_factor = len(registers) if base > 500 else 2
    
    # Final computation (this is the real answer)
    final_diagnostic = (base * scaling_factor) + modifier - diagnostic_map['trans_1']
    
    # Red herring: conditional that never triggers due to prior logic
    if diagnostic_map['entropy'] > 20000:
        final_diagnostic = int(final_diagnostic ** 0.5)
    
    return final_diagnostic

# Initialization sequence (looks complex, partially relevant)
quantum_sequence = initialize_quantum_sequence(12)
segmented = [quantum_sequence[i:i+4] for i in range(0, len(quantum_sequence), 4)]

# Add decoy transformations
processed_segments = []
for seg in segmented:
    shifted = [(x + 5) % 17 for x in seg]
    reversed_shift = list(reversed(shifted))
    processed_segments.append([a ^ b for a, b in zip(seg, reversed_shift)])

# Actual input to analysis
quantum_registers = [
    [13, 7, 21, 9],
    [8, 12, 5, 19],
    [3, 3, 3, 3]
]

# Execute main analysis
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")