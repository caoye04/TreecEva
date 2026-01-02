def preprocess_segment(data_chunk, threshold=0.75):
    """Irrelevant preprocessing function for signal filtering."""
    filtered = []
    cumulative = 0
    for val in data_chunk:
        if abs(val) > threshold:
            filtered.append(val * 0.9)
        else:
            cumulative += val ** 2
    return filtered, cumulative


def deprecated_checksum(seq):
    """Outdated integrity check – not used in current logic."""
    return sum(seq[i] * (i + 1) for i in range(len(seq))) % 1024


def generate_basis(size):
    """Generates a modular basis set – distractor."""
    basis = []
    for i in range(1, size + 1):
        basis.append((i ** 3 - i) % 17)
    return set(basis)

# Global decoy state (misleading)
current_phase = [1, 1, 2, 3, 5, 8, 13]
system_lock = False
sync_offset = 256
temporal_weights = {i: (i * i) % 19 for i in range(15)}


def rotate_key(sequence, shift):
    """Bit rotation on sequence elements – used in red herring path."""
    shifted = []
    for num in sequence:
        binary = format(num % 256, '08b')
        rotated = binary[shift % 8:] + binary[:shift % 8]
        shifted.append(int(rotated, 2))
    return shifted


def compute_entropy(vector):
    """Unused entropy metric – dead code path."""
    from math import log2
    total = sum(vector)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in vector:
        p = x / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 6)


def validate_coherence(arr):
    """Simulates hardware coherence check – irrelevant to final result."""
    return len(set(arr)) >= len(arr) // 2


def recursive_transform(n, depth=0):
    """Recursive bit manipulation with modular reduction."""
    if depth >= 5 or n < 2:
        return n
    if n % 3 == 0:
        return recursive_transform(n // 3, depth + 1) ^ (n & 127)
    else:
        return recursive_transform((n - 1) // 2, depth + 1) + (n | 43)


def analyze_system_state(sequence, mask):
    """Main diagnostic analyzer – actual critical logic."""
    # Step 1: Apply mask using bitwise XOR
    masked_seq = [a ^ mask[i % len(mask)] for i, a in enumerate(sequence)]
    
    # Step 2: Reduce via recursive transformation
    transformed = [recursive_transform(x) for x in masked_seq]
    
    # Step 3: Aggregate using modular arithmetic
    aggregate = 0
    for i, val in enumerate(transformed):
        contribution = (val * (i + 1)) % 97
        aggregate = (aggregate + contribution) % 8641
    
    # Step 4: Use set operations to extract uniqueness impact
    unique_set = set(transformed)
    set_influence = sum([x % 19 for x in unique_set if x % 2 == 1]) % 100
    
    # Step 5: Final diagnostic computation
    raw_diagnostic = (aggregate * 2 + set_influence * 3) % 10000
    
    # Irrelevant scaling branch (never taken due to constant lock)
    if system_lock:  
        raw_diagnostic = int(raw_diagnostic * 1.25)
    
    # Critical assignment point
    final_diagnostic = max(101, min(raw_diagnostic, 9876))  # Clamp range
    
    # Unused side-effect logging
    log_entry = f"DIAG:{final_diagnostic}:OK"
    
    return final_diagnostic

# Primary execution context
if __name__ == "__main__":
    # Real input data
    quantum_sequence = [12, 45, 67, 89, 112, 158, 199, 203]
    system_mask = [17, 23, 17, 23]
    
    # Decoy computations (distractors)
    _ = preprocess_segment([0.1, 0.8, 0.3, 0.9], threshold=0.5)
    _ = generate_basis(10)
    _ = rotate_key(quantum_sequence, 3)
    _ = deprecated_checksum(quantum_sequence)
    
    # Actual critical call
    final_diagnostic = analyze_system_state(quantum_sequence, system_mask)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")