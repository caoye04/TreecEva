import math

def analyze_pattern(sequence):
    magnitude = sum(x ** 2 for x in sequence)
    normalized = [x / (magnitude + 1e-9) for x in sequence]
    return [round(math.sin(x * math.pi), 6) for x in normalized]

def shift_cipher(text, offset):
    # Irrelevant distraction: text encoding function not used in final result
    return ''.join(chr((ord(c) - 97 + offset) % 26 + 97) if 'a' <= c <= 'z' else c for c in text)

def generate_primes(limit):
    # Distractor: generates primes but only a subset is used
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

def validate_checksum(data):
    # Unused validation function — red herring
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val * (i + 1)) % 257
    return checksum == 131

def transform_coordinates(coords):
    # Complex but partially irrelevant transformation
    transformed = []
    for x, y in coords:
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        new_x = r * math.cos(theta * 2)
        new_y = r * math.sin(theta * 2)
        transformed.append((round(new_x, 4), round(new_y, 4)))
    return transformed

def aggregate_metrics(grid_data, weights):
    temp_accum = 0
    weighted_sum = 0
    total_weight = 0
    
    # Real logic begins: modular arithmetic and conditional weighting
    for i, row in enumerate(grid_data):
        row_contrib = 0
        for j, val in enumerate(row):
            index_sum = i + j
            if index_sum % 3 == 0:
                temp_val = (val * 2) % 17
            elif index_sum % 3 == 1:
                temp_val = (val + 5) % 17
            else:
                temp_val = val % 17
            
            # Apply weight based on position using zip and enumerate together
            weight = next(w for idx, w in enumerate(weights) if idx % len(weights) == j % len(weights))
            weighted_sum += temp_val * weight
            total_weight += weight
            
            # Nested logic with bit manipulation distraction
            if i > 0 and j > 0:
                prev_val = grid_data[i-1][j-1]
                xor_fuse = (val ^ prev_val) & 0xF
                temp_accum += xor_fuse if xor_fuse % 2 else 0  # Only even fuses count
    
    # Character counting distractor
    log_tag = "diagnostic_run_complete_v2"
    char_count = {c: log_tag.count(c) for c in set(log_tag)}
    bonus = char_count.get('c', 0) * 10  # Adds 30, misleadingly seems important
    
    # Linear search in generated primes (distractor)
    primes = generate_primes(100)
    found = None
    for p in primes:
        if p > weighted_sum:
            found = p
            break
    
    # Final computation uses only weighted average and bonus, ignoring 'found' and most of above
    raw_result = weighted_sum / (total_weight + 1e-9)
    final_score = raw_result + bonus  # bonus is 30
    
    # Additional decoy: unused conditional override
    if temp_accum > 100:
        final_score *= 1.1
    
    return int(round(final_score))

# Main execution data
grid_data = [
    [12, 7, 15, 3],
    [8, 11, 4, 9],
    [6, 14, 10, 5],
    [13, 2, 16, 1]
]

weights = [1, 3, 2, 4]

# Unused variables — dead code paths
buffer_cache = [0] * 256
debug_trace = shift_cipher("init_phase_final", 7)
coordinates = [(1, 1), (2, 3), (3, 2)]
processed_coords = transform_coordinates(coordinates)

# Key statement
final_diagnostic = aggregate_metrics(grid_data, weights)

print(f"Result: {final_diagnostic}")