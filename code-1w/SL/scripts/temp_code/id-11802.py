from collections import defaultdict, Counter
import math

# Simulated sensor data stream with metadata tags
data_stream = [
    (1024, 'A', 7), (2048, 'B', 3), (512, 'A', 11), (4096, 'C', 5),
    (8192, 'B', 13), (16384, 'A', 17), (32768, 'C', 19), (65536, 'B', 23)
]

# Irrelevant auxiliary mapping (red herring)
symbol_map = {'A': 2, 'B': 3, 'C': 5, 'D': 7}

# Misleading intermediate accumulators
temp_accumulator = 0
shadow_buffer = []
mode_registry = defaultdict(int)

# Phantom transformation table (unused in final logic)
transform_table = {i: (i ** 2) % 97 for i in range(50)}

# Auxiliary function that appears relevant but is only partially used
def analyze_pattern(sequence, flag=None):
    if flag == 'prime_only':
        return [x for x in sequence if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
    elif flag == 'powers_of_two':
        return [x for x in sequence if (x & (x - 1)) == 0 and x > 0]
    else:
        return sorted(sequence, reverse=True)[:4]

# Decoy checksum that computes something plausible but unused
legacy_checksum = sum((x[0] // x[2]) * symbol_map[x[1]] for x in data_stream) % 65537

# Another distraction: frequency analysis not directly used
freq_analysis = Counter([tag for _, tag, _ in data_stream])

# Simulate historical mode transitions (dead code path)
for tag in [t[1] for t in data_stream]:
    mode_registry[tag] += 1
    if mode_registry[tag] > 2:
        temp_accumulator ^= symbol_map[tag]

# Buffer population with irrelevant transformations
for val, tag, pid in data_stream:
    transformed = (val ^ pid) + symbol_map[tag]
    shadow_buffer.append(transformed % 10007)

# Primary computation function with hybrid logic
def compute_integrity_value(stream, mode="hybrid"):
    base_values = [item[0] for item in stream]
    primes = [item[2] for item in stream]
    
    # Step 1: Filter valid powers of two
    filtered_powers = analyze_pattern(base_values, flag='powers_of_two')
    
    # Step 2: Compute modular product of primes
    prime_product = 1
    for p in primes:
        prime_product = (prime_product * p) % 1000003
    
    # Step 3: Bit manipulation chain
    bit_accum = 0
    for v in filtered_powers:
        rotated = ((v << 3) | (v >> (32 - 3))) & 0xFFFFFFFF  # 3-bit left rotate
        bit_accum ^= rotated
    
    # Step 4: Combine using hybrid formula
    if mode == "hybrid":
        # Real key computation
        raw_sum = sum(base_values)
        weighted_tag = sum(symbol_map[t] * (i + 1) for i, (_, t, _) in enumerate(stream))
        hybrid_component = (raw_sum ^ prime_product) & 0xFFFFFFF
        final_component = (hybrid_component + weighted_tag * 3) & 0x7FFFFFFF
        
        # Final transformation (answer depends on this)
        result = (final_component ^ bit_accum) % 891289
        return result
    
    return 0  # Unused fallback

# Execution point of interest
final_checksum = compute_integrity_value(data_stream, mode="hybrid")

# Print result as required
print(f"Result: {final_checksum}")