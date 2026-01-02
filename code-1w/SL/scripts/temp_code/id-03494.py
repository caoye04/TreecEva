def preprocess_signal(data, threshold=0.7):
    filtered = [x for x in data if abs(x) > threshold]
    return [x * 1.5 for x in filtered]


def generate_checksum(sequence):
    checksum = 0
    for val in sequence:
        checksum ^= int(abs(val)) & 255
    return checksum

# Irrelevant helper function (dead code path)
def legacy_encode(value):
    return (value << 3) | (value >> 5)

# Misleading diagnostic with decoy logic
def evaluate_health(metrics):
    score = 0
    for m in metrics:
        if m > 0.5:
            score += 1
        elif m < -0.5:
            score -= 2  # Decoy penalty
    return score * 100  # Not used in final result

# Core analysis function with critical logic
def analyze_subsystem(logic_map, mask):
    accumulator = 0
    for k, v in logic_map.items():
        if len(k) % 2 == 0:
            accumulator += v ^ mask
        else:
            accumulator -= v & mask
    return accumulator >> 1

# Main diagnostic engine
def analyze_system_state(buffer, fault_profile):
    # Step 1: Extract key frequencies
    primary_peaks = [x for x in buffer if x % 1 == 0.25]
    
    # Step 2: Apply transformation chain
    transformed = []
    for p in primary_peaks:
        temp = p * 4
        temp = (temp ^ 2047) & 4095  # Bit manipulation
        transformed.append(temp)
    
    # Step 3: Build frequency map (red herring)
    freq_map = {}
    for t in transformed:
        freq_map[t] = freq_map.get(t, 0) + 1
    
    # Step 4: Compute modular invariant
    modulus_chain = 0
    for i, t in enumerate(transformed):
        modulus_chain = (modulus_chain + t * (i + 1)) % 987
    
    # Step 5: Construct logic map from even-indexed values
    logic_map = {f"node_{i}": int(v): i*2 for i, v in enumerate(transformed) if i % 2 == 0}
    
    # Step 6: Spurious data structure (distractor)
    audit_trail = {
        'raw_count': len(buffer),
        'filtered': len(primary_peaks),
        'checksum': generate_checksum(buffer),
        'anomaly_flag': False
    }
    
    # Step 7: Actual core computation (depends on fault_profile)
    intermediate = analyze_subsystem(logic_map, fault_profile)
    
    # Step 8: Conditional adjustment based on bit count
    popcount = bin(fault_profile).count('1')
    adjustment = popcount if popcount % 3 == 0 else -popcount
    
    # Step 9: Final aggregation
    result = intermediate + adjustment + modulus_chain
    
    # Step 10: Final adjustment via conditional expression
    final_diagnostic = result if result > 0 else -result * 2
    
    return final_diagnostic

# Critical data setup
quantum_buffer = [
    1.25, -3.25, 2.75, 0.25, 4.25, 5.75, 3.25, 2.25,
    0.75, 1.75, -2.25, 3.75, 4.75, 5.25, 6.25, 7.25
]

fault_mask = 219  # 0xDB, used in bitwise operations

# Misleading preliminary calls (distraction)
dummy_signal = [-0.8, 0.9, -1.2, 0.4]
preprocess_signal(dummy_signal)
evaluate_health(dummy_signal)

# Key execution point
final_diagnostic = analyze_system_state(quantum_buffer, fault_mask)

# Output result
print(f"Result: {final_diagnostic}")