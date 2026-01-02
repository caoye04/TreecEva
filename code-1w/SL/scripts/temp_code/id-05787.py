def preprocess_signal(raw_data, threshold=0.7):
    """Irrelevant preprocessing function for sensor noise (dead code path)."""
    filtered = [x for x in raw_data if abs(x) > threshold]
    return [val * 0.95 for val in filtered]


def compute_entropy(sequence):
    """Unused entropy calculation (distractor)."""
    from math import log2
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)


def shift_cipher(text, offset):
    """Decoy function for text obfuscation (no impact on result)."""
    return ''.join(chr((ord(c) - ord('a') + offset) % 26 + ord('a')) if c.isalpha() else c for c in text.lower())

# Irrelevant data structures (red herring)
sensor_grid = [[i ^ j + 3 for j in range(8)] for i in range(8)]
baseline_checksums = {i: (i * 17) % 251 for i in range(10)}

# Core system variables (some relevant, some not)
flux_registers = [0x1A, 0x2B, 0x3C, 0x4D]
quantum_signature = (12, 18, 24, 30)

turbine_phase = {'status': 'active', 'level': 3, 'priority': 7}
log_buffer = [{'event': 'init', 'code': 0x01}] * 5

# Misleading intermediate computation (appears important)
correlation_matrix = []
for i in range(4):
    row = []
    for j in range(4):
        # Complex but irrelevant bitwise mixing
        mix = (flux_registers[i] ^ quantum_signature[j]) & 0xFF
        mix = (mix << 1) | (mix >> 7)
        row.append(mix % 100)
    correlation_matrix.append(row)

# Hidden key transformation chain
mask_sequence = [0x5, 0x9, 0x3, 0xF]
masked_values = []
for idx, reg in enumerate(flux_registers):
    masked_val = reg ^ mask_sequence[idx]  # Bitwise XOR masking
    adjusted = (masked_val + quantum_signature[idx]) // 2
    masked_values.append(adjusted)

# Conditional expression chain with nested logic
validation_key = sum(masked_values) if sum(masked_values) > 100 else max(masked_values) * 2

# Simulated diagnostic engine
system_flags = {
    'overload': False,
    'sync_lock': True,
    'parity_fail': validation_key % 2 == 0
}

# Character counting distraction
debug_trace = "System reboot initiated due to parity failure"
char_count = sum(1 for c in debug_trace if c in 'aeiou')

# Main analysis function with critical path
def analyze_system_state(signature, registers):
    # Step 1: Extract and transform components
    a, b, c, d = signature
    transformed = [
        (a ^ registers[0]) & 0xFF,  # XOR and mask
        (b + registers[1]) % 100,
        (c >> 2) ^ (registers[2] & 0xF),
        (d * 2) - registers[3]
    ]
    
    # Step 2: Conditional adjustments
    adjusted = []
    for val in transformed:
        # Nested conditional expression
        new_val = val + 10 if val < 50 else (val - 5 if val < 80 else val // 2)
        adjusted.append(new_val)
    
    # Step 3: Compute weighted score
    weights = [1, -1, 2, -2]
    score = sum(adjusted[i] * weights[i] for i in range(4))
    
    # Step 4: Apply flag-based correction
    if system_flags['sync_lock'] and not system_flags['overload']:
        score += 25
    
    # Step 5: Final threshold check
    final_score = score * 2 if system_flags['parity_fail'] else score // 2
    
    # Step 6: Diagnostic normalization
    normalized = max(-1000, min(1000, final_score))  # Clamp to range
    
    return normalized

# Execute critical statement
final_diagnostic = analyze_system_state(quantum_signature, flux_registers)

# Print result as required
print(f"Result: {final_diagnostic}")