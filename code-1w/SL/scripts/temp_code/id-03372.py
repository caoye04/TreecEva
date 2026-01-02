import math

# Simulated quantum register diagnostics with extensive irrelevant processing
def generate_entropy_sequence(length):
    """Irrelevant function: generates decoy entropy values"""
    return [math.sin(i) * math.log(i + 1) for i in range(1, length + 1)]

def compute_hamming_classifiers(state_vector):
    """Misleading function: computes fake classifiers"""
    return sum((x & 3) ^ (x >> 2) for x in state_vector if x % 5 == 0)

def validate_coherence_protocol(registers):
    """Dead code path: never actually used in logic"""
    for r in registers:
        if sum(r) % 7 == 0:
            return False
    return True

def extract_syndrome_patterns(registers):
    """Distractor: computes unused syndrome values"""
    patterns = []
    for reg in registers:
        pattern = 0
        for bit in reg:
            pattern = (pattern << 1) ^ bit ^ (bit * 3)
        patterns.append(pattern % 16)
    return patterns

def filter_redundant_states(states):
    """Unused filtering logic to mislead analysis"""
    filtered = []
    for s in states:
        if len(set(s)) > 2:
            filtered.append(s[1:-1])
    return filtered

def calculate_thermal_drift(registers):
    """Irrelevant physics simulation"""
    total_drift = 0.0
    for i, reg in enumerate(registers):
        drift = sum(math.cos(val + i) for val in reg)
        total_drift += drift * 0.01
    return round(total_drift, 6)

def analyze_system_state(registers):
    # Core relevant logic buried under distractions
    
    # Irrelevant pre-processing
    entropy_seq = generate_entropy_sequence(len(registers))
    coherence = validate_coherence_protocol(registers)
    syndromes = extract_syndrome_patterns(registers)
    
    # Critical data transformation
    processed_bits = []
    for reg in registers:
        # Bit manipulation with masking and shifting
        transformed = 0
        for bit in reg:
            transformed = (transformed << 1) | (bit & 1)
        processed_bits.append(transformed)
    
    # Relevant combinatorial calculation
    max_frequency = 0
    frequency_map = {}
    for val in processed_bits:
        freq = processed_bits.count(val)
        frequency_map[val] = freq
        if freq > max_frequency:
            max_frequency = freq
    
    # Determine dominant state with XOR-based tiebreaker
    dominant_candidates = [v for v, f in frequency_map.items() if f == max_frequency]
    primary_dominant = dominant_candidates[0]
    if len(dominant_candidates) > 1:
        # Tie-breaking via bitwise reduction
        tiebreaker = 0
        for candidate in dominant_candidates:
            tiebreaker ^= candidate * (candidate % 5)
        primary_dominant = tiebreaker
    
    # Red herring: use of lambda and set operations (partially irrelevant)
    anomaly_detector = lambda x: len(set(bin(x).split('1'))) > 4
    anomalies = [x for x in processed_bits if anomaly_detector(x)]
    
    # Decoy average calculation
    decoy_avg = sum(processed_bits) / len(processed_bits) if processed_bits else 0
    
    # Actual answer derivation: modular interaction of dominant pattern and system size
    system_size = len(registers) * sum(len(reg) for reg in registers)
    raw_diagnostic = (primary_dominant * system_size) % 98765
    
    # Final adjustment using list comprehension (mixed relevance)
    adjustments = [i * 2 for i, r in enumerate(registers) if sum(r) > 5]
    adjustment_factor = sum(adjustments) % 100
    
    final_diagnostic = raw_diagnostic - adjustment_factor
    
    # Print required output
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Initialize complex quantum register configuration (meaningful input)
    quantum_registers = [
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 0, 1, 1]
    ]

    # Extensive irrelevant preprocessing
    _ = generate_entropy_sequence(10)
    _ = compute_hamming_classifiers([5, 10, 15, 20, 25])
    _ = extract_syndrome_patterns(quantum_registers)
    _ = calculate_thermal_drift(quantum_registers)

    # Key execution point
    final_diagnostic = analyze_system_state(quantum_registers)
    print(f"Target result: {final_diagnostic}")