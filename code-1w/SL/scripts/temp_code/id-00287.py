from collections import defaultdict
import math

# Simulate a secure data transmission protocol with noise filtering and checksum validation
def generate_primes(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# Irrelevant helper function – dead code path (not used)
def calculate_checksum(data):
    checksum = 0
    for val in data:
        checksum = (checksum + val) % 257
    return checksum

def apply_noise_filter(signal, threshold=10):
    # Filter out values below threshold (only relevant part)
    filtered = [x for x in signal if abs(x) > threshold]
    normalization_factor = sum(abs(x) for x in filtered) or 1
    return [x / normalization_factor for x in filtered]

# Unused distractor function
def encrypt_chunk(chunk, key):
    return [c ^ key for c in chunk]

# Main processing function
def process_transmission(signal_sequence, transformation_matrix):
    # Step 1: Apply noise filter to raw signal
    clean_signal = apply_noise_filter(signal_sequence)
    
    # Distractor: Prime-related computation (unused)
    primes_up_to_100 = generate_primes(100)
    prime_offset = len(primes_up_to_100)  # Misleading intermediate
    
    # Step 2: Normalize signal using matrix transformation (dot product simulation)
    transformed = []
    for i in range(len(clean_signal)):
        val = clean_signal[i]
        row = transformation_matrix[i % len(transformation_matrix)]
        weighted = sum(val * row[j % len(row)] for j in range(3))  # Use first 3 weights
        transformed.append(weighted)
    
    # Step 3: Quantize signal values using bitwise manipulation
    quantized = []
    shift_key = 2
    for x in transformed:
        raw_int = int(abs(x) * 1000)
        # Apply XOR mask based on sign
        if x < 0:
            masked = raw_int ^ 0xFF
        else:
            masked = raw_int | 0xAA  # Distractor operation
        quantized.append((masked >> shift_key) & 0xFFFF)  # Keep lower 16 bits after shift
    
    # Step 4: Frequency analysis using defaultdict (distractor with partial relevance)
    freq_map = defaultdict(int)
    for q in quantized:
        freq_map[q % 256] += 1  # Track low byte frequency
    
    # Step 5: Compute aggregate signal strength via modular reduction
    aggregate = 0
    mod_base = 982451653  # Large prime for mod (overkill, but distracts)
    for i, q in enumerate(quantized):
        contribution = (q * (i + 1)) ^ (i << 2)
        aggregate = (aggregate + contribution) % mod_base
    
    # Step 6: Final adjustment using lambda-based decay (only one term used)
    decay_func = lambda x, t: x / (1 + t)
    decayed_aggregate = int(decay_func(aggregate, 5.5))
    
    # Final output derived from last quantized value and decayed aggregate
    final_signal = (decayed_aggregate + quantized[-1]) % 65536
    
    # Red herring variables (never used again)
    verification_hash = sum(freq_map.values()) * prime_offset
    error_margin = math.log(verification_hash + 1) if verification_hash > 0 else 0
    
    return final_signal

# Simulated input data
raw_sequence = [15, -23, 8, 0, -45, 67, 12, -19, 34, -56, 89, -12, 7, 28, -31]
key_matrix = [
    [0.1, 0.3, 0.2],
    [0.4, 0.1, 0.5],
    [0.2, 0.2, 0.1]
]

# Execute main logic
final_signal = process_transmission(raw_sequence, key_matrix)
print(f"Target result: {final_signal}")