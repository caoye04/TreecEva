import itertools

# Simulated quantum sensor readings with noise masking
def generate_quantum_noise(length):
    base = [i ^ (i >> 2) for i in range(length)]
    noise = [(b + (b << 3)) & 0xFF for b in base]
    return [n ^ 0xAA for n in noise]  # Bit-flipped pattern

# Irrelevant image processing stub (dead abstraction)
def preprocess_image_buffer(buffer):
    if len(buffer) > 64:
        return [b & 0x7F for b in buffer[:64]]
    return buffer

# Decoy function – looks important but unused in critical path
def compute_entropy_signature(data):
    entropy = 0
    for x in data:
        if x != 0:
            entropy -= x * math.log2(x) if x > 0 else 0
    return entropy

# Core analysis with distractors and nested logic
def analyze_system_state(sequence, flags):
    temp_result = 0
    shift_accumulator = 0
    
    # Meaningful transformation: extract every 3rd element where index satisfies bit condition
    filtered = [v for i, v in enumerate(sequence) if i % 3 == 0 and (i & (i - 1)) == 0]  # Powers of two indices divisible by 3

    # Red herring: complex-looking but unused calculation
    phantom_sum = sum((x | 5) ^ (x & 7) for x in sequence if x < 50)
    scaling_factor = 1.0
    for i in range(len(sequence)):
        if sequence[i] > 100:
            scaling_factor *= 0.95

    # Real logic begins: process filtered values with flag-controlled behavior
    for val in filtered:
        if flags['diagnostic_mode']:
            shifted = val >> 2
            if shifted % 2 == 0:
                temp_result += shifted ** 2
            else:
                temp_result -= shifted * 3
        
        # Additional valid operation: XOR with position-based key
        key = len(filtered) ^ 7
        shift_accumulator += (val ^ key) & 0xF

    # Critical branching based on flag combination
    if flags['safe_override'] and not flags['diagnostic_mode']:
        return -999  # Dead end — not taken due to flag settings

    # Actual result computation (depends on above loops)
    intermediate = temp_result ^ shift_accumulator
    correction = len(list(itertools.groupby(filtered)))  # Number of consecutive groups
    final_value = intermediate + correction * 5

    # Distractor: string-based checksum with no effect
    status_str = "System_" + "Active" if final_value > 0 else "Inactive"
    checksum = sum(ord(c) for c in status_str) % 100

    return final_value

# Entry point with decoy data structures
if __name__ == '__main__':
    # Primary input data
    quantum_sequence = generate_quantum_noise(64)

    # Unused image buffer (distractor)
    image_buffer = [i ^ 0x55 for i in range(128)]
    processed_buffer = preprocess_image_buffer(image_buffer)

    # System configuration – only 'diagnostic_mode' and 'safe_override' matter
    system_flags = {
        'diagnostic_mode': True,
        'safe_override': False,
        'legacy_support': True,
        'encrypt_transmission': False,
        'enable_audit_log': True
    }

    # Critical execution point
    final_diagnostic = analyze_system_state(quantum_sequence, system_flags)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")