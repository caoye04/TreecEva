import itertools

# Simulate a secure data transmission protocol with encoding, noise filtering, and validation
def generate_hamming_code(data_bits):
    # Adds parity bits at positions 1, 2, 4, 8...
    n = len(data_bits)
    m = 0
    while (2**m) < (n + m + 1):
        m += 1

    hamming = [0] * (n + m)
    j = 0
    for i in range(1, len(hamming) + 1):
        if (i & (i - 1)) != 0:  # Not a power of two
            hamming[i - 1] = data_bits[j]
            j += 1

    # Set parity bits
    for i in range(m):
        pos = (2**i)
        count = 0
        for j in range(1, len(hamming) + 1):
            if j & pos:
                count += hamming[j - 1]
        hamming[pos - 1] = count % 2

    return hamming

def apply_noise(signal, seed=42):
    # Simulated noise (distractor - not actually used in final path)
    noisy = signal.copy()
    for i in range(len(noisy)):
        if (seed * i) % 7 == 0:
            noisy[i] ^= 1
    return noisy

def compute_checksum(frame):
    # Simple XOR checksum (used in decoy validation)
    chk = 0
    for bit in frame:
        chk ^= bit
    return chk

def validate_frame(frame):
    # Validates using checksum (dead code path - never called in execution)
    return compute_checksum(frame) == 0

def decode_hamming(hamming):
    # Extract data bits from hamming code (positions that are not powers of two)
    data = []
    for i in range(1, len(hamming) + 1):
        if (i & (i - 1)) != 0:  # Not a power of two
            data.append(hamming[i - 1])
    return data

def matrix_multiply_mod2(matrix, vector):
    # Multiplies a matrix by a vector mod 2
    result = []
    for row in matrix:
        val = sum(r * v for r, v in zip(row, vector)) % 2
        result.append(val)
    return result

def xor_lists(a, b):
    # Element-wise XOR
    return [x ^ y for x, y in zip(a, b)]

def process_transmission(encoded_seq, key_mat):
    # Main processing chain
    stage1 = decode_hamming(encoded_seq)
    
    # Decoy transformation - looks important but unused
    alt_path = apply_noise(stage1, seed=99)
    temp_checksum = compute_checksum(alt_path)
    
    # Actual relevant path
    extended = stage1 + [sum(stage1) % 2]  # Add one more parity
    transformed = matrix_multiply_mod2(key_mat, extended)
    
    # Conditional manipulation based on length
    if len(transformed) > 10:
        midpoint = len(transformed) // 2
        left = transformed[:midpoint]
        right = transformed[midpoint:]
        combined = xor_lists(left, right) if len(left) == len(right) else left
    else:
        combined = transformed
    
    # Final reduction using lambda and conditional expression
    reduce_fn = lambda x: sum(x) * 2 if sum(x) > 5 else sum(x) * (-1)
    score = reduce_fn(combined) if sum(combined) % 2 == 0 else reduce_fn(combined) * -1
    
    # Introduce distraction variables
    debug_trace = f"Path completed with {len(combined)} elements"
    metadata_log = {'version': '2.1', 'mode': 'secure'}
    
    # Final signal calculation — this is the real answer
    correction_factor = 3
    base_value = score * correction_factor
    
    # One last transformation using itertools
    cyclic_shift = list(itertools.islice(itertools.cycle(base_value.to_bytes(4, 'big')), 2, 6))
    final_signal = sum(cyclic_shift) - 256  # Deterministic result via byte arithmetic
    
    return final_signal

# Irrelevant helper (dead code)
def encrypt_aes_stub(data, key):
    return data  # Placeholder

# Setup inputs
raw_data = [1, 0, 1, 1, 0, 1, 0]
encoded_sequence = generate_hamming_code(raw_data)

# Key matrix for transformation (6x7)
key_matrix = [
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1]
]

# Additional red herring variables
transmission_id = "TX-7819"
destination_node = "N4"
packet_size = 1500
retries = 2
is_urgent = True
priority_flag = (retries < 3) and is_urgent

# Execute main logic
final_signal = process_transmission(encoded_sequence, key_matrix)
print(f"Result: {final_signal}")